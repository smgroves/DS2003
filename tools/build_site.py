"""Builds index.html (schedule) and datasets.html for the DS 2003 site from schedule_data.py."""
import sys, os
from urllib.parse import quote
from html import escape
sys.path.insert(0, os.path.dirname(__file__))
from schedule_data import WEEKS, DATASETS, DS, week_range, used_in

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def href(p): return p if p.startswith("http") else quote(p, safe="/#")

def link(text, h): return f'<a href="{href(h)}">{escape(text)}</a>' if h else escape(text)

NBVIEWER = "https://nbviewer.org/github/smgroves/DS2003/blob/main/"

def nb_links(h):
    """Notebooks get two links: view rendered on nbviewer, or download the .ipynb."""
    return (f'<a href="{NBVIEWER}{href(h)}">nbviewer</a> &middot; '
            f'<a href="{href(h)}" download>download .ipynb</a>')

def items(lst, sep=", "):
    """Join items; lowercase-initial items (e.g. 'rubric') attach to the previous one in parens.
    A notebook's title is plain text with its nbviewer/download links in the parens."""
    groups = []
    for text, h in lst or []:
        is_nb = bool(h) and h.endswith(".ipynb")
        if text[:1].islower() and groups:
            groups[-1][1].append(f"{escape(text)}: {nb_links(h)}" if is_nb else link(text, h))
        elif is_nb:
            groups.append([escape(text), [nb_links(h)]])
        else:
            groups.append([link(text, h), []])
    return sep.join(m + (f' <span class="sub">({", ".join(s)})</span>' if s else "") for m, s in groups)

def data_links(ids):
    return ", ".join(f'<a href="datasets.html#{i}">{escape(DS[i]["label"])}</a>' for i in ids)

CSS = """
:root {
  --ink: #1c1c1c; --mute: #6f6f6f; --line: #dcdcdc; --paper: #ffffff; --bg: #f6f6f6;
  --purple: #b509ac; --purple-dark: #7d0677; --purple-tint: #fbeefa; --purple-light: #ecc2e9;
  --due: #b71c1c;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font: 15px/1.45 "Source Sans 3", "Segoe UI", system-ui, sans-serif; }
main { max-width: 1100px; margin: 0 auto; padding: 28px 18px 60px; }
h1 { font: 700 30px/1.15 "Source Serif 4", Georgia, serif; margin: 0; }
.info { margin: 6px 0 2px; } .oh { color: var(--mute); font-size: 13.5px; margin: 0 0 10px; }
a { color: var(--purple); text-underline-offset: 2px; }
a:hover { color: var(--purple-dark); }
.blurb { max-width: 720px; }
nav.tabs { display: flex; gap: 4px; margin: 18px 0 0; border-bottom: 2px solid var(--ink); }
nav.tabs a { padding: 7px 16px; text-decoration: none; color: var(--ink); font-weight: 600;
  border: 1px solid var(--line); border-bottom: none; border-radius: 6px 6px 0 0; background: var(--paper); }
nav.tabs a.on { background: var(--ink); color: #fff; border-color: var(--ink); }
.grid { display: grid; grid-template-columns: 110px repeat(3, 1fr); border: 1px solid var(--line); border-top: none; background: var(--paper); }
.grid > div { border-bottom: 1px solid var(--line); padding: 8px 10px; min-width: 0; }
.grid > div + div { border-left: 1px solid var(--line); }
.grid .wk { font-weight: 700; } .grid .wk small { display: block; font-weight: normal; color: var(--mute); }
.grid .wk .unit { display: block; font-weight: normal; font-size: 12px; color: var(--mute); margin-top: 4px; }
.grid .hd { font-weight: 700; font-size: 13px; border-bottom: 2px solid var(--ink); background: var(--bg); }
.cell .dt { font: 12px/1 ui-monospace, Menlo, monospace; color: var(--mute); margin-bottom: 4px; }
.cell .t { font-weight: 600; }
.cell .t a { color: var(--ink); text-decoration-color: var(--line); }
.cell .t a:hover { color: var(--purple); text-decoration-color: currentColor; }
.cell p { margin: 3px 0 0; font-size: 13.5px; }
.cell p i { font-style: normal; font-size: 11px; font-weight: 700; color: var(--mute); margin-right: 4px; }
.cell p.dl, .cell p.dl i { color: var(--due); }
.sub { font-size: 12.5px; }
.cell.off { color: var(--mute); font-style: italic; background: repeating-linear-gradient(135deg, #fafafa 0 6px, #f0f0f0 6px 12px); }
.cell.later { color: #555; }
.cell.next { box-shadow: inset 3px 0 0 var(--purple); background: #f3f3f3; }
.ds { background: var(--paper); border: 1px solid var(--line); border-top: none; padding: 16px 18px; }
.ds h2 { font: 700 19px/1.2 "Source Serif 4", Georgia, serif; margin: 0 0 4px; }
.ds .size { font: 12px ui-monospace, Menlo, monospace; color: var(--mute); }
.ds p { margin: 6px 0; max-width: 760px; }
.ds ul { margin: 6px 0; padding-left: 20px; }
.ds .used { font-size: 13.5px; color: var(--mute); }
.ds code { font-size: 13px; background: var(--bg); padding: 1px 4px; border-radius: 3px; }
.ds h3 { font-size: 14.5px; margin: 10px 0 2px; }
.ds:target { box-shadow: inset 4px 0 0 var(--purple); }
.ds img { max-width: 100%; height: auto; border: 1px solid var(--line); margin: 8px 12px 4px 0; vertical-align: top; }
.ds .imgs { display: flex; flex-wrap: wrap; align-items: flex-start; }
.ds .imgs img { max-width: min(100%, 560px); }
@media (max-width: 760px) {
  .grid { grid-template-columns: 1fr; } .grid .hd { display: none; }
  .grid > div + div { border-left: none; } .grid .wk { background: var(--bg); border-top: 2px solid var(--ink); }
}
"""

