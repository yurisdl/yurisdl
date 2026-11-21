from common import C, esc, write, MONO

BTNS = [
    ("linkedin", "LinkedIn", "/in/yurisdl", C["sky"],
     '<rect x="0" y="0" width="16" height="16" rx="3" fill="{c}"/>'
     '<rect x="3" y="6.5" width="2.4" height="6.5" fill="{bg}"/><circle cx="4.2" cy="4" r="1.4" fill="{bg}"/>'
     '<path d="M7.2 6.5H9.5V7.6C10 6.8 10.9 6.3 12 6.3C13.6 6.3 14 7.4 14 9V13H11.6V9.5C11.6 8.7 11.4 8.2 10.7 8.2C9.9 8.2 9.6 8.8 9.6 9.6V13H7.2Z" fill="{bg}"/>'),
    ("email", "E-mail", "yurilima01@hotmail.com", C["teal"],
     '<rect x="0" y="2" width="16" height="12" rx="2" fill="none" stroke="{c}" stroke-width="1.8"/>'
     '<path d="M1 3.5L8 9L15 3.5" fill="none" stroke="{c}" stroke-width="1.8"/>'),
    ("portfolio", "Portfólio", "youtube.com/@nation3713", C["rose"],
     '<rect x="0" y="2" width="16" height="12" rx="3.5" fill="{c}"/>'
     '<path d="M6.3 5.2V10.8L11 8Z" fill="{bg}"/>'),
]


def button(key, label, value, col, icon):
    h = 40
    w = round(58 + (len(label) + len(value) + 3) * 7.3)
    ic = icon.format(c=col, bg=C["bg0"])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}: {esc(value)}">
<title>{esc(label)}: {esc(value)}</title>
<defs>
  <linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{col}" stop-opacity="0"/><stop offset=".5" stop-color="{col}" stop-opacity=".22"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></linearGradient>
  <clipPath id="c"><rect width="{w}" height="{h}" rx="8"/></clipPath>
</defs>
<style>text {{ font-family: {MONO}; }}</style>
<g clip-path="url(#c)">
  <rect width="{w}" height="{h}" fill="{C["bg0"]}"/>
  <rect x="-80" y="0" width="80" height="{h}" fill="url(#g)"><animate attributeName="x" values="-80;{w};{w}" keyTimes="0;.4;1" dur="4s" repeatCount="indefinite"/></rect>
  <g transform="translate(16,12)">{ic}</g>
  <text x="44" y="25" font-size="12.5" font-weight="700" fill="{col}">{esc(label)}<tspan fill="{C["dim"]}" font-weight="400"> · {esc(value)}</tspan></text>
</g>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="8" fill="none" stroke="{col}" stroke-opacity=".55"/>
</svg>
'''


if __name__ == "__main__":
    import sys
    for key, label, value, col, icon in BTNS:
        write(f"{sys.argv[1]}/btn-{key}.svg", button(key, label, value, col, icon))
