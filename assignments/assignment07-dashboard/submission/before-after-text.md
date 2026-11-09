# Before And After

**Original:** “For example, change the line to `selected_income <- "Middle Income"` — the other valid value in the classroom dataset is `"High Income (>3.5)"`. Copy the value exactly, including the quotes and any parentheses.”

**Revised:** “In this static dashboard, replace `selected_income` with one of these exact groups: `Low Income (<1.3)`, `Middle Income`, or `High Income (>3.5)`, then render the document again. The table and figure update to that group; no interactive dropdown is embedded in this page.”

The revised text identifies every valid choice and accurately describes the static control, making the dashboard easier to use and the alternate-value test reproducible. The chart caption also now discloses that the display axis starts at BMI 24. The cohort and summary calculations did not change; the axis adjustment uses `coord_cartesian()` only.