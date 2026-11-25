# AI Use and Verification

Copilot helped structure the report, add code-generated table and figure sections, and revise the limitations and grounding audit. I verified the source, cohort, missingness, income-group Ns, BMI means, bibliography entry, and generated outputs against the rendered report and the cached CSV. No row-level records were sent to an external AI service.

## Cell: Load Data

**AI prompt:** Load the committed NHANES CSV with a relative repository path and stop clearly if the file is missing.

**Verified:** The source renders from the repository root and loads all 105,626 rows from the cached classroom CSV.

## Cell: Cohort and Missingness

**AI prompt:** Define the inclusive adult cohort and report missingness for Age, BMI, and IncomeGroup before creating the complete-case summary.

**Verified:** The cohort has 57,137 records; the missingness table reports 0 missing Age, 1,009 missing BMI, and 5,395 missing IncomeGroup.

## Cell: Table Results

**AI prompt:** Create a code-generated Table 1 for the complete age-20-80 cohort, with N and mean (SD) for BMI and age, and export it to the submission outputs folder.

**Verified:** The table matches the independent A6 calculation and the exported CSV.

## Cell: BMI Figure

**AI prompt:** Generate a clear code-generated column chart of mean BMI by IncomeGroup and save the plot in the A9 outputs folder.

**Verified:** The HTML chart and exported PNG show the same three mean values and income groups.

## Cell: Technical Counts

**AI prompt:** Print the source, cohort, missingness, and income-group result counts needed to audit the technical appendix.

**Verified:** The output matches the table and missingness sections rendered earlier in the report.
