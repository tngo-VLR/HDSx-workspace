# AI use note

I used AI to translate the R `dplyr` pipeline into a pandas workflow one step at a time. The model suggested equivalent operations for filtering missing values, grouping by `IncomeGroup` and `Gender`, summarizing with counts and standard deviations, and sorting the result.

I then verified the translation by checking row counts, filtered-row counts, grouping labels, and rounded summary values against the R output. The results agreed after rounding, so the final notebook reflects the verified parity check rather than a purely generated script.
