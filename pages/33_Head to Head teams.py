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
from dplython import (DplyFrame, X, diamonds, select, sift, sample_n, sample_frac, head, arrange, mutate, group_by,
                      summarize, DelayFunction)
from itables.streamlit import interactive_table
from itables import to_html_datatable
from streamlit.components.v1 import html
from plotly.subplots import make_subplots

st.set_page_config(layout='wide', page_title="Head to Head teams", page_icon="🏀")
def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)

download_image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh6BYfXG_CbAZa1KEDq4pu2Fxw_OeTLLmFcA&s','eurologo.png')
st.image(Image.open("eurologo.png"),width=100)

def fixture_format1(Fixture):
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
        return "PO 5"
    elif Fixture == 36:
        return "Semi Final"
    elif Fixture == 37:
        return "Third Place"
    elif Fixture == 38:
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

@st.cache_data  
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



def games_format(HA, Fixture, Season, Team, Against):
    if HA == "H":
        return Fixture + " / " + Season + ' / ' + Team + ' - ' + Against
    elif HA == "A":
        return Fixture + " / " + Season + ' / ' + Against + ' - ' + Team


def result_format(Win):
    if Win == 1:
        return "W"
    elif Win == 0:
        return "L"


def period_win_format(S, C):
    if S > C:
        return 1
    else:
        return 0


def result_format(Win):
    if Win == 1:
        return "W"
    elif Win == 0:
        return "L"


def period_win_res_win_format(S, C, result):
    if S > C and result == "W":
        return 1
    else:
        return 0


home_team = (All_Seasons_results[['Fixture', "Phase", "Home", "Away", "Home_Points", "Away_Points",
                                  "Q1H", "Q2H", "Q3H", "Q4H", 'EXH', "Q1A", "Q2A", "Q3A", "Q4A", 'EXA', 'Season',
                                  'Round', 'Home_win', 'idseason']]
             .rename(columns={"Home": 'Team', "Away": 'Against', "Home_Points": 'Scored', "Away_Points": "Conceed",
                              "Q1H": 'Q1S', "Q2H": 'Q2S', "Q3H": 'Q3S', "Q4H": 'Q4S', 'EXH': 'EXS', "Q1A": 'Q1C',
                              "Q2A": 'Q2C', "Q3A": 'Q3C', "Q4A": 'Q4C', 'EXA': 'EXC', 'Home_win': 'Win'}))

home_team['HA'] = "H"
away_team = (All_Seasons_results[['Fixture', "Phase", "Home", "Away", "Home_Points", "Away_Points",
                                  "Q1H", "Q2H", "Q3H", "Q4H", 'EXH', "Q1A", "Q2A", "Q3A", "Q4A", 'EXA', 'Season',
                                  'Round', 'Away_win', 'idseason']]
             .rename(columns={"Home": 'Against', "Away": 'Team', "Home_Points": 'Conceed', "Away_Points": "Scored",
                              "Q1H": 'Q1C', "Q2H": 'Q2C', "Q3H": 'Q3C', "Q4H": 'Q4C', 'EXH': 'EXC', "Q1A": 'Q1S',
                              "Q2A": 'Q2S', "Q3A": 'Q3S', "Q4A": 'Q4S', 'EXA': 'EXS', 'Away_win': 'Win'}))
away_team['HA'] = "A"

period_points = pd.concat([home_team, away_team])

period_points["FHS"] = period_points["Q1S"] + period_points["Q2S"]
period_points["FHC"] = period_points["Q1C"] + period_points["Q2C"]
period_points["SHS"] = period_points["Q3S"] + period_points["Q4S"]
period_points["SHC"] = period_points["Q3C"] + period_points["Q4C"]
period_points["results"] = period_points["Win"].apply(result_format)
period_points['EXS'].replace(0, np.nan, inplace=True)
period_points['EXC'].replace(0, np.nan, inplace=True)

st.sidebar.write("## Select First team filters")
compare_teams_team1 = st.sidebar.selectbox("Choose First Team:",
                                           All_Seasons['Team'].reset_index().sort_values('Team')['Team'].unique())
compare_teams_ha_team1 = st.sidebar.selectbox("Home or Away games(First Team):", ['A', 'H', 'All'], index=2)
compare_teams_season_team1 = st.sidebar.selectbox("Season(First Team):",
                                                  ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021',
                                                   '2021-2022', '2022-2023', '2023-2024',"2024-2025", 'All'], index=9)
compare_teams_phase_team1 = st.sidebar.selectbox("Phase(First Team):",
                                                 ['Regular Season', 'Play In', 'Play offs', 'Final Four', 'All'],
                                                 index=4)
compare_teams_wl_team1 = st.sidebar.selectbox("Result(First Team):", ['W', 'L', 'All'], index=2)
compare_teams_round_team1 = st.sidebar.selectbox("Round(First Team):",
                                                 ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3',
                                                  'PO 4', 'PO 5', 'Semi Final', 'Third Place', 'Final', 'All'],
                                                 index=12)

st.sidebar.write("## ______________________________")
st.sidebar.write("## Select Second team filters")
compare_teams_team2 = st.sidebar.selectbox("Choose Second Team:",
                                           All_Seasons['Team'].reset_index().sort_values('Team')['Team'].unique(),index=1)
compare_teams_ha_team2 = st.sidebar.selectbox("Home or Away games(Second Team):", ['A', 'H', 'All'], index=2)
compare_teams_season_team2 = st.sidebar.selectbox("Season(Second Team):",
                                                  ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021',
                                                   '2021-2022', '2022-2023', '2023-2024',"2024-2025", 'All'], index=9)
compare_teams_phase_team2 = st.sidebar.selectbox("Phase(Second Team):",
                                                 ['Regular Season', 'Play In', 'Play offs', 'Final Four', 'All'],
                                                 index=4)
compare_teams_wl_team2 = st.sidebar.selectbox("Result(Second Team):", ['W', 'L', 'All'], index=2)
compare_teams_round_team2 = st.sidebar.selectbox("Round(Second Team):",
                                                 ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3',
                                                  'PO 4', 'PO 5', 'Semi Final', 'Third Place', 'Final', 'All'],
                                                 index=12)