UPCOMING_JS = """<script>
(function(){
  var t = new Date(); t.setHours(0,0,0,0); var next = null;
  document.querySelectorAll('[data-date]').forEach(function(el){
    var d = new Date(el.getAttribute('data-date') + 'T00:00:00');
    if (d > t) el.classList.add('later');
    if (d >= t && !next && !el.classList.contains('off')) { next = el; el.classList.add('next'); }
  });
})();
</script>"""

def page(active, content):
    tabs = "".join(f'<a href="{h}"{" class=on" if k == active else ""}>{n}</a>'
                   for k, n, h in [("schedule", "Schedule", "index.html"), ("data", "Datasets", "datasets.html")])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DS 2003 &middot; Communicating with Data</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&family=Source+Serif+4:wght@700&display=swap">
<style>{CSS}</style>
</head>
<body>
<main>
<h1>DS 2003: Communicating with Data</h1>
<p class="info">Fall 2026 &middot; Mon/Wed/Fri &middot; Sarah Groves &middot; <a href="DS2003_Syllabus%20Fall%202026.pdf">Syllabus</a> &middot; <a href="DS2003_Computer_Setup_Guide.pdf">Computer setup guide</a> &middot; <a href="https://canvas.instructure.com">Canvas</a></p>
<p class="oh">Office hours: Fri 1&ndash;2 pm, Rm 437 (Sarah) &middot; Wed 1&ndash;2 pm, Capital One Hub (Isabelle Lee, TA)</p>
<nav class="tabs">{tabs}</nav>
{content}
</main>
{UPCOMING_JS if active == "schedule" else ""}
</body>
</html>
"""

def schedule():
    cells = ['<div class="hd"></div><div class="hd">Monday</div><div class="hd">Wednesday</div><div class="hd">Friday</div>']
    for w in WEEKS:
        unit = f'<span class="unit">{escape(w["unit"])}</span>' if w.get("unit") else ""
        cells.append(f'<div class="wk">Week {w["n"]}<small>{week_range(w)}</small>{unit}</div>')
        byday = {x["date"].weekday(): x for x in w["days"]}
        for wd in (0, 2, 4):
            x = byday.get(wd)
            if x is None:
                cells.append('<div class="cell off"></div>'); continue
            num = f' &middot; #{x["cls"]}' if "cls" in x else ""
            dt = f'<div class="dt">{x["date"].strftime("%b %-d")}{num}</div>'
            if "noclass" in x:
                cells.append(f'<div class="cell off" data-date="{x["date"]}">{dt}{escape(x["noclass"])}</div>'); continue
            title = items(x.get("lecture")) or items(x.get("activity")) or items(x.get("lab"))
            ps = []
            if x.get("lecture") and x.get("activity"): ps.append(f'<p><i>CLASS</i>{items(x["activity"])}</p>')
            if (x.get("lecture") or x.get("activity")) and x.get("lab"): ps.append(f'<p><i>LAB</i>{items(x["lab"])}</p>')
            if x.get("data"): ps.append(f'<p><i>DATA</i>{data_links(x["data"])}</p>')
            if x.get("reading"): ps.append(f'<p><i>READ</i>{items(x["reading"])}</p>')
            if x.get("deadline"): ps.append(f'<p class="dl"><i>DUE</i>{items(x["deadline"], "; ")}</p>')
            cells.append(f'<div class="cell" data-date="{x["date"]}">{dt}<div class="t">{title}</div>{"".join(ps)}</div>')
    return page("schedule", f"""
