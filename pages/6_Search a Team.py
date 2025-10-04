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



st.set_page_config(layout='wide', page_title="Search a Team", page_icon="🏀")
st.sidebar.write("If an error message appears, please refresh the page")


def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)


download_image('https://raw.githubusercontent.com/sotiristiga/Euroleague_dash/refs/heads/main/eurologo.png',
               'eurologo.png')
st.image(Image.open("eurologo.png"), width=100)


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


euroleague_2016_2017_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2016_2017_playerstats.csv")
euroleague_2016_2017_playerstats['idseason'] = euroleague_2016_2017_playerstats['IDGAME'] + "_" + \
                                               euroleague_2016_2017_playerstats['Season']
euroleague_2016_2017_playerstats[['Fixture', 'Game']] = euroleague_2016_2017_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2016_2017_playerstats['Fixture'] = pd.to_numeric(euroleague_2016_2017_playerstats['Fixture'])
euroleague_2016_2017_playerstats['Round'] = euroleague_2016_2017_playerstats['Fixture'].apply(fixture_format1)

euroleague_2017_2018_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2017_2018_playerstats.csv")
euroleague_2017_2018_playerstats['idseason'] = euroleague_2017_2018_playerstats['IDGAME'] + "_" + \
                                               euroleague_2017_2018_playerstats['Season']
euroleague_2017_2018_playerstats[['Fixture', 'Game']] = euroleague_2017_2018_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2017_2018_playerstats['Fixture'] = pd.to_numeric(euroleague_2017_2018_playerstats['Fixture'])
euroleague_2017_2018_playerstats['Round'] = euroleague_2017_2018_playerstats['Fixture'].apply(fixture_format2)

euroleague_2018_2019_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2018_2019_playerstats.csv")
euroleague_2018_2019_playerstats['idseason'] = euroleague_2018_2019_playerstats['IDGAME'] + "_" + \
                                               euroleague_2018_2019_playerstats['Season']
euroleague_2018_2019_playerstats[['Fixture', 'Game']] = euroleague_2018_2019_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2018_2019_playerstats['Fixture'] = pd.to_numeric(euroleague_2018_2019_playerstats['Fixture'])
euroleague_2018_2019_playerstats['Round'] = euroleague_2018_2019_playerstats['Fixture'].apply(fixture_format1)

euroleague_2019_2020_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2019_2020_playerstats.csv")
euroleague_2019_2020_playerstats['idseason'] = euroleague_2019_2020_playerstats['IDGAME'] + "_" + \
                                               euroleague_2019_2020_playerstats['Season']
euroleague_2019_2020_playerstats[['Fixture', 'Game']] = euroleague_2019_2020_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2019_2020_playerstats['Fixture'] = pd.to_numeric(euroleague_2019_2020_playerstats['Fixture'])
euroleague_2019_2020_playerstats['Round'] = euroleague_2019_2020_playerstats['Fixture'].apply(fixture_format3)

euroleague_2020_2021_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2020_2021_playerstats.csv")
euroleague_2020_2021_playerstats['idseason'] = euroleague_2020_2021_playerstats['IDGAME'] + "_" + \
                                               euroleague_2020_2021_playerstats['Season']
euroleague_2020_2021_playerstats[['Fixture', 'Game']] = euroleague_2020_2021_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2020_2021_playerstats['Fixture'] = pd.to_numeric(euroleague_2020_2021_playerstats['Fixture'])
euroleague_2020_2021_playerstats['Round'] = euroleague_2020_2021_playerstats['Fixture'].apply(fixture_format4)

euroleague_2021_2022_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2021_2022_playerstats.csv")
euroleague_2021_2022_playerstats['idseason'] = euroleague_2021_2022_playerstats['IDGAME'] + "_" + \
                                               euroleague_2021_2022_playerstats['Season']
euroleague_2021_2022_playerstats[['Fixture', 'Game']] = euroleague_2021_2022_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2021_2022_playerstats['Fixture'] = pd.to_numeric(euroleague_2021_2022_playerstats['Fixture'])
euroleague_2021_2022_playerstats['Round'] = euroleague_2021_2022_playerstats['Fixture'].apply(fixture_format4)

euroleague_2022_2023_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2022_2023_playerstats.csv")
euroleague_2022_2023_playerstats['idseason'] = euroleague_2022_2023_playerstats['IDGAME'] + "_" + \
                                               euroleague_2022_2023_playerstats['Season']
euroleague_2022_2023_playerstats[['Fixture', 'Game']] = euroleague_2022_2023_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2022_2023_playerstats['Fixture'] = pd.to_numeric(euroleague_2022_2023_playerstats['Fixture'])
euroleague_2022_2023_playerstats['Round'] = euroleague_2022_2023_playerstats['Fixture'].apply(fixture_format4)

euroleague_2023_2024_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2023_2024_playerstats.csv")
euroleague_2023_2024_playerstats['idseason'] = euroleague_2023_2024_playerstats['IDGAME'] + "_" + \
                                               euroleague_2023_2024_playerstats['Season']
euroleague_2023_2024_playerstats[['Fixture', 'Game']] = euroleague_2023_2024_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2023_2024_playerstats['Fixture'] = pd.to_numeric(euroleague_2023_2024_playerstats['Fixture'])
euroleague_2023_2024_playerstats['Round'] = euroleague_2023_2024_playerstats['Fixture'].apply(fixture_format5)

euroleague_2024_2025_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2024_2025_playerstats.csv")
euroleague_2024_2025_playerstats['idseason'] = euroleague_2024_2025_playerstats['IDGAME'] + "_" + \
                                               euroleague_2024_2025_playerstats['Season']
euroleague_2024_2025_playerstats[['Fixture', 'Game']] = euroleague_2024_2025_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2024_2025_playerstats['Fixture'] = pd.to_numeric(euroleague_2024_2025_playerstats['Fixture'])
euroleague_2024_2025_playerstats['Round'] = euroleague_2024_2025_playerstats['Fixture'].apply(fixture_format5)

euroleague_2016_2017_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2016_2017_results.csv")
euroleague_2016_2017_results['idseason'] = euroleague_2016_2017_results['IDGAME'] + "_" + euroleague_2016_2017_results[
    'Season']
euroleague_2016_2017_results[['Fixture', 'Game']] = euroleague_2016_2017_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2016_2017_results['Fixture'] = pd.to_numeric(euroleague_2016_2017_results['Fixture'])
euroleague_2016_2017_results['Round'] = euroleague_2016_2017_results['Fixture'].apply(fixture_format1)

euroleague_2017_2018_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2017_2018_results.csv")
euroleague_2017_2018_results['idseason'] = euroleague_2017_2018_results['IDGAME'] + "_" + euroleague_2017_2018_results[
    'Season']
euroleague_2017_2018_results[['Fixture', 'Game']] = euroleague_2017_2018_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2017_2018_results['Fixture'] = pd.to_numeric(euroleague_2017_2018_results['Fixture'])
euroleague_2017_2018_results['Round'] = euroleague_2017_2018_results['Fixture'].apply(fixture_format2)

euroleague_2018_2019_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2018_2019_results.csv")
euroleague_2018_2019_results['idseason'] = euroleague_2018_2019_results['IDGAME'] + "_" + euroleague_2018_2019_results[
    'Season']
euroleague_2018_2019_results[['Fixture', 'Game']] = euroleague_2018_2019_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2018_2019_results['Fixture'] = pd.to_numeric(euroleague_2018_2019_results['Fixture'])
euroleague_2018_2019_results['Round'] = euroleague_2018_2019_results['Fixture'].apply(fixture_format1)

euroleague_2019_2020_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2019_2020_results.csv")
euroleague_2019_2020_results['idseason'] = euroleague_2019_2020_results['IDGAME'] + "_" + euroleague_2019_2020_results[
    'Season']
euroleague_2019_2020_results[['Fixture', 'Game']] = euroleague_2019_2020_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2019_2020_results['Fixture'] = pd.to_numeric(euroleague_2019_2020_results['Fixture'])
euroleague_2019_2020_results['Round'] = euroleague_2019_2020_results['Fixture'].apply(fixture_format3)

euroleague_2020_2021_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2020_2021_results.csv")
euroleague_2020_2021_results['idseason'] = euroleague_2020_2021_results['IDGAME'] + "_" + euroleague_2020_2021_results[
    'Season']
euroleague_2020_2021_results[['Fixture', 'Game']] = euroleague_2020_2021_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2020_2021_results['Fixture'] = pd.to_numeric(euroleague_2020_2021_results['Fixture'])
euroleague_2020_2021_results['Round'] = euroleague_2020_2021_results['Fixture'].apply(fixture_format4)

euroleague_2021_2022_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2021_2022_results.csv")
euroleague_2021_2022_results['idseason'] = euroleague_2021_2022_results['IDGAME'] + "_" + euroleague_2021_2022_results[
    'Season']
