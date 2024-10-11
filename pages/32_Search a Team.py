import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from math import ceil
from datetime import date
from streamlit_dynamic_filters import DynamicFilters
import urllib.request
from PIL import Image
import time
from dplython import (DplyFrame, X, diamonds, select, sift, sample_n, sample_frac, head, arrange, mutate, group_by, summarize, DelayFunction)
from itables.streamlit import interactive_table
from itables import to_html_datatable
from streamlit.components.v1 import html
from plotly.subplots import make_subplots


st.set_page_config(layout='wide',page_title="Search a Team",page_icon="🏀")
def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)

download_image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh6BYfXG_CbAZa1KEDq4pu2Fxw_OeTLLmFcA&s','eurologo.png')
st.image(Image.open("eurologo.png"),width=100)
st.sidebar.write("If an error message appears, please refresh the page")
def fixture_format1(Fixture):
    if Fixture<=15:
        return "First Round"
    elif Fixture>15 and Fixture<=30:
        return "Second Round"
    elif Fixture==31:
        return "PO 1"
    elif Fixture == 32:
        return "PO 2"
    elif Fixture == 33:
        return "PO 3"
    elif Fixture == 34:
        return "PO 4"
    elif Fixture == 35:
        return "PO 5"
    elif Fixture==36:
        return "Semi Final"
    elif Fixture==37:
        return "Third Place"
    elif Fixture==38:
        return "Final"
def fixture_format2(Fixture):
    if Fixture <= 15:
        return "First Round"
    elif Fixture > 15 and Fixture <= 30:
        return "Second Round"
    elif Fixture == 31:
        return "PO 1"
    elif Fixture == 32:
        return "PO 2"
    elif Fixture == 33:
        return "PO 3"
    elif Fixture == 34:
        return "PO 4"
    elif Fixture == 35:
        return "Semi Final"
    elif Fixture == 36:
        return "Third Place"
    elif Fixture == 37:
        return "Final"
def fixture_format3(Fixture):
    if Fixture <= 17:
        return "First Round"
    elif Fixture > 17 and Fixture <= 34:
        return "Second Round"
def fixture_format4(Fixture):
    if Fixture <= 17:
        return "First Round"
    elif Fixture > 17 and Fixture <= 34:
        return "Second Round"
    elif Fixture == 35:
        return "PO 1"
    elif Fixture == 36:
        return "PO 2"
    elif Fixture == 37:
        return "PO 3"
    elif Fixture == 38:
        return "PO 4"
    elif Fixture == 39:
        return "PO 5"
    elif Fixture == 40:
        return "Semi Final"
    elif Fixture == 41:
        return "Third Place"
    elif Fixture == 42:
        return "Final"

def fixture_format5(Fixture):
        if Fixture <= 17:
            return "First Round"
        elif Fixture > 17 and Fixture <= 34:
            return "Second Round"
        elif Fixture == 35:
            return "PI 1"
        elif Fixture == 36:
            return "PI 2"
        elif Fixture == 37:
            return "PO 1"
        elif Fixture == 38:
            return "PO 2"
        elif Fixture == 39:
            return "PO 3"
        elif Fixture == 40:
            return "PO 4"
        elif Fixture == 41:
            return "PO 5"
        elif Fixture == 42:
            return "Semi Final"
        elif Fixture == 43:
            return "Third Place"
        elif Fixture == 44:
            return "Final"


euroleague_2016_2017_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2016_2017_playerstats.csv")
euroleague_2016_2017_playerstats['idseason']=euroleague_2016_2017_playerstats['IDGAME'] + "_" + euroleague_2016_2017_playerstats['Season']
euroleague_2016_2017_playerstats[['Fixture', 'Game']] = euroleague_2016_2017_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2016_2017_playerstats['Fixture']=pd.to_numeric(euroleague_2016_2017_playerstats['Fixture'])
euroleague_2016_2017_playerstats['Round']=euroleague_2016_2017_playerstats['Fixture'].apply(fixture_format1)


euroleague_2017_2018_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2017_2018_playerstats.csv")
euroleague_2017_2018_playerstats['idseason']=euroleague_2017_2018_playerstats['IDGAME'] + "_" + euroleague_2017_2018_playerstats['Season']
euroleague_2017_2018_playerstats[['Fixture', 'Game']] = euroleague_2017_2018_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2017_2018_playerstats['Fixture']=pd.to_numeric(euroleague_2017_2018_playerstats['Fixture'])
euroleague_2017_2018_playerstats['Round']=euroleague_2017_2018_playerstats['Fixture'].apply(fixture_format2)


euroleague_2018_2019_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2018_2019_playerstats.csv")
euroleague_2018_2019_playerstats['idseason']=euroleague_2018_2019_playerstats['IDGAME'] + "_" + euroleague_2018_2019_playerstats['Season']
euroleague_2018_2019_playerstats[['Fixture', 'Game']] = euroleague_2018_2019_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2018_2019_playerstats['Fixture']=pd.to_numeric(euroleague_2018_2019_playerstats['Fixture'])
euroleague_2018_2019_playerstats['Round']=euroleague_2018_2019_playerstats['Fixture'].apply(fixture_format1)


euroleague_2019_2020_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2019_2020_playerstats.csv")
euroleague_2019_2020_playerstats['idseason']=euroleague_2019_2020_playerstats['IDGAME'] + "_" + euroleague_2019_2020_playerstats['Season']
euroleague_2019_2020_playerstats[['Fixture', 'Game']] = euroleague_2019_2020_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2019_2020_playerstats['Fixture']=pd.to_numeric(euroleague_2019_2020_playerstats['Fixture'])
euroleague_2019_2020_playerstats['Round']=euroleague_2019_2020_playerstats['Fixture'].apply(fixture_format3)


