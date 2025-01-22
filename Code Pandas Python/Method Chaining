>.<

Title: Method Chaining
Link: https://leetcode.com/problems/method-chaining/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Level: Easy

Write a solution to list the names of animals that weigh strictly more than 100 kilograms.
Return the animals sorted by weight in descending order.

Data animals:
name: object
species: object
age: int
weight: int

>.<

Solution:

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    findHeavyAnimals = (animals.loc[animals['weight']>100].sort_values(by='weight',ascending=False))
    return findHeavyAnimals[['name']]

Output:

| name     |
+----------+
| Tatiana  |
| Jonathan |
| Tommy    |
| Alex     |