euroleague_2021_2022_results[['Fixture', 'Game']] = euroleague_2021_2022_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2021_2022_results['Fixture'] = pd.to_numeric(euroleague_2021_2022_results['Fixture'])
euroleague_2021_2022_results['Round'] = euroleague_2021_2022_results['Fixture'].apply(fixture_format4)

euroleague_2022_2023_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2022_2023_results.csv")
euroleague_2022_2023_results['idseason'] = euroleague_2022_2023_results['IDGAME'] + "_" + euroleague_2022_2023_results[
    'Season']
euroleague_2022_2023_results[['Fixture', 'Game']] = euroleague_2022_2023_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2022_2023_results['Fixture'] = pd.to_numeric(euroleague_2022_2023_results['Fixture'])
euroleague_2022_2023_results['Round'] = euroleague_2022_2023_results['Fixture'].apply(fixture_format4)

euroleague_2023_2024_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2023_2024_results.csv")
euroleague_2023_2024_results['idseason'] = euroleague_2023_2024_results['IDGAME'] + "_" + euroleague_2023_2024_results[
    'Season']
euroleague_2023_2024_results[['Fixture', 'Game']] = euroleague_2023_2024_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2023_2024_results['Fixture'] = pd.to_numeric(euroleague_2023_2024_results['Fixture'])
euroleague_2023_2024_results['Round'] = euroleague_2023_2024_results['Fixture'].apply(fixture_format5)

euroleague_2024_2025_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2024_2025_results.csv")
euroleague_2024_2025_results['idseason'] = euroleague_2024_2025_results['IDGAME'] + "_" + euroleague_2024_2025_results[
    'Season']
euroleague_2024_2025_results[['Fixture', 'Game']] = euroleague_2024_2025_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2024_2025_results['Fixture'] = pd.to_numeric(euroleague_2024_2025_results['Fixture'])
euroleague_2024_2025_results['Round'] = euroleague_2024_2025_results['Fixture'].apply(fixture_format5)

euroleague_2025_2026_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2025_2026_playerstats.csv")
euroleague_2025_2026_playerstats['idseason']=euroleague_2025_2026_playerstats['IDGAME'] + "_" + euroleague_2025_2026_playerstats['Season']
euroleague_2025_2026_playerstats[['Fixture', 'Game']] = euroleague_2025_2026_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2025_2026_playerstats['Fixture']=pd.to_numeric(euroleague_2025_2026_playerstats['Fixture'])
euroleague_2025_2026_playerstats['Round']=euroleague_2025_2026_playerstats['Fixture'].apply(fixture_format5)

euroleague_2025_2026_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2025_2026_results.csv")
euroleague_2025_2026_results['idseason']=euroleague_2025_2026_results['IDGAME'] + "_" + euroleague_2025_2026_results['Season']
euroleague_2025_2026_results[['Fixture', 'Game']] = euroleague_2025_2026_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2025_2026_results['Fixture']=pd.to_numeric(euroleague_2025_2026_results['Fixture'])
euroleague_2025_2026_results['Round']=euroleague_2025_2026_results['Fixture'].apply(fixture_format5)


All_Seasons=pd.concat([euroleague_2016_2017_playerstats,euroleague_2017_2018_playerstats,euroleague_2018_2019_playerstats,euroleague_2019_2020_playerstats,euroleague_2020_2021_playerstats,euroleague_2021_2022_playerstats,euroleague_2022_2023_playerstats,euroleague_2023_2024_playerstats,euroleague_2024_2025_playerstats,euroleague_2025_2026_playerstats])

All_Seasons_results=pd.concat([euroleague_2016_2017_results,euroleague_2017_2018_results,euroleague_2018_2019_results,euroleague_2019_2020_results,euroleague_2020_2021_results,euroleague_2021_2022_results,euroleague_2022_2023_results,euroleague_2023_2024_results,euroleague_2024_2025_results,euroleague_2025_2026_results])



Positions = pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/PlayersPositions.csv")




def result_format(Win):
    if Win == 1:
        return "W"
    elif Win == 0:
        return "L"


def ha_against_format(HA):
    if HA == "A":
        return "H"
    elif HA == "H":
        return "A"


def result_against_format(results):
    if results == "W":
        return "L"
    elif results == "L":
        return "W"


def wins_against_format(results):
    if results == "W":
        return 1
    elif results == "L":
        return 0


All_Seasons["HA1"] = All_Seasons['HA'].apply(ha_against_format)
All_Seasons["Result1"] = All_Seasons['results'].apply(result_against_format)
All_Seasons["Win"] = All_Seasons['results'].apply(wins_against_format)

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
period_points["Total_Q1"] = period_points["Q1S"] + period_points["Q1C"]
period_points["Total_Q2"] = period_points["Q2S"] + period_points["Q2C"]
period_points["FHS"] = period_points["Q1S"] + period_points["Q2S"]
period_points["FHC"] = period_points["Q1C"] + period_points["Q2C"]
period_points["Total_Q3"] = period_points["Q3S"] + period_points["Q3C"]
period_points["Total_Q4"] = period_points["Q4S"] + period_points["Q4C"]
period_points["SHS"] = period_points["Q3S"] + period_points["Q4S"]
period_points["SHC"] = period_points["Q3C"] + period_points["Q4C"]
period_points["results"] = period_points["Win"].apply(result_format)
period_points['EXS'].replace(0, np.nan, inplace=True)
period_points['EXC'].replace(0, np.nan, inplace=True)

st.sidebar.markdown('''
  * ## [Filters](#filters)
  * ## [Euroleague Stats](#euroleague-stats)
  * ## [Player Stats](#player-stats)
  * ## [Opponent Players Stats](#opponent-players-stats)
  * ## [Stats by game](#stats-by-game)

''', unsafe_allow_html=True)

st.header("Filters")
f1, f2, f3, f4, f5, f6 = st.columns(6)
with f1:
    search_team_team1 = st.selectbox("Choose  Team:",
                                     All_Seasons['Team'].reset_index().sort_values('Team')['Team'].unique())
with f2:
    search_team_season_team1 = st.selectbox("Season:", ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021',
                                                        '2021-2022', '2022-2023', '2023-2024', '2024-2025','2025-2026', 'All'],
                                            index=8)
with f3:
    search_team_phase_team1 = st.selectbox("Phase:", ['Regular Season', 'Play In', 'Play offs', 'Final Four', 'All'],
                                           index=4)
with f4:
    search_team_round_team1 = st.selectbox("Round:",
                                           ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3',
                                            'PO 4', 'PO 5', 'Semi Final', 'Third Place', 'Final', 'All'], index=12)
with f5:
    search_team_ha_team1 = st.selectbox("Home or Away games:", ['A', 'H', 'All'], index=2)
with f6:
    search_team_wl_team1 = st.selectbox("Result:", ['W', 'L', 'All'], index=2)

