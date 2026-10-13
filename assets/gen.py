KO = "Pretendard, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
EN = "'Arial Black', 'Helvetica Neue', Arial, sans-serif"
EN2 = "'Helvetica Neue', Arial, Pretendard, sans-serif"
PAPER = "#F7F7F4"; MINT = "#22F5A6"; MINT_D = "#12D88F"; INK = "#000000"

def paper_defs(h):
    return f'''<defs>
  <clipPath id="card"><rect width="1200" height="{h}" rx="22"/></clipPath>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="7" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.07 0"/>
  </filter>
  <filter id="crumple" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="3" seed="3" result="n"/>
    <feDiffuseLighting in="n" lighting-color="#ffffff" surfaceScale="2.2" result="l"><feDistantLight azimuth="235" elevation="62"/></feDiffuseLighting>
    <feColorMatrix in="l" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -0.35 0 0 0 0.33"/>
  </filter>
  <filter id="blur" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="55"/></filter>
  <filter id="marker" x="-10%" y="-10%" width="120%" height="120%">
    <feTurbulence type="fractalNoise" baseFrequency="0.06" numOctaves="2" seed="2" result="t"/>
    <feDisplacementMap in="SourceGraphic" in2="t" scale="4"/>
  </filter>
</defs>'''

def paper_bg(h):
    return f'''<rect width="1200" height="{h}" fill="{PAPER}"/>
  <rect width="1200" height="{h}" filter="url(#crumple)"/>
  <rect width="1200" height="{h}" filter="url(#grain)"/>'''

def vertical(x, y, color, text="PORTFOLIO"):
    return f'<text transform="translate({x} {y}) rotate(90)" font-family="{EN}" font-weight="900" font-size="15" letter-spacing="2" fill="{color}">{text}</text>'

# ---------------- header ----------------
H = 640
anim = lambda a, b: f'<animate attributeName="stroke-dashoffset" values="1;1;0" keyTimes="0;{a};{b}" dur="2.4s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;0.4 0 0.2 1"/>'
im_paths = [
  ("M92 162 C140 150 196 140 252 133", 0.00, 0.14),
  ("M178 140 C172 186 158 232 146 276", 0.12, 0.28),
  ("M102 282 C142 272 182 266 222 262", 0.26, 0.38),
  ("M268 116 L259 160", 0.36, 0.44),
  ("M290 270 C293 240 296 214 298 196", 0.44, 0.56),
  ("M296 216 C312 186 336 184 334 222 L330 266", 0.55, 0.72),
  ("M334 220 C352 188 378 188 375 228 L370 270", 0.70, 0.88),
]
im = "\n    ".join(
  f'<path d="{d}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="0">{anim(a,b)}</path>'
  for d, a, b in im_paths)

header = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {H}" width="100%" role="img" aria-label="I'm Backend Developer. 반갑습니다. 백엔드 개발자 김시흔입니다.">
{paper_defs(H)}
<g clip-path="url(#card)">
  {paper_bg(H)}
  <g filter="url(#blur)">
    <ellipse cx="560" cy="170" rx="700" ry="300" fill="{MINT}">
      <animate attributeName="cx" values="560;600;560" dur="14s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="330" cy="420" rx="420" ry="170" fill="#5BFFC4" opacity="0.85">
      <animate attributeName="cy" values="420;400;420" dur="11s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="1040" cy="380" rx="260" ry="120" fill="{PAPER}"/>
  </g>
  <rect width="1200" height="{H}" filter="url(#grain)"/>

  <g fill="{INK}" font-family="{EN}" font-weight="900">
    <text x="92" y="372" font-size="138" textLength="680" lengthAdjust="spacingAndGlyphs">Backend</text>
    <text x="92" y="500" font-size="138" textLength="905" lengthAdjust="spacingAndGlyphs">Developer.</text>
  </g>
  <g fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round" filter="url(#marker)">
    {im}
  </g>

  <g font-family="{KO}" font-size="30" fill="{INK}">
    <text x="96" y="566">반갑습니다.</text>
    <text x="96" y="606">백엔드 개발자 <tspan font-weight="800">김시흔</tspan>입니다.</text>
  </g>
  {vertical(1146, 150, "#FFFFFF")}
  <text x="1104" y="606" text-anchor="end" font-family="{EN2}" font-weight="700" font-size="18" fill="{INK}">github.com/tlgms</text>
</g>
</svg>'''

# ---------------- about ----------------
def pill(x, y, label, outline=False):
    w = round(len(label) * 10.6 + 38)
    if outline:
        r = f'<rect x="{x+1.25}" y="{y+1.25}" width="{w-2.5}" height="37.5" rx="18.75" fill="none" stroke="{INK}" stroke-width="2.5"/>'
        c = INK
    else:
        r = f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="20" fill="{INK}"/>'
        c = "#FFFFFF"
    t = f'<text x="{x + w/2}" y="{y+26.5}" text-anchor="middle" font-family="{EN}" font-weight="900" font-size="16" fill="{c}">{label}</text>'
    return r + t, w

def pill_row(x, y, labels, outline=False, gap=10):
    out = []
    for l in labels:
        s, w = pill(x, y, l, outline); out.append(s); x += w + gap
    return "\n  ".join(out)

def heading(x, y, t):
    return f'<text x="{x}" y="{y}" font-family="{EN}" font-weight="900" font-size="28" fill="{INK}">{t}</text>'

def rows(x, y, items, lw=86, lh=31):
    out = []
    for i, (k, v) in enumerate(items):
        yy = y + i * lh
        out.append(f'<text x="{x}" y="{yy}" font-family="{EN}" font-weight="900" font-size="17" fill="{INK}">{k}</text>')
        out.append(f'<text x="{x+lw}" y="{yy}" font-family="{KO}" font-size="18" fill="{INK}">{v}</text>')
    return "\n  ".join(out)

A = 660
L, R = 136, 640
about = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {A}" width="100%" role="img" aria-label="About me: 김시흔, 백엔드 개발자를 목표로 공부하는 학생. Java, Kotlin, Spring Boot, Node.js, Express, NestJS, FastAPI, MySQL, PostgreSQL">
{paper_defs(A)}
<g clip-path="url(#card)">
  {paper_bg(A)}
  <text x="96" y="132" font-family="{EN}" font-weight="900" font-size="72" fill="{MINT_D}" transform="skewX(-10)" dx="22">#</text>
  <text x="146" y="132" font-family="{EN}" font-weight="900" font-size="72" fill="{INK}" textLength="330" lengthAdjust="spacingAndGlyphs">About me</text>
  <line x1="100" y1="128" x2="1100" y2="128" stroke="{INK}" stroke-width="2"/>

  {heading(L, 222, "Profile")}
  {rows(L, 270, [("Name","김시흔"),("GitHub","@tlgms"),("Mail","siheun9@gmail.com"),("Blog","velog.io/@siheun9")])}

  {heading(R, 222, "Focus")}
  {rows(R, 270, [("Main","Java와 Spring Boot 중심의 서버 개발"),("Learn","Node.js, Express, NestJS, FastAPI")], lw=78)}
  <text x="{R}" y="352" font-family="{KO}" font-size="18" fill="#444">백엔드 개발자를 목표로 공부하고 있는 학생입니다.</text>

  {heading(L, 452, "Skills")}
  {pill_row(L, 482, ["Java","Kotlin","Spring Boot"])}
  {pill_row(L, 532, ["Node.js","Express","NestJS","FastAPI"], outline=True)}
  <text x="{L}" y="612" font-family="{KO}" font-size="15" fill="#555">검은 배지는 주력, 테두리 배지는 함께 익히는 중인 기술</text>

  {heading(R, 452, "Database")}
  {pill_row(R, 482, ["MySQL","PostgreSQL"])}

  {vertical(1146, 420, MINT_D)}
</g>
</svg>'''

# ---------------- adaptive section titles ----------------
def title(text, desc=None, w_text=None, dark=False):
    h = 150 if desc else 120
    c = "#F0F6FC" if dark else "#000000"
    d = f'<text class="ink sub" x="104" y="140" font-family="{KO}" font-size="20">{desc}</text>' if desc else ""
    tl = f' textLength="{w_text}" lengthAdjust="spacingAndGlyphs"' if w_text else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {h}" width="100%" role="img" aria-label="{text}">
<style>
  .ink {{ fill: {c}; }} .rule {{ stroke: {c}; }} .sub {{ opacity: .7; }}
</style>
<text x="96" y="92" font-family="{EN}" font-weight="900" font-size="60" fill="{MINT_D}" transform="skewX(-10)" dx="18">#</text>
<text class="ink" x="140" y="92" font-family="{EN}" font-weight="900" font-size="60"{tl}>{text}</text>
<line class="rule" x1="100" y1="89" x2="1100" y2="89" stroke-width="2"/>
{d}
</svg>'''

# ---------------- footer ----------------
F = 200
footer = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {F}" width="100%" role="img" aria-label="Thanks for visiting">
{paper_defs(F)}
<g clip-path="url(#card)">
  {paper_bg(F)}
  <g filter="url(#blur)"><ellipse cx="980" cy="120" rx="420" ry="130" fill="{MINT}"/></g>
  <rect width="1200" height="{F}" filter="url(#grain)"/>
  <text x="96" y="118" font-family="{EN}" font-weight="900" font-size="64" fill="{INK}" textLength="640" lengthAdjust="spacingAndGlyphs">Thanks for visiting.</text>
  <text x="98" y="158" font-family="{KO}" font-size="20" fill="{INK}">읽어주셔서 감사합니다.</text>
  {vertical(1146, 40, "#FFFFFF")}
</g>
</svg>'''

files = {
  "header.svg": header, "about.svg": about, "footer.svg": footer,
  "title-contact.svg": title("Contact", w_text=250),
  "title-stats.svg": title("GitHub Stats", w_text=400),
  "title-animals.svg": title("Little Animal Zone", "개발자 프로필과 분리된, 조금 가벼운 공간", w_text=590),
}
for k, (t, d, w) in {"contact":("Contact",None,250),"stats":("GitHub Stats",None,400),
        "animals":("Little Animal Zone","개발자 프로필과 분리된, 조금 가벼운 공간",590)}.items():
    files[f"title-{k}.svg"] = title(t, d, w)
    files[f"title-{k}-dark.svg"] = title(t, d, w, dark=True)
for n, s in files.items():
    open(f"assets/{n}", "w").write(s)
