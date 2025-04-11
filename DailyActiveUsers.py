import pandas as pd
import os
currentDirectory = os.path.dirname(os.path.abspath(__file__))
def GetDailyActiveUsers():
    path = os.path.join(currentDirectory, "data", "player_logged_in.csv")
    dailyLogins = pd.read_csv(path, parse_dates=["Time"], dayfirst=True)
    dailyLogins["Date"] = dailyLogins["Time"].dt.date
    dailyLogins = dailyLogins.groupby("Date")["pid"].nunique().reset_index(name="DAU")
    return dailyLogins.sort_values("Date")