def team_rating_stat_higher(dataset, stat):
    dataset1 = dataset[["Team", stat]].sort_values(stat).reset_index()
    dataset1.drop("index", axis=1, inplace=True)
    final_dataset = dataset1.reset_index() >> mutate(Rating=(100 * (X.index + 1) / X.Team.nunique()),
                                                     Rating1=(100 - (100 - X.Rating.round(0)) * 0.5).round(0))
    final_dataset.rename(columns={'Rating1': 'Rating ' + stat}, inplace=True)
    final_dataset.drop(["index", "Rating", stat], axis=1, inplace=True)
    return final_dataset


def team_rating_stat_lower(dataset, stat):
    dataset1 = dataset[["Team", stat]].sort_values(stat, ascending=False).reset_index()
    dataset1.drop("index", axis=1, inplace=True)
    final_dataset = dataset1.reset_index() >> mutate(Rating=(100 * (X.index + 1) / X.Team.nunique()),
                                                     Rating1=(100 - (100 - X.Rating.round(0)) * 0.5).round(0))
    final_dataset.rename(columns={'Rating1': 'Rating ' + stat}, inplace=True)
    final_dataset.drop(["index", "Rating", stat], axis=1, inplace=True)
    return final_dataset


def compute_team_stats(dataset_stats, dataset_periods, Team_select, ha, season, wl, phase, rounds):
    finalstats = dataset_stats.groupby(['idseason', 'Team'])[['PTS', 'F2M',
                                                              'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                                              'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF',
                                                              'PIR', 'Possesions']].sum().reset_index()
    finalstats['2P(%)'] = 100 * (finalstats['F2M'] / finalstats['F2A'])
    finalstats['3P(%)'] = 100 * (finalstats['F3M'] / finalstats['F3A'])
    finalstats['FT(%)'] = 100 * (finalstats['FTM'] / finalstats['FTA'])
    finalstats['Offensive Rating'] = 100 * (finalstats['PTS'] / finalstats['Possesions'])
    finalstats['EFG(%)'] = 100 * (finalstats['F2M'] + 1.5 * finalstats['F3M']) / (finalstats['F2A'] + finalstats['F3A'])
    finalstats['TS(%)'] = 100 * (finalstats['PTS']) / (
                2 * (finalstats['F2A'] + finalstats['F3A'] + 0.44 * finalstats['FTA']))
    finalstats['FT Ratio'] = finalstats['FTA'] / (finalstats['F3A'] + finalstats['F2A'])
    finalstats['AS-TO Ratio'] = finalstats['AS'] / finalstats['TO']
    finalstats['TO Ratio'] = 100 * (finalstats['TO'] / finalstats['Possesions'])
    finalstats['AS Ratio'] = 100 * (finalstats['AS'] / finalstats['Possesions'])
    finalstats = finalstats[
        ['idseason', 'Team', 'PTS', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'OR', 'DR',
         'TR',
         'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'Possesions', 'Offensive Rating', 'EFG(%)',
         'TS(%)', 'FT Ratio', 'AS-TO Ratio', 'TO Ratio', 'AS Ratio']].round(1)

    finalstats_opp = dataset_stats.groupby(['idseason', 'Against'])[['PTS', 'F2M',
                                                                     'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                                                     'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF',
                                                                     'RF',
                                                                     'PIR', 'Possesions']].sum().reset_index()

    finalstats_opp['2P(%)'] = 100 * (finalstats_opp['F2M'] / finalstats_opp['F2A'])
    finalstats_opp['3P(%)'] = 100 * (finalstats_opp['F3M'] / finalstats_opp['F3A'])
    finalstats_opp['FT(%)'] = 100 * (finalstats_opp['FTM'] / finalstats_opp['FTA'])
    finalstats_opp['Offensive Rating'] = 100 * (finalstats_opp['PTS'] / finalstats_opp['Possesions'])
    finalstats_opp['EFG(%)'] = 100 * (finalstats_opp['F2M'] + 1.5 * finalstats_opp['F3M']) / (
                finalstats_opp['F2A'] + finalstats_opp['F3A'])
    finalstats_opp['TS(%)'] = 100 * (finalstats_opp['PTS']) / (
                2 * (finalstats_opp['F2A'] + finalstats_opp['F3A'] + 0.44 * finalstats_opp['FTA']))
    finalstats_opp['FT Ratio'] = finalstats_opp['FTA'] / (finalstats_opp['F3A'] + finalstats_opp['F2A'])
    finalstats_opp['AS-TO Ratio'] = finalstats_opp['AS'] / finalstats_opp['TO']
    finalstats_opp['TO Ratio'] = 100 * (finalstats_opp['TO'] / finalstats_opp['Possesions'])
    finalstats_opp['AS Ratio'] = 100 * (finalstats_opp['AS'] / finalstats_opp['Possesions'])
    finalstats_opp = finalstats_opp[
        ['idseason', 'Against', 'PTS', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'OR', 'DR',
         'TR',
         'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'Possesions', 'Offensive Rating', 'EFG(%)',
         'TS(%)', 'FT Ratio', 'AS-TO Ratio', 'TO Ratio', 'AS Ratio']].round(1)
    finalstats_opp = finalstats_opp.add_prefix('opp ').rename(
        columns={'opp Against': 'Team', 'opp idseason': 'idseason'})

    gamesstats = pd.merge(finalstats, finalstats_opp)
    allstats_in_a_game = pd.merge(dataset_periods, gamesstats, on=['idseason', 'Team'])
    if "All" in ha:
        ha = ['A', 'H']
        allstats_in_a_game1 = allstats_in_a_game.loc[allstats_in_a_game['HA'].isin(ha)]

    else:
        allstats_in_a_game1 = allstats_in_a_game.loc[allstats_in_a_game['HA'] == ha]

    if "All" in season:
        season = ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022',
                  '2022-2023', '2023-2024',"2024-2025"]
        allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Season'].isin(season)]

    else:
        allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Season'] == season]

    if "All" in wl:
        wl = ['W', 'L']
        allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['results'].isin(wl)]

    else:
        allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['results'] == wl]

    if "All" in phase:
        phase = ['Regular Season', 'Play In', 'Play offs', 'Final Four']
        allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Phase'].isin(phase)]


    else:
        allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Phase'] == phase]

    if "All" in rounds:
        rounds = ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4',
                  'PO 5', 'Semi Final', 'Third Place', 'Final']
        allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Round'].isin(rounds)]


    else:
        allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Round'] == rounds]

    avgteamstats = allstats_in_a_game1.groupby('Team')[['Q1S',
                                                        'Q2S', 'Q1C', 'Q2C', 'FHS', 'FHC', 'Q3S', 'Q4S', 'Q3C', 'Q4C',
                                                        'SHS', 'SHC', 'EXS', 'EXC',
                                                        'PTS', 'opp PTS', 'AS', 'opp AS', 'F2M', 'F2A', 'opp F2M',
                                                        'opp F2A',
                                                        'F3M', 'F3A', 'opp F3M', 'opp F3A', 'FTM', 'FTA', 'opp FTM',
                                                        'opp FTA',
                                                        'OR', 'DR', 'TR', 'opp OR', 'opp DR', 'opp TR', 'ST', 'opp ST',
                                                        'TO', 'opp TO', 'BLK', 'BLKR', 'PF', 'RF',
                                                        'PIR', 'opp PIR', 'Possesions',
                                                        'opp Possesions']].mean().reset_index().round(2)

    avgteamstats['2P(%)'] = 100 * (avgteamstats['F2M'] / avgteamstats['F2A'])
    avgteamstats['3P(%)'] = 100 * (avgteamstats['F3M'] / avgteamstats['F3A'])
    avgteamstats['FT(%)'] = 100 * (avgteamstats['FTM'] / avgteamstats['FTA'])
    avgteamstats['opp 2P(%)'] = 100 * (avgteamstats['opp F2M'] / avgteamstats['opp F2A'])
    avgteamstats['opp 3P(%)'] = 100 * (avgteamstats['opp F3M'] / avgteamstats['opp F3A'])
    avgteamstats['opp FT(%)'] = 100 * (avgteamstats['opp FTM'] / avgteamstats['opp FTA'])
    avgteamstats['Offensive Rating'] = 100 * (avgteamstats['PTS'] / avgteamstats['Possesions'])
    avgteamstats['EFG(%)'] = 100 * (avgteamstats['F2M'] + 1.5 * avgteamstats['F3M']) / (
                avgteamstats['F2A'] + avgteamstats['F3A'])
    avgteamstats['TS(%)'] = 100 * (avgteamstats['PTS']) / (
            2 * (avgteamstats['F2A'] + avgteamstats['F3A'] + 0.44 * avgteamstats['FTA']))
    avgteamstats['FT Ratio'] = avgteamstats['FTA'] / (avgteamstats['F3A'] + avgteamstats['F2A'])
    avgteamstats['AS-TO Ratio'] = avgteamstats['AS'] / avgteamstats['TO']
    avgteamstats['TO Ratio'] = 100 * (avgteamstats['TO'] / avgteamstats['Possesions'])
    avgteamstats['AS Ratio'] = 100 * (avgteamstats['AS'] / avgteamstats['Possesions'])
    avgteamstats['Defensive Rating'] = 100 * (avgteamstats['opp PTS'] / avgteamstats['opp Possesions'])
    avgteamstats['opp EFG(%)'] = 100 * (avgteamstats['opp F2M'] + 1.5 * avgteamstats['opp F3M']) / (
            avgteamstats['opp F2A'] + avgteamstats['opp F3A'])
    avgteamstats['opp TS(%)'] = 100 * (avgteamstats['opp PTS']) / (
            2 * (avgteamstats['opp F2A'] + avgteamstats['opp F3A'] + 0.44 * avgteamstats['opp FTA']))
    avgteamstats['opp FT Ratio'] = avgteamstats['opp FTA'] / (avgteamstats['opp F3A'] + avgteamstats['opp F2A'])
    avgteamstats['opp AS-TO Ratio'] = avgteamstats['opp AS'] / avgteamstats['opp TO']
    avgteamstats['opp TO Ratio'] = 100 * (avgteamstats['opp TO'] / avgteamstats['opp Possesions'])
    avgteamstats['opp AS Ratio'] = 100 * (avgteamstats['opp AS'] / avgteamstats['opp Possesions'])
    colsplus = ['AS', 'F2M', 'F2A', 'F3M', 'F3A', 'FTM',
                'FTA', 'OR', 'DR', 'TR', 'BLK', 'RF', 'ST', '2P(%)', '3P(%)', 'FT(%)', 'EFG(%)', 'TS(%)', 'FT Ratio',
                'AS-TO Ratio',
                'AS Ratio', 'opp TO Ratio', 'Offensive Rating']

    colsminus = ['BLKR', 'PF', 'opp PTS', 'opp AS', 'opp F2M', 'opp F2A', 'opp 2P(%)', 'opp F3M', 'opp F3A',
                 'opp 3P(%)',
                 'opp FTM', 'opp FTA', 'opp FT(%)', 'opp OR', 'opp DR', 'opp TR', 'opp ST', 'Defensive Rating',
                 'opp EFG(%)', 'opp TS(%)',
                 'opp FT Ratio', 'opp AS-TO Ratio', 'opp AS Ratio', 'TO Ratio']

    teams_ratings1 = team_rating_stat_higher(avgteamstats, "PTS")
    for i in colsplus:
        df2 = team_rating_stat_higher(avgteamstats, i)
        teams_ratings1 = pd.merge(teams_ratings1, df2)

    teams_ratings2 = team_rating_stat_lower(avgteamstats, "TO")
    for i in colsminus:
        df3 = team_rating_stat_lower(avgteamstats, i)
        teams_ratings2 = pd.merge(teams_ratings2, df3)
    teams_ratings = pd.merge(teams_ratings1, teams_ratings2)

    all_avg_teamstats = pd.merge(avgteamstats, teams_ratings)
    all_avg_teamstats = all_avg_teamstats.loc[all_avg_teamstats.Team == Team_select]
    return all_avg_teamstats


