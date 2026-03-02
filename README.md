# Health Coaching Modeling Analysis Platform — Member Engagement & Outcomes  — Submission by Patrick Casimir

## Overview
This project analyzes member engagement, retention, and clinical outcomes for a digital health coaching platform.
The goal is to identify actionable insights that improve retention, drive clinical improvement, and maximize ROI.


## Tools Used
- Python (pandas, numpy, matplotlib) for data analysis
- Excel for ROI modeling and scenario analysis
- HTML for dashboard delivery
- GitHub for version control and submission


## Data Quality & Preparation

To ensure the accuracy and reliability of the analysis and ROI model, three primary data quality challenges were addressed:

1. Handling Null Engagement
   - Used 'LEFT JOINs' when merging datasets to retain all members, including inactive users  
   - Prevented survivor bias, ensuring disengaged members were included in retention and outcome analysis  

2. Clinical Outlier Removal
   - Filtered biometric data (HbA1c, BMI, blood pressure) to **physiologically valid ranges**  
   - Prevented extreme values from skewing clinical outcome metrics  

3. Chronological Alignment
   - Standardized multiple time-series datasets (daily, weekly, monthly) into **monthly cohorts**  
   - Enabled consistent Baseline vs. Latest comparisons for measuring clinical improvement  

These steps ensured that insights and ROI calculations reflect realistic and actionable outcomes.

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
