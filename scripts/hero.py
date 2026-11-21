from common import C, frame, dots, esc, write, SANS

W, H = 860, 330


def hero():
    b = []
    # brilho de fundo
    b.append(f'<circle cx="700" cy="40" r="260" fill="url(#glow)" opacity=".55"/>')
    # ---- console à esquerda ----
    px, py, pw, ph = 20, 20, 486, 290
    b.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="10" fill="{C["bg0"]}" stroke="{C["line"]}"/>')
    b.append(f'<path d="M{px} {py+30}H{px+pw}" stroke="{C["line"]}"/>')
    b.append(dots(px + 18, py + 15))
    b.append(f'<text x="{px+pw/2+20}" y="{py+19}" font-size="11" fill="{C["dim"]}" text-anchor="middle">server console · nation:prod</text>')

    cmd = "ensure yuri-lima"
    cw = 8.2
    x0 = px + 16
    y = py + 56
    steps = ";".join(str(round(i * cw, 1)) for i in range(len(cmd) + 1))
    b.append(f'<clipPath id="typeClip"><rect x="{x0+16}" y="{y-14}" height="20" width="0">'
             f'<animate attributeName="width" values="{steps}" dur="1.1s" begin="0.4s" fill="freeze" calcMode="discrete"/></rect></clipPath>')
    b.append(f'<text x="{x0}" y="{y}" font-size="13" fill="{C["teal"]}" font-weight="700">$</text>')
    b.append(f'<text x="{x0+16}" y="{y}" font-size="13" fill="{C["text"]}" clip-path="url(#typeClip)">{cmd}</text>')

    logs = [
        ("boot", "Ciência da Computação · UNIFIN", C["violet"]),
        ("lua", "runtime client/server carregado", C["sky"]),
        ("api", "auth · licenças · versões :3000", C["teal"]),
        ("db", "pool MySQL/MariaDB pronto", C["amber"]),
        ("discord", "bot e webhooks conectados", C["violet"]),
        ("pay", "Mercado Pago ouvindo webhooks", C["lime"]),
        ("infra", "VPS · Cloudflare · Apache/Nginx", C["sky"]),
    ]
    t0 = 1.7
    for i, (tag, msg, col) in enumerate(logs):
        yy = y + 28 + i * 24
        d = t0 + i * 0.32
        b.append(f'<g class="fade" style="animation-delay:{d:.2f}s">'
                 f'<text x="{x0}" y="{yy}" font-size="12.5" fill="{C["faint"]}">[<tspan fill="{col}">{tag:>7}</tspan>]</text>'
                 f'<text x="{x0+86}" y="{yy}" font-size="12.5" fill="{C["dim"]}">{esc(msg)}</text>'
                 f'<text x="{px+pw-16}" y="{yy}" font-size="12.5" fill="{C["teal"]}" text-anchor="end" font-weight="700">ok</text></g>')
    yy = y + 28 + len(logs) * 24 + 6
    d = t0 + len(logs) * 0.32 + 0.3
    b.append(f'<g class="fade" style="animation-delay:{d:.2f}s">'
             f'<text x="{x0}" y="{yy}" font-size="13" fill="{C["teal"]}" font-weight="700">&gt; <tspan fill="{C["text"]}">servidor online · uptime 5+ anos</tspan></text>'
             f'<rect x="{x0+276}" y="{yy-12}" width="8" height="15" fill="{C["teal"]}" class="blink"/></g>')

    # ---- identidade à direita ----
    rx = 536
    b.append(f'<g class="rise" style="animation-delay:.2s">'
             f'<text x="{rx}" y="62" font-size="12" fill="{C["faint"]}" letter-spacing="2">// PLAYER CONECTADO</text></g>')
    b.append(f'<g class="rise" style="animation-delay:.35s">'
             f'<text x="{rx-2}" y="112" font-size="46" font-weight="800" class="sans" fill="url(#nameGrad)" letter-spacing="-1">Yuri Lima</text></g>')
    b.append(f'<g class="rise" style="animation-delay:.5s">'
             f'<text x="{rx}" y="138" font-size="13" fill="{C["dim"]}">Yuri Souza de Lima</text></g>')
    b.append(f'<g class="rise" style="animation-delay:.65s">'
             f'<text x="{rx}" y="172" font-size="17" class="sans" font-weight="600" fill="{C["text"]}">Desenvolvedor de Software</text>'
             f'<text x="{rx}" y="194" font-size="13" class="sans" fill="{C["dim"]}">Full stack com foco em back-end</text></g>')
    tags = [("Lua", C["sky"]), ("Node.js", C["lime"]), ("FiveM", C["amber"]), ("APIs", C["teal"])]
    tx = rx
    for i, (t, col) in enumerate(tags):
        w = len(t) * 7.6 + 18
        b.append(f'<g class="rise" style="animation-delay:{0.8+i*0.1:.2f}s">'
                 f'<rect x="{tx}" y="210" width="{w}" height="22" rx="11" fill="{col}" fill-opacity=".12" stroke="{col}" stroke-opacity=".6"/>'
                 f'<text x="{tx+w/2}" y="225" font-size="12" fill="{col}" text-anchor="middle">{t}</text></g>')
        tx += w + 8

    # status + localização
    b.append(f'<g class="fade" style="animation-delay:1.2s">'
             f'<circle cx="{rx+5}" cy="263" r="5" fill="{C["teal"]}" class="pulse"/>'
             f'<text x="{rx+18}" y="267" font-size="12" fill="{C["text"]}">online</text>'
             f'<text x="{rx}" y="290" font-size="12" fill="{C["dim"]}">Porto Alegre, RS · BR</text></g>')

    # radar / minimapa
    cx, cy, r = 798, 276, 38
    b.append(f'<g class="fade" style="animation-delay:1s">'
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["bg0"]}" stroke="{C["line"]}" stroke-width="1.5"/>'
             f'<circle cx="{cx}" cy="{cy}" r="{r*0.66:.1f}" fill="none" stroke="{C["line"]}"/>'
             f'<circle cx="{cx}" cy="{cy}" r="{r*0.33:.1f}" fill="none" stroke="{C["line"]}"/>'
             f'<path d="M{cx-r} {cy}H{cx+r}M{cx} {cy-r}V{cy+r}" stroke="{C["line"]}"/>'
             f'<g><path d="M{cx} {cy}L{cx} {cy-r}A{r} {r} 0 0 1 {cx+r*0.7071:.1f} {cy-r*0.7071:.1f}Z" fill="url(#sweep)"/>'
             f'<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="4s" repeatCount="indefinite"/></g>'
             f'<circle cx="{cx+14}" cy="{cy+12}" r="4" fill="{C["teal"]}"><animate attributeName="opacity" values="1;.2;1" dur="2s" repeatCount="indefinite"/></circle>'
             f'<circle cx="{cx+14}" cy="{cy+12}" r="4" fill="none" stroke="{C["teal"]}">'
             f'<animate attributeName="r" values="4;14" dur="2s" repeatCount="indefinite"/>'
             f'<animate attributeName="opacity" values=".9;0" dur="2s" repeatCount="indefinite"/></circle>'
             f'<circle cx="{cx-18}" cy="{cy-20}" r="2.5" fill="{C["amber"]}" opacity=".8"/>'
             f'<circle cx="{cx-26}" cy="{cy+18}" r="2.5" fill="{C["sky"]}" opacity=".8"/>'
             f'</g>')

    # scanline
    b.append(f'<rect x="0" y="-40" width="{W}" height="40" fill="url(#scan)" opacity=".5">'
             f'<animate attributeName="y" values="-40;{H}" dur="6s" repeatCount="indefinite"/></rect>')

    defs = f'''
  <linearGradient id="nameGrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{C['teal']}"/>
    <stop offset=".5" stop-color="{C['sky']}"/>
    <stop offset="1" stop-color="{C['teal']}"/>
    <animate attributeName="x1" values="0;-1;0" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="x2" values="1;2;1" dur="6s" repeatCount="indefinite"/>
  </linearGradient>
  <radialGradient id="glow"><stop offset="0" stop-color="{C['teal2']}" stop-opacity=".35"/><stop offset="1" stop-color="{C['teal2']}" stop-opacity="0"/></radialGradient>
  <linearGradient id="sweep" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="{C['teal']}" stop-opacity="0"/><stop offset="1" stop-color="{C['teal']}" stop-opacity=".55"/></linearGradient>
  <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{C['teal']}" stop-opacity="0"/><stop offset="1" stop-color="{C['teal']}" stop-opacity=".07"/></linearGradient>'''
    return frame(W, H, "\n  ".join(b), defs=defs, title="Yuri Lima, desenvolvedor de software full stack com foco em back-end")


if __name__ == "__main__":
    import sys
    write(sys.argv[1] + "/hero.svg", hero())
