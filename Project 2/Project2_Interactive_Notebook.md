# Project 2: Interactive Notebook + Infographic or Science Visualization

This is a **group project** with several deliverables spread across the second half of the semester. In Project 1 you explored a dataset for yourself. In Project 2 you explain a dataset to someone else, in two forms:

1. An **interactive notebook** that guides a reader through your dataset and lets them explore your research questions, built with `ipywidgets` and `plotly`.
2. A **final piece** that distills your single most important finding into a standalone visual. Your group picks one track:
   - an **infographic** for a general audience, or
   - a **science visualization**: a publication-style figure for a specialist audience.

The notebook is where the reader explores. The final piece is for a reader who will never open your data; it has to make the point on its own.

**Groups:** 2–3 students. Send your group members (or a request to be placed in a group) to the instructor by **Wednesday, Oct. 21**.

## Timeline

| Deliverable | Due |
|---|---|
| Groups formed | Wed, Oct. 21 |
| 1. Project proposal | Sun, Oct. 25, 11:59pm |
| 2. Narrative structure check-in | Sun, Nov. 15, 11:59pm |
| 3. Final-piece sketches, in-class design critique | Fri, Nov. 20 (in class) |
| Critique reflection | Sun, Nov. 22, 11:59pm |
| Presentation slides | Sun, Nov. 29, 11:59pm |
| 4. Final presentations | Nov. 30 – Dec. 4 (in class) |
| 5. Final submission: interactive notebook + infographic / science visualization | Mon, Dec. 7, 11:59pm |

## Step 1: Data Selection and Proposal

Pick a topic and a dataset. You can use any data, as long as it isn't a trivial or toy dataset that has already been explored extensively (no built-in datasets like `penguins`, `mpg`, or `nycflights13`). If you aren't sure whether your dataset is appropriate, ask the instructor early.

Your **proposal** (no more than 1 page, one per group) should include:

- **Dataset:** where it comes from, who collected it and how, its size (rows × columns), and the key variables.
- **At least three research questions** you want to investigate.
- **Audience and track:** who you imagine reading your final piece, and whether you are leaning toward an infographic or a science visualization. You can switch tracks later, but tell the instructor if you do.
- **Planned interactions:** one or two ideas for what a reader might *do* in your notebook (filter by region, pick a year, compare two groups, ...) and why a static chart wouldn't be enough.
- **Team plan:** who is taking the lead on which part (data cleaning, notebook, final piece, slides). Everyone should contribute code and design work.

## Step 2: Interactive Notebook (work on it throughout; final version due Mon, Dec. 7)

Start your notebook as soon as your proposal is in. Labs 7–9 (Plotly, ipywidgets, interactive trees) each give you a technique to try on your own data the same week. The notebook is where your group explores and **finds the main takeaway for your final piece**, and your results are what you'll use at the Nov. 15 check-in to decide what your final piece will be.

Your notebook should read like a short interactive article, not like a lab. Someone who hasn't taken this class should be able to follow it. It must contain at least two sections.

### About section

An introduction that catches the reader's attention and tells them what the project is about:

