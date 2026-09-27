"""Printable handouts in the Level 1 lab-sheet style: a letter-width document that reads the same on
screen and on paper. A header band, a name line, a goal box, numbered parts with checklist steps,
write-in lines, tips and a partner checkpoint, then a success box and footer."""
from html import escape
def E(t):return escape(str(t),quote=True)

CSS='''*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
:root{--primary:#1B365D;--va-blue:#003F72;--accent:#C9A227;--light:#fff;--off-white:#F5F7FA;--gray:#5A6A7A;--success:#1E7F44;--danger:#C2283C;--line:#b9c4d0}
body{margin:0 auto;padding:.5in;max-width:8.5in;background:var(--light);color:#333;font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;font-size:15px;line-height:1.55;overflow-wrap:anywhere}
h1,h2,h3,h4,p,ul,ol{margin:0}
.no-print{display:flex;justify-content:flex-end;gap:.5rem;margin-bottom:.75rem}
.no-print a,.no-print button{font:inherit;font-size:.85rem;font-weight:600;padding:.4rem .8rem;border-radius:6px;border:1px solid var(--va-blue);background:#fff;color:var(--va-blue);cursor:pointer;text-decoration:none}
.header{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:1.1rem 1.4rem;border-radius:10px;background:linear-gradient(135deg,var(--va-blue) 0%,var(--primary) 100%);color:#fff;margin-bottom:1.25rem}
.header h1{font-size:1.45rem;margin-top:.3rem}.header-subtitle{font-size:.95rem;opacity:.92;margin-top:.1rem}.header-meta{font-size:.8rem;opacity:.75;margin-top:.25rem}
.header-badge{display:inline-block;background:var(--accent);color:#0D1B2A;padding:.2rem .7rem;border-radius:15px;font-size:.78rem;font-weight:700;letter-spacing:.5px;text-transform:uppercase}
.header-right{text-align:right;flex-shrink:0;font-size:.8rem;opacity:.9;line-height:1.7}
.name-field{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem 1.5rem;margin-bottom:1.25rem;font-size:.95rem}
.name-field label{font-weight:600;color:var(--va-blue)}.name-field .line{flex:1;min-width:140px;max-width:300px;border-bottom:2px dashed var(--gray);height:1.2em}
.goal-box{background:linear-gradient(135deg,var(--off-white) 0%,#EDF2F7 100%);border:2px solid var(--accent);border-radius:10px;padding:1rem 1.25rem;margin-bottom:1.25rem}
.goal-box h2{color:var(--va-blue);font-size:1.05rem;margin-bottom:.4rem}.goal-box ul{list-style:none;padding:0}.goal-box li{padding:.15rem 0;font-size:.95rem}.goal-box li::before{content:"\\2713  ";color:var(--success);font-weight:700}
.part-header{display:flex;justify-content:space-between;align-items:center;gap:.5rem;background:var(--va-blue);color:#fff;padding:.6rem 1rem;border-radius:8px 8px 0 0;margin-top:1.4rem}
.part-header h2{font-size:1.1rem}.part-timing{background:var(--accent);color:#0D1B2A;padding:.15rem .6rem;border-radius:12px;font-size:.8rem;font-weight:700;white-space:nowrap}
.part-type{background:rgba(255,255,255,.2);padding:.15rem .6rem;border-radius:12px;font-size:.8rem;font-weight:600;margin-left:.4rem;white-space:nowrap}
.part-content{border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;padding:1rem 1.1rem;margin-bottom:.4rem}
.section{margin-bottom:1rem}.section:last-child{margin-bottom:0}
.section-title{background:var(--off-white);color:var(--va-blue);padding:.4rem .9rem;border-left:4px solid var(--accent);font-size:1rem;font-weight:700;margin-bottom:.6rem}
.checklist{list-style:none;padding:0}.checklist li{display:flex;align-items:flex-start;gap:.7rem;padding:.6rem .75rem;margin-bottom:.45rem;background:var(--off-white);border-radius:8px;font-size:.95rem}
.checkbox{width:20px;height:20px;border:2px solid var(--va-blue);border-radius:4px;flex-shrink:0;margin-top:2px;background:#fff}
.checklist-text{flex:1}.checklist-text strong{color:var(--va-blue)}.checklist-text .detail{display:block;font-size:.88rem;color:var(--gray);margin-top:.2rem}
.key{display:inline-block;background:#fff;border:1px solid #bbb;border-bottom-width:3px;border-radius:4px;padding:0 .35rem;font-family:Consolas,'Courier New',monospace;font-size:.85em;font-weight:600;color:var(--primary);line-height:1.5}
.fill-line{display:flex;align-items:flex-end;gap:.5rem;margin:.7rem 0;font-size:.92rem}.fill-line .label{color:#333;white-space:nowrap}.fill-line .blank{flex:1;border-bottom:1px solid var(--gray);min-height:1.5rem}
.fill-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 1.5rem}
.write{margin:.6rem 0 .2rem}.write label{display:block;font-size:.9rem;color:#333;margin-bottom:.25rem}
.write textarea{display:block;width:100%;min-height:calc(1.9rem * var(--rows,3) + .4rem);padding:.2rem .4rem;border:0;border-bottom:1px solid var(--gray);border-radius:0;resize:vertical;font:inherit;font-size:.95rem;line-height:1.9rem;background:repeating-linear-gradient(to bottom,transparent 0,transparent calc(1.9rem - 1px),var(--line) calc(1.9rem - 1px),var(--line) 1.9rem);color:#111}
.write textarea:focus{outline:2px solid var(--accent);outline-offset:2px}
.print-answer{display:none;white-space:pre-wrap}
.tip-box{background:#FFF8E1;border-left:4px solid var(--accent);padding:.6rem .9rem;border-radius:0 6px 6px 0;font-size:.9rem;margin:.7rem 0}.tip-box strong{color:#7a5a00}
.warning-box{background:#FFF3F3;border-left:4px solid var(--danger);padding:.6rem .9rem;border-radius:0 6px 6px 0;font-size:.9rem;margin:.7rem 0}.warning-box strong{color:var(--danger)}
.checkpoint-box{background:linear-gradient(135deg,rgba(0,63,114,.1) 0%,rgba(0,63,114,.04) 100%);border:2px solid var(--va-blue);border-radius:10px;padding:.8rem 1rem;margin:1rem 0 .2rem}
.checkpoint-box h4{color:var(--va-blue);font-size:.95rem;margin-bottom:.35rem}.checkpoint-box ul{list-style:none;padding:0}.checkpoint-box li{font-size:.9rem;padding:.15rem 0}.checkpoint-box li::before{content:"\\2610  "}
.form-box{border:1px solid var(--line);border-radius:8px;padding:.6rem 1rem;margin:.6rem 0;background:#fff}.form-box .fill-line{margin:.45rem 0}
.success-box{background:rgba(30,127,68,.08);border:2px solid var(--success);border-radius:10px;padding:1rem 1.25rem;margin-top:1.6rem}
.success-box h3{color:var(--success);font-size:1.05rem;margin-bottom:.4rem}.success-box p{font-size:.92rem;color:#333;margin-bottom:.4rem}.success-box ul{list-style:none;padding:0}.success-box li{font-size:.92rem;padding:.15rem 0}.success-box li::before{content:"\\2B50  "}
.footer{margin-top:1.4rem;padding-top:.9rem;border-top:2px solid var(--off-white);text-align:center;font-size:.8rem;color:var(--gray)}
table{border-collapse:collapse;width:100%;margin:.6rem 0;font-size:.9rem}th,td{padding:.45rem .6rem;border:1px solid var(--line);text-align:left;vertical-align:top}th{background:var(--off-white);color:var(--va-blue)}
.table-scroll{overflow-x:auto;position:relative}.card-table td:first-child{font-weight:600;color:var(--va-blue);width:32%}
.actions{display:flex;flex-wrap:wrap;gap:.5rem;margin:.6rem 0}.button{display:inline-block;padding:.45rem .9rem;border-radius:6px;background:var(--va-blue);color:#fff;font-weight:600;font-size:.9rem;text-decoration:none;border:1px solid var(--va-blue)}.button.secondary{background:#fff;color:var(--va-blue)}
.procedure{padding-left:1.4rem;font-size:.92rem}.procedure li{margin:.3rem 0}
.rating{display:grid;gap:.15rem;border:0;padding:0;margin:0;font-size:.85rem}.rating label{white-space:nowrap}
.visually-hidden{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}
.small{font-size:.85rem;color:var(--gray)}
@media print{@page{size:letter;margin:.5in}body{padding:0;max-width:none;font-size:10.5pt;line-height:1.45}.no-print{display:none!important}
 .header,.part-header,.checkbox,.checkpoint-box,.key,.goal-box,.tip-box,.warning-box,.success-box,.section-title,.checklist li{-webkit-print-color-adjust:exact;print-color-adjust:exact}
 .checklist li,.checkpoint-box,.form-box,.tip-box,.warning-box,.goal-box,.success-box{break-inside:avoid}.part-header{break-inside:avoid}
 .header{background:var(--va-blue)!important}.goal-box{background:var(--off-white)!important}.checkpoint-box{background:#eef3f8!important}
 .part-content{padding:.7rem .9rem}.checklist li{padding:.4rem .6rem;margin-bottom:.3rem}.fill-line{margin:.45rem 0}.section{margin-bottom:.7rem}.part-header{margin-top:1rem;padding:.45rem .9rem}
 .checklist-text .detail{font-size:.83rem}.table-scroll{overflow:visible}table{font-size:9.5pt}tr{break-inside:avoid}thead{display:table-header-group}th,td{padding:.3rem .45rem}.footer{margin-top:1rem}
 .worksheet-input{display:none!important}.print-answer{display:block;min-height:calc(1.9rem * var(--rows,3));padding:.2rem .4rem;line-height:1.9rem;background:repeating-linear-gradient(to bottom,transparent 0,transparent calc(1.9rem - 1px),var(--line) calc(1.9rem - 1px),var(--line) 1.9rem)}
 .vub-textsize-fab{display:none!important}}
@media screen and (max-width:640px){body{padding:1rem}.header,.part-header{flex-direction:column;align-items:flex-start;gap:.4rem}.header-right{text-align:left}.fill-grid{grid-template-columns:minmax(0,1fr)}.fill-line{flex-wrap:wrap}.fill-line .label{white-space:normal}.fill-line .blank{flex-basis:100%}}
'''

