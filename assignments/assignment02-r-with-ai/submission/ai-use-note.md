# AI-Use Note

## Audit trail
# AI prompt: Use a repository-root-relative path to import the NHANES CSV.
# Verified: The path resolves and the CSV imports when rendered from the repository root.
# AI prompt: Prepare BMI and income-group records for grouped BMI summaries, and write a reusable mean/SD function.
# Verified: BMI and IncomeGroup exist in the imported data; the pipeline excludes missing values, and the rendered summaries run.
# AI prompt: Return the non-missing count, mean, and SD for a numeric vector.
# Verified: The helper runs on analysis-ready BMI values and returns n, mean, and sd.

## What AI helped with
Copilot helped organize the dataset inspection, analysis-ready BMI-by-income pipeline, reusable mean/SD function, and output-writing code. It also helped confirm that the data and output paths should be relative to the repository root.

## What I changed
I completed the supplied starter with explicit `readr` and `dplyr` imports, inspection of row count, names, types, and missingness, and a BMI summary by income group. I used the required `output/summary_table.csv` filename and kept the AI prompt and verification comments alongside the assisted code.

## How I verified the result
I rendered the Quarto note from the repository root and confirmed that every code chunk ran. I inspected the imported dataset columns and missingness, then read the generated CSV to confirm that it contains the three income groups and the expected count, mean, and SD columns.
