>.<

Title: Rename Columns
Link: https://leetcode.com/problems/rename-columns/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Level: Easy

Write a solution to rename the columns as follows:
id to student_id
first to first_name
last to last_name
age to age_in_years


Data students:
id: int
first: object
last: object
age: int

>.<

Solution:

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={'id':'student_id','first':'first_name','last':'last_name','age':'age_in_years'})

Output:

| student_id | first_name | last_name | age_in_years |
| ---------- | ---------- | --------- | ------------ |
| 1          | Mason      | King      | 6            |
| 2          | Ava        | Wright    | 7            |
| 3          | Taylor     | Hall      | 16           |
| 4          | Georgia    | Thompson  | 18           |
| 5          | Thomas     | Moore     | 10           |
