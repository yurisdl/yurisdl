from common import C, frame, esc, write, header

W, H = 860, 356
BW, BH = 160, 74


def box(x, y, title, sub, tech, col, delay):
    return (f'<g class="rise" style="animation-delay:{delay:.2f}s">'
            f'<rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="10" fill="{C["panel"]}" stroke="{col}" stroke-opacity=".55"/>'
            f'<rect x="{x}" y="{y+12}" width="3" height="{BH-24}" rx="1.5" fill="{col}"/>'
            f'<text x="{x+16}" y="{y+25}" font-size="13.5" font-weight="700" class="sans" fill="{C["text"]}">{esc(title)}</text>'
            f'<text x="{x+16}" y="{y+44}" font-size="11" fill="{C["dim"]}">{esc(sub)}</text>'
            f'<text x="{x+16}" y="{y+62}" font-size="11" fill="{col}">{esc(tech)}</text></g>')


def packet(pid, col, dur, begin, r=4, rev=False):
    kp = ' keyPoints="1;0" keyTimes="0;1"' if rev else ""
    return (f'<circle r="{r}" fill="{col}" opacity="0">'
            f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.85;1" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/>'
            f'<animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite" calcMode="linear"{kp}><mpath href="#{pid}"/></animateMotion></circle>'
            f'<circle r="{r*2.4}" fill="{col}" opacity="0">'
            f'<animate attributeName="opacity" values="0;.18;.18;0" keyTimes="0;.1;.85;1" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/>'
            f'<animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite" calcMode="linear"{kp}><mpath href="#{pid}"/></animateMotion></circle>')


def arch():
    xs = [20, 240, 460, 680]
    y1, y2 = 84, 236
    b = [header(24, 34, "COMO MEUS PRODUTOS RODAM")]
    # fronteira da infraestrutura
    b.append(f'<g class="fade" style="animation-delay:.2s">'
             f'<rect x="{xs[2]-14}" y="{y1-22}" width="{xs[3]+BW-xs[2]+28}" height="{BH+36}" rx="12" fill="{C["teal2"]}" fill-opacity=".04" stroke="{C["teal"]}" stroke-opacity=".4" stroke-dasharray="5 5">'
             f'<animate attributeName="stroke-dashoffset" from="0" to="-20" dur="1.5s" repeatCount="indefinite"/></rect>'
             f'<text x="{xs[2]}" y="{y1-8}" font-size="10.5" fill="{C["teal"]}" letter-spacing=".5">VPS · Cloudflare · Apache/Nginx</text></g>')

    paths = {
        "p1": f"M{xs[0]+BW} {y1+BH/2}H{xs[1]}",
        "p2": f"M{xs[1]+BW} {y1+BH/2}H{xs[2]}",
        "p3": f"M{xs[2]+BW} {y1+BH/2}H{xs[3]}",
        "p4": f"M{xs[0]+BW} {y2+BH/2}H{xs[1]}",
        "p5": f"M{xs[1]+BW} {y2+BH/2}H{xs[2]+50}V{y1+BH}",
        "p6": f"M{xs[2]+BW-50} {y1+BH}V{y2+BH/2}H{xs[3]}",
    }
    for i, (pid, d) in enumerate(paths.items()):
        b.append(f'<path id="{pid}" d="{d}" fill="none" stroke="{C["line"]}" stroke-width="2"/>')
        b.append(f'<path d="{d}" fill="none" stroke="{C["faint"]}" stroke-width="2" stroke-dasharray="2 6">'
                 f'<animate attributeName="stroke-dashoffset" from="16" to="0" dur="1s" repeatCount="indefinite"/></path>')

    def lbl(x, y, t, anchor="middle"):
        return (f'<g class="fade" style="animation-delay:1.2s"><rect x="{x - (len(t)*6.3+12)/2 if anchor=="middle" else x-4}" y="{y-11}" width="{len(t)*6.3+12}" height="16" rx="8" fill="{C["bg1"]}"/>'
                f'<text x="{x if anchor=="middle" else x+2}" y="{y+1}" font-size="10.5" fill="{C["dim"]}" text-anchor="{anchor}">{esc(t)}</text></g>')

    mid = lambda a: a + BW + 30
    b.append(lbl(mid(xs[0]), y1 + BH / 2 - 14, "evento"))
    b.append(lbl(mid(xs[1]), y1 + BH / 2 - 14, "licença"))
    b.append(lbl(mid(xs[2]), y1 + BH / 2 - 14, "query"))
    b.append(lbl(mid(xs[0]), y2 + BH / 2 - 14, "compra"))
    b.append(lbl(xs[2] + 50 - 40, y2 - 30, "webhook"))
    b.append(lbl(xs[2] + BW - 50 + 52, y2 - 30, "entrega + log"))

    b.append(box(xs[0], y1, "Jogador", "cliente FiveM", "Lua · NUI", C["sky"], .3))
    b.append(box(xs[1], y1, "Servidor do jogo", "resources server-side", "Lua", C["sky"], .45))
    b.append(box(xs[2], y1, "Nation API", "auth e licenças", "Node.js · Express", C["teal"], .6))
    b.append(box(xs[3], y1, "Banco de dados", "dados dos produtos", "MySQL · MariaDB", C["amber"], .75))
    b.append(box(xs[0], y2, "Cliente", "loja e checkout", "HTML · CSS · JS", C["sky"], .9))
    b.append(box(xs[1], y2, "Mercado Pago", "pagamentos", "API + webhooks", C["lime"], 1.05))
    b.append(box(xs[3], y2, "Discord", "bot e webhooks", "entregas e logs", C["violet"], 1.2))

    # pacotes trafegando
    b.append(packet("p1", C["sky"], 1.6, 1.4))
    b.append(packet("p2", C["teal"], 1.6, 2.0))
    b.append(packet("p2", C["lime"], 1.6, 2.8, r=3, rev=True))
    b.append(packet("p3", C["amber"], 1.6, 2.6))
    b.append(packet("p3", C["amber"], 1.6, 3.4, r=3, rev=True))
    b.append(packet("p4", C["sky"], 1.8, 1.8))
    b.append(packet("p5", C["lime"], 2.4, 2.4))
    b.append(packet("p6", C["violet"], 2.4, 3.6))

    b.append(f'<text x="{W/2}" y="{H-16}" font-size="11" fill="{C["faint"]}" text-anchor="middle">do código Lua dentro do jogo até a infraestrutura que mantém tudo no ar</text>')
    return frame(W, H, "\n  ".join(b),
                 title="Arquitetura: jogador e servidor FiveM em Lua, API própria em Node.js e Express para auth e licenças, MySQL, Mercado Pago e Discord")


if __name__ == "__main__":
    import sys
    write(sys.argv[1] + "/architecture.svg", arch())
