>.<

Title: Select Data
Link: https://leetcode.com/problems/select-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Level: Easy

Write a solution to select the name and age of the student with student_id = 101.

Data students:
| student_id | name    | age |
| ---------- | ------- | --- |
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |

>.<

Solution:

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101,['name','age']]

Output:

| name    | age |
| ------- | --- |
| Ulysses | 13  |
