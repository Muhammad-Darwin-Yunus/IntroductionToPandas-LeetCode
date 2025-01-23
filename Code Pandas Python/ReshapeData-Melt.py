>.<

Title: Reshape Data: Melt
Link: https://leetcode.com/problems/reshape-data-melt/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Level: Easy

Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.

Data report:
product: object
quarter_1: int
quarter_2: int
quarter_3: int
quarter_4: int

>.<

Solution:

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    meltTable = pd.melt(report,id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3','quarter_4'], var_name='quarter', value_name='sales')

    return meltTable

Output:

| product     | quarter   | sales |
| ----------- | --------- | ----- |
| Umbrella    | quarter_1 | 417   |
| SleepingBag | quarter_1 | 800   |
| Umbrella    | quarter_2 | 224   |
| SleepingBag | quarter_2 | 936   |
| Umbrella    | quarter_3 | 379   |
| SleepingBag | quarter_3 | 93    |
