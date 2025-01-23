>.<

Title: Change Data Type
Link: https://leetcode.com/problems/change-data-type/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Level: Easy

The grade column is stored as floats, convert it to integers.

Data students:
student_id: int
name: object
age: int
grade: float

>.<

Solution:

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

Output:

| student_id | name | age | grade |
| ---------- | ---- | --- | ----- |
| 1          | Ava  | 6   | 73    |
| 2          | Kate | 15  | 87    |
