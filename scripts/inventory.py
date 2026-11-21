from common import C, frame, esc, write, header

W = 860
CATS = [
    ("Back-end", C["teal"]),
    ("Front-end", C["sky"]),
    ("Banco de dados", C["amber"]),
    ("Integrações", C["violet"]),
    ("Infra", C["rose"]),
    ("Ferramentas", C["lime"]),
    ("Em evolução", C["dim"]),
]
COL = dict(CATS)

ITEMS = [
    ("Lua", "Lua", "Back-end"),
    ("Node.js", "Nd", "Back-end"),
    ("Express.js", "ex", "Back-end"),
    ("API REST", "</>", "Back-end"),
    ("FiveM", "5M", "Back-end"),
    ("JavaScript", "JS", "Front-end"),
    ("HTML5", "H5", "Front-end"),
    ("CSS3", "C3", "Front-end"),
    ("NUI", "NUI", "Front-end"),
    ("jQuery", "$", "Front-end"),
    ("MySQL", "SQL", "Banco de dados"),
    ("MariaDB", "MDB", "Banco de dados"),
    ("Discord API", "DC", "Integrações"),
    ("Webhooks", "WH", "Integrações"),
    ("Mercado Pago", "MP", "Integrações"),
    ("VPS", "VPS", "Infra"),
    ("Linux", "LNX", "Infra"),
    ("Nginx", "NGX", "Infra"),
    ("Apache", "APH", "Infra"),
    ("Cloudflare", "CF", "Infra"),
    ("Git", "git", "Ferramentas"),
    ("GitHub", "GH", "Ferramentas"),
    ("TypeScript", "TS", "Em evolução"),
    ("Bun", "Bun", "Em evolução"),
    ("PostgreSQL", "PG", "Em evolução"),
    ("Docker", "DK", "Em evolução"),
]

NCOL, S, G = 9, 82, 10