finalstats = All_Seasons.groupby(['idseason', 'Team'])[['PTS', 'F2M',
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
    ['idseason', 'Team', 'PTS', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'OR', 'DR', 'TR',
     'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'Possesions', 'Offensive Rating', 'EFG(%)',
     'TS(%)', 'FT Ratio', 'AS-TO Ratio', 'TO Ratio', 'AS Ratio']].round(1)

finalstats_opp = All_Seasons.groupby(['idseason', 'Against'])[['PTS', 'F2M',
                                                               'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                                               'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF',
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
finalstats_opp = finalstats_opp.add_prefix('opp ').rename(columns={'opp Against': 'Team', 'opp idseason': 'idseason'})

gamesstats = pd.merge(finalstats, finalstats_opp)
allstats_in_a_game = pd.merge(period_points, gamesstats, on=['idseason', 'Team'])

select_allstats_in_a_game = (
    allstats_in_a_game[['Team', 'Against', 'Season', 'Phase', 'Round', 'Fixture', "HA", 'results', 'Q1S',
                        'Q2S', 'Q1C', 'Q2C', 'FHS', 'FHC', 'Q3S', 'Q4S', 'Q3C', 'Q4C', 'SHS', 'SHC', 'EXS', 'EXC',
                        'PTS', 'opp PTS', 'AS', 'opp AS', 'F2M', 'F2A', '2P(%)', 'opp F2M', 'opp F2A', 'opp 2P(%)',
                        'F3M', 'F3A', '3P(%)', 'opp F3M', 'opp F3A', 'opp 3P(%)', 'FTM', 'FTA', 'FT(%)', 'opp FTM',
                        'opp FTA', 'opp FT(%)',
                        'OR', 'DR', 'TR', 'opp OR', 'opp DR', 'opp TR', 'ST', 'opp ST', 'TO', 'opp TO', 'BLK', 'BLKR',
                        'PF', 'RF',
                        'PIR', 'opp PIR', 'Possesions', 'opp Possesions', 'Offensive Rating', 'opp Offensive Rating',
                        'EFG(%)', 'opp EFG(%)', 'TS(%)', 'opp TS(%)', 'FT Ratio', 'opp FT Ratio', 'AS-TO Ratio',
                        'opp AS-TO Ratio',
                        'TO Ratio', 'opp TO Ratio', 'AS Ratio', 'opp AS Ratio']]
    .rename(columns={'ST': 'STL', 'opp ST': 'opp STL', 'F2M': '2PM', 'F2A': '2PA',
                     'opp F2M': 'opp 2PM', 'opp F2A': 'opp 2PA', 'F3M': '3PM', 'F3A': '3PA', 'opp F3M': 'opp 3PM',
                     'opp F3A': 'opp 3PA', 'RF': 'opp PF'}))

select_allstats_in_a_game['Total PTS'] = select_allstats_in_a_game['PTS'] + select_allstats_in_a_game['opp PTS']
select_allstats_in_a_game['Total AS'] = select_allstats_in_a_game['AS'] + select_allstats_in_a_game['opp AS']
select_allstats_in_a_game['Total 2PM'] = select_allstats_in_a_game['2PM'] + select_allstats_in_a_game['opp 2PM']
select_allstats_in_a_game['Total 2PA'] = select_allstats_in_a_game['2PA'] + select_allstats_in_a_game['opp 2PA']
select_allstats_in_a_game['Total 3PM'] = select_allstats_in_a_game['3PM'] + select_allstats_in_a_game['opp 3PM']
select_allstats_in_a_game['Total 3PA'] = select_allstats_in_a_game['3PA'] + select_allstats_in_a_game['opp 3PA']
select_allstats_in_a_game['Total FTM'] = select_allstats_in_a_game['FTM'] + select_allstats_in_a_game['opp FTM']
select_allstats_in_a_game['Total FTA'] = select_allstats_in_a_game['FTA'] + select_allstats_in_a_game['opp FTA']
select_allstats_in_a_game['Total OR'] = select_allstats_in_a_game['OR'] + select_allstats_in_a_game['opp OR']
select_allstats_in_a_game['Total DR'] = select_allstats_in_a_game['DR'] + select_allstats_in_a_game['opp DR']
select_allstats_in_a_game['Total TR'] = select_allstats_in_a_game['TR'] + select_allstats_in_a_game['opp TR']
select_allstats_in_a_game['Total STL'] = select_allstats_in_a_game['STL'] + select_allstats_in_a_game['opp STL']
select_allstats_in_a_game['Total PF'] = select_allstats_in_a_game['PF'] + select_allstats_in_a_game['opp PF']
select_allstats_in_a_game['Total BLK'] = select_allstats_in_a_game['BLKR'] + select_allstats_in_a_game['BLK']

if "All" in search_team_season_team1:
    search_team_season_team1 = ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022',
                                '2022-2023', '2023-2024', '2024-2025','2025-2026']
    All_Seasons1 = All_Seasons.loc[All_Seasons['Season'].isin(search_team_season_team1)]
    period_points1 = period_points.loc[period_points['Season'].isin(search_team_season_team1)]

    select_allstats_in_a_game1 = select_allstats_in_a_game.loc[
        select_allstats_in_a_game['Season'].isin(search_team_season_team1)]
    select_allstats_in_a_game2 = select_allstats_in_a_game.loc[
        select_allstats_in_a_game['Season'].isin(search_team_season_team1)]
    All_Seasons2 = All_Seasons.loc[All_Seasons['Season'].isin(search_team_season_team1)]
    select_season_player1 = ''
else:
    All_Seasons1 = All_Seasons.loc[All_Seasons['Season'] == search_team_season_team1]
    period_points1 = period_points.loc[period_points['Season'] == search_team_season_team1]
    select_allstats_in_a_game1 = select_allstats_in_a_game.loc[
        select_allstats_in_a_game['Season'] == search_team_season_team1]
    select_allstats_in_a_game2 = select_allstats_in_a_game.loc[
        select_allstats_in_a_game['Season'] == search_team_season_team1]
    All_Seasons2 = All_Seasons.loc[All_Seasons['Season'] == search_team_season_team1]
    select_season_player1 = search_team_season_team1

if "All" in search_team_ha_team1:
    search_team_ha_team1 = ['A', 'H']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['HA'].isin(search_team_ha_team1)]
    period_points1 = period_points1.loc[period_points1['HA'].isin(search_team_ha_team1)]
    select_allstats_in_a_game1 = select_allstats_in_a_game1.loc[
        select_allstats_in_a_game1['HA'].isin(search_team_ha_team1)]
    select_allstats_in_a_game2 = select_allstats_in_a_game2.loc[
        select_allstats_in_a_game2['HA'].isin(search_team_ha_team1)]
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['HA1'].isin(search_team_ha_team1)]
    select_ha_player1 = ''
elif search_team_ha_team1 == "H":
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['HA'] == "H"]
    period_points1 = period_points1.loc[period_points1['HA'] == "H"]
    select_allstats_in_a_game1 = select_allstats_in_a_game1.loc[select_allstats_in_a_game1['HA'] == "H"]
    select_allstats_in_a_game2 = select_allstats_in_a_game2.loc[select_allstats_in_a_game2['HA'] == "A"]
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['HA1'] == "H"]
    select_ha_player1 = "H"

elif search_team_ha_team1 == "A":
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['HA'] == "A"]
    period_points1 = period_points1.loc[period_points1['HA'] == "A"]
    select_allstats_in_a_game1 = select_allstats_in_a_game1.loc[select_allstats_in_a_game1['HA'] == "A"]
    select_allstats_in_a_game2 = select_allstats_in_a_game2.loc[select_allstats_in_a_game2['HA'] == "H"]
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['HA1'] == "A"]
    select_ha_player1 = "A"

if "All" in search_team_wl_team1:
    search_team_wl_team1 = ['W', 'L']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['results'].isin(search_team_wl_team1)]
    period_points1 = period_points1.loc[period_points1['results'].isin(search_team_wl_team1)]
    select_allstats_in_a_game1 = select_allstats_in_a_game1.loc[
        select_allstats_in_a_game1['results'].isin(search_team_wl_team1)]
    select_allstats_in_a_game2 = select_allstats_in_a_game2.loc[
        select_allstats_in_a_game2['results'].isin(search_team_wl_team1)]
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['Result1'].isin(search_team_wl_team1)]

    select_wl_player1 = ''
elif search_team_wl_team1 == 'W':
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['results'] == 'W']
    period_points1 = period_points1.loc[period_points1['results'] == 'W']
    select_allstats_in_a_game1 = select_allstats_in_a_game1.loc[select_allstats_in_a_game1['results'] == 'W']
    select_allstats_in_a_game2 = select_allstats_in_a_game2.loc[select_allstats_in_a_game2['results'] == 'L']
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['Result1'] == 'W']
    select_wl_player1 = 'W'
elif search_team_wl_team1 == 'L':
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['results'] == 'L']
    period_points1 = period_points1.loc[period_points1['results'] == 'L']
    select_allstats_in_a_game1 = select_allstats_in_a_game1.loc[select_allstats_in_a_game1['results'] == 'L']
    select_allstats_in_a_game2 = select_allstats_in_a_game2.loc[select_allstats_in_a_game2['results'] == 'W']
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['Result1'] == 'L']
    select_wl_player1 = 'L'

if "All" in search_team_phase_team1:
    search_team_phase_team1 = ['Regular Season', 'Play In', 'Play offs', 'Final Four']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Phase'].isin(search_team_phase_team1)]
    period_points1 = period_points1.loc[period_points1['Phase'].isin(search_team_phase_team1)]
    select_allstats_in_a_game1 = select_allstats_in_a_game1.loc[
        select_allstats_in_a_game1['Phase'].isin(search_team_phase_team1)]
    select_allstats_in_a_game2 = select_allstats_in_a_game2.loc[
        select_allstats_in_a_game2['Phase'].isin(search_team_phase_team1)]

    All_Seasons2 = All_Seasons2.loc[All_Seasons2['Phase'].isin(search_team_phase_team1)]
    select_phase_player1 = ''
else:

    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Phase'] == search_team_phase_team1]
    period_points1 = period_points1.loc[period_points1['Phase'] == search_team_phase_team1]
    select_allstats_in_a_game1 = select_allstats_in_a_game1.loc[
        select_allstats_in_a_game1['Phase'] == search_team_phase_team1]
    select_allstats_in_a_game2 = select_allstats_in_a_game2.loc[
        select_allstats_in_a_game2['Phase'] == search_team_phase_team1]
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['Phase'] == search_team_phase_team1]
    select_phase_player1 = search_team_phase_team1

if "All" in search_team_round_team1:
    search_team_round_team1 = ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4', 'PO 5',
                               'Semi Final', 'Third Place', 'Final']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Round'].isin(search_team_round_team1)]
    period_points1 = period_points1.loc[period_points1['Round'].isin(search_team_round_team1)]
    select_allstats_in_a_game1 = select_allstats_in_a_game1.loc[
        select_allstats_in_a_game1['Round'].isin(search_team_round_team1)]
    select_allstats_in_a_game2 = select_allstats_in_a_game2.loc[
        select_allstats_in_a_game2['Round'].isin(search_team_round_team1)]
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['Round'].isin(search_team_round_team1)]
    select_round_player1 = ''