def header(badge,title,subtitle,meta,right=()):
 return f'<header class="header"><div><span class="header-badge">{E(badge)}</span><h1>{E(title)}</h1><div class="header-subtitle">{E(subtitle)}</div><div class="header-meta">{E(meta)}</div></div><div class="header-right">'+''.join(f'<div>{E(r)}</div>' for r in right)+'</div></header>'
def name_field():
 return '<div class="name-field"><label>Name:</label><div class="line"></div><label>Date:</label><div class="line" style="max-width:150px"></div></div>'
def goal_box(title,items):
 return f'<div class="goal-box"><h2>{E(title)}</h2><ul>'+''.join(f'<li>{E(x)}</li>' for x in items)+'</ul></div>'
def part(title,timing,kind,inner):
 pills=(f'<span class="part-timing">{E(timing)}</span>' if timing else '')+(f'<span class="part-type">{E(kind)}</span>' if kind else '')
 return f'<div class="part-header"><h2>{E(title)}</h2><div>{pills}</div></div><div class="part-content">{inner}</div>'
def section(title,items):
 """Checklist steps: (bold action, detail). Detail may hold <span class="key"> markup. No title: just the list."""
 rows=''.join(f'<li><div class="checkbox"></div><div class="checklist-text"><strong>{E(a)}</strong>'+(f'<span class="detail">{d}</span>' if d else '')+'</div></li>' for a,d in items)
 return '<div class="section">'+(f'<h3 class="section-title">{E(title)}</h3>' if title else '')+f'<ul class="checklist">{rows}</ul></div>'
