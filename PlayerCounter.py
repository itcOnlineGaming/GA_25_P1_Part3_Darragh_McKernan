import pandas as pd
def CountPlayers():
    dataset = pd.read_csv("C:\\Users\\gameuser\\Desktop\\GA_25_P1_Part3_Darragh_McKernan\\data\\demographics.csv")
    playerCount = dataset['pid'].nunique()
    return playerCount

def PlayerLogin():
    logins = pd.read_csv("C:\\Users\\gameuser\\Desktop\\GA_25_P1_Part3_Darragh_McKernan\\data\\player_logged_in.csv", parse_dates=["Time"])
    return logins[['pid', 'Time']].rename(columns={"Time": "LoginTime"})
    
def PlayerLogout():
    logouts = pd.read_csv("C:\\Users\\gameuser\\Desktop\\GA_25_P1_Part3_Darragh_McKernan\\data\\exited_game.csv", parse_dates=["Time"])
    return logouts[['pid', 'Time']].rename(columns={"Time": "LogoutTime"})

def GetLevelProgression():
    logouts = pd.read_csv("C:\\Users\\gameuser\\Desktop\\GA_25_P1_Part3_Darragh_McKernan\\data\\exited_game.csv", parse_dates=["Time"])
    return logouts[['pid', 'Time', 'LevelProgressionAmount']].rename(columns={"Time": "LogoutTime"})