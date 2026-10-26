# Visual Audit Note

## Plot Question

How does the mean BMI compare across income groups over time in the classroom NHANES snapshot?

## Issues Checked

| Issue | Category | Why it matters | Correction |
|---|---|---|---|
| Y-axis is truncated to 24-28 | Correctness | The narrow axis exaggerates the relative size of differences between income groups, making small changes look large. | Use the full plotting range and label the scale clearly. |
| Title states, "Low income drives rising obesity" | Interpretation | The title implies causation and a population-level claim that the plot cannot support. | Replace it with a descriptive title that reflects the evidence. |
| Subtitle mentions adults age 20-80 without filtering for that age range | Interpretation | The sample is not explicitly restricted to that age range, so the narrative does not match the underlying data selection. | State what is included and avoid unsupported age-specific claims. |
| Missing BMI or income records are not explained | Correctness | Viewers cannot tell how the summary was derived or whether the comparison excludes incomplete records. | Document the exclusion criteria and note that the result is descriptive and unweighted. |
| COVID cycle (2019-2020) is absent from the plotted series | Correctness | The figure appears to cover a continuous timeline, but NHANES does not have a 2019-2020 cycle in this classroom snapshot, so the gap is missing from the narrative. | State that the data include the available cycles and that 2019-2020 is not represented in this file. |

## Final Caption

Data source: example NHANES equity snapshot. Statistic: mean BMI among adults with non-missing BMI and income-group values across the available NHANES cycles. Exclusions: rows with missing BMI or IncomeGroup were removed; the 2019-2020 COVID cycle is not present in this snapshot. Limitation: this is a descriptive, unweighted classroom snapshot and does not establish causal effects or represent the full U.S. adult population.

## AI-Use Check

AI helped draft the ggplot code, suggest a cleaner title, and identify likely visual problems in the flawed plot. I verified the code against the actual column names and the summary values in the raw CSV, then checked that the revised plot uses the correct mean BMI calculation and an honest caption without causal language.