euroleague_2020_2021_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2020_2021_playerstats.csv")
euroleague_2020_2021_playerstats['idseason']=euroleague_2020_2021_playerstats['IDGAME'] + "_" + euroleague_2020_2021_playerstats['Season']
euroleague_2020_2021_playerstats[['Fixture', 'Game']] = euroleague_2020_2021_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2020_2021_playerstats['Fixture']=pd.to_numeric(euroleague_2020_2021_playerstats['Fixture'])
euroleague_2020_2021_playerstats['Round']=euroleague_2020_2021_playerstats['Fixture'].apply(fixture_format4)

euroleague_2021_2022_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2021_2022_playerstats.csv")
euroleague_2021_2022_playerstats['idseason']=euroleague_2021_2022_playerstats['IDGAME'] + "_" + euroleague_2021_2022_playerstats['Season']
euroleague_2021_2022_playerstats[['Fixture', 'Game']] = euroleague_2021_2022_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2021_2022_playerstats['Fixture']=pd.to_numeric(euroleague_2021_2022_playerstats['Fixture'])
euroleague_2021_2022_playerstats['Round']=euroleague_2021_2022_playerstats['Fixture'].apply(fixture_format4)


euroleague_2022_2023_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2022_2023_playerstats.csv")
euroleague_2022_2023_playerstats['idseason']=euroleague_2022_2023_playerstats['IDGAME'] + "_" + euroleague_2022_2023_playerstats['Season']
euroleague_2022_2023_playerstats[['Fixture', 'Game']] = euroleague_2022_2023_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2022_2023_playerstats['Fixture']=pd.to_numeric(euroleague_2022_2023_playerstats['Fixture'])
euroleague_2022_2023_playerstats['Round']=euroleague_2022_2023_playerstats['Fixture'].apply(fixture_format4)

euroleague_2023_2024_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2023_2024_playerstats.csv")
euroleague_2023_2024_playerstats['idseason']=euroleague_2023_2024_playerstats['IDGAME'] + "_" + euroleague_2023_2024_playerstats['Season']
euroleague_2023_2024_playerstats[['Fixture', 'Game']] = euroleague_2023_2024_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2023_2024_playerstats['Fixture']=pd.to_numeric(euroleague_2023_2024_playerstats['Fixture'])
euroleague_2023_2024_playerstats['Round']=euroleague_2023_2024_playerstats['Fixture'].apply(fixture_format5)

euroleague_2024_2025_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2024_2025_playerstats.csv")
euroleague_2024_2025_playerstats['idseason']=euroleague_2024_2025_playerstats['IDGAME'] + "_" + euroleague_2024_2025_playerstats['Season']
euroleague_2024_2025_playerstats[['Fixture', 'Game']] = euroleague_2024_2025_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2024_2025_playerstats['Fixture']=pd.to_numeric(euroleague_2024_2025_playerstats['Fixture'])
euroleague_2024_2025_playerstats['Round']=euroleague_2024_2025_playerstats['Fixture'].apply(fixture_format5)



euroleague_2016_2017_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2016_2017_results.csv")
euroleague_2016_2017_results['idseason']=euroleague_2016_2017_results['IDGAME'] + "_" + euroleague_2016_2017_results['Season']
euroleague_2016_2017_results[['Fixture', 'Game']] = euroleague_2016_2017_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2016_2017_results['Fixture']=pd.to_numeric(euroleague_2016_2017_results['Fixture'])
euroleague_2016_2017_results['Round']=euroleague_2016_2017_results['Fixture'].apply(fixture_format1)


euroleague_2017_2018_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2017_2018_results.csv")
euroleague_2017_2018_results['idseason']=euroleague_2017_2018_results['IDGAME'] + "_" + euroleague_2017_2018_results['Season']
euroleague_2017_2018_results[['Fixture', 'Game']] = euroleague_2017_2018_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2017_2018_results['Fixture']=pd.to_numeric(euroleague_2017_2018_results['Fixture'])
euroleague_2017_2018_results['Round']=euroleague_2017_2018_results['Fixture'].apply(fixture_format2)


euroleague_2018_2019_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2018_2019_results.csv")
euroleague_2018_2019_results['idseason']=euroleague_2018_2019_results['IDGAME'] + "_" + euroleague_2018_2019_results['Season']
euroleague_2018_2019_results[['Fixture', 'Game']] = euroleague_2018_2019_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2018_2019_results['Fixture']=pd.to_numeric(euroleague_2018_2019_results['Fixture'])
euroleague_2018_2019_results['Round']=euroleague_2018_2019_results['Fixture'].apply(fixture_format1)


euroleague_2019_2020_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2019_2020_results.csv")
euroleague_2019_2020_results['idseason']=euroleague_2019_2020_results['IDGAME'] + "_" + euroleague_2019_2020_results['Season']
euroleague_2019_2020_results[['Fixture', 'Game']] = euroleague_2019_2020_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2019_2020_results['Fixture']=pd.to_numeric(euroleague_2019_2020_results['Fixture'])
euroleague_2019_2020_results['Round']=euroleague_2019_2020_results['Fixture'].apply(fixture_format3)


