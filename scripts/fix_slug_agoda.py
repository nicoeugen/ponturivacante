import re

path = 'C:/Users/Eugen/Desktop/Proiecte/website turism/src/pages/oferta/[slug].astro'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\r\r\n', '\n').replace('\r\n', '\n')

pattern = r'href=\{\`/go/hotel/\?url=\$\{encodeURIComponent\(\`https://www\.agoda\.com/ro-ro/search\?[^\`]+\`\)\}&deal=\$\{deal\.id\}&provider=agoda\`\}'
new_part = 'href={`/go/hotel/?url=${encodeURIComponent((deal.accommodationOptions && deal.accommodationOptions[1]?.link) ? deal.accommodationOptions[1].link : \'https://www.agoda.com/ro-ro/?cid=1980047\')}&deal=${deal.id}&provider=agoda`}'

new_content, count = re.subn(pattern, new_part, content)
print('Replacements made:', count)

with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(new_content)
print('File updated successfully.')
