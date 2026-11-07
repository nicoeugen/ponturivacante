import os

src_dir = 'C:/Users/Eugen/Desktop/Proiecte/website turism/src'
matches = []

for root, dirs, files in os.walk(src_dir):
    for f in files:
        if f.endswith(('.astro', '.js', '.ts', '.html', '.json')):
            full_path = os.path.join(root, f)
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as fp:
                for line_no, line in enumerate(fp, 1):
                    if 'agoda.com' in line or 'search?text=' in line:
                        matches.append((full_path, line_no, line.strip()))

print(f"Found {len(matches)} occurrences:")
for path, line_no, line in matches:
    print(f"{os.path.basename(path)}:{line_no} -> {line[:100]}")