euroleague_2020_2021_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2020_2021_results.csv")
euroleague_2020_2021_results['idseason']=euroleague_2020_2021_results['IDGAME'] + "_" + euroleague_2020_2021_results['Season']
euroleague_2020_2021_results[['Fixture', 'Game']] = euroleague_2020_2021_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2020_2021_results['Fixture']=pd.to_numeric(euroleague_2020_2021_results['Fixture'])
euroleague_2020_2021_results['Round']=euroleague_2020_2021_results['Fixture'].apply(fixture_format4)

euroleague_2021_2022_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2021_2022_results.csv")
euroleague_2021_2022_results['idseason']=euroleague_2021_2022_results['IDGAME'] + "_" + euroleague_2021_2022_results['Season']
euroleague_2021_2022_results[['Fixture', 'Game']] = euroleague_2021_2022_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2021_2022_results['Fixture']=pd.to_numeric(euroleague_2021_2022_results['Fixture'])
euroleague_2021_2022_results['Round']=euroleague_2021_2022_results['Fixture'].apply(fixture_format4)


euroleague_2022_2023_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2022_2023_results.csv")
euroleague_2022_2023_results['idseason']=euroleague_2022_2023_results['IDGAME'] + "_" + euroleague_2022_2023_results['Season']
euroleague_2022_2023_results[['Fixture', 'Game']] = euroleague_2022_2023_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2022_2023_results['Fixture']=pd.to_numeric(euroleague_2022_2023_results['Fixture'])
euroleague_2022_2023_results['Round']=euroleague_2022_2023_results['Fixture'].apply(fixture_format4)

euroleague_2023_2024_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2023_2024_results.csv")
euroleague_2023_2024_results['idseason']=euroleague_2023_2024_results['IDGAME'] + "_" + euroleague_2023_2024_results['Season']
euroleague_2023_2024_results[['Fixture', 'Game']] = euroleague_2023_2024_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2023_2024_results['Fixture']=pd.to_numeric(euroleague_2023_2024_results['Fixture'])
euroleague_2023_2024_results['Round']=euroleague_2023_2024_results['Fixture'].apply(fixture_format5)

euroleague_2024_2025_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2024_2025_results.csv")
euroleague_2024_2025_results['idseason']=euroleague_2024_2025_results['IDGAME'] + "_" + euroleague_2024_2025_results['Season']
euroleague_2024_2025_results[['Fixture', 'Game']] = euroleague_2024_2025_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2024_2025_results['Fixture']=pd.to_numeric(euroleague_2024_2025_results['Fixture'])
euroleague_2024_2025_results['Round']=euroleague_2024_2025_results['Fixture'].apply(fixture_format5)


All_Seasons=pd.concat([euroleague_2016_2017_playerstats,euroleague_2017_2018_playerstats,euroleague_2018_2019_playerstats,euroleague_2019_2020_playerstats,euroleague_2020_2021_playerstats,euroleague_2021_2022_playerstats,euroleague_2022_2023_playerstats,euroleague_2023_2024_playerstats,euroleague_2024_2025_playerstats])

All_Seasons_results=pd.concat([euroleague_2016_2017_results,euroleague_2017_2018_results,euroleague_2018_2019_results,euroleague_2019_2020_results,euroleague_2020_2021_results,euroleague_2021_2022_results,euroleague_2022_2023_results,euroleague_2023_2024_results,euroleague_2024_2025_results])


def result_format(Win):
    if Win == 1:
        return "W"
    elif Win == 0:
        return "L"


def result_format(Win):
    if Win == 1:
        return "W"
    elif Win == 0:
        return "L"



home_team=(All_Seasons_results[['Fixture',"Phase","Home","Away","Home_Points","Away_Points",
                                "Q1H","Q2H","Q3H","Q4H",'EXH',"Q1A","Q2A","Q3A","Q4A",'EXA','Season','Round','Home_win','idseason']]
           .rename(columns={"Home":'Team',"Away":'Against',"Home_Points":'Scored',"Away_Points":"Conceed",
                                "Q1H":'Q1S',"Q2H":'Q2S',"Q3H":'Q3S',"Q4H":'Q4S','EXH':'EXS',"Q1A":'Q1C',
                            "Q2A":'Q2C',"Q3A":'Q3C',"Q4A":'Q4C','EXA':'EXC','Home_win':'Win'}))

home_team['HA']="H"
away_team=(All_Seasons_results[['Fixture',"Phase","Home","Away","Home_Points","Away_Points",
                                "Q1H","Q2H","Q3H","Q4H",'EXH',"Q1A","Q2A","Q3A","Q4A",'EXA','Season','Round','Away_win','idseason']]
           .rename(columns={"Home":'Against',"Away":'Team',"Home_Points":'Conceed',"Away_Points":"Scored",
                                "Q1H":'Q1C',"Q2H":'Q2C',"Q3H":'Q3C',"Q4H":'Q4C','EXH':'EXC',"Q1A":'Q1S',
                            "Q2A":'Q2S',"Q3A":'Q3S',"Q4A":'Q4S','EXA':'EXS','Away_win':'Win'}))
away_team['HA']="A"

period_points=pd.concat([home_team,away_team])

period_points["FHS"]=period_points["Q1S"]+period_points["Q2S"]
period_points["FHC"]=period_points["Q1C"]+period_points["Q2C"]
period_points["SHS"]=period_points["Q3S"]+period_points["Q4S"]
period_points["SHC"]=period_points["Q3C"]+period_points["Q4C"]
period_points["results"]=period_points["Win"].apply(result_format)
period_points['EXS'].replace(0, np.nan, inplace=True)
period_points['EXC'].replace(0, np.nan, inplace=True)