else:
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Round'] == search_team_round_team1]
    period_points1 = period_points1.loc[period_points1['Round'] == search_team_round_team1]
    select_allstats_in_a_game1 = select_allstats_in_a_game1.loc[
        select_allstats_in_a_game1['Round'] == search_team_round_team1]
    select_allstats_in_a_game2 = select_allstats_in_a_game2.loc[
        select_allstats_in_a_game2['Round'] == search_team_round_team1]
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['Round'] == search_team_round_team1]
    select_round_player1 = search_team_round_team1


def team_rating_stat_higher(dataset, stat):
    dataset1 = dataset[["Team", stat]].sort_values(stat, ascending=True).reset_index()
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


def compute_team_stats(dataset_stats1, dataset_stats2, dataset_periods):
    finalstats = dataset_stats1.groupby(['idseason', 'Team'])[['PTS', 'F2M',
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

    finalstats_opp = dataset_stats2.groupby(['idseason', 'Against'])[['PTS', 'F2M',
                                                                      'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                                                      'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF',
                                                                      'RF',
                                                                      'PIR', 'Possesions']].sum().reset_index().groupby(
        'Against')[['PTS', 'F2M',
                    'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                    'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF',
                    'PIR', 'Possesions']].mean().reset_index()

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
        ['Against', 'PTS', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'OR', 'DR', 'TR',
         'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'Possesions', 'Offensive Rating', 'EFG(%)',
         'TS(%)', 'FT Ratio', 'AS-TO Ratio', 'TO Ratio', 'AS Ratio']].round(1).rename(columns={'Against': 'Team'})

    finalstats_opp_for_rating = finalstats_opp.add_prefix("opp ").rename(columns={'opp Team': 'Team'})

    gamesstats = pd.merge(finalstats, finalstats_opp_for_rating)

    colsplus = ['AS', 'F2M', 'F2A', 'F3M', 'F3A', 'FTM',
                'FTA', 'OR', 'DR', 'TR', 'BLK', 'RF', 'ST', '2P(%)', '3P(%)', 'FT(%)', 'EFG(%)', 'TS(%)', 'FT Ratio',
                'AS-TO Ratio',
                'AS Ratio', 'opp TO Ratio', 'Offensive Rating']

    colsminus = ['BLKR', 'PF', 'opp PTS', 'opp AS', 'opp F2M', 'opp F2A', 'opp 2P(%)', 'opp F3M', 'opp F3A',
                 'opp 3P(%)',
                 'opp FTM', 'opp FTA', 'opp FT(%)', 'opp OR', 'opp DR', 'opp TR', 'opp ST', 'opp Offensive Rating',
                 'opp EFG(%)', 'opp TS(%)',
                 'opp FT Ratio', 'opp AS-TO Ratio', 'opp AS Ratio', 'TO Ratio']

    teams_ratings1 = team_rating_stat_higher(gamesstats, "PTS")
    for i in colsplus:
        df2 = team_rating_stat_higher(gamesstats, i)
        teams_ratings1 = pd.merge(teams_ratings1, df2)

    teams_ratings2 = team_rating_stat_lower(gamesstats, "TO")
    for i in colsminus:
        df3 = team_rating_stat_lower(gamesstats, i)
        teams_ratings2 = pd.merge(teams_ratings2, df3)
    teams_ratings = pd.merge(teams_ratings1, teams_ratings2)

    return [finalstats, finalstats_opp, teams_ratings]


def compute_player_stats_by_team(dataset, Team):
    computestats = dataset.groupby(['Player', 'Team'])[
        ['PTS', 'MIN', 'F2M', 'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR', 'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR',
         'PF', 'RF', 'PIR', 'Team_PTS', 'Team_F2M', 'Team_F2A', 'Team_F3M', 'Team_F3A', 'Team_FTM', 'Team_FTA',
         'Team_OR', 'Team_DR', 'Team_TR', 'Team_AS', 'Team_ST', 'Team_TO', 'Team_BLK', 'Team_PF', 'Team_opp_PTS',
         'Team_opp_F2M', 'Team_opp_F2A', 'Team_opp_F3M', 'Team_opp_F3A', 'Team_opp_FTM', 'Team_opp_FTA', 'Team_opp_OR',
         'Team_opp_DR', 'Team_opp_TR', 'Team_opp_AS', 'Team_opp_ST', 'Team_opp_TO', 'Team_opp_BLK',
         'Team_opp_PF']].mean().round(1).reset_index()
    computestats['P2'] = 100 * (computestats['F2M'] / computestats['F2A'])
    computestats['P3'] = 100 * (computestats['F3M'] / computestats['F3A'])
    computestats['PFT'] = 100 * (computestats['FTM'] / computestats['FTA'])
    computestats['POS'] = 0.96 * (
            computestats['F2A'] + computestats['F3A'] - computestats['OR'] + computestats['TO'] + 0.44 *
            computestats['FTA'])
    computestats['ORA'] = 100 * (computestats['PTS'] / computestats['POS'])
    computestats['EFG'] = 100 * (computestats['F2M'] + 1.5 * computestats['F3M']) / (
            computestats['F2A'] + computestats['F3A'])
    computestats['TS'] = 100 * (computestats['PTS']) / (
            2 * (computestats['F2A'] + computestats['F3A'] + 0.44 * computestats['FTA']))
    computestats['FTR'] = computestats['FTA'] / (computestats['F3A'] + computestats['F2A'])
    computestats['ASTOR'] = computestats['AS'] / computestats['TO']
    computestats['TOR'] = 100 * (computestats['TO'] / computestats['POS'])
    computestats['ASR'] = 100 * (computestats['AS'] / computestats['POS'])
    computestats['USG'] = 100 * (
            ((computestats['F3A'] + computestats['F2A']) + 0.44 * computestats['FTA'] + computestats['TO']) * (
        40)) / (computestats['MIN'] * (
            computestats['Team_F2A'] + computestats['Team_F3A'] + 0.44 * computestats['Team_FTA'] + computestats[
        'Team_TO']))
    computestats['ORP'] = (100 * computestats['OR']) / (computestats['Team_OR'] + computestats['Team_opp_OR'])

    computestatsfinal = computestats.loc[computestats['Team'] == Team]
    computestatsfinal.drop('Team', axis=1, inplace=True)
    computestatsfinal = computestatsfinal.set_index('Player').round(1)
    computestatsfinal = computestatsfinal[
        ['PTS', 'MIN', 'F2M', 'F2A', 'P2', 'F3M', 'F3A', 'P3', 'FTM', 'FTA', 'PFT', 'OR',
         'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'POS', 'ORA', 'EFG', 'TS', 'FTR', 'ASTOR',
         'TOR', 'ASR', 'USG', 'ORP']]
    return computestatsfinal


def compute_player_stats_by_team_against(dataset, Team):
    player_wins = dataset.loc[(dataset['Against'] == Team)].groupby('Player')['Win'].sum().reset_index()
    player_games = dataset.loc[(dataset['Against'] == Team)]['Player'].value_counts().reset_index().rename(
        columns={"count": 'Games'})

    computestats = dataset.groupby(['Player', 'Against'])[
        ['PTS', 'MIN', 'F2M', 'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR', 'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR',
         'PF', 'RF', 'PIR', 'Team_PTS', 'Team_F2M', 'Team_F2A', 'Team_F3M', 'Team_F3A', 'Team_FTM', 'Team_FTA',
         'Team_OR', 'Team_DR', 'Team_TR', 'Team_AS', 'Team_ST', 'Team_TO', 'Team_BLK', 'Team_PF', 'Team_opp_PTS',
         'Team_opp_F2M', 'Team_opp_F2A', 'Team_opp_F3M', 'Team_opp_F3A', 'Team_opp_FTM', 'Team_opp_FTA', 'Team_opp_OR',
         'Team_opp_DR', 'Team_opp_TR', 'Team_opp_AS', 'Team_opp_ST', 'Team_opp_TO', 'Team_opp_BLK',
         'Team_opp_PF']].mean().round(1).reset_index()
    computestats['P2'] = 100 * (computestats['F2M'] / computestats['F2A'])
    computestats['P3'] = 100 * (computestats['F3M'] / computestats['F3A'])
    computestats['PFT'] = 100 * (computestats['FTM'] / computestats['FTA'])
    computestats['POS'] = 0.96 * (
                computestats['F2A'] + computestats['F3A'] - computestats['OR'] + computestats['TO'] + 0.44 *
                computestats['FTA'])
    computestats['ORA'] = 100 * (computestats['PTS'] / computestats['POS'])
    computestats['EFG'] = 100 * (computestats['F2M'] + 1.5 * computestats['F3M']) / (
                computestats['F2A'] + computestats['F3A'])
    computestats['TS'] = 100 * (computestats['PTS']) / (
                2 * (computestats['F2A'] + computestats['F3A'] + 0.44 * computestats['FTA']))
    computestats['FTR'] = computestats['FTA'] / (computestats['F3A'] + computestats['F2A'])
    computestats['ASTOR'] = computestats['AS'] / computestats['TO']
    computestats['TOR'] = 100 * (computestats['TO'] / computestats['POS'])
    computestats['ASR'] = 100 * (computestats['AS'] / computestats['POS'])
    computestats['USG'] = 100 * (
                ((computestats['F3A'] + computestats['F2A']) + 0.44 * computestats['FTA'] + computestats['TO']) * (
            40)) / (computestats['MIN'] * (
                computestats['Team_F2A'] + computestats['Team_F3A'] + 0.44 * computestats['Team_FTA'] + computestats[
            'Team_TO']))
    computestats['ORP'] = (100 * computestats['OR']) / (computestats['Team_OR'] + computestats['Team_opp_OR'])

    computestatsfinal = computestats.loc[computestats['Against'] == Team]
    computestatsfinal.drop('Against', axis=1, inplace=True)
    player_extra = pd.merge(player_games, player_wins)
    computestatsfinal = pd.merge(player_extra, computestatsfinal)

    computestatsfinal = computestatsfinal.set_index('Player').round(1)
    computestatsfinal = computestatsfinal[
        ['Games', 'Win', 'PTS', 'MIN', 'F2M', 'F2A', 'P2', 'F3M', 'F3A', 'P3', 'FTM', 'FTA', 'PFT', 'OR',
         'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'POS', 'ORA', 'EFG', 'TS', 'FTR', 'ASTOR',
         'TOR', 'ASR', 'USG', 'ORP']]

    return computestatsfinal


teamstats = compute_team_stats(All_Seasons1, All_Seasons2, period_points1)[0]
oppstats = compute_team_stats(All_Seasons1, All_Seasons2, period_points1)[1]
ratingstats = compute_team_stats(All_Seasons1, All_Seasons2, period_points1)[2]
All_seasons_pos = pd.merge(All_Seasons1, Positions, on='Player')

st.header('Euroleague Stats')
teams, ratings, gamesstats = st.columns([1, 1, 1])

with teams:
    st.write('### Team: ' + search_team_team1)
    st.write('Season: ' + select_season_player1)
    st.write('Phase: ' + select_phase_player1)
    st.write('Round: ' + select_round_player1)
    st.write('Home or away: ' + select_ha_player1)
    st.write('Result: ' + select_wl_player1)

with ratings:
    try:

        offense_rating_data1 = ratingstats.loc[ratingstats.Team == search_team_team1][
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
            width=200,
            height=150,
            margin=dict(
                l=30,
                r=50,
                b=10,
                t=40,
                pad=0
            ))

        st.write(off1)

        defense_ratings1 = ratingstats.loc[ratingstats.Team == search_team_team1][
            ['Rating ST', 'Rating DR', 'Rating PF', 'Rating BLK', 'Rating opp PTS', 'Rating opp AS',
             'Rating opp F2M', 'Rating opp F2A', 'Rating opp 2P(%)', 'Rating opp F3M', 'Rating opp F3A',
             'Rating opp 3P(%)',
             'Rating opp FTM', 'Rating opp FTA', 'Rating opp FT(%)', 'Rating opp OR', 'Rating opp Offensive Rating',
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
            width=200,
            height=150,
            margin=dict(
                l=30,
                r=50,
                b=10,
                t=40,
                pad=0
            ))

        st.write(defe1)

        total_ratings1 = ratingstats.loc[ratingstats.Team == search_team_team1].filter(regex='Rating').melt()[
            'value'].mean()

        tot = go.Figure(go.Indicator(
            mode="gauge+number",
            value=total_ratings1.round(0),
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 100]},
                   'bordercolor': "gray"},
            title={'text': "Overall"}))

        tot.update_layout(
            autosize=True,
            width=200,
            height=150,
            margin=dict(
                l=30,
                r=50,
                b=10,
                t=40,
                pad=0
            ))

        st.write(tot)
    except:
        st.error("No data available with this parameters")

