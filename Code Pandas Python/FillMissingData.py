>.<

Title: Fill Missing Data
Link: https://leetcode.com/problems/fill-missing-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Level: Easy

Write a solution to fill in the missing value as 0 in the quantity column.

Data products:
name: object
quantity: int
price: int

>.<

Solution:

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0,inplace=True)
    return products

Output:

| name            | quantity | price |
| --------------- | -------- | ----- |
| Wristwatch      | 0        | 135   |
| WirelessEarbuds | 0        | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
