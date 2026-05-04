Title: SQL Cohort Analysis Framework
Source: 
- https://medium.com/analytics-vidhya/cohort-analysis-using-sql-1c217817d393
- https://www.holistics.io/blog/calculate-cohort-retention-analysis-with-sql/
- https://observablehq.com/@vda-lab/sql-cohort-analysis

---

Cohort analysis is a technique used to understand user behavior over time by grouping users based on shared characteristics.

### SQL Implementation Steps
1. **User Cohort Date**: Find the first event for each user (e.g., first purchase).
2. **Activity Join**: Join all user activities with their cohort date.
3. **Time Difference**: Calculate the distance (in months/days) between the activity and the cohort date.
4. **Aggregate**: Group by cohort and time index to see retention rates.

### Standard Query Pattern
```sql
WITH user_cohorts AS (
    SELECT user_id, DATE_TRUNC('month', MIN(event_date)) AS cohort_month
    FROM events GROUP BY 1
),
activities AS (
    SELECT e.user_id, uc.cohort_month, DATE_TRUNC('month', e.event_date) AS activity_month
    FROM events e JOIN user_cohorts uc ON e.user_id = uc.user_id
)
SELECT cohort_month, (EXTRACT(YEAR FROM activity_month) - EXTRACT(YEAR FROM cohort_month)) * 12 + 
       (EXTRACT(MONTH FROM activity_month) - EXTRACT(MONTH FROM cohort_month)) AS month_number,
       COUNT(DISTINCT user_id) as users
FROM activities
GROUP BY 1, 2;
```
