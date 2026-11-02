# AI Use and Verification

Copilot helped draft the R code structure, audit classifications, and explanatory notes. I checked the code against the assignment's inclusive age definition and the dataset's documented cached-file provenance, rendered the Quarto document from the repository root, and compared cohort, missingness, and grouped counts/statistics with independent calculations from the same local CSV. No row-level records were sent to an external AI service.

The following prompt and verification pairs are copied from the corresponding code cells in `eda-note.qmd`.

## Cell: Load Cached Data

**AI prompt:** Load the committed NHANES classroom CSV from its repository-relative path, stop clearly if it is absent, and avoid retrieving data from the internet.

**Verified:** Rendering from the repository root reads the cached file and reports 105,626 rows with the expected Age, BMI, and IncomeGroup columns.

## Cell: Define Cohort

**AI prompt:** Define the inclusive age-20-to-80 cohort, make missing-age and out-of-range exclusions visible, and report a mutually exclusive cohort flow before any grouped summaries.

**Verified:** The cohort contains 57,137 records; missing-age and out-of-range counts plus included records sum to the 105,626 input rows, and every included age is within 20-80.

## Cell: Summarize Missingness

**AI prompt:** Before the Table 1, count missing Age, BMI, and IncomeGroup within the defined age cohort and show each count with its denominator and percentage.

**Verified:** The rendered table uses 57,137 as the cohort denominator and reports 0 missing Age, 1,009 missing BMI, and 5,395 missing IncomeGroup, matching direct sums over analysis_cohort.

## Cell: Create Table 1

**AI prompt:** Within the age cohort, summarize complete cases for BMI and IncomeGroup by IncomeGroup; report N, BMI mean (sample SD), and age mean (sample SD), then export the generated table as a CSV in this submission folder.

**Verified:** The rendered table has one row per income group and matches independent calculations from the cached CSV: N is 16,330, 15,293, and 19,228; the group BMI means are 28.6, 29.4, and 29.3. The exported CSV has the same rows and columns.