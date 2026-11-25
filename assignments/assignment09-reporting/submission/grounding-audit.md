# Grounding Audit

| Claim in report | Evidence type | Evidence location | Verified |
|---|---|---|---|
| The practice report uses the 105,626-row prepared classroom CSV. | Code output | `load-data` chunk and `technical-counts` chunk | Yes — render loads the local cached CSV and reports 105,626 source rows. |
| The age 20-80 cohort contains 57,137 records. | Code output | `cohort-missingness` and `technical-counts` chunks | Yes — independent checks reproduce this count. |
| Missing BMI and IncomeGroup values are 1,009 and 5,395 in the cohort. | Code output | `cohort-missingness` missingness table | Yes — the rendered table reports 1,009 and 5,395 missing values. |
| High-, low-, and middle-income mean BMI values are 28.6, 29.4, and 29.3. | Code output | `table-results` table and `bmi-figure` chart | Yes — values match the code-generated table and CSV/PNG outputs. |
| The NHANES source is CDC/NCHS public-use data. | Citation | `@cdc-nhanes` in `references.bib` and the data-source section | Yes — the bibliography entry resolves and identifies the CDC/NCHS source. |
| The results are unweighted, descriptive, and not causal or nationally representative. | Limitation | Limitations section and methods text | Yes — these claims match the classroom snapshot, lack of survey weights, and absence of a causal design. |
| Complete-case grouping excludes missing BMI or IncomeGroup values. | Code output and limitation | `table-results` filter and limitations section | Yes — the code filters both variables before grouping. |

## Notes

The grounded language avoids claims of significance, causation, or national representation. If a future project finding changes the cohort or uses a different dataset, these evidence locations must be rechecked before reuse.
