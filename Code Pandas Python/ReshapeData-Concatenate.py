>.<

Title: Reshape Data: Concatenate
Link: https://leetcode.com/problems/reshape-data-concatenate/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Level: Easy

Write a solution to concatenate these two DataFrames vertically into one DataFrame.

Data df1:
student_id: int
name: object
age: int

Data df2:
student_id: int
name: object
age: int

>.<

Solution:

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df3 = pd.merge(df1,df2,how='outer')
    return df3

Output:

| student_id | name    | age |
| ---------- | ------- | --- |
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
| 5          | Leo     | 7   |
| 6          | Alex    | 7   |
