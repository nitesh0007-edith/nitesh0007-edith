"""Build the profile's original SVG artwork; no third-party image service needed."""

from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, monospace"


def svg(name, width, height, title, body, defs=""):
    document = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{name}-title">
<title id="{name}-title">{title}</title>
<defs>{defs}</defs>
<style>@media (prefers-reduced-motion: reduce) {{ .motion {{ display: none; }} }}</style>
{body}
</svg>
'''
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / f"{name}.svg").write_text(document)


def hero(mobile=False):
    name = "hero-mobile" if mobile else "hero"
    w, h = (700, 570) if mobile else (1200, 480)
    defs = '''
<linearGradient id="hero-bg" x2="1" y2="1"><stop stop-color="#0B1020"/><stop offset=".55" stop-color="#11172D"/><stop offset="1" stop-color="#1B1840"/></linearGradient>
<linearGradient id="hero-accent"><stop stop-color="#7DCFFF"/><stop offset=".5" stop-color="#7AA2F7"/><stop offset="1" stop-color="#BB9AF7"/></linearGradient>
<radialGradient id="hero-aura"><stop stop-color="#7AA2F7" stop-opacity=".2"/><stop offset="1" stop-color="#7AA2F7" stop-opacity="0"/></radialGradient>
<pattern id="hero-grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#7AA2F7" stroke-opacity=".06"/></pattern>
<filter id="hero-glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="3"/></filter>
'''
    graphic = '''
<ellipse cx="960" cy="224" rx="275" ry="250" fill="url(#hero-aura)"/>
<g fill="none" stroke="#7AA2F7">
<path d="M960 67 1096 145V301L960 379 824 301V145Z" stroke-opacity=".22"/>
<path d="M960 94 1072 159V287L960 352 848 287V159Z" stroke-opacity=".12"/>
<path d="M960 67V379M824 145 1096 301M824 301 1096 145" stroke-opacity=".1"/>
<circle cx="960" cy="223" r="101" stroke-dasharray="2 10" stroke-opacity=".35"/>
</g>
<g fill="#11182D" stroke="#7AA2F7" stroke-width="1.5">
<path d="m960 161 54 31v62l-54 31-54-31v-62Z"/>
<path d="m906 192 54 31 54-31M960 223v62" fill="none"/>
</g>
<path d="m960 161 54 31-54 31-54-31Z" fill="#7AA2F7" fill-opacity=".15"/>
<g fill="none" stroke-width="1.5">
<path id="hero-route-a" d="M780 285h48l46-62h32" stroke="#7DCFFF" stroke-opacity=".55"/>
<path id="hero-route-b" d="M1014 223h37l44-66h48" stroke="#BB9AF7" stroke-opacity=".55"/>
<path d="M960 161V124h-75l-30-29h-55M960 285v40h80l28 28h75" stroke="#7AA2F7" stroke-opacity=".35"/>
</g>
<g fill="#7DCFFF"><circle cx="780" cy="285" r="4"/><circle cx="906" cy="223" r="3"/></g>
<g fill="#BB9AF7"><circle cx="1143" cy="157" r="4"/><circle cx="1014" cy="223" r="3"/></g>
<g fill="#7AA2F7"><circle cx="800" cy="95" r="3"/><circle cx="1143" cy="353" r="3"/></g>
<g class="motion" fill="#C0E8FF">
<circle r="3"><animateMotion dur="4s" repeatCount="indefinite" path="M780 285h48l46-62h32"/></circle>
<circle r="3"><animateMotion dur="4s" begin="2s" repeatCount="indefinite" path="M1014 223h37l44-66h48"/></circle>
</g>
<g font-family="Consolas, monospace" font-size="10" letter-spacing="2" fill="#8998BD">
<text x="779" y="311">INGEST</text><text x="1068" y="139">SERVE</text>
<text x="960" y="400" text-anchor="middle">DATA → INTELLIGENCE</text>
</g>'''
    if mobile:
        graphic = '<g transform="translate(-490 -12)" opacity=".16">'+graphic+'</g>'
    text = f'''
