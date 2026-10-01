"""Schedule data for DS 2003 Fall 2026. Links are repo-relative paths (unencoded)."""
from datetime import date, timedelta

S = "Lectures/"
L = "Labs/"
A = "Class activities/"

def d(m, day): return date(2026, m, day)

# Each class: date, title, plus optional lists of (text, href|None)
# keys: lecture, activity, lab, reading, deadline. noclass=str for days off.
WEEKS = [
  dict(n=1, unit="Unit 1: Exploratory visualization: the building blocks", days=[
    dict(date=d(8,24), noclass="No class"),
    dict(date=d(8,26), lecture=[("Introduction", S+"pdf/01-Intro.pdf")],
         deadline=[("Pre-course survey (Canvas)", None)]),
    dict(date=d(8,28), lecture=[("Python setup", S+"pdf/02_Lab0_python.pdf")],
         lab=[("Lab 0: Python review", L+"Lab 0/Lab0_blank_python.ipynb")], data=["penguins"],
         reading=[("Computer setup guide", "DS2003_Computer_Setup_Guide.pdf")],
         deadline=[("Lab 0 due Sun", None)]),
  ]),
  dict(n=2, days=[
    dict(date=d(8,31), lecture=[("Why we visualize", S+"pdf/03-Why we visualize.pdf")],
         activity=[("Getting Around NYC", A+"Subway maps/Subway_Map_Wayfinding_Activity.html")]),
    dict(date=d(9,2), lecture=[("Data types, tables & models", S+"pdf/04-VisualDesign-Data.pdf")],
         activity=[("Levels of measurement sort", None),
                   ("Simpson's Paradox", A+"simpsons-paradox/")],
         reading=[("A Tour through the Visualization Zoo", "Readings/3-TourThroughVisualizationZoo.pdf")]),
    dict(date=d(9,4), lecture=[("Intro to pandas", S+"pdf/05-Pandas_lab.pdf")],
         lab=[("Lab 1: pandas & data types", L+"Lab01/Lab01_blank_pandas.ipynb"),
              ("rubric", L+"Lab01/Lab01_Rubric.html")], data=["volcanoes"],
         deadline=[("Project 1 assigned", "Project 1/Project1_Exploratory_Analysis.md"),
                   ("Lab 1 due Sun", None)]),
  ]),
  dict(n=3, days=[
    dict(date=d(9,7), noclass="No class (Labor Day)"),
    dict(date=d(9,9), lecture=[("Visual encodings & scale", S+"pdf/06-VisualDesign-encodings+07+matplotlib_students.pdf")],
         reading=[("Vis Zoo discussion post", None)]),
    dict(date=d(9,11), lecture=[("Encodings & scale, day 2", S+"pdf/07-encodings_scale_part2.pdf")],
         activity=[("Decoding charts", None)],
         lab=[("Lab 2: grouping & aggregating", L+"Lab02/Lab02_blank.ipynb")],
         data=["fastfood", "flights"],
         deadline=[("P1 topic & dataset due Sun", None), ("Lab 2 due Sun", None)]),
  ]),
  dict(n=4, days=[
    dict(date=d(9,14), lecture=[("Expressiveness & effectiveness", S+"pdf/08-VisualDesign-Scale_Effectiveness Principles.pdf")]),
    dict(date=d(9,16), lecture=[("Color", S+"pdf/09-color.pdf")],
         activity=[("Colormap Designer", A+"colormap designer/Colormap Designer - Guided Sandbox.html"),
                   ("notebook", A+"colormap designer/colormap_making.ipynb")],
         deadline=[("Bad-viz discussion post due Thu", None)]),
    dict(date=d(9,18), lecture=[("Matplotlib", S+"pdf/10_matplotlib_lab.pdf")],
         lab=[("Lab 3: anatomy of a figure", L+"Lab03/Lab03_blank_in class.ipynb")],
         data=["penguins", "fastfood", "flights", "volcanoes"],
         deadline=[("Colormap activity due", None), ("End-of-unit-1 survey due Sat", None),
                   ("Lab 3 due Sun", None)]),
  ]),
  dict(n=5, days=[
    dict(date=d(9,21), lecture=[("Perception I", S+"pdf/11-Perception-partI.pdf")]),
    dict(date=d(9,23), lecture=[("Perception II: Gestalt principles", S+"pdf/12-Perception-partII.pdf")],
         activity=[("One chart, one flaw", None)],
         reading=[("The chartjunk debate", "Readings/the_chartjunk_debate.pdf")]),
    dict(date=d(9,25),
         lab=[("Lab 4: encodings, color & chart types", L+"Lab4/Lab04_blank.ipynb")],
         data=["penguins", "flights", "fastfood"],
         deadline=[("Lab 4 due Sun", None)]),
  ]),
  dict(n=6, days=[
    dict(date=d(9,28), lecture=[("Visual tasks: from questions to sketches", S+"pdf/13-Visual Tasks.pdf")],
         activity=[("Question storm", None)], data=["fastfood"]),
    dict(date=d(9,30), lecture=[("Applications", None)],
         activity=[("Fixing bad charts", A+"data_for_bad_charts/9_31_Fixing bad charts.docx")], data=["bad-charts"],
         deadline=[("P1 question sketches", None)]),
    dict(date=d(10,2), lab=[("Lab 5: bad chart redesign", L+"Lab05/Lab05_blank_fixing_bad_design.ipynb")],
         data=["bad-charts"], deadline=[("Lab 5 due Sun", None)]),
  ]),
  # ---- not yet taught: carried over from the previous version of the page ----
  dict(n=7, days=[
    dict(date=d(10,5), noclass="No class (Fall break)"),
    dict(date=d(10,7), lecture=[("Graphs, networks & trees", None)]),
    dict(date=d(10,9), lab=[("Lab 6: alluvial diagrams & graphs", None)]),
  ]),
  dict(n=8, unit="Unit 2: Explanatory visualization: storytelling", days=[
    dict(date=d(10,12), activity=[("EDA presentations", None)]),
    dict(date=d(10,14), activity=[("EDA presentations", None)]),
    dict(date=d(10,16), lecture=[("Data as art / storytelling", None)], deadline=[("Project 1 due", None)]),
  ]),
  dict(n=9, days=[
    dict(date=d(10,19), lecture=[("Storytelling", None)]),
    dict(date=d(10,21), lecture=[("Data journalism & deceptive plots", None)], deadline=[("Project 2 assigned", None)]),
    dict(date=d(10,23), lab=[("Lab 7 (async, family weekend)", None)]),
  ]),
  dict(n=10, days=[
    dict(date=d(10,26), lecture=[("Infographics", None)]),
    dict(date=d(10,28), lecture=[("Infographics II", None)]),
    dict(date=d(10,30), activity=[("Final project introduced", None)], lab=[("Lab 8: decompose an infographic", None)],
         deadline=[("Project 2 proposals due", None)]),
  ]),
  dict(n=11, days=[
    dict(date=d(11,2), lecture=[("Data quality", None)]),
    dict(date=d(11,4), lecture=[("Ethics & rhetoric", None)]),
    dict(date=d(11,6), activity=[("Infographic challenge + critique", None)], lab=[("Lab 9", None)]),
  ]),
  dict(n=12, days=[
    dict(date=d(11,9), lecture=[("Science visualizations", None)]),
    dict(date=d(11,11), lecture=[("Data journalism", None)]),
    dict(date=d(11,13), lab=[("Lab 10: Plotly infographics", None)]),
  ]),
  dict(n=13, days=[
    dict(date=d(11,16), lecture=[("Interaction taxonomies", None)]),
    dict(date=d(11,18), lecture=[("Plotly", None)]),
    dict(date=d(11,20), activity=[("Plotly widget challenge / Tableau track", None)], lab=[("Lab 11", None)]),
  ]),
  dict(n=14, days=[
    dict(date=d(11,23), lecture=[("Communicating uncertainty", None)]),
    dict(date=d(11,25), noclass="No class (Thanksgiving)"),
    dict(date=d(11,27), noclass="No class (Thanksgiving)"),
  ]),
  dict(n=15, days=[
    dict(date=d(11,30), activity=[("Draft presentations", None)]),
    dict(date=d(12,2), activity=[("Draft presentations", None)]),
    dict(date=d(12,4), activity=[("Draft presentations", None)]),
  ]),
  dict(n=16, unit="Final week", days=[
    dict(date=d(12,7), activity=[("Final presentations", None)], deadline=[("Project 2 due", None)]),
  ]),
]