<p class="blurb">Slides, labs, and in-class activities go up here after each class. Submissions and grades are on <a href="https://canvas.instructure.com">Canvas</a>. Anything past this week is tentative and will probably move around.</p>
<div class="grid">
{chr(10).join(cells)}
</div>""")

def datasets():
    secs = []
    for d in DATASETS:
        if d.get("groups"):
            files = "".join(f'<h3>{escape(g)} <span class="sub">(<a href="bad-charts.html#chart-{g.split()[1][0].lower()}">see chart</a>)</span></h3><ul>{"".join(f"<li>{link(t, h)}</li>" for t, h in fs)}</ul>' for g, fs in d["groups"])
        else:
            files = "<ul>" + "".join(f"<li>{link(t, h)}</li>" for t, h in d["files"]) + "</ul>"
        load = f'<p class="used">Or: <code>{escape(d["load"])}</code></p>' if d.get("load") else ""
        uses = "; ".join(f'{dt.strftime("%a %-m/%-d")} {escape(w)}' for dt, w in used_in(d["id"]))
        size = f'<div class="size">{d["size"]}</div>' if d.get("size") else ""
        secs.append(f'<section class="ds" id="{d["id"]}"><h2>{escape(d["name"])}</h2>{size}'
                    f'<p>{escape(d["desc"])}</p>{files}{load}<p class="used">Used in: {uses}</p></section>')
    return page("data", f"""
<p class="blurb" style="margin-top:14px">Every dataset we've used so far, in one place. If a lab reads a CSV, save it in the same folder as the notebook. The penguins and volcano data load straight from the web, so you don't need to download them.</p>
{chr(10).join(secs)}""")

CH = "Class activities/data_for_bad_charts/charts/"
BAD_CHARTS = [
  ("A", "US household income, 1995–2016",
   "Percentage of US households in each income range, with average annual personal income and median annual household income over time. From a research paper on the &ldquo;financialization&rdquo; of the US economy.",
   "The paper argues the economy became more &ldquo;financialized&rdquo; from 1995 to 2016: more economic activity came from finance itself (like trading stocks) rather than from making and selling goods and services. The second figure shows how much finance grew. Your redesign must be one chart, but it should include data from this context.",
   ["A1_household_income.png", "A2_financial_assets.png"]),
  ("B", "Ranked rating in an online game",
   "A player's ranked rating over time in the online game TETR.IO. Each point is one match, placed at the opponent's rating and colored by whether it was a win, loss, or (self-)disqualification.",
   None, ["B_game_rating.png"]),
  ("C", "Gun deaths in Florida",
   "Firearm murders in Florida over time, with 2005 marked as the year the &ldquo;Stand Your Ground&rdquo; law was enacted (Reuters, 2014).",
   "Pair this chart with Pew Research Center's national firearm homicide and non-fatal violent crime rates, 1993–2011 (second figure). Your redesign must be one chart, but it should use information from both. The question you ask and the redesign you make should reflect the context of the Pew charts.",
   ["C1_florida_firearm_murders.png", "C2_pew_crime_rates.png"]),
  ("D", "Slime mold traits across a phylogeny",
   "From a scientific paper on slime molds (dictyostelids). Based on their DNA, the species fall into four main groups on a phylogenetic tree showing how closely related they are; the colored and gray boxes show each species' traits.",
   None, ["D_slime_mold_traits.png"]),
]

def bad_charts():
    secs = []
    for k, title, desc, ctx, imgs in BAD_CHARTS:
        ctx_html = f"<p><b>Context:</b> {ctx}</p>" if ctx else ""
        im = "".join(f'<img src="{href(CH + f)}" alt="Chart {k}">' for f in imgs)
        secs.append(f'<section class="ds" id="chart-{k.lower()}"><h2>Chart {k}: {title}</h2>'
                    f'<p>{desc}</p>{ctx_html}<div class="imgs">{im}</div></section>')
    return page(None, f"""
<p class="blurb" style="margin-top:14px">The four charts for the <a href="{href("Class activities/data_for_bad_charts/9_31_Fixing bad charts.docx")}">Fixing bad charts</a> activity (Wed 9/30) and Lab 5 <span class="sub">({nb_links("Labs/Lab05/Lab05_blank_fixing_bad_design.ipynb")})</span>. Pick one to redesign. The data behind each chart is on the <a href="datasets.html#bad-charts">Datasets</a> page.</p>
{chr(10).join(secs)}""")

if __name__ == "__main__":
    open(f"{OUT}/index.html", "w").write(schedule())
    open(f"{OUT}/datasets.html", "w").write(datasets())
    open(f"{OUT}/bad-charts.html", "w").write(bad_charts())
    print("built")