<g font-family="{FONT}">
<g font-family="{MONO}" font-size="13" letter-spacing="2" fill="#9AA5CE"><text x="52" y="58">NRS / DEVELOPER PROFILE</text></g>
<path d="M52 83h40" stroke="#7DCFFF" stroke-width="3"/>
<text x="48" y="181" fill="#F1F5FF" font-size="82" font-weight="750" letter-spacing="-3">NITESH</text>
<text x="50" y="251" fill="url(#hero-accent)" font-size="61" font-weight="700" letter-spacing="-2">RANJAN SINGH<tspan fill="#7DCFFF">.</tspan></text>
<text x="53" y="305" fill="#C0CAF5" font-size="23">Data Engineer <tspan fill="#565F89">/</tspan> AI Engineer</text>
<text x="53" y="343" fill="#9AA5CE" font-size="17">Reliable pipelines. Grounded AI. A little main-character energy.</text>
</g>'''
    if mobile:
        text = text.replace('font-size="82"', 'font-size="91"').replace('y="181"','y="194"').replace('y="251"','y="269"').replace('y="305"','y="329"').replace('y="343"','y="374"')
        text = text.replace('A little main-character energy.', '').replace('Reliable pipelines. Grounded AI. ', 'Reliable pipelines. Grounded AI.')
    footer_y = 444 if not mobile else 526
    meta = f'''
<path d="M52 {footer_y-39}H{w-52}" stroke="#7AA2F7" stroke-opacity=".18"/>
<g font-family="{MONO}" font-size="12" letter-spacing="1.2" fill="#9AA5CE">
<circle cx="57" cy="{footer_y-4}" r="3" fill="#9ECE6A"/>
<text x="70" y="{footer_y}">GLASGOW, SCOTLAND</text>
<text x="{w-52}" y="{footer_y}" text-anchor="end">{'MSc DATA SCIENCE / UofG' if mobile else 'MSc DATA SCIENCE / UNIVERSITY OF GLASGOW'}</text></g>'''
    svg(name,w,h,"Nitesh Ranjan Singh — Data Engineer / AI Engineer, Glasgow",f'<rect width="{w}" height="{h}" rx="18" fill="url(#hero-bg)"/><rect width="{w}" height="{h}" rx="18" fill="url(#hero-grid)"/><path d="M18 .5H{w-18}" stroke="url(#hero-accent)" stroke-opacity=".8"/>'+graphic+text+meta,defs)


def impact():
    body = '<rect width="1200" height="148" rx="14" fill="#11172A" stroke="#27314D"/>'
    entries=[("10M+","RECORDS / BATCH","Data-platform engineering"),("3+ YEARS","INDUSTRY EXPERIENCE","IQVIA &amp; Axtria"),("2ND PLACE","KAGGLE / TEAM HYPERX","Agentic legal retrieval")]
    for i,(value,label,desc) in enumerate(entries):
        x=40+i*400
        if i: body+=f'<path d="M{x-20} 27v94" stroke="#27314D"/>'
        body+=f'<g font-family="{FONT}"><text x="{x}" y="55" fill="{["#7DCFFF","#BB9AF7","#E0AF68"][i]}" font-size="34" font-weight="700">{value}</text><text x="{x}" y="87" fill="#C0CAF5" font-size="13" letter-spacing="1.5">{label}</text><text x="{x}" y="115" fill="#9AA5CE" font-size="14">{desc}</text></g>'
    svg('impact',1200,148,'10M+ records per batch; 3+ years at IQVIA and Axtria; Kaggle 2nd place, Team HyperX',body)
    mobile = '<rect width="700" height="270" rx="14" fill="#11172A" stroke="#27314D"/>'
    for i,(value,label,desc) in enumerate(entries):
        y=58+i*82
        if i: mobile+=f'<path d="M28 {y-49}H672" stroke="#27314D"/>'
        mobile+=f'<g font-family="{FONT}"><text x="28" y="{y}" fill="{["#7DCFFF","#BB9AF7","#E0AF68"][i]}" font-size="34" font-weight="700">{value}</text><text x="670" y="{y-4}" fill="#C0CAF5" font-size="21" text-anchor="end">{label}</text></g>'
    svg('impact-mobile',700,270,'10M+ records per batch; 3+ years industry experience; Kaggle 2nd place',mobile)


def project(name,title,kicker,color,art):
    defs=f'<linearGradient id="{name}-bg" x2="1" y2="1"><stop stop-color="#11172A"/><stop offset="1" stop-color="#1B1C37"/></linearGradient>'
    body=f'<rect width="600" height="200" rx="12" fill="url(#{name}-bg)"/><path d="M24 1h552" stroke="{color}" stroke-opacity=".7"/>{art}<g font-family="{FONT}"><text x="28" y="137" fill="{color}" font-size="11" letter-spacing="2.5">{kicker}</text><text x="26" y="176" fill="#F1F5FF" font-size="32" font-weight="700" letter-spacing="-.7">{title}</text></g>'
    svg(name,600,200,title,body,defs)


def main():
    hero(); hero(True); impact()
    project('lecturelens','LectureLens','RETRIEVAL / LEARNING','#7DCFFF','''