teamstats1 = compute_team_stats(All_Seasons, period_points, compare_teams_team1, compare_teams_ha_team1,
                                compare_teams_season_team1, compare_teams_wl_team1, compare_teams_phase_team1,
                                compare_teams_round_team1)
teamstats2 = compute_team_stats(All_Seasons, period_points, compare_teams_team2, compare_teams_ha_team2,
                                compare_teams_season_team2, compare_teams_wl_team2, compare_teams_phase_team2,
                                compare_teams_round_team2)

if "All" in compare_teams_ha_team1:
    select_ha_player1 = ''
else:
    select_ha_player1 = compare_teams_ha_team1

if "All" in compare_teams_season_team1:
    select_season_player1 = ''
else:
    select_season_player1 = compare_teams_season_team1

if "All" in compare_teams_wl_team1:
    select_wl_player1 = ''
else:
    select_wl_player1 = compare_teams_wl_team1

if "All" in compare_teams_phase_team1:
    select_phase_player1 = ''
else:
    select_phase_player1 = compare_teams_phase_team1

if "All" in compare_teams_round_team1:
    select_round_player1 = ''
else:

    select_round_player1 = compare_teams_round_team1

if "All" in compare_teams_ha_team2:
    select_ha_player2 = ''
else:
    select_ha_player2 = compare_teams_ha_team2