search_team_team1=st.sidebar.selectbox("Choose  Team:",All_Seasons['Team'].reset_index().sort_values('Team')['Team'].unique())
search_team_ha_team1 = st.sidebar.selectbox("Home or Away games(First Team):",['A', 'H', 'All'],index=2)
search_team_season_team1 = st.sidebar.selectbox("Season(First Team):",['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021','2021-2022', '2022-2023', '2023-2024','2024-2025','All'],index=8)
search_team_phase_team1 = st.sidebar.selectbox("Phase(First Team):",['Regular Season', 'Play In','Play offs', 'Final Four','All'],index=4)
search_team_wl_team1 = st.sidebar.selectbox("Result(First Team):",['W', 'L','All'],index=2)
search_team_round_team1 = st.sidebar.selectbox("Round(First Team):",['First Round', 'Second Round','PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final', 'All'],index=12)




if "All" in search_team_ha_team1:
    search_team_ha_team1 = ['A', 'H']
    All_Seasons1=All_Seasons.loc[All_Seasons['HA'].isin(search_team_ha_team1)]
    period_points1=period_points.loc[period_points['HA'].isin(search_team_ha_team1)]
    select_ha_player1=''
else:
    All_Seasons1=All_Seasons.loc[All_Seasons['HA']==search_team_ha_team1]
    period_points1 = period_points.loc[period_points['HA'] == search_team_ha_team1]
    select_ha_player1 = search_team_ha_team1

if "All" in search_team_season_team1:
    search_team_season_team1 = ['2016-2017', '2017-2018', '2018-2019', '2019-2020','2020-2021','2021-2022', '2022-2023','2023-2024','2024-2025']
    All_Seasons1=All_Seasons1.loc[All_Seasons1['Season'].isin(search_team_season_team1)]
    period_points1 = period_points1.loc[period_points1['Season'].isin(search_team_season_team1)]
    select_season_player1 = ''
else:
    All_Seasons1=All_Seasons1.loc[All_Seasons1['Season']==search_team_season_team1]
    period_points1 = period_points1.loc[period_points1['Season'] == search_team_season_team1]
    select_season_player1 = search_team_season_team1

if "All" in search_team_wl_team1:
    search_team_wl_team1 = ['W', 'L']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['results'].isin(search_team_wl_team1)]
    period_points1 = period_points1.loc[period_points1['results'].isin(search_team_wl_team1)]
    select_wl_player1 = ''
else:
    All_Seasons1= All_Seasons1.loc[All_Seasons1['results'] == search_team_wl_team1]
    period_points1 = period_points1.loc[period_points1['results'] == search_team_wl_team1]
    select_wl_player1 = search_team_wl_team1

if "All" in search_team_phase_team1:
    search_team_phase_team1 = ['Regular Season', 'Play In','Play offs', 'Final Four']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Phase'].isin(search_team_phase_team1)]
    period_points1 = period_points1.loc[period_points1['Phase'].isin(search_team_phase_team1)]
    select_phase_player1 = ''
else:
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Phase'] == search_team_phase_team1]
    period_points1 = period_points1.loc[period_points1['Phase'] == search_team_phase_team1]
    select_phase_player1 = search_team_phase_team1


if "All" in search_team_round_team1:
    search_team_round_team1 = ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Round'].isin(search_team_round_team1)]
    period_points1 = period_points1.loc[ period_points1['Round'].isin(search_team_round_team1)]
    select_round_player1 = ''
else:
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Round'] == search_team_round_team1]
    period_points1 = period_points1.loc[period_points1['Round']==search_team_round_team1]
    select_round_player1 = search_team_round_team1



def team_rating_stat_higher(dataset,stat):
    dataset1=dataset[["Team",stat]].sort_values(stat).reset_index()
    dataset1.drop("index",axis=1,inplace=True)
    final_dataset=dataset1.reset_index() >> mutate(Rating=(100*(X.index+1)/X.Team.nunique()),Rating1=(100-(100-X.Rating.round(0))*0.5).round(0))
    final_dataset.rename(columns={'Rating1':'Rating '+ stat},inplace=True)
    final_dataset.drop(["index","Rating",stat],axis=1,inplace=True)
    return final_dataset

def team_rating_stat_lower(dataset,stat):
    dataset1=dataset[["Team",stat]].sort_values(stat,ascending=False).reset_index()
    dataset1.drop("index",axis=1,inplace=True)
    final_dataset=dataset1.reset_index() >> mutate(Rating=(100*(X.index+1)/X.Team.nunique()),Rating1=(100-(100-X.Rating.round(0))*0.5).round(0))
    final_dataset.rename(columns={'Rating1':'Rating '+ stat},inplace=True)
    final_dataset.drop(["index","Rating",stat],axis=1,inplace=True)
    return final_dataset