<g transform="translate(28 25)" fill="none" stroke="#7DCFFF" stroke-opacity=".7"><path d="M0 4q28-8 55 2v55Q27 50 0 57ZM55 6Q82-4 110 4v53q-28-7-55 4Z"/><path d="M13 18h27M13 29h27M70 18h27M70 29h20" stroke-opacity=".35"/><path d="M132 32h55M179 26l8 6-8 6"/><rect x="210" y="7" width="180" height="51" rx="8"/><path d="M225 24h118M225 37h83"/><circle cx="416" cy="32" r="11"/><path d="m411 32 4 4 6-8"/></g>''')
    project('hyperx','HyperX / Legal Retrieval','KAGGLE / 2ND PLACE','#BB9AF7','''
<g transform="translate(28 22)" fill="none" stroke="#BB9AF7" stroke-opacity=".7"><path d="M42 4v62M12 66h60M4 18h76M18 18 3 46h30ZM66 18 51 46h30Z"/><path d="M98 36h63M153 30l8 6-8 6"/><rect x="185" y="10" width="82" height="52" rx="6"/><path d="M198 24h55M198 35h42M198 46h48" stroke-opacity=".4"/><path d="m280 36 30-21 30 21-30 21Z"/><circle cx="385" cy="36" r="25"/><path d="m374 36 8 8 15-17"/></g>''')
    project('autopipeline','AutoPipelineAI','NATURAL LANGUAGE / DATA PIPELINES','#9ECE6A','''
<g transform="translate(28 26)" fill="none" stroke="#9ECE6A" stroke-opacity=".7"><rect width="115" height="55" rx="8"/><path d="m16 19 9 8-9 8M39 35h45"/><path d="M130 28h47M169 22l8 6-8 6"/><rect x="200" y="9" width="63" height="38" rx="6"/><path d="M263 28h37l24-19h49M300 28l24 20h49"/><circle cx="390" cy="9" r="12"/><circle cx="390" cy="48" r="12"/></g>''')
    project('ecg','ECG / Explainable ML','HEALTHCARE / EXPLAINABILITY','#F7768E','''
<g transform="translate(28 20)" fill="none" stroke="#F7768E" stroke-opacity=".75"><path d="M0 39h40l12-14 14 40L85 4l18 48 13-13h42" stroke-width="2"/><path d="M185 39h46M223 33l8 6-8 6"/><path d="M260 63v-20h21v20M296 63V16h21v47M332 63V31h21v32M368 63V4h21v59"/><path d="M251 71h151" stroke-opacity=".25"/></g>''')
    svg('footer',1200,170,"Let's build something reliable together — Nitesh Ranjan Singh",f'''
<rect width="1200" height="170" rx="14" fill="#11172A"/>
<path d="M0 1h1200" stroke="#7AA2F7" stroke-opacity=".4"/>
<g font-family="{FONT}" text-anchor="middle"><text x="600" y="69" fill="#E0E7FF" font-size="28" font-weight="600">Good data. Thoughtful AI. Let's build.</text><text x="600" y="107" fill="#9AA5CE" font-size="16">Data / AI opportunities · Collaborations · Mentoring</text></g>
<g fill="#7DCFFF"><circle cx="568" cy="139" r="2"/><circle cx="584" cy="139" r="2" fill="#7AA2F7"/><circle cx="600" cy="139" r="2" fill="#BB9AF7"/><circle cx="616" cy="139" r="2" fill="#7AA2F7"/><circle cx="632" cy="139" r="2"/></g>
<path class="motion" d="M530 139h140" stroke="#7DCFFF" stroke-dasharray="6 134"><animate attributeName="stroke-dashoffset" values="140;0" dur="5s" repeatCount="indefinite"/></path>''')


if __name__ == "__main__":
    main()