if "All" in compare_teams_season_team2:
    select_season_player2 = ''
else:
    select_season_player2 = compare_teams_season_team2

if "All" in compare_teams_wl_team2:
    select_wl_player2 = ''
else:
    select_wl_player2 = compare_teams_wl_team2

if "All" in compare_teams_phase_team2:
    select_phase_player2 = ''
else:
    select_phase_player2 = compare_teams_phase_team2

if "All" in compare_teams_round_team2:
    select_round_player2 = ''
else:

    select_round_player2 = compare_teams_round_team2

t1, rat1 ,t2,rat2= st.columns([1, 1, 1,1])
try:

    with t1:




        st.write('### Team 1: '+ compare_teams_team1)
        st.write('Season: ' + select_season_player1)
        st.write('Phase: ' + select_phase_player1)
        st.write('Round: ' + select_round_player1)
        st.write('Home or away: ' + select_ha_player1)
        st.write('Result: ' + select_wl_player1)
    with rat1:
        offense_rating_data1 = teamstats1[
            ['Rating PTS', 'Rating AS', 'Rating TO', 'Rating OR', 'Rating BLKR', 'Rating RF', 'Rating F2M',
             'Rating F2A',
             'Rating 2P(%)', 'Rating F3M', 'Rating F3A', 'Rating 3P(%)', 'Rating FTM', 'Rating FTA', 'Rating FT(%)',
             'Rating FT Ratio',
             'Rating EFG(%)', 'Rating TS(%)', "Rating Offensive Rating", 'Rating AS-TO Ratio', "Rating AS Ratio",
             'Rating opp DR', 'Rating opp ST',
             'Rating TO Ratio', 'Rating opp TO Ratio']].melt()
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

        defense_ratings1 = teamstats1[
            ['Rating ST', 'Rating DR', 'Rating PF', 'Rating BLK', 'Rating opp PTS', 'Rating opp AS',
             'Rating opp F2M', 'Rating opp F2A', 'Rating opp 2P(%)', 'Rating opp F3M', 'Rating opp F3A',
             'Rating opp 3P(%)',
             'Rating opp FTM', 'Rating opp FTA', 'Rating opp FT(%)', 'Rating opp OR', 'Rating Defensive Rating',
             'Rating opp EFG(%)', 'Rating opp TS(%)',
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

        total_ratings1 = teamstats1.filter(regex='Rating').melt()['value'].mean()

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
                t=40,
                pad=0
            )
        )

        st.write(tot)


    with t2:

        st.write('### Team 2: '+ compare_teams_team2)
        st.write('Season: ' + select_season_player2)
        st.write('Phase: ' + select_phase_player2)
        st.write('Round: ' + select_round_player2)
        st.write('Home or away: ' + select_ha_player2)
        st.write('Result: ' + select_wl_player2)
    with rat2:

        offense_rating_data2 = teamstats2[
            ['Rating PTS', 'Rating AS', 'Rating TO', 'Rating OR', 'Rating BLKR', 'Rating RF', 'Rating F2M',
             'Rating F2A',
             'Rating 2P(%)', 'Rating F3M', 'Rating F3A', 'Rating 3P(%)', 'Rating FTM', 'Rating FTA', 'Rating FT(%)',
             'Rating FT Ratio',
             'Rating EFG(%)', 'Rating TS(%)', "Rating Offensive Rating", 'Rating AS-TO Ratio', "Rating AS Ratio",
             'Rating opp DR', 'Rating opp ST',
             'Rating TO Ratio', 'Rating opp TO Ratio']].melt()
        offense_ratings2 = offense_rating_data2['value'].mean()

        off2 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=offense_ratings2.round(0),
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 100]},
                   'bordercolor': "gray"},
            title={'text': "Offense"}))

        off2.update_layout(
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

        st.write(off2)

        defense_ratings2 = teamstats2[
            ['Rating ST', 'Rating DR', 'Rating PF', 'Rating BLK', 'Rating opp PTS', 'Rating opp AS',
             'Rating opp F2M', 'Rating opp F2A', 'Rating opp 2P(%)', 'Rating opp F3M', 'Rating opp F3A',
             'Rating opp 3P(%)',
             'Rating opp FTM', 'Rating opp FTA', 'Rating opp FT(%)', 'Rating opp OR', 'Rating Defensive Rating',
             'Rating opp EFG(%)', 'Rating opp TS(%)',
             'Rating opp FT Ratio', 'Rating opp AS-TO Ratio', 'Rating opp AS Ratio']].melt()['value'].mean()

        defe2 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=defense_ratings2.round(0),
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 100]},
                   'bordercolor': "gray"},
            title={'text': "Defense"}))

        defe2.update_layout(
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

        st.write(defe2)

        total_ratings2 = teamstats2.filter(regex='Rating').melt()['value'].mean()

        tot = go.Figure(go.Indicator(
            mode="gauge+number",
            value=total_ratings2.round(0),
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
                t=40,
                pad=0
            )
        )

        st.write(tot)

except:
    st.error("No data available with this parameters")


st.write("### Euroleague Stats")
try:
    periods, basic, shooting, advanced = st.tabs(
        ['Period Points', 'Basic Stats', 'Shooting Stats', 'Advanced Stats'])
    with periods:
        periodteam1 = (teamstats1[
                           ['Team','Q1S', 'Q1C', 'Q2S', 'Q2C', 'FHS', 'FHC', 'Q3S', 'Q3C', 'Q4S', 'Q4C', 'SHS', 'SHC',
                            'EXS', 'EXC']]
                       .rename(
            columns={'Q1S': 'Q1 Scored', 'Q2S': 'Q2 Scored', 'Q3S': 'Q3 Scored', 'Q4S': 'Q4 Scored',
                     'EXS': 'Extra time Scored', 'FHS': 'First Half Scored', 'SHS': 'Second Half Scored',
                     'Q1C': 'Q1 Conceed', 'Q2C': 'Q2 Conceed', 'Q3C': 'Q3 Conceed', 'Q4C': 'Q4 Conceed',
                     'EXC': 'Extra time Conceed', 'FHC': 'First Half Conceed', 'SHC': 'Second Half Conceed'
                     }))
        periodteam2 = (
            teamstats2[
                ['Team','Q1S', 'Q1C', 'Q2S', 'Q2C', 'FHS', 'FHC', 'Q3S', 'Q3C', 'Q4S', 'Q4C', 'SHS', 'SHC', 'EXS', 'EXC']]
            .rename(columns={'Q1S': 'Q1 Scored', 'Q2S': 'Q2 Scored', 'Q3S': 'Q3 Scored', 'Q4S': 'Q4 Scored',
                     'EXS': 'Extra time Scored', 'FHS': 'First Half Scored', 'SHS': 'Second Half Scored',
                     'Q1C': 'Q1 Conceed', 'Q2C': 'Q2 Conceed', 'Q3C': 'Q3 Conceed', 'Q4C': 'Q4 Conceed',
                     'EXC': 'Extra time Conceed', 'FHC': 'First Half Conceed', 'SHC': 'Second Half Conceed'
                             })
            )
        periodteam1[
            'Team'] = compare_teams_team1 + " " + select_season_player1 + " " + select_phase_player1 + " " + select_round_player1 + " " + select_ha_player1 + " " + select_wl_player1
        periodteam2[
            'Team'] = compare_teams_team2 + " " + select_season_player2 + " " + select_phase_player2 + " " + select_round_player2 + " " + select_ha_player2 + " " + select_wl_player2
        periodteams = pd.concat([periodteam1, periodteam2])
        interactive_table(periodteams.set_index('Team').round(1),
                          paging=False, height=900, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])


    with basic:

        basic_stats1 = teamstats1[
            ['Team','PTS', 'opp PTS', 'AS', 'opp AS', 'TO', 'opp TO', 'TR', 'DR', 'OR', 'opp TR', 'opp DR', 'opp OR',
             'BLK', 'BLKR', 'ST', 'opp ST', 'PF', 'RF', 'PIR', 'opp PIR']].rename(
            columns={'PTS': 'Points Scored',
                     'AS': 'Assists made',
                     'TO': 'Turnovers made',
                     'TR': 'TotalRebounds taken',
                     'OR': 'OffensiveRebounds taken',
                     'DR': 'DefensiveRebounds taken',
                     'opp PTS': 'Points Conceed',
                     'opp AS': 'opp Assists',
                     'opp TO': 'opp Turnovers',
                     'opp TR': 'Total Rebounds opp taken',
                     'opp OR': 'Offensive Rebounds opp taken',
                     'opp DR': 'Defensive Rebounds opp taken',
                     'BLK': 'Blocks',
                     'BLKR': 'Blocks Reversed',
                     'ST': 'Steals made',
                     'opp ST': 'opp Steals',
                     'PF': 'Personal Fouls',
                     'RF': 'Fouls Drawn',
                     'opp PIR': 'opp PIR'}).round(1)

        basic_stats2 = teamstats2[
            ['Team','PTS', 'opp PTS', 'AS', 'opp AS', 'TO', 'opp TO', 'TR', 'DR', 'OR', 'opp TR', 'opp DR', 'opp OR',
             'BLK', 'BLKR', 'ST', 'opp ST', 'PF', 'RF', 'PIR', 'opp PIR']].rename(
            columns={'PTS': 'Points Scored',
                     'AS': 'Assists made',
                     'TO': 'Turnovers made',
                     'TR': 'TotalRebounds taken',
                     'OR': 'OffensiveRebounds taken',
                     'DR': 'DefensiveRebounds taken',
                     'opp PTS': 'Points Conceed',
                     'opp AS': 'opp Assists',
                     'opp TO': 'opp Turnovers',
                     'opp TR': 'Total Rebounds opp taken',
                     'opp OR': 'Offensive Rebounds opp taken',
                     'opp DR': 'Defensive Rebounds opp taken',
                     'BLK': 'Blocks',
                     'BLKR': 'Blocks Reversed',
                     'ST': 'Steals made',
                     'opp ST': 'opp Steals',
                     'PF': 'Personal Fouls',
                     'RF': 'Fouls Drawn',
                     'opp PIR': 'opp PIR'}).round(1)
        basic_stats1[
            'Team'] = compare_teams_team1 + " " + select_season_player1 + " " + select_phase_player1 + " " + select_round_player1 + " " + select_ha_player1 + " " + select_wl_player1
        basic_stats2[
            'Team'] = compare_teams_team2 + " " + select_season_player2 + " " + select_phase_player2 + " " + select_round_player2 + " " + select_ha_player2 + " " + select_wl_player2

        basic_stats_data = pd.concat([basic_stats1, basic_stats2])
        interactive_table(basic_stats_data.set_index('Team').round(1),
                          paging=False, height=900, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with shooting:
        shooting_stats1 = teamstats1[
            ['Team','F2M', 'F2A', '2P(%)', 'opp F2M', 'opp F2A', 'opp 2P(%)', 'F3M', 'F3A', '3P(%)', 'opp F3M', 'opp F3A',
             'opp 3P(%)', 'FTM', 'FTA', 'FT(%)', 'opp FTM', 'opp FTA', 'opp FT(%)',
             'FT Ratio', 'opp FT Ratio', 'EFG(%)', 'opp EFG(%)', 'TS(%)', 'opp TS(%)']].rename(
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
                     'TS': 'TS(%)',
                     'opp F2M': 'opp 2P Made',
                     'opp F2A': 'opp 2P Attempt',
                     'opp 2P(%)': 'opp 2P(%)',
                     'opp F3M': 'opp 3P Made',
                     'opp F3A': 'opp 3P Attempt',
                     'opp 3P(%)': 'opp 3P(%)',
                     'opp FTM': 'opp FT Made',
                     'opp FTA': 'opp FT Attempt',
                     'opp FT(%)': 'opp FT(%)',
                     'opp FTR': 'opp FT Ratio',
                     'opp EFG(%)': 'opp EFG(%)',
                     'opp TS(%)': 'opp TS(%)',
                     'FT Ratio': 'FT Ratio',
                     'opp FT Ratio': 'opp FT Ratio'})

        shooting_stats2 = teamstats2[
            ['Team','F2M', 'F2A', '2P(%)', 'opp F2M', 'opp F2A', 'opp 2P(%)', 'F3M', 'F3A', '3P(%)', 'opp F3M', 'opp F3A',
             'opp 3P(%)', 'FTM', 'FTA', 'FT(%)', 'opp FTM', 'opp FTA', 'opp FT(%)',
             'FT Ratio', 'opp FT Ratio', 'EFG(%)', 'opp EFG(%)', 'TS(%)', 'opp TS(%)']].rename(
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
                     'TS': 'TS(%)',
                     'opp F2M': 'opp 2P Made',
                     'opp F2A': 'opp 2P Attempt',
                     'opp 2P(%)': 'opp 2P(%)',
                     'opp F3M': 'opp 3P Made',
                     'opp F3A': 'opp 3P Attempt',
                     'opp 3P(%)': 'opp 3P(%)',
                     'opp FTM': 'opp FT Made',
                     'opp FTA': 'opp FT Attempt',
                     'opp FT(%)': 'opp FT(%)',
                     'opp FTR': 'opp FT Ratio',
                     'opp EFG(%)': 'opp EFG(%)',
                     'opp TS(%)': 'opp TS(%)',
                     'FT Ratio': 'FT Ratio',
                     'opp FT Ratio': 'opp FT Ratio'})
        shooting_stats1[
            'Team'] = compare_teams_team1 + " " + select_season_player1 + " " + select_phase_player1 + " " + select_round_player1 + " " + select_ha_player1 + " " + select_wl_player1
        shooting_stats2[
            'Team'] = compare_teams_team2 + " " + select_season_player2 + " " + select_phase_player2 + " " + select_round_player2 + " " + select_ha_player2 + " " + select_wl_player2
        shooting_stats_data = pd.concat([shooting_stats1, shooting_stats2])

        interactive_table(shooting_stats_data.set_index('Team').round(1),
                      paging=False, height=900, width=2000, showIndex=True,
                      classes="display order-column nowrap table_with_monospace_font", searching=True,
                      fixedColumns=True, select=True, info=False, scrollCollapse=True,
                      scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                      columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with advanced:
        advanced_stats1 = (teamstats1[['Team','Possesions', 'opp Possesions', 'Offensive Rating', 'Defensive Rating',
                                       'AS-TO Ratio', 'opp AS-TO Ratio', 'TO Ratio', 'opp TO Ratio', 'AS Ratio',
                                       'opp AS Ratio']]
                         )

        advanced_stats2 = teamstats2[['Team','Possesions', 'opp Possesions', 'Offensive Rating', 'Defensive Rating',
                                      'AS-TO Ratio', 'opp AS-TO Ratio', 'TO Ratio', 'opp TO Ratio', 'AS Ratio',
                                      'opp AS Ratio']]
        advanced_stats1['Team'] = compare_teams_team1 + " " + select_season_player1 + " " + select_phase_player1 + " " + select_round_player1 + " " + select_ha_player1 + " " + select_wl_player1
        advanced_stats2['Team'] = compare_teams_team2 + " " + select_season_player2 + " " + select_phase_player2 + " " + select_round_player2 + " " + select_ha_player2 + " " + select_wl_player2
        advanced_stats_data = pd.concat([advanced_stats1, advanced_stats2])
        interactive_table(advanced_stats_data.set_index('Team').round(1),
                          paging=False, height=900, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])