def compute_team_stats(dataset_stats,dataset_periods):


    finalstats=dataset_stats.groupby(['idseason','Team'])[['PTS','F2M',
                                  'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                  'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF',
                                  'PIR','Possesions']].sum().reset_index().groupby('Team')[['PTS','F2M',
                                  'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                  'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF',
                                  'PIR','Possesions']].mean().reset_index()
    finalstats['2P(%)']=100*(finalstats['F2M']/finalstats['F2A'])
    finalstats['3P(%)']=100*(finalstats['F3M']/finalstats['F3A'])
    finalstats['FT(%)']=100*(finalstats['FTM']/finalstats['FTA'])
    finalstats['Offensive Rating']=100*(finalstats['PTS']/finalstats['Possesions'])
    finalstats['EFG(%)']=100*(finalstats['F2M']+1.5*finalstats['F3M'])/(finalstats['F2A']+finalstats['F3A'])
    finalstats['TS(%)']=100*(finalstats['PTS'])/(2*(finalstats['F2A']+finalstats['F3A']+0.44*finalstats['FTA']))
    finalstats['FT Ratio']=finalstats['FTA']/(finalstats['F3A']+finalstats['F2A'])
    finalstats['AS-TO Ratio']=finalstats['AS']/finalstats['TO']
    finalstats['TO Ratio']=100*(finalstats['TO']/finalstats['Possesions'])
    finalstats['AS Ratio']=100*(finalstats['AS']/finalstats['Possesions'])
    finalstats=finalstats[['Team','PTS','F2M','F2A', '2P(%)','F3M', 'F3A','3P(%)', 'FTM', 'FTA','FT(%)', 'OR','DR', 'TR',
                           'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF','PIR','Possesions','Offensive Rating','EFG(%)',
                           'TS(%)','FT Ratio','AS-TO Ratio','TO Ratio','AS Ratio']].round(1)

    finalstats_opp=dataset_stats.groupby(['idseason','Against'])[['PTS','F2M',
                                  'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                  'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF',
                                  'PIR','Possesions']].sum().reset_index().groupby('Against')[['PTS','F2M',
                                  'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                  'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF',
                                  'PIR','Possesions']].mean().reset_index()


    finalstats_opp['2P(%)']=100*(finalstats_opp['F2M']/finalstats_opp['F2A'])
    finalstats_opp['3P(%)']=100*(finalstats_opp['F3M']/finalstats_opp['F3A'])
    finalstats_opp['FT(%)']=100*(finalstats_opp['FTM']/finalstats_opp['FTA'])
    finalstats_opp['Offensive Rating']=100*(finalstats_opp['PTS']/finalstats_opp['Possesions'])
    finalstats_opp['EFG(%)']=100*(finalstats_opp['F2M']+1.5*finalstats_opp['F3M'])/(finalstats_opp['F2A']+finalstats_opp['F3A'])
    finalstats_opp['TS(%)']=100*(finalstats_opp['PTS'])/(2*(finalstats_opp['F2A']+finalstats_opp['F3A']+0.44*finalstats_opp['FTA']))
    finalstats_opp['FT Ratio']=finalstats_opp['FTA']/(finalstats_opp['F3A']+finalstats_opp['F2A'])
    finalstats_opp['AS-TO Ratio']=finalstats_opp['AS']/finalstats_opp['TO']
    finalstats_opp['TO Ratio']=100*(finalstats_opp['TO']/finalstats_opp['Possesions'])
    finalstats_opp['AS Ratio']=100*(finalstats_opp['AS']/finalstats_opp['Possesions'])
    finalstats_opp=finalstats_opp[['Against','PTS','F2M','F2A', '2P(%)','F3M', 'F3A','3P(%)', 'FTM', 'FTA','FT(%)', 'OR','DR', 'TR',
                           'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF','PIR','Possesions','Offensive Rating','EFG(%)',
                           'TS(%)','FT Ratio','AS-TO Ratio','TO Ratio','AS Ratio']].round(1).rename(columns={'Against':'Team'})

    finalstats_opp_for_rating=finalstats_opp.add_prefix("opp ").rename(columns={'opp Team':'Team'})

    gamesstats=pd.merge(finalstats,finalstats_opp_for_rating)


    colsplus = ['AS', 'F2M', 'F2A', 'F3M', 'F3A', 'FTM',
                'FTA', 'OR', 'DR', 'TR', 'BLK', 'RF', 'ST', '2P(%)', '3P(%)', 'FT(%)',  'EFG(%)', 'TS(%)', 'FT Ratio', 'AS-TO Ratio',
                'AS Ratio',  'opp TO Ratio','Offensive Rating']

    colsminus = ['BLKR', 'PF','opp PTS', 'opp AS', 'opp F2M', 'opp F2A','opp 2P(%)', 'opp F3M', 'opp F3A', 'opp 3P(%)',
                 'opp FTM', 'opp FTA', 'opp FT(%)', 'opp OR', 'opp DR','opp TR','opp ST','opp Offensive Rating', 'opp EFG(%)','opp TS(%)',
                 'opp FT Ratio','opp AS-TO Ratio','opp AS Ratio','TO Ratio']

    teams_ratings1 = team_rating_stat_higher(gamesstats, "PTS")
    for i in colsplus:
        df2 = team_rating_stat_higher(gamesstats, i)
        teams_ratings1 = pd.merge(teams_ratings1, df2)

    teams_ratings2 = team_rating_stat_lower(gamesstats, "TO")
    for i in colsminus:
        df3 = team_rating_stat_lower(gamesstats, i)
        teams_ratings2 = pd.merge(teams_ratings2, df3)
    teams_ratings = pd.merge(teams_ratings1, teams_ratings2)

    return [finalstats,finalstats_opp,teams_ratings]



teamstats=compute_team_stats(All_Seasons1,period_points1)[0]
oppstats=compute_team_stats(All_Seasons1,period_points1)[1]
ratingstats=compute_team_stats(All_Seasons1,period_points1)[2]

teams,ratings,gamesstats=st.columns([1,1,1])

with teams:
    st.write('### Team: ' + search_team_team1)
    st.write('Season: ' + select_season_player1)
    st.write('Phase: ' + select_phase_player1)
    st.write('Round: ' + select_round_player1)
    st.write('Home or away: ' + select_ha_player1)
    st.write('Result: ' + select_wl_player1)

