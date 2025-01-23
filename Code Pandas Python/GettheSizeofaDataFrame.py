>.<

Title: Get the Size of a DataFrame
Link: https://leetcode.com/problems/get-the-size-of-a-dataframe/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Level: Easy

Write a solution to calculate and display the number of rows and columns of players.

Data players:
player_id: int
name: object
age: int
position: object

>.<

Solution:

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

Output:

| 0  |
| -- |
| 10 |
| 5  |
