import math
from common import C, frame, esc, write, SANS

W = 860


def stats():
    H = 128
    items = [
        ("5+", "anos de código", "produtos próprios", C["teal"], 1.0),
        ("2020", "Nation Resources", "fundada e ativa", C["amber"], 1.0),
        ("1º", "melhor média", "entre formandos", C["violet"], 1.0),
        ("3", "idiomas", "pt · en · es", C["sky"], 0.7),
    ]
    cw = (W - 40 - 3 * 12) / 4
    b = []
    for i, (val, l1, l2, col, frac) in enumerate(items):
        x = 20 + i * (cw + 12)
        y = 20
        d = 0.2 + i * 0.2
        cx, cy, r = x + 40, y + 44, 24
        circ = 2 * math.pi * r
        b.append(
            f'<g class="rise" style="animation-delay:{d:.2f}s">'
            f'<rect x="{x}" y="{y}" width="{cw:.1f}" height="88" rx="10" fill="{C["panel"]}" stroke="{C["line"]}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{C["line"]}" stroke-width="5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="5" stroke-linecap="round" '
            f'transform="rotate(-90 {cx} {cy})" stroke-dasharray="{circ:.1f}" stroke-dashoffset="{circ:.1f}">'
            f'<animate attributeName="stroke-dashoffset" from="{circ:.1f}" to="{circ*(1-frac):.1f}" dur="1.4s" begin="{d+0.2:.2f}s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1" keyTimes="0;1"/></circle>'
            f'<text x="{cx}" y="{cy+6}" font-size="{16 if len(val) < 3 else 12}" font-weight="800" class="sans" fill="{col}" text-anchor="middle">{esc(val)}</text>'
            f'<text x="{x+76}" y="{y+40}" font-size="13" font-weight="700" class="sans" fill="{C["text"]}">{esc(l1)}</text>'
            f'<text x="{x+76}" y="{y+59}" font-size="11" fill="{C["dim"]}">{esc(l2)}</text></g>')
    return frame(W, H, "\n  ".join(b), title="Destaques: mais de 5 anos de experiência, fundador da Nation Resources em 2020, melhor média entre os formandos, 3 idiomas")


def footer():
    H = 92
    words = ["ensure yuri-lima", "Lua", "Node.js", "Express", "MySQL", "API REST", "Discord", "Mercado Pago",
             "FiveM", "VPS", "Cloudflare", "Nginx", "Git"]
    seq = "   ◆   ".join(words) + "   ◆   "
    cw = 7.2
    seg = len(seq) * cw
    b = [f'<rect x="0" y="0" width="{W}" height="34" fill="{C["bg0"]}"/>',
         f'<path d="M0 34H{W}" stroke="{C["line"]}"/>',
         f'<g><text x="0" y="22" font-size="12" fill="{C["faint"]}" xml:space="preserve">{esc(seq*4)}</text>'
         f'<animateTransform attributeName="transform" type="translate" from="0 0" to="{-seg:.1f} 0" dur="22s" repeatCount="indefinite"/></g>',
         f'<text x="24" y="66" font-size="13" fill="{C["teal"]}" font-weight="700">&gt; <tspan fill="{C["text"]}" font-weight="400">obrigado pela visita, bora conversar?</tspan></text>',
         f'<rect x="{24+39*7.85:.0f}" y="54" width="8" height="15" fill="{C["teal"]}" class="blink"/>',
         f'<text x="{W-24}" y="66" font-size="11.5" fill="{C["dim"]}" text-anchor="end">'
         f'<tspan fill="{C["teal"]}">●</tspan> conexão estável · Porto Alegre, RS</text>']
    return frame(W, H, "\n  ".join(b), title="Obrigado pela visita")


if __name__ == "__main__":
    import sys
    write(sys.argv[1] + "/stats.svg", stats())
    write(sys.argv[1] + "/footer.svg", footer())
