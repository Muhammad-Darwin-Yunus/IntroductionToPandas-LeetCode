>.<

Title: Drop Missing Data
Link: https://leetcode.com/problems/drop-missing-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Level: Easy

There are some rows having missing values in the name column.
Write a solution to remove the rows with missing values.

Data students:
| student_id | name    | age |
| ---------- | ------- | --- |
| 32         | Piper   | 5   |
| 217        | null    | 19  |
| 779        | Georgia | 20  |
| 849        | Willow  | 14  |

>.<

Solution:

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students = students.dropna(subset=['name'])
    return students

Output:

| student_id | name    | age |
| ---------- | ------- | --- |
| 32         | Piper   | 5   |
| 779        | Georgia | 20  |
| 849        | Willow  | 14  |
