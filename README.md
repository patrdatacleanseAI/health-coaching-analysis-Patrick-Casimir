# Health Coaching Modeling Analysis Platform — Member Engagement & Outcomes  — Submission by Patrick Casimir

## Overview
In this Data Analysis project, I analyze member engagement, retention, and clinical outcomes for a digital health coaching platform.
The goal is to identify actionable insights that improve retention, drive clinical improvement, and maximize ROI.


## Tools Used
- Python (pandas, numpy, matplotlib) for data analysis
- Excel for ROI modeling and scenario analysis
- HTML for dashboard delivery
- GitHub for version control and submission

## Data Quality & Structural Validation

A comprehensive data quality audit was performed across all five source datasets prior to modeling.

1. Missing Value Assessment

Each dataset was evaluated independently for null density.

- 0% missing across members, biomarkers, engagement, and activity tables.
- ~2.06% missing across nutrition variables only (calories and macronutrients).

The NaN values observed during schema concatenation reflect structural differences between tables and do not indicate missing data within individual datasets.

Given the low and isolated missingness in nutrition logging, affected records were retained. No imputation or row deletion was required.


2. Duplicate Record Audit

Full-row duplicate checks were performed across all datasets:

- Members: 0 duplicates  
- Biomarkers: 0 duplicates  
- Engagement: 0 duplicates  
- Activity: 0 duplicates  
- Nutrition: 0 duplicates  

No duplication was detected.


3. Grain Integrity Validation

Each dataset was validated against its intended grain:

- Members: 1 row per `member_id`
- Biomarkers: unique by (`member_id`, `reading_date`)
- Activity: unique by (`member_id`, `date`)
- Engagement: unique by (`member_id`, `week_start`)
- Nutrition: unique by (`member_id`, `log_date`)

No grain violations were found.


4. Referential Integrity

Foreign key relationships were validated:

- No orphan records detected
- All time-series tables correctly map to valid `member_id` values


5. Temporal Integrity

- No activity records occurred before a member’s `signup_date`
- Chronological consistency confirmed across datasets


6. Logical Clinical Validation

Biometric measures were evaluated against reasonable physiological thresholds:

- HbA1c within valid clinical bounds
- BMI within plausible human range
- Systolic blood pressure within valid limits

No out-of-range clinical values were identified.

Summary

The dataset demonstrates:

- High completeness
- Zero duplication
- Strong structural and referential integrity
- Valid chronological sequencing
- Clinically plausible measurements

The data was production-ready and required no aggressive preprocessing prior to analysis.

## Deliverables

1. Interactive Dashboard
- File: `dashboard.html`
- Fully self-contained HTML file
- Open locally in any browser (Chrome/Edge recommended)

2. ROI Model
- File: `Casimir_Patrick_Health_Coaching_Model_ROI_Assignment.xlsx`
- Contains program health metrics and 3 ROI scenarios

3. Insights Write-Up
- Key findings and prioritized recommendations embedded in the dashboard


## How to Navigate the Submission

1. Start with the Dashboard
   - Open `dashboard.html`
   - Review the story: retention → risk → behavior → outcomes

2. Review the ROI Model
   - Open the Excel file  
   - Adjust assumptions (cost, lift, targeted members)  
   - Observe impact on ROI across scenarios  

3. Connect Insights to Action
   - Dashboard highlights key insights and recommendations  
   - Each recommendation ties directly to measurable outcomes  


## Key Insights

- Retention declines significantly from 30 to 90 days, with early drop-off as the main challenge  
- High-risk members represent ~67% of the population and the largest opportunity  
- Engagement behaviors (steps, coaching, app usage, nudges) are the strongest drivers of clinical outcomes  
- Nudge responsiveness shows a strong positive relationship with HbA1c improvement  


## Recommendations

1. Implement a Day-21 Intervention Trigger  
   - Target early disengagement within the first 3–4 weeks  
   - Use automated nudges and coach outreach  

2. Cap High-Risk Intervention Cost at $300 
   - Maintain positive ROI while focusing on the highest-impact segment  

3. Promote 7,000 Daily Steps as a Behavioral Target  
   - Use nudges and incentives to drive sustained engagement  


## How to View the Dashboard

1. Download `dashboard.html`
2. Open in Chrome or Edge
3. All charts are embedded and will display automatically