- What the dataset is, where it comes from, and any important limitations (missing values, sampling, what the data *can't* tell you).
- Your research questions and why a reader should care.
- A few key insights shown with **static visualizations** (matplotlib/seaborn is fine). Use the explanatory techniques from class: active titles, annotations, highlighting what matters, and direct labels.

### Interactive section

**At least three charts** that meaningfully answer your research questions. Requirements across the section:

- **At least one `ipywidgets` control** (dropdown, slider, checkbox, toggle, ...) that changes what a chart shows.
- **At least one Plotly chart** with useful micro-interactions: custom hover text (formatted values and units, not raw column names), and zooming or legend toggling where it helps.
- **Every chart is interactive in some way**, and each one gets a 1–2 sentence note saying **what the interaction lets the reader do that a static chart wouldn't.** Interactivity that adds nothing (a dropdown with one sensible option, hover text that repeats the axis) will cost you points. Think carefully about which charts actually benefit.
- Charts can stand alone, or widgets can control several charts at once (linked views). Linked views are not required but count toward creativity.
- Each chart is followed by **2–4 sentences of interpretation**: what pattern should the reader look for, and what does it mean?

### Takeaway section

End with a short summary of what you learned, and state the **single main takeaway** you've chosen for your final piece.

### Technical requirements

`ipywidgets` need a running Python kernel, so **they will not work in an exported HTML file.** Because of that:

- Submit the **`.ipynb`**, your **data** (or a script that downloads it), and a `requirements.txt` (or a list of packages at the top of the notebook).
- Your notebook must run from top to bottom in a fresh kernel (**Kernel → Restart Kernel and Run All Cells**) with no errors and no manual steps.
- If your data is large (more than ~50 MB, e.g. Chicago Crimes, Yelp, Citi Bike), do your filtering and aggregation in a separate preparation notebook and load the smaller result in your main notebook. Submit both.
- Also submit an **HTML export** as a backup record. Plotly charts survive the export; widgets won't. If your Plotly charts come out blank in the HTML, add `import plotly.io as pio; pio.renderers.default = "notebook"` at the top and re-export.

## Step 3: Narrative Structure Check-in (Sun, Nov. 15)

By mid-November your notebook should have real results. Use them to decide what your final piece will be, and plan how it will tell its story before you start sketching. Submit a 1–2 page plan (one per group):

- **What your notebook found:** two or three candidate findings from your notebook, each with the chart (screenshot or export) that supports it.
- **Your decision:** the **one main takeaway** you'll communicate (one sentence), your **track** (infographic or science visualization), and your **audience**. Briefly explain why you chose this finding over the others.
- **Your narrative structure:** which structure from class you'll use (for example, one of Segel & Heer's genres such as an annotated chart, partitioned poster, or magazine style; or a multi-panel A → B → C figure for a science visualization), and why it fits your takeaway and audience.
- **A beat-by-beat outline:** what the reader sees first, second, and third. Cover the hook or context, the evidence (which charts, in what order), and the takeaway.
- **Chart plan:** which notebook charts you'll reuse, which you'll redesign for a static, explanatory version, and any new ones you need.

This plan is what you'll sketch from for the Nov. 20 critique.

## Step 4: Design Sketches and Critique (Fri, Nov. 20; reflection due Sun, Nov. 22)

The critique is on your **final piece** (infographic or science visualization), not your notebook. Bring:

- **At least two different thumbnail layouts** for your final piece, with your one-sentence main takeaway written at the top. Build them from your narrative structure plan.
- **A rough draft of your strongest layout.** Paper, whiteboard photos, or quick slides are all fine. Charts can be placeholders or early versions from your notebook.
- **One sentence naming your audience**, so critics can judge whether the piece works for them.

Groups will rotate through critique stations giving and receiving feedback. Come with questions you want answered. By **Sun, Nov. 22**, submit a **critique reflection**: a photo or PDF of your sketches, the feedback you got, and what you plan to change in response.

## Step 5: Final Presentation (Nov. 30 – Dec. 4)

Each group has a **10-minute slot**. Present two things together:

1. **Your interactive notebook, live.** Don't scroll through every cell. Pick the interactions that show your most important insights and *use* them in front of the audience.
2. **A near-final draft of your final piece.** Feedback from this presentation should shape your revisions.

Every group member should speak. Submit your slides by Sun, Nov. 29 so all groups' slides are ready before presentations start. Feedback from the presentation can shape both your final notebook and your final piece.

## Step 6: Final Submission (Mon, Dec. 7)

Your final submission is your revised **interactive notebook** (see Step 2) together with your **final piece**, described below.

Design a standalone visual that communicates your single main takeaway, combining text and chart(s). Use one chart or several, whatever best supports the point. Choose a track:

**Infographic** (general audience)
- Built for a reader who has a minute or two and no background: a poster, a web graphic, or a social-media graphic.
- A clear headline that states the takeaway, a visual hierarchy that tells the reader where to look first, and plain-language text.

**Science visualization** (specialist audience)
- A publication-style figure like you'd see in a journal: typically several panels labeled **A, B, C...**, with a **figure legend** (a title sentence followed by a description of each panel, sample sizes, and what any error bars mean).
- Follow the science-figure conventions from class: show the data rather than only summaries, use color carefully and accessibly, and keep fonts and alignment consistent across panels.

