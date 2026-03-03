# Health Coaching Modeling Analysis Platform — Member Engagement & Outcomes  — Submission by Patrick Casimir

## Overview

In this project, I analyzed member engagement, retention, and clinical outcomes for a digital health coaching platform serving ~10,000 members managing chronic conditions.

The objective was to identify:

- Drivers of sustained engagement
- Predictors of meaningful clinical improvement
- Levers that maximize ROI for leadership

The final deliverable included an interactive dashboard, ROI model, and structured insights for executive decision-making.


## Tools Used

- Python (pandas, numpy) for data wrangling and feature engineering
- Matplotlib / visualization libraries for chart generation
- Excel for ROI scenario modeling
- HTML for dashboard packaging
- GitHub for version control and submission


# Data Quality & Structural Validation

A comprehensive data audit was conducted before modeling and analysis.


## 1. Missing Value Assessment 

Each dataset was evaluated independently for null density.

Results:
- 0% missing in members
- 0% missing in biomarkers
- 0% missing in engagement
- 0% missing in activity
- 0% missing in raw nutrition logs

The NaN values observed during cross-table concatenation reflect schema differences between datasets and do not represent missing data within individual tables.


## 2. Nutrition Feature Missingness 

After aggregating nutrition logs and left-joining them into the unified member-level dataset, ~2.06% missing values were detected across nutrition features:

- nut_total_calories
- nut_carbs_g
- nut_protein_g
- nut_fat_g
- nut_fiber_g
- nut_sugar_g
- nut_meals_logged

This missingness occurred because some members did not log nutrition activity during the observation window.

### Handling Approach

To preserve the full cohort and avoid survivor bias:

- Missing nutrition values were set to 0 (interpreted as no logged intake)
- A binary indicator `has_nutrition_logs` was created to preserve behavioral signal
- No rows were removed

This ensures ROI and outcome estimates are not artificially inflated by excluding low-engagement members.


## 3. Duplicate Record Audit

Full-row duplicate checks were performed across all five datasets.

Results:
- Members: 0 duplicates
- Biomarkers: 0 duplicates
- Engagement: 0 duplicates
- Activity: 0 duplicates
- Nutrition: 0 duplicates

No duplication was detected.


## 4. Grain Integrity Validation

Each dataset was validated at its intended grain:

- Members → 1 row per `member_id`
- Biomarkers → unique by (`member_id`, `reading_date`)
- Activity → unique by (`member_id`, `date`)
- Engagement → unique by (`member_id`, `week_start`)
- Nutrition → unique by (`member_id`, `log_date`)

No grain violations were found.


## 5. Referential Integrity

Foreign key validation confirmed:

- No orphan records
- All time-series datasets correctly map to valid `member_id` values

All joins are structurally safe.


## 6. Temporal Integrity

Chronological validation confirmed:

- No activity occurred prior to `signup_date`
- Time sequencing across datasets is valid
- Baseline-to-last-observation comparisons are logically consistent


## 7. Clinical Logical Validation

Biometric measures were validated against reasonable physiological thresholds:

- HbA1c within valid range
- BMI within plausible human range
- Systolic blood pressure within acceptable limits

No implausible values were detected.


# Summary of Data Integrity

The dataset demonstrates:

- High completeness
- Zero duplication
- Strong structural integrity
- Referential consistency
- Valid temporal sequencing
- Minimal feature-level missingness (nutrition only, behavior-driven)

The data was production-ready and required no aggressive preprocessing prior to analysis.


# Key Insights

- Retention declines significantly between 30 and 90 days, highlighting early disengagement risk.
- High-risk members represent the largest opportunity for impact.
- Engagement behaviors (steps, coaching sessions, nudges, app usage) are stronger predictors of improvement than baseline risk tier.
- Nutrition logging participation is itself a behavioral signal tied to engagement intensity.


# Prioritized Recommendations

1. **Implement a Day-21 Intervention Trigger**
   - Detect disengagement within the first 3–4 weeks
   - Trigger automated nudges and coach outreach

2. **Cap High-Risk Intervention Cost at $300**
   - Maintain positive ROI while targeting the highest-impact segment

3. **Promote 7,000 Daily Steps as a Behavioral Anchor**
   - Use nudges and incentives to reinforce sustainable engagement


# How to Navigate the Submission

### 1. Start with the Dashboard
Open `dashboard.html`
- Review retention trends
- Examine behavioral drivers
- Understand improvement segmentation

### 2. Review the ROI Model
Open the Excel file
- Adjust assumptions (cost, lift, targeted members)
- Evaluate financial impact across scenarios

### 3. Connect Insights to Action
Each recommendation ties directly to:
- Observed engagement behavior
- Clinical improvement metrics
- Quantified ROI impact

---

# How to View the Dashboard

1. Download `dashboard.html`
2. Open locally in Chrome or Edge
3. All charts are embedded and require no additional dependencies
