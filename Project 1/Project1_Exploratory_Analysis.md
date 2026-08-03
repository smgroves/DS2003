# Project 1: Exploratory Data Analysis

In this project, you will perform an exploratory analysis on a dataset. This is an **individual project** that will entail finding an interesting dataset, proposing research questions, cleaning/preparing the data, and designing elaborate and compelling visualizations that assist in answering your proposed questions. Your final submission will take the form of a **Jupyter Notebook report** consisting of captioned visualizations that convey key insights gained during your analysis.

## Step 1: Data Selection

First, you will pick a topic area of interest to you and find a dataset that can provide insights into that topic. To streamline the project, we provided a number of datasets (described below) for you to choose from. However, if you would like to investigate a different topic and dataset, you are free to do so. If working with a self-selected dataset, please check with the TA (during their office hours) to ensure it is appropriate for the project.

After selecting a topic and dataset — but prior to analysis — you should write down an initial set of **at least three questions** you'd like to investigate.

## Step 2: Exploratory Visual Analysis

Next, you will perform an exploratory analysis of your dataset using Python — `pandas` for data wrangling, `matplotlib` (the library you've been using in lab) for visualization, and other libraries as needed. If you want to try `seaborn` (a shortcut layer built on top of `matplotlib`) for a specific chart type, that's fine too — pick whichever tool gets the visual encoding right, not whichever is fastest to type.

You should consider two different phases of exploration.

**In the first phase**, you should seek to gain an overview of the structure of your dataset. What variables does the dataset contain? How are they distributed? Are there any notable data quality issues (e.g., missing values)? Are there any surprising relationships among the variables?

**In the second phase**, you should investigate your initial questions, as well as any new questions that arise during your exploration. For each question:

1. Start by creating a visualization that might provide a useful answer.
2. Then refine the visualization (by adding additional variables, changing sorting or changing axis scales, filtering or subsetting data, etc.) to develop better perspectives, explore unexpected observations, or sanity check your assumptions.

You should repeat this process for each of your questions, but feel free to revise your questions or branch off to explore new questions if needed.

## Final Deliverable

Your final submission should take the form of a **Jupyter Notebook exported to HTML** that consists of **5 or more captioned visualizations** detailing your most important insights. Your "insights" can include important surprises as well as responses to your analysis questions.

To export your notebook to HTML: in Jupyter, use **File → Save and Export Notebook As → HTML**, or from a terminal run:

```
jupyter nbconvert --to html your_notebook.ipynb
```

Each visualization should be accompanied with a **title and descriptive caption (1–5 sentences long)** describing the visualization and insight(s) learned from that view. Provide sufficient detail for each caption such that anyone could read through your report and understand what you've learned. You are free, but not required, to annotate your images to draw attention to specific features of the data — you may add annotations directly in matplotlib (e.g., `ax.annotate()`, `ax.text()`) or draw on the exported image afterward.

The end of your report should include a brief **summary of the main lessons learned**.

> **[Instructor note: link a sample Python/Jupyter report here to critique as a class, the same way the original R version of this assignment used an NYCflights R Markdown example — e.g., export one of the Lab notebooks or a short sample analysis to HTML, then walk through what's missing: no guiding research questions, too few visualizations, some chart-type choices that don't fit the data, no dataset introduction, no data-quality checks, no summary section.]**

## Grading

The project score is out of a maximum of **100 points**. We will use the following rubric to grade your assignment. Note, rubric cells may not map exactly to specific point scores.

| Component | Excellent | Satisfactory | Poor |
|---|---|---|---|
| **Dataset Overview** | Effective and complete introduction and dataset summary with descriptions of variables and data quality checks. | Introduction and dataset summary are sparse and incomplete (e.g., no context on data, no check for missing values). | Complete lack of introduction and dataset summary. |
| **Research Questions and Discussion** | Interesting and insightful questions were asked that yielded engaging insights. | Decent questions were asked, but they did not take the analysis much deeper. | Completely trivial questions with little discussion. |
| **Visualizations** | Well designed and formatted visualizations were produced with informative captions. | The visualizations were decent, but some errors remain in terms of selected chart types or visual encodings. | Poorly designed visualizations with ineffective design choices. |
| **Captions** | Captions richly describe the visualizations and contextualize the insight within the analysis. | Captions do a good job describing the visualizations, but could better contextualize the insight. | Captions are missing, overly brief, or shallow in their analysis of visualizations. |
| **Creativity & Originality** | You exceeded the parameters of the assignment, with original insights or a particularly engaging design. | You met all the parameters of the assignment. | You met most of the parameters of the assignment. |

## Recommended Data Sources

To get up and running quickly, you already know the schema of several datasets from lab — these are zero-setup options if you'd rather spend your time on analysis than data-hunting:

- `palmerpenguins` (`from palmerpenguins import load_penguins`)
- `nycflights13` (`from nycflights13 import flights, planes, airports, ...`)
- `gapminder` (`from gapminder import gapminder`)
- `pydataset` (`from pydataset import data; data("mtcars")`, and many others — run `data()` with no arguments to list them all)

If you'd like to explore a new topic, here are some other sources to consider. You are also free to use data from a source different from those included here. If you have any questions on whether your dataset is appropriate, please ask the TA ASAP!

- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Rdatasets](https://vincentarelbundock.github.io/Rdatasets/datasets.html) — a compiled list of datasets bundled with R packages, each hosted as a plain CSV you can load directly with `pd.read_csv(url)` regardless of language
- [UC Irvine ML Repository](https://archive.ics.uci.edu/datasets)
- [FiveThirtyEight datasets](https://github.com/fivethirtyeight/data/tree/master) on sports, politics, and entertainment
- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets), organized by domain

## Submission Details

This is an **individual project**. You may not work in groups. Your completed assignment is due on **[INSTRUCTOR: insert due date/time]**.

Submit your assignment as an **HTML file** on Canvas.

## Acknowledgments

Components of this assignment were inspired by Adam Perer and Dominik Moritz's *Interactive Data Science* course at CMU, adapted here from an earlier R/tidyverse version to Python/pandas/matplotlib.
