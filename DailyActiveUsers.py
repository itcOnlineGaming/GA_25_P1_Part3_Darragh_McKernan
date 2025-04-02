import pandas as pd
def GetDailyActiveUsers():

    dailyLogins = pd.read_csv("C:\\Users\\Darragh\\Desktop\\Programming\\Year 4\\Game Analytics\\GA_25_P1_Part3_Darragh_McKernan\\data\\player_logged_in.csv",parse_dates=["Time"],dayfirst=True)
    dailyLogins["Date"] = dailyLogins["Time"].dt.date
    dailyLogins = dailyLogins.groupby("Date")["pid"].nunique().reset_index(name="DAU")

    return dailyLogins.sort_values("Date")