# number classes sequentially
_c = 0
for w in WEEKS:
    for day in w["days"]:
        if "noclass" not in day:
            _c += 1
            day["cls"] = _c

def week_range(w):
    ds = [x["date"] for x in w["days"]]
    a, b = ds[0], ds[-1]
    if a == b: return a.strftime("%b %-d")
    if a.month == b.month: return f"{a.strftime('%b %-d')}–{b.day}"
    return f"{a.strftime('%b %-d')} – {b.strftime('%b %-d')}"

# ---- datasets: id -> info. "files" are (label, href) with href repo-relative or a URL ----
DATASETS = [
  dict(id="penguins", name="Palmer penguins", label="penguins",
       desc="Measurements of 344 penguins (three species) from three islands in the Palmer Archipelago, Antarctica: bill length and depth, flipper length, body mass, sex.",
       size="344 rows × 7 columns",
       files=[("penguins.csv (seaborn-data)", "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")],
       load='pip install palmerpenguins, then from palmerpenguins import load_penguins'),
  dict(id="volcanoes", name="Smithsonian Holocene volcanoes", label="volcanoes",
       desc="The Smithsonian Global Volcanism Program's list of volcanoes active in the last ~12,000 years: name, country, region, type, elevation, and how strong the evidence of eruption is.",
       size="1,328 rows × 20 columns",
       files=[("Smithsonian_VOTW_Holocene_Volcanoes.csv", "https://gist.githubusercontent.com/mattkram/9684863843254402942dfede27af2cb7/raw/2590dd8185b833aacf247c0595edbb07a025a6d7/Smithsonian_VOTW_Holocene_Volcanoes.csv")]),
  dict(id="fastfood", name="Fast food nutrition", label="fastfood",
       desc="Nutrition facts for 515 menu items from eight fast food chains: calories, fat, sodium, carbs, sugar, protein, and a few vitamins.",
       size="515 rows × 18 columns · 48 KB",
       files=[("fastfood.csv", "Data/fastfood.csv")]),
  dict(id="flights", name="NYC flights, 2013", label="flights",
       desc="Every flight that departed New York City's three airports (JFK, LGA, EWR) in 2013: scheduled and actual times, delays, carrier, origin, destination, distance.",
       size="336,776 rows × 19 columns · 33 MB",
       files=[("flights.csv", "Data/flights.csv")],
       load="pip install nycflights13, then import nycflights13 as nf; nf.flights"),
  dict(id="bad-charts", name="Bad chart redesign", label="bad-chart data",
       desc="Data behind the four charts from the Fixing bad charts activity (Wed 9/30) and Lab 5. Some are collected from the original source; where the raw data wasn't available, it's a synthetic best guess.",
       groups=[
         ("Chart A: US household income & financial assets", [
            ("tang2023_fig4_household_income.csv", "Data/tang2023_fig4_household_income.csv"),
            ("tang2023_fig3_financial_assets_pct_gdp.csv", "Data/tang2023_fig3_financial_assets_pct_gdp.csv")]),
         ("Chart B: ranked game rating over time", [
            ("gaming_scores.csv", "Data/gaming_scores.csv")]),
         ("Chart C: Florida firearm murders & national crime rates", [
            ("reuters_florida_firearm_murders.csv", "Data/reuters_florida_firearm_murders.csv"),
            ("florida_population.csv", "Data/florida_population.csv"),
            ("pew_2013_crime_rates.csv", "Data/pew_2013_crime_rates.csv")]),
         ("Chart D: slime mold traits by group (synthetic)", [
            ("biology_dataset_synthetic.csv", "Data/biology_dataset_synthetic.csv")]),
       ]),
]
DS = {x["id"]: x for x in DATASETS}

def used_in(ds_id):
    out = []
    for w in WEEKS:
        for day in w["days"]:
            if ds_id in day.get("data", []):
                what = (day.get("lab") or day.get("activity") or day.get("lecture"))[0][0]
                out.append((day["date"], what))
    return out
