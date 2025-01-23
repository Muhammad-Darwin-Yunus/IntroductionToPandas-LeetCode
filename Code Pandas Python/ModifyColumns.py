>.<

Title: Modify Columns
Link: https://leetcode.com/problems/modify-columns/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Level: Easy

Write a solution to modify the salary column by multiplying each salary by 2.

Data employees:
| name    | salary |
| ------- | ------ |
| Jack    | 19666  |
| Piper   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |

>.<

Solution:

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary']=employees['salary']*2
    return employees

Output:

| name    | salary |
| ------- | ------ |
| Jack    | 39332  |
| Piper   | 149508 |
| Mia     | 125018 |
| Ulysses | 109732 |