with ratings:
    try:


        offense_rating_data1=ratingstats.loc[ratingstats.Team==search_team_team1][
            ['Rating PTS', 'Rating AS', 'Rating TO', 'Rating OR', 'Rating BLKR', 'Rating RF', 'Rating F2M', 'Rating F2A',
             'Rating 2P(%)', 'Rating F3M', 'Rating F3A', 'Rating 3P(%)','Rating FTM', 'Rating FTA', 'Rating FT(%)', 'Rating FT Ratio',
             'Rating EFG(%)', 'Rating TS(%)', "Rating Offensive Rating",'Rating AS-TO Ratio', "Rating AS Ratio", 'Rating opp DR', 'Rating opp ST',
             'Rating TO Ratio','Rating opp TO Ratio']].melt()
        offense_ratings1 = offense_rating_data1['value'].mean()

        off1 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=offense_ratings1.round(0),
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 100]},
                   'bordercolor': "gray"},
            title={'text': "Offense"}))

        off1.update_layout(
            autosize=False,
            width=250,
            height=150,
            margin=dict(
                l=30,
                r=50,
                b=10,
                t=40,
                pad=0
            ))

        st.write(off1)



        defense_ratings1 = ratingstats.loc[ratingstats.Team==search_team_team1][
            ['Rating ST', 'Rating DR', 'Rating PF', 'Rating BLK','Rating opp PTS', 'Rating opp AS',
             'Rating opp F2M', 'Rating opp F2A', 'Rating opp 2P(%)', 'Rating opp F3M', 'Rating opp F3A', 'Rating opp 3P(%)',
                 'Rating opp FTM', 'Rating opp FTA', 'Rating opp FT(%)', 'Rating opp OR','Rating opp Offensive Rating','Rating opp EFG(%)', 'Rating opp TS(%)',
                 'Rating opp FT Ratio', 'Rating opp AS-TO Ratio', 'Rating opp AS Ratio']].melt()['value'].mean()

        defe1 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=defense_ratings1.round(0),
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 100]},
                   'bordercolor': "gray"},
            title={'text': "Defense"}))

        defe1.update_layout(
            autosize=True,
            width=250,
            height=150,
            margin=dict(
                l=30,
                r=50,
                b=10,
                t=40,
                pad=0
            )
        )

        st.write(defe1)


        total_ratings1 = ratingstats.loc[ratingstats.Team==search_team_team1].filter(regex='Rating').melt()['value'].mean()

        tot = go.Figure(go.Indicator(
            mode="gauge+number",
            value=total_ratings1.round(0),
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 100]},
                   'bordercolor': "gray"},
            title={'text': "Overall"}))

        tot.update_layout(
            autosize=True,
            width=250,
            height=150,
            margin=dict(
                l=30,
                r=50,
                b=10,
                t=10,
                pad=0
            )
        )

        st.write(tot)
    except:
        st.error("No data available with this parameters")


with gamesstats:

    games=pd.DataFrame({'Played':['Total Games'],'No.Games':[period_points1.loc[period_points1.Team == search_team_team1]['Team'].value_counts().reset_index()['count'].sum()]})
    try:
        wins = pd.DataFrame({'Played': ['Total Wins'], 'No.Games': [
            period_points1.loc[(period_points1.Team == search_team_team1)&(period_points1.results == "W")]['Team'].value_counts().reset_index()[
                'count'].sum()]})
    except:
        wins=pd.DataFrame({'Played': ['Total Wins'], 'No.Games': [0]})
    try:
        loses = pd.DataFrame({'Played': ['Total Loses'], 'No.Games': [
            period_points1.loc[(period_points1.Team == search_team_team1) & (period_points1.results == "L")][
                'Team'].value_counts().reset_index()[
                'count'].sum()]})
    except:
        loses=pd.DataFrame({'Played': ['Total Loses'], 'No.Games': [0]})
    parts=pd.DataFrame({'Euroleague':['Years'],'Participation':[period_points.loc[(period_points.Team == search_team_team1)][['Phase', 'Season']].value_counts().reset_index()['Season'].nunique()]})
    playoff = pd.DataFrame({'Euroleague': ['Playoffs'], 'Participation': [
        period_points.loc[(period_points.Team == search_team_team1)&(period_points.Phase == 'Play offs')][['Phase', 'Season']].value_counts().reset_index()[
            'Season'].nunique()]})
    finalfour = pd.DataFrame({'Euroleague': ['F4'], 'Participation': [
        period_points.loc[(period_points.Team == search_team_team1) & (period_points.Phase == 'Final Four')][
            ['Phase', 'Season']].value_counts().reset_index()[
            'Season'].nunique()]})
    title = pd.DataFrame({'Euroleague': ['Titles'], 'Participation': [
        period_points.loc[(period_points.Team == search_team_team1) & (period_points.Phase == 'Final Four')& (period_points.Round == 'Final')& (period_points.results == 'W')][
            ['Phase', 'Season']].value_counts().reset_index()[
            'Season'].nunique()]})

    st.write('##### History in Euroleague')
    interactive_table(pd.concat([parts, playoff, finalfour, title]).set_index('Euroleague'),
                      paging=False, height=900, width=2000, showIndex=True,
                      classes="display order-column nowrap table_with_monospace_font", searching=True,
                      fixedColumns=True, select=True, info=False, scrollCollapse=True,
                      scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                      columnDefs=[{"className": "dt-center", "targets": "_all"}])

    st.write('##### Games in Euroleague')
    interactive_table(pd.concat([games,wins,loses]).set_index('Played'),
                  paging=False, height=900, width=2000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])