def inventory():
    gx = (W - (NCOL * S + (NCOL - 1) * G)) / 2
    gy = 96
    rows = (len(ITEMS) + 1 + NCOL - 1) // NCOL
    H = gy + rows * (S + G) + 18
    b = [header(gx, 36, "INVENTÁRIO DE SKILLS")]
    # capacidade
    cap_w = 170
    used = len(ITEMS)
    total = rows * NCOL
    b.append(f'<text x="{W-gx}" y="36" font-size="12" fill="{C["dim"]}" text-anchor="end">{used}/{total} slots</text>')
    b.append(f'<rect x="{W-gx-cap_w-84}" y="27" width="{cap_w}" height="10" rx="5" fill="{C["bg0"]}" stroke="{C["line"]}"/>')
    b.append(f'<rect x="{W-gx-cap_w-84}" y="27" width="0" height="10" rx="5" fill="url(#capGrad)">'
             f'<animate attributeName="width" from="0" to="{cap_w*used/total:.0f}" dur="1.6s" begin=".3s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1" keyTimes="0;1"/></rect>')
    # legenda
    lx = gx
    for i, (name, col) in enumerate(CATS):
        dash = ' stroke-dasharray="3 2"' if name == "Em evolução" else ""
        b.append(f'<g class="fade" style="animation-delay:{0.1+i*0.06:.2f}s">'
                 f'<rect x="{lx}" y="56" width="10" height="10" rx="2" fill="{col}" fill-opacity=".25" stroke="{col}"{dash}/>'
                 f'<text x="{lx+16}" y="65" font-size="11.5" fill="{C["dim"]}">{esc(name)}</text></g>')
        lx += 16 + len(name) * 7.1 + 22

    clip = []
    for i in range(total):
        r, c = divmod(i, NCOL)
        x = gx + c * (S + G)
        y = gy + r * (S + G)
        clip.append(f'<rect x="{x}" y="{y}" width="{S}" height="{S}" rx="8"/>')
        d = 0.35 + i * 0.045
        if i >= len(ITEMS):
            b.append(f'<g class="pop" style="animation-delay:{d:.2f}s">'
                     f'<rect x="{x}" y="{y}" width="{S}" height="{S}" rx="8" fill="{C["bg0"]}" stroke="{C["line"]}" stroke-dasharray="4 4"/>'
                     f'<text x="{x+S/2}" y="{y+S/2+2}" font-size="22" fill="{C["faint"]}" text-anchor="middle">+</text>'
                     f'<text x="{x+S/2}" y="{y+S-12}" font-size="10" fill="{C["faint"]}" text-anchor="middle">próximo</text></g>')
            continue
        name, glyph, cat = ITEMS[i]
        col = COL[cat]
        new = cat == "Em evolução"
        stroke = f'stroke="{col}" stroke-opacity=".9" stroke-dasharray="4 3"' if new else f'stroke="{col}" stroke-opacity=".45"'
        g = [f'<rect x="{x}" y="{y}" width="{S}" height="{S}" rx="8" fill="{C["panel"]}" {stroke}/>',
             f'<rect x="{x}" y="{y}" width="{S}" height="{S}" rx="8" fill="url(#slotShade)"/>']
        if not new:
            g.append(f'<path d="M{x+S-22} {y}H{x+S-8}A8 8 0 0 1 {x+S} {y+8}V{y+22}Z" fill="{col}" opacity=".85"/>')
            g.append(f'<rect x="{x+10}" y="{y+S-7}" width="{S-20}" height="3" rx="1.5" fill="{col}" opacity=".7"/>')
        else:
            g.append(f'<rect x="{x+S-32}" y="{y+6}" width="26" height="13" rx="3" fill="{C["amber"]}" class="pulse"/>'
                     f'<text x="{x+S-19}" y="{y+16}" font-size="8.5" font-weight="700" fill="{C["bg0"]}" text-anchor="middle">NEW</text>')
        fs = 17 if len(glyph) <= 2 else 14
        g.append(f'<circle cx="{x+S/2}" cy="{y+33}" r="19" fill="{col}" fill-opacity=".13" stroke="{col}" stroke-opacity=".5"/>')
        g.append(f'<text x="{x+S/2}" y="{y+33+fs*0.36:.1f}" font-size="{fs}" font-weight="700" fill="{col}" text-anchor="middle">{esc(glyph)}</text>')
        nfs = 10.5 if len(name) <= 10 else 9.5
        g.append(f'<text x="{x+S/2}" y="{y+S-16}" font-size="{nfs}" fill="{C["text"]}" text-anchor="middle">{esc(name)}</text>')
        b.append(f'<g class="pop" style="animation-delay:{d:.2f}s">' + "".join(g) + "</g>")

    # brilho passando pelos slots
    b.append(f'<clipPath id="slots">{"".join(clip)}</clipPath>')
    b.append(f'<g clip-path="url(#slots)"><rect x="-200" y="{gy}" width="140" height="{rows*(S+G)}" fill="url(#shine)" transform="skewX(-20)">'
             f'<animate attributeName="x" values="-200;{W+300};{W+300}" keyTimes="0;.45;1" dur="5s" begin="2.2s" repeatCount="indefinite"/></rect></g>')

    style = """.pop { opacity: 0; transform-box: fill-box; transform-origin: center; animation: pop .45s cubic-bezier(.3,1.6,.5,1) forwards; }
  @keyframes pop { from { opacity: 0; transform: scale(.6); } to { opacity: 1; transform: scale(1); } }"""
    defs = f'''
  <linearGradient id="capGrad" x1="0" x2="1"><stop offset="0" stop-color="{C['teal2']}"/><stop offset="1" stop-color="{C['sky']}"/></linearGradient>
  <linearGradient id="slotShade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".04"/><stop offset="1" stop-color="#000" stop-opacity=".18"/></linearGradient>
  <linearGradient id="shine" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".09"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'''
    return frame(W, H, "\n  ".join(b), style=style, defs=defs,
                 title="Inventário de skills: Lua, Node.js, Express, JavaScript, MySQL, MariaDB, Discord API, Mercado Pago, VPS, Linux, Nginx, Git e mais")


if __name__ == "__main__":
    import sys
    write(sys.argv[1] + "/skills.svg", inventory())
