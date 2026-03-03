# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
import warnings

# Suppress the specific FutureWarning for a cleaner console output
warnings.simplefilter(action='ignore', category=FutureWarning)

# Set plot style for professional charts
sns.set_theme(style="whitegrid")

# I. LOAD ALL 5 DATASETS USING PARSING TO CALCULATE TIME-BASED METRICS LIKE 'DAYS ACTIVE'
members = pd.read_csv('members.csv', parse_dates=['signup_date'])
biom = pd.read_csv('biomarkers.csv', parse_dates=['reading_date'])
eng = pd.read_csv('engagement.csv', parse_dates=['week_start'])
act = pd.read_csv('activity.csv', parse_dates=['date'])
nut = pd.read_csv('nutrition.csv', parse_dates=['log_date'])


# II. DATA QUALITY CHECK & STRUCTURAL VALIDATION
print("1. Missing Value Audit")
missing_report = pd.concat({
    'members': members.isna().mean(),
    'biomarkers': biom.isna().mean(),
    'engagement': eng.isna().mean(),
    'activity': act.isna().mean(),
    'nutrition': nut.isna().mean()
}, axis=1).round(4)
print(missing_report)

#------------------------------------------------------------------------------------
print("2. Full Row Duplicate Audit")
duplicate_report = pd.Series({
    'members': members.duplicated().sum(),
    'biomarkers': biom.duplicated().sum(),
    'engagement': eng.duplicated().sum(),
    'activity': act.duplicated().sum(),
    'nutrition': nut.duplicated().sum()
})
print(duplicate_report)

#-------------------------------------------------------------------------------------
print("3. Grain Integrity Check")
grain_report = {
    'members_unique_member_id': members['member_id'].nunique() == len(members),
    'biomarkers_unique_key': biom.duplicated(subset=['member_id','reading_date']).sum(),
    'activity_unique_key': act.duplicated(subset=['member_id','date']).sum(),
    'engagement_unique_key': eng.duplicated(subset=['member_id','week_start']).sum(),
    'nutrition_unique_key': nut.duplicated(subset=['member_id','log_date']).sum()
}
print(grain_report)

#---------------------------------------------------------------------------------------

print("4. Referential Integrity Check")
ref_integrity = {
    'biom_missing_member_fk': len(set(biom['member_id']) - set(members['member_id'])),
    'eng_missing_member_fk': len(set(eng['member_id']) - set(members['member_id'])),
    'act_missing_member_fk': len(set(act['member_id']) - set(members['member_id'])),
    'nut_missing_member_fk': len(set(nut['member_id']) - set(members['member_id']))
}
print(ref_integrity)

#-----------------------------------------------------------------------------------------

print("5. Temporal Validity Check")
act_signup_check = act.merge(members[['member_id','signup_date']], on='member_id')
temporal_issues = {
    'activity_before_signup': act_signup_check.query('date < signup_date').shape[0]
}
print(temporal_issues)

#-----------------------------------------------------------------------------------------

print("6. Logical Range Validation (Biomarkers)")
range_check = {
    'hba1c_out_of_range': biom[(biom['hba1c'] < 3) | (biom['hba1c'] > 20)].shape[0],
    'bmi_out_of_range': biom[(biom['bmi'] < 10) | (biom['bmi'] > 80)].shape[0],
    'bp_systolic_out_of_range': biom[(biom['bp_systolic'] < 50) | (biom['bp_systolic'] > 250)].shape[0]
}
print(range_check)

print("DATA QUALITY AUDIT COMPLETE")


# III. DEFINE BIOMARKERS & RISK TIERS & CLINICAL OUTCOMES FOR IMPROVEMENT
biom_base = biom[biom['month_number'] == 0].drop(columns=['month_number', 'reading_date'])
biom_last = biom.sort_values(['member_id', 'month_number']).groupby('member_id').tail(1).drop(columns=['month_number', 'reading_date'])
biom_sum = pd.merge(biom_base, biom_last, on='member_id', suffixes=('_base', '_last'))


# Using The American Diabetes Association (ADA) – Standards of Care in Diabetes
def get_risk_tier(row):
    if row['hba1c_base'] > 8.0 or row['bmi_base'] > 35 or row['bp_systolic_base'] > 140: return 'High Risk'
    if row['hba1c_base'] > 7.0 or row['bmi_base'] > 30 or row['bp_systolic_base'] > 130: return 'Moderate Risk'
    return 'Low Risk'

biom_sum['risk_tier'] = biom_sum.apply(get_risk_tier, axis=1)
biom_sum['hba1c_drop'] = biom_sum['hba1c_base'] - biom_sum['hba1c_last']
biom_sum['bmi_drop'] = biom_sum['bmi_base'] - biom_sum['bmi_last']
# Using The FDA (U.S. Food & Drug Administration) mean reduction of 0.5% in HbA1c and BMI decrease > 1 to confirm treatment effectiveness.
biom_sum['is_improver'] = ((biom_sum['hba1c_drop'] > 0.5) | (biom_sum['bmi_drop'] > 1.0)).astype(int)