with gamesstats:
    games = pd.DataFrame({'Played': ['Total Games'], 'No.Games': [
        period_points1.loc[period_points1.Team == search_team_team1]['Team'].value_counts().reset_index()[
            'count'].sum()]})
    try:
        wins = pd.DataFrame({'Played': ['Total Wins'], 'No.Games': [
            period_points1.loc[(period_points1.Team == search_team_team1) & (period_points1.results == "W")][
                'Team'].value_counts().reset_index()[
                'count'].sum()]})
    except:
        wins = pd.DataFrame({'Played': ['Total Wins'], 'No.Games': [0]})
    try:
        loses = pd.DataFrame({'Played': ['Total Loses'], 'No.Games': [
            period_points1.loc[(period_points1.Team == search_team_team1) & (period_points1.results == "L")][
                'Team'].value_counts().reset_index()[
                'count'].sum()]})
    except:
        loses = pd.DataFrame({'Played': ['Total Loses'], 'No.Games': [0]})
    parts = pd.DataFrame({'Euroleague': ['Years'], 'Participation': [
        period_points.loc[(period_points.Team == search_team_team1)][['Phase', 'Season']].value_counts().reset_index()[
            'Season'].nunique()]})
    playoff = pd.DataFrame({'Euroleague': ['Playoffs'], 'Participation': [
        period_points.loc[(period_points.Team == search_team_team1) & (period_points.Phase == 'Play offs')][
            ['Phase', 'Season']].value_counts().reset_index()[
            'Season'].nunique()]})
    finalfour = pd.DataFrame({'Euroleague': ['F4'], 'Participation': [
        period_points.loc[(period_points.Team == search_team_team1) & (period_points.Phase == 'Final Four')][
            ['Phase', 'Season']].value_counts().reset_index()[
            'Season'].nunique()]})
    title = pd.DataFrame({'Euroleague': ['Titles'], 'Participation': [
        period_points.loc[(period_points.Team == search_team_team1) & (period_points.Phase == 'Final Four') & (
                    period_points.Round == 'Final') & (period_points.results == 'W')][
            ['Phase', 'Season']].value_counts().reset_index()[
            'Season'].nunique()]})

st.write('##### History in Euroleague')
interactive_table(pd.concat([parts, playoff, finalfour, title]).set_index('Euroleague'), paging=False, height=900,
                  width=2000, showIndex=True, classes = "display order-column nowrap table_with_monospace_font", searching = True,
fixedColumns = True, select = True, info = False, scrollCollapse = True,
scrollX = True, scrollY = 1000, fixedHeader = True, scroller = True, filter = 'bottom',
columnDefs = [{"className": "dt-center", "targets": "_all"}])

st.write('##### Games in Euroleague')
interactive_table(pd.concat([games, wins, loses]).set_index('Played'),
                  paging=False, height=900, width=2000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])

periodteam1 = (period_points1.loc[period_points1.Team == search_team_team1].groupby('Team')[
                   ['Q1S', 'Q2S', 'FHS', 'Q3S', 'Q4S', 'SHS', 'EXS']].mean().reset_index().round(1)
               .rename(columns={'Q1S': 'Q1', 'Q2S': 'Q2', 'Q3S': 'Q3', 'Q4S': 'Q4',
                                'EXS': 'Extra time', 'FHS': 'First Half', 'SHS': 'Second Half'
                                }))
periodteam2 = (period_points1.loc[period_points1.Team == search_team_team1].groupby('Team')[
                   ['Q1C', 'Q2C', 'FHC', 'Q3C', 'Q4C', 'SHC', 'EXC']].mean().reset_index().round(1)
               .rename(
    columns={'Q1C': 'Q1', 'Q2C': 'Q2', 'Q3C': 'Q3', 'Q4C': 'Q4', 'EXC': 'Extra time', 'FHC': 'First Half',
             'SHC': 'Second Half'
             }))
periodteam2['Team'] = periodteam2['Team'].str.replace(search_team_team1, "Opponent")
periodteams = pd.concat([periodteam1, periodteam2])

st.write('##### Period Points per game')
interactive_table(periodteams.set_index("Team"),
                  paging=False, height=900, width=2000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])

basic_stats1 = teamstats.loc[teamstats.Team == search_team_team1][
    ['Team', 'PTS', 'AS', 'TO', 'TR', 'DR', 'OR', 'BLK', 'ST', 'PF', 'PIR']].rename(
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
    ['Team', 'PTS', 'AS', 'TO', 'TR', 'DR', 'OR', 'BLK', 'ST', 'PF', 'PIR']].rename(
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
    ['Team', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)',
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
    ['Team', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)',
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
advanced_stats1 = (teamstats.loc[teamstats.Team == search_team_team1][["Team", 'Possesions', 'Offensive Rating',
                                                                       'AS-TO Ratio', 'TO Ratio', 'AS Ratio']]
)

advanced_stats2 = (oppstats.loc[oppstats.Team == search_team_team1][["Team", 'Possesions', 'Offensive Rating',
                                                                     'AS-TO Ratio', 'TO Ratio', 'AS Ratio']]
)
advanced_stats2['Team'] = advanced_stats2['Team'].str.replace(search_team_team1, "Opponent")
advanced_stats_data = pd.concat([advanced_stats1, advanced_stats2])
interactive_table(advanced_stats_data.set_index("Team"),
                  paging=False, height=1000, width=2000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])


