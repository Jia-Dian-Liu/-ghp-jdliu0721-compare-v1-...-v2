from PIL import Image, ImageDraw, ImageFont
import os

width, height = 1000, 600
bg_color = (30, 30, 30)
text_color = (200, 200, 200)
header_color = (45, 45, 45)
folder_color = (255, 215, 0)
file_color = (135, 206, 250)
new_file_color = (150, 255, 150)

img = Image.new('RGB', (width, height), color=bg_color)
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype('consola.ttf', 22)
except:
    font = ImageFont.load_default()

draw.rectangle([0, 0, width, 50], fill=header_color)
draw.text((20, 15), 'Empathetic Engineering - Core Structure v2', fill=(255, 255, 255), font=font)

lines = [
    ('> tree .gemini /f', (0, 255, 150)),
    ('C:\\PROJECTS\\AUGMENTALIGN\\.GEMINI', (255, 215, 0)),
    ('├── agents', (255, 215, 0)),
    ('│   ├── coo.md', (135, 206, 250)),
    ('│   ├── data-architect.md', (135, 206, 250)),
    ('│   ├── interface-designer.md', (135, 206, 250)),
    ('│   ├── latent-intent-director.md  <-- NEW', (150, 255, 150)),
    ('│   └── workflow-engineer.md', (135, 206, 250)),
    ('└── commands', (255, 215, 0)),
    ('    └── commands.toml', (135, 206, 250)),
]

y_offset = 80
for text, color in lines:
    draw.text((40, y_offset), text, fill=color, font=font)
    y_offset += 35

img.save('w10/company-structure-v2.png')

