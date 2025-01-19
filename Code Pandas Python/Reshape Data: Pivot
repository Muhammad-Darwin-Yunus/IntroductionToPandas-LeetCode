>.<

Title: Reshape Data: Pivot
Link: https://leetcode.com/problems/reshape-data-pivot/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Level: Easy

Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.

Data weather:
city: object
month: object
temperature: int

>.<

Solution:

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivotTable = weather.pivot(index='month',columns='city',values='temperature')

    return pivotTable 

Output:

| month    | ElPaso | Jacksonville |
| -------- | ------ | ------------ |
| April    | 2      | 5            |
| February | 6      | 23           |
| January  | 20     | 13           |
| March    | 26     | 38           |
| May      | 43     | 34           |