periodteam1 = (period_points1.loc[period_points1.Team==search_team_team1].groupby('Team')[['Q1S', 'Q2S', 'FHS', 'Q3S', 'Q4S', 'SHS', 'EXS']].mean().reset_index().round(1)
               .rename(columns={'Q1S': 'Q1', 'Q2S': 'Q2', 'Q3S': 'Q3', 'Q4S': 'Q4',
                                'EXS': 'Extra time', 'FHS': 'First Half', 'SHS': 'Second Half'
                                }))
periodteam2 = (period_points1.loc[period_points1.Team==search_team_team1].groupby('Team')[['Q1C', 'Q2C', 'FHC', 'Q3C', 'Q4C', 'SHC', 'EXC']].mean().reset_index().round(1)
    .rename(columns={'Q1C': 'Q1', 'Q2C': 'Q2', 'Q3C': 'Q3', 'Q4C': 'Q4','EXC': 'Extra time', 'FHC': 'First Half', 'SHC': 'Second Half'
                     }))
periodteam2['Team']=periodteam2['Team'].str.replace(search_team_team1,"Opponent")
periodteams = pd.concat([periodteam1, periodteam2])

st.write('##### Period Points per game')
interactive_table(periodteams.set_index("Team"),
                  paging=False, height=900, width=2000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])


basic_stats1 = teamstats.loc[teamstats.Team == search_team_team1][
    ['Team','PTS', 'AS', 'TO', 'TR', 'DR', 'OR', 'BLK', 'ST', 'PF', 'PIR']].rename(
    columns={'PTS': 'Points',
             'AS': 'Assists',
             'TO': 'Turnovers',
             'TR': 'Total Rebounds',
             'OR': 'Offensive Rebounds',
             'DR': 'Defensive Rebounds',
             'BLK': 'Blocks',
             'ST': 'Steals',
             'PF': 'Personal Fouls'}).round(1)

basic_stats2 = oppstats.loc[oppstats.Team == search_team_team1][
    ['Team','PTS', 'AS', 'TO', 'TR', 'DR', 'OR', 'BLK', 'ST', 'PF', 'PIR']].rename(
    columns={'PTS': 'Points',
             'AS': 'Assists',
             'TO': 'Turnovers',
             'TR': 'Total Rebounds',
             'OR': 'Offensive Rebounds',
             'DR': 'Defensive Rebounds',
             'BLK': 'Blocks',
             'ST': 'Steals',
             'PF': 'Personal Fouls'}).round(1)
basic_stats2['Team'] = basic_stats2['Team'].str.replace(search_team_team1, "Opponent")
basic_stats_data = pd.concat([basic_stats1, basic_stats2])
st.write('##### Basic Stats per game')
interactive_table(basic_stats_data.set_index("Team"),
                  paging=False, height=900, width=2000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])


st.write("##### Shooting Stats per game")
shooting_stats1 = teamstats.loc[teamstats.Team == search_team_team1][
    ['Team','F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)',
     'FT Ratio', 'EFG(%)', 'TS(%)']].rename(
    columns={'F2M': '2P Made',
             'F2A': '2P Attempt',
             'P2': '2P(%)',
             'F3M': '3P Made',
             'F3A': '3P Attempt',
             'P3': '3P(%)',
             'FTM': 'FT Made',
             'FTA': 'FT Attempt',
             'PFT': 'FT(%)',
             'FTR': 'FT Ratio',
             'EFG': 'EFG(%)',
             'TS': 'TS(%)'})

shooting_stats2 = oppstats.loc[oppstats.Team == search_team_team1][
    ['Team','F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)',
     'FT Ratio', 'EFG(%)', 'TS(%)']].rename(
    columns={'F2M': '2P Made',
             'F2A': '2P Attempt',
             'P2': '2P(%)',
             'F3M': '3P Made',
             'F3A': '3P Attempt',
             'P3': '3P(%)',
             'FTM': 'FT Made',
             'FTA': 'FT Attempt',
             'PFT': 'FT(%)',
             'FTR': 'FT Ratio',
             'EFG': 'EFG(%)',
             'TS': 'TS(%)'
             })
shooting_stats2['Team'] = shooting_stats2['Team'].str.replace(search_team_team1, "Opponent")
shooting_stats_data = pd.concat([shooting_stats1, shooting_stats2])
interactive_table(shooting_stats_data.set_index("Team"),
                  paging=False, height=900, width=2000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])
st.write("##### Advanced Stats per game")
advanced_stats1 = (teamstats.loc[teamstats.Team == search_team_team1][["Team",'Possesions', 'Offensive Rating',
                                 'AS-TO Ratio', 'TO Ratio', 'AS Ratio']]
                   )

advanced_stats2 = (oppstats.loc[oppstats.Team == search_team_team1][["Team",'Possesions', 'Offensive Rating',
                                 'AS-TO Ratio', 'TO Ratio', 'AS Ratio']]
                   )
advanced_stats2['Team'] = advanced_stats2['Team'].str.replace(search_team_team1, "Opponent")
advanced_stats_data = pd.concat([advanced_stats1, advanced_stats2])
interactive_table(advanced_stats_data.set_index("Team"),
                  paging=False, height=900, width=2000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])



