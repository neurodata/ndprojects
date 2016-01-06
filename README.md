# ndprojects
analysis of neurodata projects

## Format
Format is important, because we crawl this page automatically to generate summary pages. Each token should be its own folder (named exactly the same as the token appears in the database).

The title of each notebook is the title of the claim on the summary page. The first cell of the notebook should be markdown, and should reflect the "title" of the claim the notebook inspects.

The final output of the notebook should be exactly what you want the output to say in the summary page. Take the following example:

![image](https://cloud.githubusercontent.com/assets/693511/11901241/78c255ec-a578-11e5-8eba-3770279fffa3.png)

This will appear on the summary page as:

> # Mitochondrion Count
> There are 1967 mitochondria total in the annotated volume.
