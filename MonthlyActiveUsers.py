import pandas as pd
def GetMonthlyActiveUsers():

    monthlyLogins = pd.read_csv("C:\\Users\\gameuser\\Desktop\\GA_25_P1_Part3_Darragh_McKernan\\data\\player_logged_in.csv",parse_dates=["Time"],dayfirst=True)
    monthlyLogins["Month"] = monthlyLogins["Time"].dt.to_period("M").astype(str)
    monthlyLogins = monthlyLogins.groupby("Month")["pid"].nunique().reset_index(name="MAU")

    return monthlyLogins.sort_values("Month")