# Health Coaching Modeling Analysis Platform — Member Engagement & Outcomes  — Submission by Patrick Casimir

## Overview
In this Data Analysis project, I analyze member engagement, retention, and clinical outcomes for a digital health coaching platform.
The goal is to identify actionable insights that improve retention, drive clinical improvement, and maximize ROI.


## Tools Used
- Python (pandas, numpy, matplotlib) for data analysis
- Excel for ROI modeling and scenario analysis
- HTML for dashboard delivery
- GitHub for version control and submission


## Data Quality & Preparation

To ensure the accuracy and reliability of the analysis and ROI model, I used a structured approach to handle temporal consistency, missing data, and outcome measurement.

1. Baseline-to-Outcome Methodology (Temporal Integrity)
Instead of using all time-series data points, I focused on the most stable and comparable observations:

- I extracted the 'first recorded value' per member as the baseline.
- I extracted the 'last recorded value' as the outcome.
- I ignored intermediate fluctuations to reduce noise.

This approach ensures that clinical improvement is measured as a 'true net change over time', rather than short-term variability.


2. Handling Missing Outcome Data (Intent-to-Treat Approach)
Not all members have complete follow-up data (e.g., missing second biomarker readings).

To avoid inflating results:

- I used a 'LEFT JOIN' when merging biomarker outcomes.
- Members without a follow-up reading were retained in the dataset'.
- These members were treated as 'No Improvement'.

This conservative approach follows an 'intent-to-treat principle', ensuring ROI is not overstated due to missing data.


3. Chronological Alignment Across Datasets
The dataset contained multiple time granularities (daily, weekly, monthly).

To ensure consistency:

- All activity, engagement, and biomarker data were aligned into monthly cohorts.
- This enabled consistent Baseline vs. Latest comparisons.
- Allowed for accurate retention and outcome measurement over time.


4. Risk Tier Validation (Logical Consistency Check)
Members were segmented into 'Low, Moderate, and High Risk tiers' using clinical indicators.

- Risk classification provided a 'sanity check' on the data.
- Extreme values naturally map to higher-risk categories.
- Ensures that outcome comparisons are 'clinically meaningful and comparable'.

Summary

This approach prioritizes:
- Temporal consistency (baseline vs outcome)
- Conservative outcome estimation (intent-to-treat)
- Comparability across members (cohort alignment)

As a result, the analysis produces robust, realistic, and decision-ready insights for both clinical impact and ROI.

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