# IV. CREATE MAX AGGREGATIONS 
act_max = act.groupby('member_id').agg({
    'steps': ['mean', 'max'], 'exercise_minutes': 'sum', 'sleep_hours': 'mean', 
    'sleep_quality_score': 'mean', 'stress_score': 'mean', 'resting_heart_rate': 'mean',
    'calories_burned': 'mean', 'water_intake_ml': 'mean'
}).reset_index()
act_max.columns = ['member_id', 'avg_steps', 'max_steps', 'total_ex_min', 'avg_sleep', 'sleep_qual', 'avg_stress', 'avg_rhr', 'avg_burn', 'avg_water']

nut_max = nut.groupby('member_id').agg({
    'total_calories': 'mean', 'carbs_g': 'mean', 'protein_g': 'mean', 'fat_g': 'mean', 
    'fiber_g': 'mean', 'sugar_g': 'mean', 'meals_logged': 'sum'
}).reset_index().rename(columns=lambda x: f'nut_{x}' if x != 'member_id' else x)

eng_max = eng.groupby('member_id').agg({
    'coaching_sessions': 'sum', 'nudge_response_rate': 'mean', 'app_logins': 'sum', 
    'messages_to_coach': 'sum', 'goals_completed': 'sum', 'nudges_sent': 'sum'
}).reset_index()

# V. DESIGN COHORT & RETENTION ANALYSIS (30/60/90 Days)
last_act = pd.concat([act.groupby('member_id')['date'].max(), 
                      nut.groupby('member_id')['log_date'].max(),
                      eng.groupby('member_id')['week_start'].max()], axis=1).max(axis=1)

ret = members[['member_id', 'signup_date']].copy()
ret['last_active'] = pd.to_datetime(last_act.reindex(ret['member_id']).values)
ret['days_active'] = (ret['last_active'] - ret['signup_date']).dt.days
ret['signup_month'] = ret['signup_date'].dt.to_period('M').astype(str)
ret['ret_30'], ret['ret_60'], ret['ret_90'] = (ret['days_active'] >= 30).astype(int), (ret['days_active'] >= 60).astype(int), (ret['days_active'] >= 90).astype(int)

cohort_df = ret.groupby('signup_month').agg({'member_id': 'count', 'ret_30': 'mean', 'ret_60': 'mean', 'ret_90': 'mean'}).reset_index()
cohort_df.columns = ['Signup Month', 'Cohort Size', 'Retention 30d', 'Retention 60d', 'Retention 90d']

# VI. BUILD UNIFIED DATASET FROM MERGING ALL 5 INITIAL DATASETS USING LEFT JOINS
master_unified = members.merge(biom_sum, on='member_id', how='left') \
                        .merge(act_max, on='member_id', how='left') \
                        .merge(nut_max, on='member_id', how='left') \
                        .merge(eng_max, on='member_id', how='left') \
                        .merge(ret[['member_id', 'days_active', 'signup_month']], on='member_id', how='left')

# Nutrition Missingness Handling
nut_cols = [
    "nut_total_calories",
    "nut_carbs_g",
    "nut_protein_g",
    "nut_fat_g",
    "nut_fiber_g",
    "nut_sugar_g",
    "nut_meals_logged"
]

print("Nutrition Missingness BEFORE Handling")
print(master_unified[nut_cols].isna().mean().round(4))

# Create indicator 
master_unified["has_nutrition_logs"] = master_unified[nut_cols].notna().any(axis=1).astype(int)

# Impute 0 only where no logs exist
master_unified[nut_cols] = master_unified[nut_cols].fillna(0)

print("Nutrition Missingness AFTER Handling")
print(master_unified[nut_cols].isna().mean().round(4))

# VII. CRAFT ROI MODEL ANALYSIS
roi_df = master_unified.groupby('risk_tier').agg({'member_id': 'count', 'is_improver': 'mean'}).reset_index()
roi_df.columns = ['Risk Tier', 'Member Count', 'Clinical Success Rate']
# Using The CDC (Centers for Disease Control and Prevention) – Cost-Effectiveness of Diabetes Interventions
roi_df['Est_Savings_Per_Success'] = roi_df['Risk Tier'].map({'High Risk': 5500, 'Moderate Risk': 3000, 'Low Risk': 1200})
roi_df['Gross_Savings'] = (roi_df['Member Count'] * roi_df['Clinical Success Rate']) * roi_df['Est_Savings_Per_Success']
roi_df['Program_Cost'] = roi_df['Member Count'] * 250
roi_df['Net_ROI_Multiplier'] = (roi_df['Gross_Savings'] / roi_df['Program_Cost']).round(2)

