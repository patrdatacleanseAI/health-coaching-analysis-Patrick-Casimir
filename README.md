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

A data quality audit was conducted across all five datasets following consolidation.

Missing Data Assessment

- 0% missing across demographics, biomarkers, engagement, activity, and derived outcome variables.
- ~2.06% missing across nutrition variables only (calories and macronutrients).

The limited missingness was isolated to nutrition logging and does not materially impact clinical outcome calculations.

Nutrition nulls were treated as zero logged intake, preserving all members in the dataset without requiring imputation.


Duplicate Record Validation

A duplicate audit was performed at the full-row level across all datasets.

- 0% duplicate rows detected in members, biomarkers, engagement, activity, or nutrition tables.

Each dataset maintained structural integrity at its intended grain (member-level or time-series level).


Summary of Dataset Integrity

- High completeness (≈98–100%)
- No duplication
- Stable baseline and outcome values available for all members
- No row deletions required

The dataset was production-ready for modeling without aggressive preprocessing.


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
