import pandas as pd
def CountPlayers():
    dataset = pd.read_csv("C:\\Users\\Darragh\\Desktop\\Programming\\Year 4\\Game Analytics\\GA_25_P1_Part3_Darragh_McKernan\\data\\demographics.csv")
    playerCount = dataset['pid'].nunique()
    return playerCount