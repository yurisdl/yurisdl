from xml.sax.saxutils import escape as _esc

MONO = "'JetBrains Mono','Fira Code','Cascadia Code','SF Mono',Menlo,Consolas,'DejaVu Sans Mono','Courier New',monospace"
SANS = "system-ui,-apple-system,'Segoe UI','Inter','Helvetica Neue',Helvetica,Arial,sans-serif"

# paleta tirada do currículo (sidebar azul-marinho + acento verde-água)
C = dict(
    bg0="#070d19",
    bg1="#0c1527",
    panel="#101c33",
    panel2="#15243f",
    line="#1f3355",
    text="#e6edf7",
    dim="#8a9bb8",
    faint="#4a5d7e",
    teal="#2dd4bf",
    teal2="#14b8a6",
    amber="#fbbf24",
    sky="#60a5fa",
    rose="#fb7185",
    violet="#a78bfa",
    lime="#a3e635",
)


def esc(s):
    return _esc(s, {'"': "&quot;"})


def frame(w, h, body, style="", defs="", title=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}">
<title>{esc(title)}</title>
<defs>
  <linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{C['bg1']}"/>
    <stop offset="1" stop-color="{C['bg0']}"/>
  </linearGradient>
  <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
    <path d="M24 0H0V24" fill="none" stroke="{C['line']}" stroke-width="0.6" opacity="0.45"/>
  </pattern>
  <clipPath id="cardClip"><rect width="{w}" height="{h}" rx="14"/></clipPath>
  {defs}
</defs>
<style>
  text {{ font-family: {MONO}; }}
  .sans {{ font-family: {SANS}; }}
  .fade {{ opacity: 0; animation: fadeIn .5s ease-out forwards; }}
  .rise {{ opacity: 0; animation: rise .6s cubic-bezier(.2,.8,.2,1) forwards; }}
  .blink {{ animation: blink 1s steps(1) infinite; }}
  .pulse {{ animation: pulse 2s ease-in-out infinite; }}
  @keyframes fadeIn {{ to {{ opacity: 1; }} }}
  @keyframes rise {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: translateY(0); }} }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
  @keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .35; }} }}
  {style}
  @media (prefers-reduced-motion: reduce) {{
    * {{ animation-duration: 0s !important; animation-delay: 0s !important; animation-iteration-count: 1 !important; }}
  }}
</style>
<g clip-path="url(#cardClip)">
  <rect width="{w}" height="{h}" fill="url(#bgGrad)"/>
  <rect width="{w}" height="{h}" fill="url(#grid)"/>
  {body}
</g>
<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="14" fill="none" stroke="{C['line']}"/>
</svg>
'''


def header(x, y, label, color=None):
    """Título no estilo dos cabeçalhos '// Seção' do currículo."""
    color = color or C["teal"]
    return (f'<text x="{x}" y="{y}" font-size="13" fill="{color}" font-weight="700" letter-spacing="1.5">'
            f'<tspan fill="{C["faint"]}">// </tspan>{esc(label)}</text>')


def dots(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="5" fill="{C["rose"]}"/>'
            f'<circle cx="{x+16}" cy="{y}" r="5" fill="{C["amber"]}"/>'
            f'<circle cx="{x+32}" cy="{y}" r="5" fill="{C["teal"]}"/>')


def write(path, svg):
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