def compute_team_stats_against_each_team(dataset_stats1, dataset_stats2, dataset_periods):
    teamstats = dataset_stats1.loc[dataset_stats1.Team == search_team_team1]

    oppstats = dataset_stats2.loc[dataset_stats2.Against == search_team_team1]


    finalstats = teamstats.groupby(['idseason', 'Against'])[['PTS', 'F2M',
                                                             'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                                             'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF',
                                                             'PIR', 'Possesions']].sum().reset_index().groupby('Against')[
        ['PTS', 'F2M',
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
        ['Against', 'PTS', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'OR', 'DR', 'TR',
         'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'Possesions', 'Offensive Rating', 'EFG(%)',
         'TS(%)', 'FT Ratio', 'AS-TO Ratio', 'TO Ratio', 'AS Ratio']].round(1)

    finalstats_opp = oppstats.groupby(['idseason', 'Team'])[['PTS', 'F2M',
                                                             'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                                             'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF',
                                                             'PIR', 'Possesions']].sum().reset_index().groupby('Team')[
        ['PTS', 'F2M',
         'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
         'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF',
         'PIR', 'Possesions']].mean().reset_index()

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
        ['Team', 'PTS', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'OR', 'DR', 'TR',
         'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'Possesions', 'Offensive Rating', 'EFG(%)',
         'TS(%)', 'FT Ratio', 'AS-TO Ratio', 'TO Ratio', 'AS Ratio']].round(1).add_prefix('opp ').rename(
        columns={'opp Team': 'Against', 'opp Offensive Rating': 'Defensive Rating'})

    final = pd.merge(finalstats, finalstats_opp)[
        ['Against', 'PTS', 'opp PTS', 'F2M', 'F2A', '2P(%)', 'opp F2M', 'opp F2A', 'opp 2P(%)', 'F3M', 'F3A', '3P(%)',
         'opp F3M', 'opp F3A', 'opp 3P(%)',
         'FTM', 'FTA', 'FT(%)', 'opp FTM', 'opp FTA', 'opp FT(%)', 'OR', 'opp OR', 'DR', 'opp DR', 'TR', 'opp TR',
         'AS', 'opp AS', 'ST', 'opp ST', 'TO', 'opp TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'opp PIR', 'Possesions',
         'opp Possesions', 'Offensive Rating', 'Defensive Rating', 'EFG(%)', 'opp EFG(%)',
         'TS(%)', 'opp TS(%)', 'FT Ratio', 'opp FT Ratio', 'AS-TO Ratio', 'opp AS-TO Ratio', 'TO Ratio', 'opp TO Ratio',
         'AS Ratio', 'opp AS Ratio']]
    return final

st.write('##### Stats against each team in Euroleague')
interactive_table(compute_team_stats_against_each_team(All_Seasons1, All_Seasons2, period_points1).set_index('Against'),
                  paging=False, height=1000, width=2000, showIndex=True,
classes = "display order-column nowrap table_with_monospace_font", searching = False, fixedColumns = True, select = True, info = False, scrollCollapse = True,
scrollX = True, scrollY = 1000, fixedHeader = True, scroller = True, filter = 'bottom',
columnDefs = [{"className": "dt-center", "targets": "_all"}])
st.header("Player Stats")
stats_by_pos = \
All_seasons_pos.loc[All_seasons_pos.Team == search_team_team1].groupby(['Team', 'Position', 'idseason']).sum()[
    ['PTS', 'F2M',
     'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
     'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF',
     'PIR', 'Possesions', 'Team_F2A', 'Team_F3A', 'Team_FTA', 'Team_TO', 'MIN']].groupby(
    ['Team', 'Position']).mean().reset_index().round(1).sort_values('Position')

stats_by_pos['2P(%)'] = 100 * (stats_by_pos['F2M'] / stats_by_pos['F2A'])
stats_by_pos['3P(%)'] = 100 * (stats_by_pos['F3M'] / stats_by_pos['F3A'])
stats_by_pos['FT(%)'] = 100 * (stats_by_pos['FTM'] / stats_by_pos['FTA'])
stats_by_pos['Offensive Rating'] = 100 * (stats_by_pos['PTS'] / stats_by_pos['Possesions'])
stats_by_pos['EFG(%)'] = 100 * (stats_by_pos['F2M'] + 1.5 * stats_by_pos['F3M']) / (
        stats_by_pos['F2A'] + stats_by_pos['F3A'])
stats_by_pos['TS(%)'] = 100 * (stats_by_pos['PTS']) / (
        2 * (stats_by_pos['F2A'] + stats_by_pos['F3A'] + 0.44 * stats_by_pos['FTA']))
stats_by_pos['FT Ratio'] = stats_by_pos['FTA'] / (stats_by_pos['F3A'] + stats_by_pos['F2A'])
stats_by_pos['AS-TO Ratio'] = stats_by_pos['AS'] / stats_by_pos['TO']
stats_by_pos['TO Ratio'] = 100 * (stats_by_pos['TO'] / stats_by_pos['Possesions'])
stats_by_pos['AS Ratio'] = 100 * (stats_by_pos['AS'] / stats_by_pos['Possesions'])
stats_by_pos['USG(%)'] = 100 * (
        ((stats_by_pos['F3A'] + stats_by_pos['F2A']) + 0.44 * stats_by_pos['FTA'] + stats_by_pos['TO']) * (
    40)) / (stats_by_pos['MIN'] * (
        stats_by_pos['Team_F2A'] + stats_by_pos['Team_F3A'] + 0.44 * stats_by_pos['Team_FTA'] + stats_by_pos[
    'Team_TO']))
stats_by_pos = stats_by_pos[
    ['Position', 'PTS', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'OR', 'DR', 'TR',
     'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'Possesions', 'Offensive Rating', 'EFG(%)',
     'TS(%)', 'FT Ratio', 'AS-TO Ratio', 'TO Ratio', 'AS Ratio', 'USG(%)']].round(1)

st.write("### Stats by Player")
interactive_table(compute_player_stats_by_team(All_Seasons1, search_team_team1),
                  paging=False, height=960, width=20000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=False,
                  fixedColumns=True,
                  select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True,
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])
st.write("### Stats by Position")
interactive_table(stats_by_pos.set_index('Position'),
                  paging=False, height=960, width=20000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=False,
                  fixedColumns=True,
                  select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True,
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])

st.header("Opponent Players Stats")
stats_by_pos_opp = All_seasons_pos.loc[All_seasons_pos.Against == search_team_team1].groupby(
    ['Against', 'Position', 'idseason']).sum()[
    ['PTS', 'F2M',
     'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
     'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF',
     'PIR', 'Possesions', 'Team_F2A', 'Team_F3A', 'Team_FTA', 'Team_TO', 'MIN']].groupby(
    ['Against', 'Position']).mean().reset_index().round(1).sort_values('Position')

stats_by_pos_opp['2P(%)'] = 100 * (stats_by_pos_opp['F2M'] / stats_by_pos_opp['F2A'])
stats_by_pos_opp['3P(%)'] = 100 * (stats_by_pos_opp['F3M'] / stats_by_pos_opp['F3A'])
stats_by_pos_opp['FT(%)'] = 100 * (stats_by_pos_opp['FTM'] / stats_by_pos_opp['FTA'])
stats_by_pos_opp['Offensive Rating'] = 100 * (stats_by_pos_opp['PTS'] / stats_by_pos_opp['Possesions'])
stats_by_pos_opp['EFG(%)'] = 100 * (stats_by_pos_opp['F2M'] + 1.5 * stats_by_pos_opp['F3M']) / (
        stats_by_pos_opp['F2A'] + stats_by_pos_opp['F3A'])
stats_by_pos_opp['TS(%)'] = 100 * (stats_by_pos_opp['PTS']) / (
        2 * (stats_by_pos_opp['F2A'] + stats_by_pos_opp['F3A'] + 0.44 * stats_by_pos_opp['FTA']))
stats_by_pos_opp['FT Ratio'] = stats_by_pos_opp['FTA'] / (stats_by_pos_opp['F3A'] + stats_by_pos_opp['F2A'])
stats_by_pos_opp['AS-TO Ratio'] = stats_by_pos_opp['AS'] / stats_by_pos_opp['TO']
stats_by_pos_opp['TO Ratio'] = 100 * (stats_by_pos_opp['TO'] / stats_by_pos_opp['Possesions'])
stats_by_pos_opp['AS Ratio'] = 100 * (stats_by_pos_opp['AS'] / stats_by_pos_opp['Possesions'])
stats_by_pos_opp['USG(%)'] = 100 * (
        ((stats_by_pos_opp['F3A'] + stats_by_pos_opp['F2A']) + 0.44 * stats_by_pos_opp['FTA'] +
         stats_by_pos_opp['TO']) * (
            40)) / (stats_by_pos_opp['MIN'] * (
        stats_by_pos_opp['Team_F2A'] + stats_by_pos_opp['Team_F3A'] + 0.44 * stats_by_pos_opp['Team_FTA'] +
        stats_by_pos_opp[
            'Team_TO']))
