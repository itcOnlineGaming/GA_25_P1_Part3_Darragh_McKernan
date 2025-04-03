import pandas as pd
def GetEstimatedSessions():
    dailyLogins = pd.read_csv("C:\\Users\\gameuser\\Desktop\\GA_25_P1_Part3_Darragh_McKernan\\data\\player_logged_in.csv")
    return dailyLogins["EventName"].count()