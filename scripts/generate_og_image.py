"""Generate 1200x630 og-image.png for WhatsApp/Facebook sharing."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
img = Image.new("RGB", (W, H), "#0a0f1a")
draw = ImageDraw.Draw(img)

# Gradient-like overlays
for i in range(H):
    t = i / H
    r = int(10 + t * 20)
    g = int(15 + t * 28)
    b = int(26 + t * 40)
    draw.line([(0, i), (W, i)], fill=(r, g, b))

# Glow circles
for cx, cy, radius, color in [
    (180, 120, 220, (14, 165, 233, 40)),
    (1020, 80, 180, (56, 189, 248, 30)),
    (600, 580, 260, (14, 165, 233, 25)),
]:
    for r in range(radius, 0, -2):
        alpha = int(color[3] * (1 - r / radius))
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        od.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(color[0], color[1], color[2], alpha))
        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
        draw = ImageDraw.Draw(img)

# Grid pattern (subtle)
for x in range(0, W, 40):
    draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 8), width=1)
for y in range(0, H, 40):
    draw.line([(0, y), (W, y)], fill=(255, 255, 255, 8), width=1)

try:
    font_bold_l = ImageFont.truetype("arialbd.ttf", 72)
    font_bold_m = ImageFont.truetype("arialbd.ttf", 44)
    font_reg = ImageFont.truetype("arial.ttf", 28)
    font_sm = ImageFont.truetype("arial.ttf", 24)
except OSError:
    font_bold_l = ImageFont.load_default()
    font_bold_m = font_bold_l
    font_reg = font_bold_l
    font_sm = font_bold_l

# Icon box
draw.rounded_rectangle([80, 80, 160, 160], radius=20, fill=(14, 165, 233))
draw.text((108, 98), "🎨", font=font_bold_m, fill="white")

# Brand
draw.text((190, 95), "Elbay", font=font_bold_l, fill=(56, 189, 248))
draw.text((190, 165), "Yapı Dekorasyon", font=font_bold_m, fill="white")

# Main headline
draw.text((80, 260), "Sivas Boya Badana", font=font_bold_l, fill="white")
draw.text((80, 345), "& Yapı Dekorasyon", font=font_bold_m, fill=(148, 163, 184))

# Tags
tags = "Ev · Ofis · Alçıpan · Ters Tavan · Anahtar Teslim"
draw.text((80, 420), tags, font=font_reg, fill=(148, 163, 184))

# Badge
draw.rounded_rectangle([80, 490, 420, 550], radius=28, fill=(14, 165, 233))
draw.text((110, 505), "20 Yıl Tecrübe · Ücretsiz Keşif", font=font_sm, fill="white")

# Phone
draw.text((80, 575), "0535 629 27 06", font=font_reg, fill=(56, 189, 248))

# Right side decorative panel
draw.rounded_rectangle([720, 200, 1120, 520], radius=24, outline=(56, 189, 248), width=2)
services = [
    "✓  İç & Dış Cephe Boyama",
    "✓  Alçıpan & Ters Tavan",
    "✓  Klipin & Lambiri",
    "✓  Kartonpiyer & LED",
    "✓  Anahtar Teslim Tadilat",
]
y = 240
for s in services:
    draw.text((760, y), s, font=font_reg, fill=(226, 232, 240))
    y += 52

out = r"c:\Users\furka\OneDrive\Masaüstü\boyacı\og-image.png"
img.save(out, "PNG", optimize=True)
print("Saved:", out)
