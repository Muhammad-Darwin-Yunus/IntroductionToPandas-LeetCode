>.<

Title: Create a DataFrame from List
Link: https://leetcode.com/problems/create-a-dataframe-from-list/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Level: Easy

Write a solution to create a DataFrame from a 2D list called student_data.
This 2D list contains the IDs and ages of some students.
The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.

Data student_data:
[[1,15],[2,11],[3,11],[4,20]]

>.<

Solution:

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data,columns =['student_id','age'])

Output:

{"headers": ["student_id", "age"], "values": [[1, 15], [2, 11], [3, 11], [4, 20]]}
