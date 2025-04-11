import pandas as pd
import os
currentDirectory = os.path.dirname(os.path.abspath(__file__))
def GetMonthlyActiveUsers():
    path = os.path.join(currentDirectory, "data", "player_logged_in.csv")
    monthlyLogins = pd.read_csv(path, parse_dates=["Time"], dayfirst=True)
    monthlyLogins["Month"] = monthlyLogins["Time"].dt.to_period("M").astype(str)
    monthlyLogins = monthlyLogins.groupby("Month")["pid"].nunique().reset_index(name="MAU")

    return monthlyLogins.sort_values("Month")