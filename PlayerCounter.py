import pandas as pd
import os
currentDirectory = os.path.dirname(os.path.abspath(__file__))
def CountPlayers():
    dataset = pd.read_csv(os.path.join(currentDirectory,"data","demographics.csv"))
    playerCount = dataset['pid'].nunique()
    return playerCount

def PlayerLogin():
    logins = pd.read_csv(os.path.join(currentDirectory, "data", "player_logged_in.csv"), parse_dates=["Time"])
    return logins[['pid', 'Time']].rename(columns={"Time": "LoginTime"})
    
def PlayerLogout():
    logouts = pd.read_csv(os.path.join(currentDirectory, "data", "exited_game.csv"), parse_dates=["Time"])
    return logouts[['pid', 'Time']].rename(columns={"Time": "LogoutTime"})

def GetLevelProgression():
    logouts = pd.read_csv(os.path.join(currentDirectory, "data", "exited_game.csv"), parse_dates=["Time"])
    return logouts[['pid', 'Time', 'LevelProgressionAmount']].rename(columns={"Time": "LogoutTime"})

def GetJobCompleted():
    jobCompleted = pd.read_csv(os.path.join(currentDirectory,"data","job_completed.csv"))
    return jobCompleted