stats_by_pos_opp = stats_by_pos_opp[
    ['Position', 'PTS', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'OR', 'DR', 'TR',
     'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'Possesions', 'Offensive Rating', 'EFG(%)',
     'TS(%)', 'FT Ratio', 'AS-TO Ratio', 'TO Ratio', 'AS Ratio', 'USG(%)']].round(1)

st.write("### Stats by Players")
interactive_table(compute_player_stats_by_team_against(All_Seasons2, search_team_team1),
                  paging=False, height=960, width=20000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])

st.write("### Stats by Position")
interactive_table(stats_by_pos_opp.set_index('Position'),
                  paging=False, height=960, width=20000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])
st.header("Stats by game")
Teams = All_Seasons1['Team'].unique()
dataset_all = pd.DataFrame()
for team in Teams:
    dataset = select_allstats_in_a_game2.loc[select_allstats_in_a_game2.Team == team]
    dataset = dataset.sort_values(['Season', 'Fixture']).reset_index()
    dataset.drop('index', axis=1, inplace=True)
    dataset = dataset.reset_index()
    dataset['Q1S Before'] = ((dataset['Q1S'].cumsum() - dataset['Q1S']) / (dataset['index'])).round(1)
    dataset['Q1C Before'] = ((dataset['Q1C'].cumsum() - dataset['Q1C']) / (dataset['index'])).round(1)
    dataset['Q2S Before'] = ((dataset['Q2S'].cumsum() - dataset['Q2S']) / (dataset['index'])).round(1)
    dataset['Q2C Before'] = ((dataset['Q2C'].cumsum() - dataset['Q2C']) / (dataset['index'])).round(1)
    dataset['Q3S Before'] = ((dataset['Q3S'].cumsum() - dataset['Q3S']) / (dataset['index'])).round(1)
    dataset['Q3C Before'] = ((dataset['Q3C'].cumsum() - dataset['Q3C']) / (dataset['index'])).round(1)
    dataset['Q4S Before'] = ((dataset['Q4S'].cumsum() - dataset['Q4S']) / (dataset['index'])).round(1)
    dataset['Q4C Before'] = ((dataset['Q4C'].cumsum() - dataset['Q4C']) / (dataset['index'])).round(1)
    dataset['EXS Before'] = ((dataset['EXS'].cumsum() - dataset['EXS']) / (dataset['index'])).round(1)
    dataset['EXC Before'] = ((dataset['EXC'].cumsum() - dataset['EXC']) / (dataset['index'])).round(1)
    dataset['FHS Before'] = ((dataset['FHS'].cumsum() - dataset['FHS']) / (dataset['index'])).round(1)
    dataset['FHC Before'] = ((dataset['FHC'].cumsum() - dataset['FHC']) / (dataset['index'])).round(1)
    dataset['SHS Before'] = ((dataset['SHS'].cumsum() - dataset['SHS']) / (dataset['index'])).round(1)
    dataset['SHC Before'] = ((dataset['SHC'].cumsum() - dataset['SHC']) / (dataset['index'])).round(1)

    dataset['PTS Before'] = ((dataset['PTS'].cumsum() - dataset['PTS']) / (dataset['index'])).round(1)
    dataset['2PM Before'] = ((dataset['2PM'].cumsum() - dataset['2PM']) / (dataset['index'])).round(1)
    dataset['2PA Before'] = ((dataset['2PA'].cumsum() - dataset['2PA']) / (dataset['index'])).round(1)
    dataset['2P(%) Before'] = (100 * dataset['2PM Before'] / dataset['2PA Before']).round(1)
    dataset['3PM Before'] = ((dataset['3PM'].cumsum() - dataset['3PM']) / (dataset['index'])).round(1)
    dataset['3PA Before'] = ((dataset['3PA'].cumsum() - dataset['3PA']) / (dataset['index'])).round(1)
    dataset['3P(%) Before'] = (100 * dataset['3PM Before'] / dataset['3PA Before']).round(1)
    dataset['FTM Before'] = ((dataset['FTM'].cumsum() - dataset['FTM']) / (dataset['index'])).round(1)
    dataset['FTA Before'] = ((dataset['FTA'].cumsum() - dataset['FTA']) / (dataset['index'])).round(1)
    dataset['FT(%) Before'] = (100 * dataset['FTM Before'] / dataset['FTA Before']).round(1)
    dataset['OR Before'] = ((dataset['OR'].cumsum() - dataset['OR']) / (dataset['index'])).round(1)
    dataset['DR Before'] = ((dataset['DR'].cumsum() - dataset['DR']) / (dataset['index'])).round(1)
    dataset['TR Before'] = ((dataset['TR'].cumsum() - dataset['TR']) / (dataset['index'])).round(1)
    dataset['AS Before'] = ((dataset['AS'].cumsum() - dataset['AS']) / (dataset['index'])).round(1)
    dataset['STL Before'] = ((dataset['STL'].cumsum() - dataset['STL']) / (dataset['index'])).round(1)
    dataset['TO Before'] = ((dataset['TO'].cumsum() - dataset['TO']) / (dataset['index'])).round(1)
    dataset['BLK Before'] = ((dataset['BLK'].cumsum() - dataset['BLK']) / (dataset['index'])).round(1)
    dataset['BLKR Before'] = ((dataset['BLKR'].cumsum() - dataset['BLKR']) / (dataset['index'])).round(1)
    dataset['PF Before'] = ((dataset['PF'].cumsum() - dataset['PF']) / (dataset['index'])).round(1)

    dataset['PTS conc Before'] = ((dataset['opp PTS'].cumsum() - dataset['opp PTS']) / (dataset['index'])).round(1)
    dataset['2PM conc Before'] = ((dataset['opp 2PM'].cumsum() - dataset['opp 2PM']) / (dataset['index'])).round(1)
    dataset['2PA conc Before'] = ((dataset['opp 2PA'].cumsum() - dataset['opp 2PA']) / (dataset['index'])).round(1)
    dataset['2P(%) conc Before'] = (100 * dataset['2PM conc Before'] / dataset['2PA conc Before']).round(1)
    dataset['3PM conc Before'] = ((dataset['opp 3PM'].cumsum() - dataset['opp 3PM']) / (dataset['index'])).round(1)
    dataset['3PA conc Before'] = ((dataset['opp 3PA'].cumsum() - dataset['opp 3PA']) / (dataset['index'])).round(1)
    dataset['3P(%) conc Before'] = (100 * dataset['3PM conc Before'] / dataset['3PA conc Before']).round(1)
    dataset['FTM conc Before'] = ((dataset['opp FTM'].cumsum() - dataset['opp FTM']) / (dataset['index'])).round(1)
    dataset['FTA conc Before'] = ((dataset['opp FTA'].cumsum() - dataset['opp FTA']) / (dataset['index'])).round(1)
    dataset['FT(%) conc Before'] = (100 * dataset['FTM conc Before'] / dataset['FTA conc Before']).round(1)
    dataset['OR conc Before'] = ((dataset['opp OR'].cumsum() - dataset['opp OR']) / (dataset['index'])).round(1)
    dataset['DR conc Before'] = ((dataset['opp DR'].cumsum() - dataset['opp DR']) / (dataset['index'])).round(1)
    dataset['TR conc Before'] = ((dataset['opp TR'].cumsum() - dataset['opp TR']) / (dataset['index'])).round(1)
    dataset['AS conc Before'] = ((dataset['opp AS'].cumsum() - dataset['opp AS']) / (dataset['index'])).round(1)
    dataset['STL conc Before'] = ((dataset['opp STL'].cumsum() - dataset['opp STL']) / (dataset['index'])).round(1)
    dataset['TO conc Before'] = ((dataset['opp TO'].cumsum() - dataset['opp TO']) / (dataset['index'])).round(1)
    dataset['PF conc Before'] = ((dataset['opp PF'].cumsum() - dataset['opp PF']) / (dataset['index'])).round(1)
    dataset = dataset.filter(regex='Team|Season|Fixture|Before')
    dataset_all = pd.concat([dataset_all, dataset])

dataset_all = dataset_all.add_prefix('opp ').rename(
    columns={'opp Team': 'Against', 'opp Fixture': 'Fixture', 'opp Season': 'Season'})