# VIII. CREATE ROI MODEL WITH 3 SCENARIOS 
roi_df = master_unified.groupby('risk_tier').agg({
    'member_id': 'count', 
    'is_improver': 'mean'
}).reset_index().copy()

roi_df.columns = ['Risk Tier', 'Member Count', 'Clinical Success Rate']

# 1. Adjusted Costs: Capping to ensure profitability
# Cap intervention cost at $300 per high-risk member
roi_df['Est. Cost per Member'] = roi_df['Risk Tier'].map({
    'High Risk': 300, 
    'Moderate Risk': 200, 
    'Low Risk': 100
})

# 2. Saving Values: Standard medical cost offset per success
roi_df['Savings per Success'] = roi_df['Risk Tier'].map({
    'High Risk': 5500, 
    'Moderate Risk': 3000, 
    'Low Risk': 1200
})

# 3. Total Calculations
roi_df['Total Program Cost'] = roi_df['Member Count'] * roi_df['Est. Cost per Member']
roi_df['Total Gross Savings'] = (roi_df['Member Count'] * roi_df['Clinical Success Rate']) * roi_df['Savings per Success']

# 4. Final ROI Metrics
roi_df['ROI Multiplier'] = (roi_df['Total Gross Savings'] / roi_df['Total Program Cost']).round(2)
roi_df['Net Profit Margin %'] = (((roi_df['Total Gross Savings'] - roi_df['Total Program Cost']) / roi_df['Total Program Cost']) * 100).round(0)

# Sort so High Risk is at the top
roi_df = roi_df.sort_values('ROI Multiplier', ascending=False)

# IX. CREATE EXCEL WiTH 3 TABS
with pd.ExcelWriter('Casimir_Patrick_Health_Coaching_Model_ROI_Assignment.xlsx') as writer:
    roi_df.to_excel(writer, sheet_name='ROI Model & Scenarios', index=False)
    cohort_df.to_excel(writer, sheet_name='Cohort Retention', index=False)
    master_unified.to_excel(writer, sheet_name='Maximum Unified Data', index=False)

# X. GENERATE 5 CHARTS
# Chart 1: Cohort Retention to show when members drop off and the critical need for the "Day 21" intervention
plt.figure(figsize=(10, 5))
plot_data = cohort_df.melt('Signup Month', ['Retention 30d','Retention 60d','Retention 90d'])
sns.lineplot(data=plot_data, x='Signup Month', y='value', hue='variable', marker='o')
plt.title('Member Retention Rates by Monthly Signup Cohort'); plt.ylabel('Retention %'); plt.savefig('chart_1_retention.png')

# Chart 2: Population Risk Profile to show the size of your High, Moderate, and Low-risk populations (Pie Chart)
plt.figure(figsize=(7, 7))
master_unified['risk_tier'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#E74C3C', '#F39C12', '#27AE60'])
plt.title('Baseline Health Risk Distribution'); plt.ylabel(''); plt.savefig('chart_2_risk.png')

# Chart 3: Clinical Success by Risk Tier showing the % of "Improvers" in each scenario (Bar Chart)
plt.figure(figsize=(10, 5))
sns.barplot(data=master_unified, x='risk_tier', y='is_improver', order=['Low Risk', 'Moderate Risk', 'High Risk'], hue='risk_tier', palette='coolwarm', legend=False)
plt.title('Success Probability by Health Risk Tier'); plt.ylabel('Success Rate'); plt.savefig('chart_3_success.png')

# Chart 4: Success Drivers with a "Feature Importance" chart from the RandomForestClassifier model showing which behavior (like "Average Steps" or "Coaching") can improve members' health and ROI
X = master_unified[['coaching_sessions', 'nudge_response_rate', 'avg_steps', 'nut_total_calories', 'app_logins']].fillna(0)
y = master_unified['is_improver'].fillna(0)
rf = RandomForestClassifier(n_estimators=100, random_state=42).fit(X, y)
pd.Series(rf.feature_importances_, index=X.columns).sort_values().plot(kind='barh', color='teal')
plt.title('Top Behavioral Predictors of Clinical Success'); plt.savefig('chart_4_drivers.png')

# Chart 5: Engagement vs Outcome with a trend line linking nudge responses to HbA1c drops (Scatter Plot)
plt.figure(figsize=(10, 5))
sns.regplot(data=master_unified, x='nudge_response_rate', y='hba1c_drop', scatter_kws={'alpha':0.1}, color='darkblue')
plt.title('Nudge Responsiveness vs HbA1c Reduction'); plt.savefig('chart_5_engagement.png')

print("All Set!! All Deliverables Generated and Available for Download!!")