# Dashboard Adaptation Note

## Audience

A public-health analyst preparing a short briefing on descriptive BMI patterns
in the prepared NHANES Health Equity classroom dataset.

## Dashboard Question

Among adults age 20-80, how does unweighted mean BMI vary across NHANES cycles
for one selected income group?

## Control And Visualization

- Control or interaction: Edit `selected_income` to one of the listed income groups and rerender; this is a static Quarto page, not an interactive dropdown.
- Visualization affected: A line-and-point chart of mean BMI by NHANES cycle, with an aggregate summary table. Following prior feedback, the chart view starts at BMI 24 to make cycle differences easier to see; `coord_cartesian()` leaves the summary values unchanged.
- What changes when the control changes: The summary table, chart title, and plotted series use the selected income group.

## Before And After

The control help text now identifies all three exact group values and avoids
the starter's inaccurate phrase “the other valid value.” This makes the
re-render workflow reproducible for a briefing audience. The chart's viewing
window also starts at BMI 24, as suggested in prior feedback; this changes
display only, not the cohort or summary calculations.

## Test Result

From `assignments/assignment07-dashboard/submission/`, rendered `dashboard.qmd`
with both `Low Income (<1.3)` and `High Income (>3.5)` selected; both renders
succeeded and produced the expected HTML output.

## Limitation

The unweighted classroom summary does not account for NHANES survey design,
does not estimate national prevalence, and cannot establish causation.

## Privacy Check

The PNG preview shows only cycle-level aggregate mean BMI; the rendered HTML
table also reports cycle-level counts. Neither artifact exposes row-level
records or makes causal or population-level claims.