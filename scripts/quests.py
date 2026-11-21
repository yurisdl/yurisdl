from common import C, frame, esc, write, header, SANS

W, H = 860, 340


def X(year):
    return 44 + (year - 2019) * 108


def quests():
    b = [header(24, 34, "LOG DE MISSÕES")]
    b.append(f'<text x="{W-24}" y="34" font-size="11.5" fill="{C["dim"]}" text-anchor="end">'
             f'<tspan fill="{C["amber"]}">■</tspan> em andamento</text>')
    ay = 292
    # grade de anos
    for yr in range(2019, 2027):
        x = X(yr)
        b.append(f'<path d="M{x} 52V{ay}" stroke="{C["line"]}" stroke-dasharray="2 4"/>')
        b.append(f'<text x="{x}" y="{ay+24}" font-size="12" fill="{C["dim"] if yr < 2026 else C["teal"]}" text-anchor="middle" font-weight="{700 if yr==2026 else 400}">{yr}</text>')
        b.append(f'<circle cx="{x}" cy="{ay}" r="3.5" fill="{C["faint"]}"/>')
    # eixo desenhando
    b.append(f'<path d="M{X(2019)-20} {ay}H{W-20}" stroke="{C["teal"]}" stroke-width="2" stroke-dasharray="{W}" stroke-dashoffset="{W}">'
             f'<animate attributeName="stroke-dashoffset" from="{W}" to="0" dur="1.6s" begin=".2s" fill="freeze"/></path>')

    lanes = [
        # (y, y0, y1, titulo, subt, cor, em_andamento)
        (60, 2019, 2025, "Ciência da Computação · UNIFIN", "bacharelado", C["violet"], False),
        (100, 2020, 2026.6, "Nation Resources · Fundador & Dev", "produtos FiveM de ponta a ponta", C["amber"], True),
        (140, 2024, 2025, "Hype Roleplay", "full stack · garagem", C["sky"], False),
        (180, 2024.55, 2025, "TCC: chatbot WhatsApp com NLP", "", C["lime"], False),
    ]
    for i, (y, a, z, t, s, col, live) in enumerate(lanes):
        x0, x1 = X(a), min(X(z), W - 24)
        w = x1 - x0
        d = 0.6 + i * 0.35
        fill = "url(#stripes)" if live else col
        g = [f'<rect x="{x0}" y="{y}" width="{w:.0f}" height="28" rx="6" fill="{col}" fill-opacity=".14" stroke="{col}" stroke-opacity=".7"/>',
             f'<rect x="{x0}" y="{y}" width="{w:.0f}" height="28" rx="6" fill="{fill}" fill-opacity="{1 if live else .0}"/>',
             f'<rect x="{x0}" y="{y}" width="4" height="28" rx="2" fill="{col}"/>']
        inside = w > len(t) * 7 + 30
        if inside:
            g.append(f'<text x="{x0+14}" y="{y+18.5}" font-size="12" fill="{C["text"]}" font-weight="700">{esc(t)}'
                     + (f'<tspan fill="{C["dim"]}" font-weight="400">  ·  {esc(s)}</tspan>' if s and w > (len(t) + len(s)) * 7 + 50 else "") + '</text>')
        else:
            g.append(f'<text x="{x0-10}" y="{y+18.5}" font-size="12" fill="{C["text"]}" font-weight="700" text-anchor="end">{esc(t)}'
                     + (f'<tspan fill="{C["dim"]}" font-weight="400">  ·  {esc(s)}</tspan>' if s else "") + '</text>')
        if live:
            g.append(f'<circle cx="{x1-14}" cy="{y+14}" r="4" fill="{C["amber"]}" class="pulse"/>')
        b.append(f'<g class="grow" style="animation-delay:{d:.2f}s">' + "".join(g) + "</g>")

    # conquista desbloqueada (formatura)
    tx, ty, tw, th = X(2025) - 384, 222, 372, 50
    b.append(f'<g class="toast" style="animation-delay:2.4s">'
             f'<path d="M{tx+tw} {ty+th/2}H{X(2025)}" stroke="{C["amber"]}" stroke-dasharray="3 3"/>'
             f'<circle cx="{X(2025)}" cy="{ty+th/2}" r="4" fill="{C["amber"]}"/>'
             f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="10" fill="{C["panel2"]}" stroke="{C["amber"]}" stroke-opacity=".8"/>'
             f'<g transform="translate({tx+14},{ty+11})">'
             f'<path d="M4 2H24V9A10 10 0 0 1 4 9Z" fill="{C["amber"]}"/>'
             f'<path d="M4 4H0V7A5 5 0 0 0 5 12M24 4H28V7A5 5 0 0 1 23 12" fill="none" stroke="{C["amber"]}" stroke-width="2"/>'
             f'<rect x="12" y="18" width="4" height="6" fill="{C["amber"]}"/><rect x="7" y="24" width="14" height="4" rx="1" fill="{C["amber"]}"/></g>'
             f'<text x="{tx+56}" y="{ty+21}" font-size="10.5" fill="{C["amber"]}" letter-spacing="1.5" font-weight="700">CONQUISTA DESBLOQUEADA</text>'
             f'<text x="{tx+56}" y="{ty+39}" font-size="12.5" class="sans" fill="{C["text"]}">Honra ao mérito: melhor média dos formandos</text>'
             f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="10" fill="url(#toastShine)" opacity="0">'
             f'<animate attributeName="opacity" values="0;1;0" dur="1.2s" begin="2.9s" fill="freeze"/></rect></g>')

    # você está aqui
    x = X(2026)
    b.append(f'<g class="fade" style="animation-delay:2s">'
             f'<circle cx="{x}" cy="{ay}" r="6" fill="{C["teal"]}"/>'
             f'<circle cx="{x}" cy="{ay}" r="6" fill="none" stroke="{C["teal"]}" stroke-width="2">'
             f'<animate attributeName="r" values="6;18" dur="1.8s" repeatCount="indefinite"/>'
             f'<animate attributeName="opacity" values="1;0" dur="1.8s" repeatCount="indefinite"/></circle>'
             f'<rect x="{x-94}" y="{ay-58}" width="124" height="24" rx="6" fill="{C["teal2"]}" fill-opacity=".15" stroke="{C["teal"]}" stroke-opacity=".7"/>'
             f'<text x="{x-32}" y="{ay-41.5}" font-size="11.5" fill="{C["teal"]}" text-anchor="middle">próxima missão<tspan class="blink">_</tspan></text>'
             f'<path d="M{x} {ay-34}V{ay-8}" stroke="{C["teal"]}" stroke-dasharray="2 3"/></g>')

    style = """.grow { opacity: 0; transform-box: fill-box; transform-origin: left center; animation: grow .7s cubic-bezier(.2,.8,.2,1) forwards; }
  @keyframes grow { from { opacity: 0; transform: scaleX(.05); } to { opacity: 1; transform: scaleX(1); } }
  .toast { opacity: 0; animation: toast .6s cubic-bezier(.2,1.4,.4,1) forwards; }
  @keyframes toast { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: translateY(0); } }"""
    defs = f'''
  <pattern id="stripes" width="16" height="28" patternUnits="userSpaceOnUse" patternTransform="skewX(-30)">
    <rect width="16" height="28" fill="{C['amber']}" fill-opacity=".14"/>
    <rect width="8" height="28" fill="{C['amber']}" fill-opacity=".14"/>
    <animateTransform attributeName="patternTransform" type="translate" from="0 0" to="16 0" dur=".8s" repeatCount="indefinite" additive="sum"/>
  </pattern>
  <linearGradient id="toastShine" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="{C['amber']}" stop-opacity=".25"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'''
    return frame(W, H, "\n  ".join(b), style=style, defs=defs,
                 title="Linha do tempo: Ciência da Computação na UNIFIN (2019 a 2025), Nation Resources (2020 até hoje), Hype Roleplay (2024 a 2025), TCC e honra ao mérito")


if __name__ == "__main__":
    import sys
    write(sys.argv[1] + "/quests.svg", quests())