**Requirements for both tracks**
- **Final assembly can happen outside of code** (Figma, Canva, Illustrator, Inkscape, PowerPoint, ...). However, **every data-driven element must be generated from code** in your notebook: no hand-drawn, traced, or manually adjusted data marks. Text, layout, icons, and annotations can be added by hand.
- Cite your data source on the graphic itself.
- No deceptive encodings: check your piece against the ethics and deceptive-plots material from class.
- Submit as a **PNG or PDF** (vector PDF preferred for science figures).
- Include a **design rationale** (about 1 page): your audience, your takeaway, three key design decisions and why you made them, and **what you changed after the presentation feedback.**
- Include a short **contribution statement** listing what each group member did.

## Grading

Project 2 is worth **20%** of your final grade. The project score is out of **225 points**, split across deliverables. See the full rubric: [Project2_Rubric.html](Project2_Rubric.html).

| Deliverable | Points |
|---|---|
| Proposal | 25 |
| Narrative structure check-in | 25 |
| Final-piece sketches + critique reflection | 25 |
| Final presentation | 50 |
| Final submission: interactive notebook (50) + infographic / science visualization incl. design rationale (50) | 100 |

Group members normally receive the same grade. If the contribution statement or instructor observation shows that work was very uneven, individual grades may be adjusted.

## Recommended Data Sources

To get up and running quickly, consider one of these:

- [COVID-19 Worldwide Testing Data](https://www.kaggle.com/datasets/lin0li/covid19testing)
- [Citi Bike NYC trip data](https://citibikenyc.com/system-data): large; pick a few months
- [Inside Airbnb](https://insideairbnb.com/get-the-data/): pick one or two cities
- [Top Spotify songs 2010–2019](https://www.kaggle.com/datasets/leonardopena/top-spotify-songs-from-20102019-by-year): ~600 Billboard top songs
- [Chicago Crimes, 2001–present](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data): millions of rows; filter by year or type before loading
- [World Bank Indicators, 1960–2017](https://github.com/light-and-salt/World-Bank-Data-by-Indicators): or browse the original data by indicator or country
- [Daily U.S. weather, 2017 (NOAA GHCN)](https://vis.csail.mit.edu/classes/6.894/data/): see the accompanying `weather.txt` for column descriptions
- [Opportunity Insights: social mobility in the U.S.](https://opportunityinsights.org/data/): Raj Chetty's group; consider joining multiple files from the same paper
- [Yelp Open Dataset](https://business.yelp.com/data/resources/open-dataset/): large JSON; you don't need all of it (requires agreeing to Yelp's license)
- [Ookla Speedtest open data](https://www.ookla.com/articles/announcing-ookla-open-datasets): mobile and fixed internet speeds

Science-visualization groups may want data from their own field, a lab they work in, or a public repository (e.g., NASA, NOAA, NCBI/GEO, the Allen Institute). Check with the instructor first.

### Additional data sources

- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Rdatasets](https://vincentarelbundock.github.io/Rdatasets/datasets.html)
- [UC Irvine ML Repository](https://archive.ics.uci.edu/datasets)
- [FiveThirtyEight datasets](https://github.com/fivethirtyeight/data/tree/master)
- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)

## Submission Details

Submit everything on Canvas; each deliverable has its own submission page. One submission per group.

- **Proposal** (PDF): Sun, Oct. 25, 11:59pm
- **Narrative structure check-in** (PDF): Sun, Nov. 15, 11:59pm
- **Sketches** in class Fri, Nov. 20; **critique reflection** (PDF/photos): Sun, Nov. 22, 11:59pm
- **Presentation slides**: Sun, Nov. 29, 11:59pm
- **Final submission**: Mon, Dec. 7, 11:59pm
  - **Notebook**: `.ipynb` + data or download script + `requirements.txt` + HTML export
  - **Final piece** (PNG/PDF) + **design rationale** + **contribution statement**

Generative AI use follows the course policy in the syllabus. Cite any AI help in your notebook and design rationale.

## Acknowledgments

Components of this assignment were inspired by Adam Perer and Dominik Moritz's *Interactive Data Science* course at CMU.