select_allstats_in_a_game1 = select_allstats_in_a_game1.loc[select_allstats_in_a_game1.Team == search_team_team1]
select_allstats_in_a_game1 = select_allstats_in_a_game1.sort_values(['Season', 'Fixture']).reset_index()
select_allstats_in_a_game1.drop('index', axis=1, inplace=True)
select_allstats_in_a_game1 = select_allstats_in_a_game1.reset_index()
select_allstats_in_a_game1['Q1S Before'] = (
        (select_allstats_in_a_game1['Q1S'].cumsum() - select_allstats_in_a_game1['Q1S']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['Q1C Before'] = (
        (select_allstats_in_a_game1['Q1C'].cumsum() - select_allstats_in_a_game1['Q1C']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['Q2S Before'] = (
        (select_allstats_in_a_game1['Q2S'].cumsum() - select_allstats_in_a_game1['Q2S']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['Q2C Before'] = (
        (select_allstats_in_a_game1['Q2C'].cumsum() - select_allstats_in_a_game1['Q2C']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['Q3S Before'] = (
        (select_allstats_in_a_game1['Q3S'].cumsum() - select_allstats_in_a_game1['Q3S']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['Q3C Before'] = (
        (select_allstats_in_a_game1['Q3C'].cumsum() - select_allstats_in_a_game1['Q3C']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['Q4S Before'] = (
        (select_allstats_in_a_game1['Q4S'].cumsum() - select_allstats_in_a_game1['Q4S']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['Q4C Before'] = (
        (select_allstats_in_a_game1['Q4C'].cumsum() - select_allstats_in_a_game1['Q4C']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['EXS Before'] = (
        (select_allstats_in_a_game1['EXS'].cumsum() - select_allstats_in_a_game1['EXS']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['EXC Before'] = (
        (select_allstats_in_a_game1['EXC'].cumsum() - select_allstats_in_a_game1['EXC']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['FHS Before'] = (
        (select_allstats_in_a_game1['FHS'].cumsum() - select_allstats_in_a_game1['FHS']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['FHC Before'] = (
        (select_allstats_in_a_game1['FHC'].cumsum() - select_allstats_in_a_game1['FHC']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['SHS Before'] = (
        (select_allstats_in_a_game1['SHS'].cumsum() - select_allstats_in_a_game1['SHS']) / (
    select_allstats_in_a_game1['index'])).round(1)

select_allstats_in_a_game1['SHC Before'] = (
        (select_allstats_in_a_game1['SHC'].cumsum() - select_allstats_in_a_game1['SHC']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['PTS Before'] = (
(select_allstats_in_a_game1['PTS'].cumsum() - select_allstats_in_a_game1['PTS']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['2PM Before'] = (
        (select_allstats_in_a_game1['2PM'].cumsum() - select_allstats_in_a_game1['2PM']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['2PA Before'] = (
        (select_allstats_in_a_game1['2PA'].cumsum() - select_allstats_in_a_game1['2PA']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['2P(%) Before'] = (
        100 * select_allstats_in_a_game1['2PM Before'] / select_allstats_in_a_game1['2PA Before']).round(1)
select_allstats_in_a_game1['3PM Before'] = (
        (select_allstats_in_a_game1['3PM'].cumsum() - select_allstats_in_a_game1['3PM']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['3PA Before'] = (
        (select_allstats_in_a_game1['3PA'].cumsum() - select_allstats_in_a_game1['3PA']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['3P(%) Before'] = (
        100 * select_allstats_in_a_game1['3PM Before'] / select_allstats_in_a_game1['3PA Before']).round(1)
select_allstats_in_a_game1['FTM Before'] = (
        (select_allstats_in_a_game1['FTM'].cumsum() - select_allstats_in_a_game1['FTM']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['FTA Before'] = (
        (select_allstats_in_a_game1['FTA'].cumsum() - select_allstats_in_a_game1['FTA']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['FT(%) Before'] = (
        100 * select_allstats_in_a_game1['FTM Before'] / select_allstats_in_a_game1['FTA Before']).round(1)
select_allstats_in_a_game1['OR Before'] = (
        (select_allstats_in_a_game1['OR'].cumsum() - select_allstats_in_a_game1['OR']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['DR Before'] = (
        (select_allstats_in_a_game1['DR'].cumsum() - select_allstats_in_a_game1['DR']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['TR Before'] = (
        (select_allstats_in_a_game1['TR'].cumsum() - select_allstats_in_a_game1['TR']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['AS Before'] = (
        (select_allstats_in_a_game1['AS'].cumsum() - select_allstats_in_a_game1['AS']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['STL Before'] = (
        (select_allstats_in_a_game1['STL'].cumsum() - select_allstats_in_a_game1['STL']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['TO Before'] = (
        (select_allstats_in_a_game1['TO'].cumsum() - select_allstats_in_a_game1['TO']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['BLK Before'] = (
        (select_allstats_in_a_game1['BLK'].cumsum() - select_allstats_in_a_game1['BLK']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['BLKR Before'] = (
        (select_allstats_in_a_game1['BLKR'].cumsum() - select_allstats_in_a_game1['BLKR']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['PF Before'] = (
        (select_allstats_in_a_game1['PF'].cumsum() - select_allstats_in_a_game1['PF']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['PTS conc Before'] = (
        (select_allstats_in_a_game1['opp PTS'].cumsum() - select_allstats_in_a_game1['opp PTS']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['2PM conc Before'] = (
        (select_allstats_in_a_game1['opp 2PM'].cumsum() - select_allstats_in_a_game1['opp 2PM']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['2PA conc Before'] = (
        (select_allstats_in_a_game1['opp 2PA'].cumsum() - select_allstats_in_a_game1['opp 2PA']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['2P(%) conc Before'] = (
        100 * select_allstats_in_a_game1['2PM conc Before'] / select_allstats_in_a_game1[
    '2PA conc Before']).round(1)
select_allstats_in_a_game1['3PM conc Before'] = (
        (select_allstats_in_a_game1['opp 3PM'].cumsum() - select_allstats_in_a_game1['opp 3PM']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['3PA conc Before'] = (
        (select_allstats_in_a_game1['opp 3PA'].cumsum() - select_allstats_in_a_game1['opp 3PA']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['3P(%) conc Before'] = (
        100 * select_allstats_in_a_game1['3PM conc Before'] / select_allstats_in_a_game1[
    '3PA conc Before']).round(1)
select_allstats_in_a_game1['FTM conc Before'] = (
        (select_allstats_in_a_game1['opp FTM'].cumsum() - select_allstats_in_a_game1['opp FTM']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['FTA conc Before'] = (
        (select_allstats_in_a_game1['opp FTA'].cumsum() - select_allstats_in_a_game1['opp FTA']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['FT(%) conc Before'] = (
        100 * select_allstats_in_a_game1['FTM conc Before'] / select_allstats_in_a_game1[
    'FTA conc Before']).round(1)
select_allstats_in_a_game1['OR conc Before'] = (
        (select_allstats_in_a_game1['opp OR'].cumsum() - select_allstats_in_a_game1['opp OR']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['DR conc Before'] = (
        (select_allstats_in_a_game1['opp DR'].cumsum() - select_allstats_in_a_game1['opp DR']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['TR conc Before'] = (
        (select_allstats_in_a_game1['opp TR'].cumsum() - select_allstats_in_a_game1['opp TR']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['AS conc Before'] = (
        (select_allstats_in_a_game1['opp AS'].cumsum() - select_allstats_in_a_game1['opp AS']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['STL conc Before'] = (
        (select_allstats_in_a_game1['opp STL'].cumsum() - select_allstats_in_a_game1['opp STL']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['TO conc Before'] = (
        (select_allstats_in_a_game1['opp TO'].cumsum() - select_allstats_in_a_game1['opp TO']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1['PF conc Before'] = (
(select_allstats_in_a_game1['opp PF'].cumsum() - select_allstats_in_a_game1['opp PF']) / (
    select_allstats_in_a_game1['index'])).round(1)
select_allstats_in_a_game1 = pd.merge(select_allstats_in_a_game1, dataset_all)
select_allstats_in_a_game1.drop(['index', 'Team'], axis=1, inplace=True)

team_ranking_stat = st.selectbox("Select Stat:", ["All", 'PTS', '2P', '3P', 'FT', 'OR', 'DR',
                                                  'TR', 'AS', 'STL', 'TO', 'BLK', 'PF', 'PIR'], index=0)
if team_ranking_stat == "All":
    interactive_table(select_allstats_in_a_game1.set_index('Against').sort_values('Fixture', ascending=True), paging=False,
                      height=900, width=2000, showIndex=True,
                      classes="display order-column nowrap table_with_monospace_font", searching=False, fixedColumns=True,
                      select=True, info=False, scrollCollapse=True,
    scrollX = True, scrollY = 1000, fixedHeader = True, scroller = True, filter = 'bottom',
    columnDefs = [{"className": "dt-center", "targets": "_all"}])
else:
    regex1 = "Against|Season|Phase|Round|Fixture|HA|results" + "|" + team_ranking_stat
    interactive_table(
    select_allstats_in_a_game1.filter(regex=regex1).set_index('Against').sort_values('Fixture',
                                                                                     ascending=True), paging = False, height = 900, width = 2000, showIndex = True,
    classes = "display order-column nowrap table_with_monospace_font", searching = False, fixedColumns = True, select = True, info = False, scrollCollapse = True,
    scrollX = True, scrollY = 1000, fixedHeader = True, scroller = True, filter = 'bottom',
    columnDefs = [{"className": "dt-center", "targets": "_all"}])
