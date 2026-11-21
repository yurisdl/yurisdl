import re
from common import C, frame, dots, esc, write

W = 860
KW = {"local", "function", "return", "end", "true", "false", "nil"}


def hl(line):
    """Destaque de sintaxe Lua bem simples -> tspans."""
    out = []
    m = re.search(r"--.*$", line)
    comment = ""
    if m and not re.search(r'"[^"]*--', line[:m.start() + 2]):
        comment = line[m.start():]
        line = line[:m.start()]
    for tok in re.findall(r'"[^"]*"|\b\w+\b(?=\s*=(?!=))|\b\w+\b|\s+|.', line):
        if tok.startswith('"'):
            col = C["lime"]
        elif tok in KW:
            col = C["violet"]
        elif re.fullmatch(r"\d+", tok):
            col = C["amber"]
        elif re.fullmatch(r"\w+", tok) and re.search(re.escape(tok) + r"\s*=(?!=)", line):
            col = C["sky"]
        elif tok in "{}()[],.:=":
            col = C["dim"]
        else:
            col = C["text"]
        out.append(f'<tspan fill="{col}">{esc(tok)}</tspan>')
    if comment:
        out.append(f'<tspan fill="{C["faint"]}" font-style="italic">{esc(comment)}</tspan>')
    return "".join(out)


LINES = [
    "-- yuri.lua · resource principal deste perfil",
    "local Yuri = {",
    '    nome        = "Yuri Souza de Lima",',
    '    cargo       = "Desenvolvedor de Software",',
    '    foco        = { "back-end", "APIs", "infraestrutura" },',
    '    base        = "Porto Alegre, RS",',
    '    formacao    = "Ciência da Computação · UNIFIN",',
    '    destaque    = "Melhor média entre os formandos",',
    "    experiencia = 5, -- anos criando produtos para FiveM",
    '    idiomas     = { pt = "nativo", en = "intermediário", es = "básico" },',
    "}",
    "",
    "function Yuri:agora()",
    '    return "evoluindo a Nation Resources e aberto a novos desafios"',
    "end",
]


def about():
    lh = 21
    top = 64
    H = top + len(LINES) * lh + 46
    b = []
    b.append(f'<rect x="0" y="0" width="{W}" height="36" fill="{C["bg0"]}"/>')
    b.append(dots(20, 18))
    # abas
    b.append(f'<rect x="80" y="6" width="104" height="30" rx="6" fill="{C["bg1"]}"/>'
             f'<rect x="80" y="34" width="104" height="2" fill="{C["teal"]}"/>'
             f'<text x="96" y="25" font-size="12" fill="{C["text"]}"><tspan fill="{C["sky"]}">◆</tspan> yuri.lua</text>'
             f'<text x="204" y="25" font-size="12" fill="{C["faint"]}"><tspan fill="{C["faint"]}">◆</tspan> fxmanifest.lua</text>'
             f'<text x="360" y="25" font-size="12" fill="{C["faint"]}">{{}} package.json</text>')
    # gutter
    b.append(f'<rect x="0" y="36" width="52" height="{H-36-26}" fill="{C["bg0"]}" opacity=".55"/>')
    cw = 7.75
    t = 0.3
    last_y = top
    for i, ln in enumerate(LINES):
        y = top + i * lh + 6
        b.append(f'<text x="38" y="{y}" font-size="12" fill="{C["faint"]}" text-anchor="end">{i+1}</text>')
        if not ln:
            t += 0.1
            continue
        dur = max(0.25, len(ln) * 0.012)
        b.append(f'<clipPath id="l{i}"><rect x="64" y="{y-15}" height="20" width="0">'
                 f'<animate attributeName="width" from="0" to="{len(ln)*cw+20:.0f}" dur="{dur:.2f}s" begin="{t:.2f}s" fill="freeze"/></rect></clipPath>')
        b.append(f'<text x="64" y="{y}" font-size="13" xml:space="preserve" clip-path="url(#l{i})">{hl(ln)}</text>')
        t += dur + 0.06
        last_y = y
    # cursor no fim
    end_x = 64 + len(LINES[-1]) * cw + 2
    b.append(f'<rect x="{end_x:.0f}" y="{last_y-13}" width="2" height="17" fill="{C["teal"]}" opacity="0">'
             f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.01;.5;.51" dur="1s" begin="{t:.2f}s" repeatCount="indefinite"/></rect>')
    # barra de status
    sy = H - 26
    b.append(f'<rect x="0" y="{sy}" width="{W}" height="26" fill="{C["teal2"]}" fill-opacity=".14"/>'
             f'<path d="M0 {sy}H{W}" stroke="{C["line"]}"/>'
             f'<circle cx="20" cy="{sy+13}" r="4" fill="{C["teal"]}" class="pulse"/>'
             f'<text x="32" y="{sy+17}" font-size="11" fill="{C["teal"]}">nation:prod</text>'
             f'<text x="130" y="{sy+17}" font-size="11" fill="{C["dim"]}">main ✓</text>'
             f'<text x="{W-16}" y="{sy+17}" font-size="11" fill="{C["dim"]}" text-anchor="end">Ln {len(LINES)}, Col 4   ·   Lua   ·   UTF-8   ·   LF</text>')
    return frame(W, H, "\n  ".join(b), title="Sobre mim: Yuri Souza de Lima, desenvolvedor de software em Porto Alegre, formado em Ciência da Computação")


if __name__ == "__main__":
    import sys
    write(sys.argv[1] + "/about.svg", about())
