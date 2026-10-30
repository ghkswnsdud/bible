# Inline book.glb into src.html -> index.html (standalone/Vercel) and bible.html (artifact, no doc skeleton).
import base64, re

src = open('src.html', encoding='utf-8').read()
assert '__MODEL__' in src
uri = 'data:model/gltf-binary;base64,' + base64.b64encode(open('book.glb', 'rb').read()).decode()
page = src.replace('__MODEL__', uri)
open('index.html', 'w', encoding='utf-8').write(page)

art = re.sub(r'<!doctype html>\s*|</?html[^>]*>\s*|</?head>\s*|</?body>\s*|<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*', '', page)
open('bible.html', 'w', encoding='utf-8').write(art)
print('built', len(page), len(art))
