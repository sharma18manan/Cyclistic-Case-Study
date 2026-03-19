# Cyclistic Bike-Share Case Study

## Overview
This project analyzes user behavior in Cyclistic’s bike-share program to identify differences between **annual members** and **casual riders**, with the goal of supporting strategies to convert casual users into long-term members.

---

## Business Objective
Cyclistic aims to increase profitability by converting casual riders into annual members.  
This analysis answers:

> **How do annual members and casual riders use Cyclistic bikes differently?**

---

## Tools & Technologies
- Python (Pandas) – Data cleaning & feature engineering  
- MySQL – Data aggregation & validation  
- Tableau – Data visualization (interactive dashboard)  
- Excel – Intermediate data handling  

---

## Dataset
- 12 months of historical ride data  
- ~5.39 million cleaned records  

Key fields:
- `member_casual`
- `ride_length_minutes`
- `day_of_week`
- `month`
- `rideable_type`

---

## Workflow
Raw CSV → Python Cleaning → Feature Engineering → SQL Validation → Tableau Visualization → Business Insights

---

## Key Insights

- **Members dominate usage** (~64.5% of total rides), indicating consistent and habitual usage  
- **Casual riders have ~63% longer ride durations**, suggesting leisure-based behavior  
- **Members ride more on weekdays**, while casual riders peak on weekends  
- **Strong seasonality observed**, with peak usage during summer months  
- **Electric bikes are preferred** across both user segments  

---

## Recommendations

- Target casual riders with **weekend-focused promotions and discounts**  
- Introduce **flexible or seasonal membership plans**  
- Focus marketing efforts during **peak summer months**  
- Promote **electric bikes** as a convenience-driven upgrade  

---

## Interactive Dashboard
https://public.tableau.com/views/CyclisticBikeShareAnalysis_17739178366630/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## 📊 Dashboard Preview
![Dashboard](dashboard/cyclistic_dashboard.png)


---

## Project Structure
Cyclistic-Case-Study/
│
├── data/
│ ├── raw/
│ └── cleaned/
│
├── notebooks/
├── sql/
├── dashboard/
├── report/
└── README.md

---

## Limitations
- No demographic data available  
- No pricing or revenue data  
- No geographic/station-level analysis  

---

## Author
Manan Sharma
