with open("C:/Users/Eugen/Desktop/Proiecte/website turism/engine/update_exact_deeplinks.py", "r", encoding="utf-8") as f:
    text = f.read()

old_slugs = """    "ro-006": "https://www.booking.com/hotel/ro/green-village.ro.html"
}"""

new_slugs = """    "ro-006": "https://www.booking.com/hotel/ro/green-village.ro.html",
    "ro-007": "https://www.booking.com/hotel/ro/aparthotel-alpin.ro.html",
    "ro-008": "https://www.booking.com/hotel/ro/rina-cerbul.ro.html",
    "ro-009": "https://www.booking.com/hotel/ro/vila-alpin.ro.html",
    "ro-010": "https://www.booking.com/hotel/ro/cindrel.html"
}"""

if old_slugs in text:
    text = text.replace(old_slugs, new_slugs)
    with open("C:/Users/Eugen/Desktop/Proiecte/website turism/engine/update_exact_deeplinks.py", "w", encoding="utf-8") as f:
        f.write(text)
    print("Slug-urile de schi au fost adaugate in update_exact_deeplinks.py!")
else:
    print("Nu s-a gasit old_slugs!")