def compute_team_stats_against_each_team(dataset_stats,dataset_periods):
    teamstats=dataset_stats.loc[dataset_stats.Team==search_team_team1]
    oppstats=dataset_stats.loc[dataset_stats.Against==search_team_team1]

    finalstats=teamstats.groupby(['idseason','Against'])[['PTS','F2M',
                                  'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                  'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF',
                                  'PIR','Possesions']].sum().reset_index().groupby('Against')[['PTS','F2M',
                                  'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                  'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF',
                                  'PIR','Possesions']].mean().reset_index()
    finalstats['2P(%)']=100*(finalstats['F2M']/finalstats['F2A'])
    finalstats['3P(%)']=100*(finalstats['F3M']/finalstats['F3A'])
    finalstats['FT(%)']=100*(finalstats['FTM']/finalstats['FTA'])
    finalstats['Offensive Rating']=100*(finalstats['PTS']/finalstats['Possesions'])
    finalstats['EFG(%)']=100*(finalstats['F2M']+1.5*finalstats['F3M'])/(finalstats['F2A']+finalstats['F3A'])
    finalstats['TS(%)']=100*(finalstats['PTS'])/(2*(finalstats['F2A']+finalstats['F3A']+0.44*finalstats['FTA']))
    finalstats['FT Ratio']=finalstats['FTA']/(finalstats['F3A']+finalstats['F2A'])
    finalstats['AS-TO Ratio']=finalstats['AS']/finalstats['TO']
    finalstats['TO Ratio']=100*(finalstats['TO']/finalstats['Possesions'])
    finalstats['AS Ratio']=100*(finalstats['AS']/finalstats['Possesions'])
    finalstats=finalstats[['Against','PTS','F2M','F2A', '2P(%)','F3M', 'F3A','3P(%)', 'FTM', 'FTA','FT(%)', 'OR','DR', 'TR',
                           'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF','PIR','Possesions','Offensive Rating','EFG(%)',
                           'TS(%)','FT Ratio','AS-TO Ratio','TO Ratio','AS Ratio']].round(1)

    finalstats_opp=oppstats.groupby(['idseason','Team'])[['PTS','F2M',
                                  'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                  'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF',
                                  'PIR','Possesions']].sum().reset_index().groupby('Team')[['PTS','F2M',
                                  'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                  'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF',
                                  'PIR','Possesions']].mean().reset_index()


    finalstats_opp['2P(%)']=100*(finalstats_opp['F2M']/finalstats_opp['F2A'])
    finalstats_opp['3P(%)']=100*(finalstats_opp['F3M']/finalstats_opp['F3A'])
    finalstats_opp['FT(%)']=100*(finalstats_opp['FTM']/finalstats_opp['FTA'])
    finalstats_opp['Offensive Rating']=100*(finalstats_opp['PTS']/finalstats_opp['Possesions'])
    finalstats_opp['EFG(%)']=100*(finalstats_opp['F2M']+1.5*finalstats_opp['F3M'])/(finalstats_opp['F2A']+finalstats_opp['F3A'])
    finalstats_opp['TS(%)']=100*(finalstats_opp['PTS'])/(2*(finalstats_opp['F2A']+finalstats_opp['F3A']+0.44*finalstats_opp['FTA']))
    finalstats_opp['FT Ratio']=finalstats_opp['FTA']/(finalstats_opp['F3A']+finalstats_opp['F2A'])
    finalstats_opp['AS-TO Ratio']=finalstats_opp['AS']/finalstats_opp['TO']
    finalstats_opp['TO Ratio']=100*(finalstats_opp['TO']/finalstats_opp['Possesions'])
    finalstats_opp['AS Ratio']=100*(finalstats_opp['AS']/finalstats_opp['Possesions'])
    finalstats_opp=finalstats_opp[['Team','PTS','F2M','F2A', '2P(%)','F3M', 'F3A','3P(%)', 'FTM', 'FTA','FT(%)', 'OR','DR', 'TR',
                           'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF','PIR','Possesions','Offensive Rating','EFG(%)',
                           'TS(%)','FT Ratio','AS-TO Ratio','TO Ratio','AS Ratio']].round(1).add_prefix('opp ').rename(columns={'opp Team':'Against','opp Offensive Rating':'Defensive Rating'})


    final=pd.merge(finalstats,finalstats_opp)[['Against','PTS','opp PTS','F2M','F2A', '2P(%)','opp F2M','opp F2A', 'opp 2P(%)','F3M', 'F3A','3P(%)', 'opp F3M', 'opp F3A','opp 3P(%)',
                                               'FTM', 'FTA','FT(%)',  'opp FTM', 'opp FTA','opp FT(%)', 'OR','opp OR','DR','opp DR', 'TR', 'opp TR',
                           'AS','opp AS', 'ST', 'opp ST', 'TO', 'opp TO',  'BLK', 'BLKR','PF', 'RF','PIR','opp PIR','Possesions', 'opp Possesions','Offensive Rating','Defensive Rating','EFG(%)','opp EFG(%)',
                           'TS(%)','opp TS(%)','FT Ratio','opp FT Ratio','AS-TO Ratio','opp AS-TO Ratio','TO Ratio','opp TO Ratio','AS Ratio','opp AS Ratio']]
    return final


st.write('##### Stats against each team in Euroleague')
interactive_table(compute_team_stats_against_each_team(All_Seasons1,period_points1).set_index('Against'),
                      paging=False, height=900, width=2000, showIndex=True,
                      classes="display order-column nowrap table_with_monospace_font", searching=False,
                      fixedColumns=True, select=True, info=False, scrollCollapse=True,
                      scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                      columnDefs=[{"className": "dt-center", "targets": "_all"}])
