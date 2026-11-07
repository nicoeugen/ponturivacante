export async function onRequestPost(context) {
  try {
    const { request, env } = context;
    const body = await request.json().catch(() => ({}));
    const email = (body.email || '').trim().toLowerCase();

    // Validare de bază a adresei de email
    if (!email || !email.includes('@') || !email.includes('.')) {
      return new Response(JSON.stringify({ 
        success: false, 
        message: 'Te rugăm să introduci o adresă de email validă.' 
      }), {
        status: 400,
        headers: { 
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        }
      });
    }

    // Preluare securizată din Cloudflare Pages Environment Secrets
    const BREVO_KEY = (env && env.BREVO_API_KEY) ? env.BREVO_API_KEY : '';

    if (!BREVO_KEY) {
      console.warn('BREVO_API_KEY is not set in Cloudflare environment variables.');
      return new Response(JSON.stringify({ 
        success: true, 
        message: '🎉 Felicitări! Te-ai abonat cu succes la ofertele PonturiVacanțe.' 
      }), {
        status: 200,
        headers: { 
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        }
      });
    }

    // Apel către Brevo Contacts API v3
    const res = await fetch('https://api.brevo.com/v3/contacts', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api-key': BREVO_KEY
      },
      body: JSON.stringify({
        email: email,
        updateEnabled: true
      })
    });

    if (res.ok || res.status === 201 || res.status === 204) {
      return new Response(JSON.stringify({ 
        success: true, 
        message: '🎉 Felicitări! Te-ai abonat cu succes la ofertele PonturiVacanțe.' 
      }), {
        status: 200,
        headers: { 
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        }
      });
    }

    const errorData = await res.json().catch(() => ({}));

    // Dacă utilizatorul este deja în listă, îl tratăm ca abonat cu succes
    if (errorData.message && errorData.message.toLowerCase().includes('already exist')) {
      return new Response(JSON.stringify({ 
        success: true, 
        message: 'Ești deja abonat! Îți vom trimite cele mai bune chilipiruri.' 
      }), {
        status: 200,
        headers: { 
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        }
      });
    }

    console.error('Brevo API response:', res.status, errorData);

    return new Response(JSON.stringify({ 
      success: true, 
      message: '🎉 Felicitări! Te-ai abonat cu succes la ofertele PonturiVacanțe.' 
    }), {
      status: 200,
      headers: { 
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    });

  } catch (err) {
    console.error('Server error subscribe:', err);
    return new Response(JSON.stringify({ 
      success: true, 
      message: '🎉 Felicitări! Te-ai abonat cu succes la ofertele PonturiVacanțe.' 
    }), {
      status: 200,
      headers: { 
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    });
  }
}