except:
    st.error("No data available with this parameters")

try:
    st.write("### Between teams games stats")


    def teams_format(Team):
        if Team == compare_teams_team1:
            return "Team 1"
        elif Team == compare_teams_team2:
            return "Team 2"


    lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'


    def metrics_customize(red, green, blue, iconname, sline, i):

        htmlstr = f"""<p style='background-color: rgb({red},{green},{blue}, 0.75); 
                            color: rgb(0,0,0, 0.75); 
                            font-size: 25px; 
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:25px;'>
                            <i class='{iconname} fa-xs'></i> {i}
                            </style><BR><span style='font-size: 22px; 
                            margin-top: 0;'>{sline}</style></span></p>"""
        return htmlstr


    filters1, filters2 = st.columns(2)
    with filters1:
        team1=compare_teams_team1+" "+select_season_player1+" "+select_phase_player1+" "+select_round_player1+" "+select_ha_player1+" "+select_wl_player1
        team2 = compare_teams_team2 + " " + select_season_player2 + " " + select_phase_player2 + " " + select_round_player2 + " " + select_ha_player2 + " " + select_wl_player2
        between_teams_ha_team = st.selectbox("Home team:", [team1, team2, 'All'], index=2)
        between_teams_season_team = st.selectbox("Season:",
                                                 ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021',
                                                  '2021-2022', '2022-2023', '2023-2024','2024-2025', 'All'], index=8)
    with filters2:
        between_teams_phase_team = st.selectbox("Phase:",
                                                ['Regular Season', 'Play In', 'Play offs', 'Final Four', 'All'],
                                                index=4)
        between_teams_round_team = st.selectbox("Round:",
                                                ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3',
                                                 'PO 4', 'PO 5', 'Semi Final', 'Third Place', 'Final', 'All'], index=12)

    teams = [compare_teams_team1, compare_teams_team2]
    between_stats = All_Seasons.loc[(All_Seasons.Team.isin(teams)) & (All_Seasons.Against.isin(teams))]
    between_stats['Team_select'] = between_stats['Team'].apply(teams_format)
    between_periods = period_points.loc[(period_points.Team.isin(teams)) & (period_points.Against.isin(teams))]
    between_periods['Team_select'] = between_periods['Team'].apply(teams_format)
    if "All" in between_teams_ha_team:
        between_stats1 = between_stats
        between_periods1 = between_periods
    elif compare_teams_team1 in between_teams_ha_team:
        between_stats1 = between_stats.loc[((between_stats.HA == "H") & (between_stats.Team == compare_teams_team1)) | (
                    (between_stats.HA == "A") & (between_stats.Team == compare_teams_team2))]
        between_periods1 = between_periods.loc[
            ((between_periods.HA == "H") & (between_periods.Team == compare_teams_team1)) | (
                        (between_periods.HA == "A") & (between_periods.Team == compare_teams_team2))]
    elif compare_teams_team2 in between_teams_ha_team:
        between_stats1 = between_stats.loc[((between_stats.HA == "H") & (between_stats.Team == compare_teams_team2)) | (
                    (between_stats.HA == "A") & (between_stats.Team == compare_teams_team1))]
        between_periods1 = between_periods.loc[
            ((between_periods.HA == "H") & (between_periods.Team == compare_teams_team2)) | (
                        (between_periods.HA == "A") & (between_periods.Team == compare_teams_team1))]

    if "All" in between_teams_season_team:
        between_teams_season_team1 = ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022',
                                      '2022-2023', '2023-2024','2024-2025']
        between_stats1 = between_stats1.loc[between_stats1['Season'].isin(between_teams_season_team1)]
        between_periods1 = between_periods1.loc[between_periods1['Season'].isin(between_teams_season_team1)]
    else:
        between_stats1 = between_stats1.loc[between_stats1['Season'] == between_teams_season_team]
        between_periods1 = between_periods1.loc[between_periods1['Season'] == between_teams_season_team]

    if "All" in between_teams_phase_team:
        between_teams_phase_team1 = ['Regular Season', 'Play In', 'Play offs', 'Final Four']
        between_stats1 = between_stats1.loc[between_stats1['Phase'].isin(between_teams_phase_team1)]
        between_periods1 = between_periods1.loc[between_periods1['Phase'].isin(between_teams_phase_team1)]
    else:
        between_stats1 = between_stats1.loc[between_stats1['Phase'] == between_teams_phase_team]
        between_periods1 = between_periods1.loc[between_periods1['Phase'] == between_teams_phase_team]

    if "All" in between_teams_round_team:
        between_teams_round_team1 = ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4',
                                     'PO 5', 'Semi Final', 'Third Place', 'Final']
        between_stats1 = between_stats1.loc[between_stats1['Round'].isin(between_teams_round_team1)]
        between_periods1 = between_periods1.loc[between_periods1['Round'].isin(between_teams_round_team1)]

    else:
        between_stats1 = between_stats1.loc[between_stats1['Round'] == between_teams_round_team]
        between_periods1 = between_periods1.loc[between_periods1['Round'].isin(between_teams_round_team)]

    wins = (between_stats1[['idseason', 'Team_select', 'results']]
            .value_counts().reset_index()[['idseason', 'Team_select', 'results']]
            .value_counts().reset_index().groupby(["Team_select", 'results'])['count']
            .sum().reset_index())

    try:
        winsteam1 = wins.loc[(wins.results == "W") & (wins.Team_select == 'Team 1')]['count'].unique()[0]
    except:
        winsteam1 = 0
    try:
        winsteam2 = wins.loc[(wins.results == "W") & (wins.Team_select == 'Team 2')]['count'].unique()[0]
    except:
        winsteam2 = 0
    kpi1, kpi2, kpi3 = st.columns(3)
    with kpi1:
        st.markdown(lnk + metrics_customize(204, 153, 0, "", between_stats1['idseason'].nunique(), "Total Games"),
                    unsafe_allow_html=True)
    with kpi2:
        st.markdown(lnk + metrics_customize(204, 153, 0, "", winsteam1, compare_teams_team1 + " Wins"),
                    unsafe_allow_html=True)
    with kpi3:
        st.markdown(lnk + metrics_customize(204, 153, 0, "", winsteam2, compare_teams_team2 + " Wins"),
                    unsafe_allow_html=True)

    finalstats = between_stats1.groupby(['idseason', 'Team'])[['PTS', 'F2M',
                                                               'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                                               'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF',
                                                               'PIR', 'Possesions']].sum().reset_index().groupby(
        'Team')[['PTS', 'F2M',
                 'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                 'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF',
                 'PIR', 'Possesions']].mean().reset_index()

    finalstats['2P(%)'] = 100 * (finalstats['F2M'] / finalstats['F2A'])
    finalstats['3P(%)'] = 100 * (finalstats['F3M'] / finalstats['F3A'])
    finalstats['FT(%)'] = 100 * (finalstats['FTM'] / finalstats['FTA'])
    finalstats['Offensive Rating'] = 100 * (finalstats['PTS'] / finalstats['Possesions'])
    finalstats['EFG(%)'] = 100 * (finalstats['F2M'] + 1.5 * finalstats['F3M']) / (finalstats['F2A'] + finalstats['F3A'])
    finalstats['TS(%)'] = 100 * (finalstats['PTS']) / (
                2 * (finalstats['F2A'] + finalstats['F3A'] + 0.44 * finalstats['FTA']))
    finalstats['FT Ratio'] = finalstats['FTA'] / (finalstats['F3A'] + finalstats['F2A'])
    finalstats['AS-TO Ratio'] = finalstats['AS'] / finalstats['TO']
    finalstats['TO Ratio'] = 100 * (finalstats['TO'] / finalstats['Possesions'])
    finalstats['AS Ratio'] = 100 * (finalstats['AS'] / finalstats['Possesions'])
    finalstats = finalstats[
        ['Team', 'PTS', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'OR', 'DR', 'TR',
         'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'Possesions', 'Offensive Rating', 'EFG(%)',
         'TS(%)', 'FT Ratio', 'AS-TO Ratio', 'TO Ratio', 'AS Ratio']].round(1)

    finalperiods = between_periods1.groupby('Team')[
        ['Q1S', 'Q2S', 'Q1C', 'Q2C', 'FHS', 'FHC', 'Q3S', 'Q4S', 'Q3C', 'Q4C', 'SHS', 'SHC', 'EXS',
         'EXC']].mean().reset_index().round(2)
    final = pd.merge(finalperiods, finalstats)

    periodsbet, basicbet, shootbet, advbet = st.tabs(['Period Points','Basic Stats','Shooting Stats','Advanced Stats'])

    with periodsbet:
        periodbetdata1 = final.loc[final.Team == compare_teams_team1][['Team','Q1S', 'Q2S', 'FHS',
                                                                       'Q3S', 'Q4S',
                                                                       'SHS', 'EXS', ]].rename(
            columns={'Q1S': 'Q1 Scored', 'Q2S': 'Q2 Scored', 'Q3S': 'Q3 Scored', 'Q4S': 'Q4 Scored',
                     'EXS': 'Extra time Scored', 'FHS': 'First Half Scored',
                     'SHS': 'Second Half Scored'})

        periodbetdata2 = final.loc[final.Team == compare_teams_team2][
            ['Team','Q1S', 'Q2S', 'FHS',
             'Q3S', 'Q4S',
             'SHS', 'EXS', ]].rename(
            columns={'Q1S': 'Q1 Scored', 'Q2S': 'Q2 Scored', 'Q3S': 'Q3 Scored', 'Q4S': 'Q4 Scored',
                     'EXS': 'Extra time Scored', 'FHS': 'First Half Scored',
                     'SHS': 'Second Half Scored'})
        periodbetdata = pd.concat([periodbetdata1, periodbetdata2])

        interactive_table(periodbetdata.set_index('Team').round(1),
                          paging=False, height=900, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])

    with basicbet:
        basicbetdata1 = final.loc[final.Team == compare_teams_team1][
            ['Team','PTS', 'AS', 'TO', 'TR', 'DR', 'OR', 'BLK', 'ST', 'PF', 'PIR']].rename(
            columns={'PTS': 'Points Scored',
                     'AS': 'Assists made',
                     'TO': 'Turnovers made',
                     'TR': 'TotalRebounds taken',
                     'OR': 'OffensiveRebounds taken',
                     'DR': 'DefensiveRebounds taken',
                     'BLK': 'Blocks',
                     'ST': 'Steals made',
                     'PF': 'Personal Fouls'})

        basicbetdata2 = final.loc[final.Team == compare_teams_team2][
            ['Team','PTS', 'AS', 'TO', 'TR', 'DR', 'OR', 'BLK', 'ST', 'PF', 'PIR']].rename(
            columns={'PTS': 'Points Scored',
                     'AS': 'Assists made',
                     'TO': 'Turnovers made',
                     'TR': 'TotalRebounds taken',
                     'OR': 'OffensiveRebounds taken',
                     'DR': 'DefensiveRebounds taken',
                     'BLK': 'Blocks',
                     'ST': 'Steals made',
                     'PF': 'Personal Fouls'})
        basicbetdata = pd.concat([basicbetdata1, basicbetdata2])
        interactive_table(basicbetdata.set_index('Team').round(1),
                          paging=False, height=900, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])


    with shootbet:
        shootbetdata1 = final.loc[final.Team == compare_teams_team1][
            ['Team','F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'FT Ratio', 'EFG(%)',
             'TS(%)']].rename(
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

        shootbetdata2 = final.loc[final.Team == compare_teams_team2][
            ['Team','F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'FT Ratio', 'EFG(%)',
             'TS(%)']].rename(
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
        shootbetdata = pd.concat([shootbetdata1, shootbetdata2])
        interactive_table(shootbetdata.set_index('Team').round(1),
                          paging=False, height=900, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])


    with advbet:
        advbetdata1 = final.loc[final.Team == compare_teams_team1][['Team','Possesions', 'Offensive Rating',
                                                                    'AS-TO Ratio', 'TO Ratio', 'AS Ratio']].round(
            1)

        advbetdata2 = final.loc[final.Team == compare_teams_team2][['Team','Possesions', 'Offensive Rating',
                                                                    'AS-TO Ratio', 'TO Ratio', 'AS Ratio']].round(
            1)
        advbetdata = pd.concat([advbetdata1, advbetdata2])
        interactive_table(advbetdata.set_index('Team').round(1),
                          paging=False, height=900, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])


except:
    st.error("No data available with this parameters")
