from PIL import Image, ImageDraw, ImageFont
import os

# Set up image dimensions and colors
width, height = 1200, 800
bg_color = (30, 30, 30)
text_color = (200, 200, 200)
header_color = (50, 50, 50)
command_color = (0, 255, 150)
agent_color = (100, 180, 255)
success_color = (150, 255, 150)
warning_color = (255, 200, 100)

# Create image
img = Image.new('RGB', (width, height), color=bg_color)
draw = ImageDraw.Draw(img)

# Try to load a font, fallback to default
try:
    # On Windows, Consolas or Courier New are common
    font = ImageFont.truetype("consola.ttf", 20)
    font_bold = ImageFont.truetype("consolab.ttf", 24)
except:
    font = ImageFont.load_default()
    font_bold = font

# Draw Header
draw.rectangle([0, 0, width, 40], fill=header_color)
draw.text((20, 10), "AugmentAlign - Operation Console (Active Project: Demo Client)", fill=(255, 255, 255), font=font)

# Simulated Terminal Output
lines = [
    ("> /aa:diagnose", command_color),
    ("[COO] Analyzing brief.md... Client alignment: HIGH. Status: ACCEPTED.", text_color),
    ("[COO] Selected Package: Package A (AI Readiness Evaluation).", success_color),
    ("", text_color),
    ("> /aa:dispatch", command_color),
    ("[COO] Dispatching Technical Specs to Specialists...", text_color),
    ("  - [Data Architect] Task: RAG Pipeline Design for Teaching Assets.", agent_color),
    ("  - [Workflow Engineer] Task: Multi-Agent Marketing & Prep Workflow.", agent_color),
    ("", text_color),
    ("[Data Architect] Initializing Vector DB (ChromaDB) for 'Academic Assets'...", text_color),
    ("[Data Architect] QUALITY GATE: Recall@5 = 92% [PASS]", success_color),
    ("", text_color),
    ("[Workflow Engineer] Designing Marketing-Agent Prompt (Tone: Professional-Friendly)...", text_color),
    ("[Workflow Engineer] QUALITY GATE: Tool Calling Success Rate = 98% [PASS]", success_color),
    ("", text_color),
    ("> /aa:integrate", command_color),
    ("[COO] Integrating modules. Ensuring Human-in-the-Loop constraints...", text_color),
    ("[COO] All Quality Gates PASSED. Finalizing Deliverable.md...", success_color),
    ("", text_color),
    ("[SYSTEM] STATUS: STANDBY - Waiting for Human Oversight Approval.", warning_color),
]

y_offset = 60
for line, color in lines:
    draw.text((30, y_offset), line, fill=color, font=font)
    y_offset += 30

# Save image
img.save('company-screenshot.png')
print("Screenshot generated: company-screenshot.png")
