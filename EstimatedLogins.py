import pandas as pd
import os
currentDirectory = os.path.dirname(os.path.abspath(__file__))
def GetEstimatedSessions():
    path = os.path.join(currentDirectory, "data", "player_logged_in.csv")
    dailyLogins = pd.read_csv(path)
    return dailyLogins["EventName"].count()