def fill(label,unit=''):
 return f'<div class="fill-line"><span class="label">{E(label)}</span><span class="blank"></span>'+(f'<span class="label">{E(unit)}</span>' if unit else '')+'</div>'
def fill_grid(labels):return '<div class="fill-grid">'+''.join(fill(l) for l in labels)+'</div>'
def write(key,label,rows=3):
 return f'<div class="write" style="--rows:{rows}"><label for="{key}">{E(label)}</label><textarea class="worksheet-input" id="{key}"></textarea><div class="print-answer"></div></div>'
def tip(text,kind='tip'):return f'<div class="{"warning-box" if kind=="warning" else "tip-box"}"><strong>{"Caution:" if kind=="warning" else "Tip:"}</strong> {text}</div>'
def checkpoint(items,title='Partner check — done when:'):
 return f'<div class="checkpoint-box"><h4>{E(title)}</h4><ul>'+''.join(f'<li>{E(x)}</li>' for x in items)+'</ul></div>'
def form_box(labels):return '<div class="form-box">'+''.join(fill(l) for l in labels)+'</div>'
def success(title,text,skills):
 return f'<div class="success-box"><h3>{E(title)}</h3><p>{E(text)}</p><ul>'+''.join(f'<li>{E(s)}</li>' for s in skills)+'</ul></div>'
def footer(left,right):return f'<footer class="footer"><p><strong>{E(left)}</strong> | {E(right)}</p></footer>'
def key(k):return f'<span class="key">{E(k)}</span>'
def page(title,body,base,scripts=()):
 s=''.join(f'<script src="{x}"></script>' for x in scripts)
 return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{E(title)} — VUB Digital Literacy Level 2 worksheet."><title>{E(title)} | VUB Learning</title><style>{CSS}</style></head>
<body><div class="no-print"><button type="button" data-print>Print / Save as PDF</button><a href="{base}/index.html">Course home</a></div>
<main>{body}</main>
<script src="/shared/progress.js"></script><script src="/shared/text-size.js" defer></script>{s}</body></html>'''
