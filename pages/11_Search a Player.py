
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


st.set_page_config(layout='wide',page_title="Search a Player",page_icon="🏀")
st.sidebar.write("If an error message appears, please refresh the page")
def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)

download_image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh6BYfXG_CbAZa1KEDq4pu2Fxw_OeTLLmFcA&s','eurologo.png')
st.image(Image.open("eurologo.png"),width=100)

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

All_Seasons_res=pd.concat([euroleague_2016_2017_results,euroleague_2017_2018_results,euroleague_2018_2019_results,euroleague_2019_2020_results,euroleague_2020_2021_results,euroleague_2021_2022_results,euroleague_2022_2023_results,euroleague_2023_2024_results,euroleague_2024_2025_results])

search_player_player=st.sidebar.selectbox("Choose a player:",All_Seasons['Player'].reset_index().sort_values('Player')['Player'].unique())
selected_ha_player1 = st.sidebar.selectbox("Home or Away games:",['A', 'H', 'All'],index=2)
selected_season_player1 = st.sidebar.selectbox("Season:",['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021','2021-2022', '2022-2023', '2023-2024','2024-2025','All'],index=9)
selected_phase_player1 = st.sidebar.selectbox("Phase:",['Regular Season', 'Play In','Play offs', 'Final Four','All'],index=4)
selected_wl_player1 = st.sidebar.selectbox("Result:",['W', 'L','All'],index=2)
selected_round_player1 = st.sidebar.selectbox("Round:",['First Round', 'Second Round','PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final', 'All'],index=12)


if "All" in selected_ha_player1:
    selected_ha_player1 = ['A', 'H']
    All_Seasons_filter=All_Seasons.loc[All_Seasons['HA'].isin(selected_ha_player1)]
    select_ha_player1=''
else:
    All_Seasons_filter=All_Seasons.loc[All_Seasons['HA']==selected_ha_player1]
    select_ha_player1 = selected_ha_player1

if "All" in selected_season_player1:
    selected_season_player1 = ['2016-2017', '2017-2018', '2018-2019', '2019-2020','2020-2021','2021-2022', '2022-2023','2023-2024','2024-2025']
    All_Seasons_filter=All_Seasons_filter.loc[All_Seasons_filter['Season'].isin(selected_season_player1)]
    select_season_player1 = ''
else:
    All_Seasons_filter=All_Seasons_filter.loc[All_Seasons_filter['Season']==selected_season_player1]
    select_season_player1 = selected_season_player1

if "All" in selected_wl_player1:
    selected_wl_player1 = ['W', 'L']
    All_Seasons_filter = All_Seasons_filter.loc[All_Seasons_filter['results'].isin(selected_wl_player1)]
    select_wl_player1 = ''
else:
    All_Seasons_filter= All_Seasons_filter.loc[All_Seasons_filter['results'] == selected_wl_player1]
    select_wl_player1 = selected_wl_player1

if "All" in selected_phase_player1:
    selected_phase_player1 = ['Regular Season', 'Play In','Play offs', 'Final Four']
    All_Seasons_filter = All_Seasons_filter.loc[All_Seasons_filter['Phase'].isin(selected_phase_player1)]
    select_phase_player1 = ''
else:
    All_Seasons_filter = All_Seasons_filter.loc[All_Seasons_filter['Phase'] == selected_phase_player1]
    select_phase_player1 = selected_phase_player1

if "All" in selected_round_player1:
    selected_round_player1 = ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final']
    All_Seasons_filter = All_Seasons_filter.loc[All_Seasons_filter['Round'].isin(selected_round_player1)]
    select_round_player1 = ''
else:
    All_Seasons_filter = All_Seasons_filter.loc[All_Seasons_filter['Round'] == selected_round_player1]
    select_round_player1 = selected_round_player1



def null_replace(x):
    if x==' ':
        return 0
    else:
        return x



teams_min_games_played=pd.merge(All_Seasons_filter.loc[All_Seasons_filter['Player']==search_player_player].groupby(["Player",'Team'])['MIN'].mean().round(1).reset_index(),All_Seasons_filter.loc[All_Seasons_filter['Player']==search_player_player][["Player",'Team']].value_counts().reset_index()).rename(columns={'count':'Games'})

computestats=All_Seasons_filter.groupby('Player')[['PTS','MIN','F2M', 'F2A','F3M', 'F3A','FTM', 'FTA','OR', 'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR','Team_PTS','Team_F2M', 'Team_F2A','Team_F3M', 'Team_F3A','Team_FTM', 'Team_FTA','Team_OR', 'Team_DR', 'Team_TR', 'Team_AS', 'Team_ST', 'Team_TO', 'Team_BLK', 'Team_PF','Team_opp_PTS','Team_opp_F2M', 'Team_opp_F2A','Team_opp_F3M', 'Team_opp_F3A','Team_opp_FTM', 'Team_opp_FTA','Team_opp_OR', 'Team_opp_DR', 'Team_opp_TR', 'Team_opp_AS', 'Team_opp_ST', 'Team_opp_TO', 'Team_opp_BLK', 'Team_opp_PF']].mean().round(1).reset_index()


computestats['P2']=100*(computestats['F2M']/computestats['F2A'])
computestats['P2']=computestats['P2'].fillna(0)
computestats['P3']=100*(computestats['F3M']/computestats['F3A'])
computestats['P3']=computestats['P3'].fillna(0)
computestats['PFT']=100*(computestats['FTM']/computestats['FTA'])
computestats['PFT']=computestats['PFT'].fillna(0)
computestats['POS']=0.96*(computestats['F2A']+computestats['F3A']-computestats['OR']+computestats['TO']+0.44*computestats['FTA'])
computestats['ORA']=100*(computestats['PTS']/computestats['POS'])
computestats['ORA']=computestats['ORA'].fillna(0)
computestats['EFG']=100*(computestats['F2M']+1.5*computestats['F3M'])/(computestats['F2A']+computestats['F3A'])
computestats['EFG']=computestats['EFG'].fillna(0)
computestats['TS']=100*(computestats['PTS'])/(2*(computestats['F2A']+computestats['F3A']+0.44*computestats['FTA']))
computestats['TS']=computestats['TS'].fillna(0)
computestats['FTR']=computestats['FTA']/(computestats['F3A']+computestats['F2A'])
computestats['FTR']=computestats['FTR'].fillna(0)
computestats['ASTOR']=computestats['AS']/computestats['TO']
computestats['ASTOR']=computestats['ASTOR'].fillna(0)
computestats['TOR']=100*(computestats['TO']/computestats['POS'])
computestats['TOR']=computestats['TOR'].fillna(0)
computestats['ASR']=100*(computestats['AS']/computestats['POS'])
computestats['ASR']=computestats['ASR'].fillna(0)
computestats['USG'] = 100 * (((computestats['F3A'] + computestats['F2A']) + 0.44 * computestats['FTA'] + computestats['TO']) * (40)) / (computestats['MIN'] * (computestats['Team_F2A'] +computestats['Team_F3A'] + 0.44 * computestats['Team_FTA'] + computestats['Team_TO']))
computestats['USG']=computestats['USG'].fillna(0)
computestats['ORP'] = (100 * computestats['OR']) / (computestats['Team_OR'] + computestats['Team_opp_OR'])
def player_rating_stat_higher(dataset,stat,ascending=True):
    dataset1=dataset[["Player",stat]].sort_values(stat).reset_index()
    dataset1.drop("index",axis=1,inplace=True)
    final_dataset=dataset1.reset_index() >> mutate(Rating=(100*(X.index+1)/X.Player.nunique()),Rating1=(100-(100-X.Rating.round(0))*0.5).round(0))
    final_dataset.rename(columns={'Rating1':'Rating_'+ stat},inplace=True)
    final_dataset.drop(["index","Rating",stat],axis=1,inplace=True)
    return final_dataset

def player_rating_stat_lower(dataset,stat):
    dataset1=dataset[["Player",stat]].sort_values(stat,ascending=False).reset_index()
    dataset1.drop("index",axis=1,inplace=True)
    final_dataset=dataset1.reset_index() >> mutate(Rating=(100*(X.index+1)/X.Player.nunique()),Rating1=(100-(100-X.Rating.round(0))*0.5).round(0))
    final_dataset.rename(columns={'Rating1':'Rating_'+ stat},inplace=True)
    final_dataset.drop(["index","Rating",stat],axis=1,inplace=True)
    return final_dataset


player_rating_stat_higher(computestats,'PTS')

colsplus=['AS', 'F2M', 'F2A', 'F3M', 'F3A', 'FTM',
       'FTA', 'OR', 'DR', 'TR',  'BLK',  'RF', 'ST', 'P2', 'P3', 'PFT','ORA','EFG','TS','FTR','ASTOR','ASR','USG','ORP']


colsminus=[ 'BLKR',
       'PF','TOR' ]

players_ratings1=player_rating_stat_higher(computestats,"PTS")
for i in colsplus:
    df2=player_rating_stat_higher(computestats,i)
    players_ratings1=pd.merge(players_ratings1,df2)

players_ratings2=player_rating_stat_lower(computestats,"TO")
for i in colsminus:
    df3=player_rating_stat_lower(computestats,i)
    players_ratings2=pd.merge(players_ratings2,df3)


players_ratings=pd.merge(players_ratings1,players_ratings2)
computestats=computestats.loc[computestats['Player']==search_player_player]
games=All_Seasons_filter.loc[All_Seasons_filter['Player'] == search_player_player][["Player"]].value_counts().reset_index().rename(columns={'count': 'Games'})
computestats=pd.merge(computestats,games)
teams_min_games_played = All_Seasons_filter.loc[All_Seasons_filter['Player'] == search_player_player][
    ["Season", 'Team']].value_counts().reset_index()[
    ["Season", 'Team']].sort_values('Season')
col1,col2,col3=st.columns([1,1,1])
with col1:
    st.write('### Player: ' + search_player_player)
    st.write('Season: ' + select_season_player1)
    st.write('Phase: ' + select_phase_player1)
    st.write('Round: ' + select_round_player1)
    st.write('Home or away: ' + select_ha_player1)
    st.write('Result: ' + select_wl_player1)
with col2:
    try:
        offense_rating_data = players_ratings.loc[players_ratings['Player'] == search_player_player][
            ['Rating_PTS', 'Rating_AS', 'Rating_TO', 'Rating_OR', 'Rating_BLKR', 'Rating_RF', 'Rating_F2M', 'Rating_F2A',
             'Rating_P2', 'Rating_F3M', 'Rating_F3A', 'Rating_P3',
             'Rating_FTM', 'Rating_FTA', 'Rating_PFT', 'Rating_FTR', 'Rating_EFG', 'Rating_TS', "Rating_ORA",
             'Rating_ASTOR', "Rating_TOR", "Rating_ASR", 'Rating_USG', 'Rating_ORP']].melt()
        offense_ratings = offense_rating_data['value'].mean()

        off = go.Figure(go.Indicator(
            mode="gauge+number",
            value=offense_ratings.round(0),
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 100]},
                   'bordercolor': "gray"},
            title={'text': "Offense"}))

        off.update_layout(
            autosize=False,
            width=250,
            height=180,
            margin=dict(
                l=30,
                r=50,
                b=0,
                t=0,
                pad=0
            ))

        st.write(off)
        defense_ratings = players_ratings.loc[players_ratings['Player'] == search_player_player][
            ['Rating_ST', 'Rating_DR', 'Rating_PF', 'Rating_BLK']].melt()['value'].mean()

        defe = go.Figure(go.Indicator(
            mode="gauge+number",
            value=defense_ratings.round(0),
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 100]},
                   'bordercolor': "gray"},
            title={'text': "Defense"}))

        defe.update_layout(
            autosize=True,
            width=250,
            height=180,
            margin=dict(
                l=30,
                r=50,
                b=0,
                t=0,
                pad=0
            )
        )

        st.write(defe)
        total_ratings = players_ratings.loc[players_ratings['Player'] == search_player_player].melt(id_vars='Player')[
            'value'].mean()

        tot = go.Figure(go.Indicator(
            mode="gauge+number",
            value=total_ratings.round(0),
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 100]},
                   'bordercolor': "gray"},
            title={'text': "Overall"}))

        tot.update_layout(
            autosize=True,
            width=250,
            height=180,
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
        st.error("No data available with these parameters")

with col3:
    try:
        team_min_games = go.Figure(data=go.Table(columnwidth=[1, 1, 1],
                                                     header=dict(
                                                         values=list(teams_min_games_played[['Team', 'Season']].columns),
                                                         align='center', font_size=18, height=30), cells=dict(
                    values=[teams_min_games_played.Team, teams_min_games_played.Season],
                    align='center', font_size=16, height=30)))

        team_min_games.update_layout(
            autosize=True,
            width=400,
            height=200,
            margin=dict(
                l=30,
                r=50,
                b=10,
                t=10,
                pad=10
            ))
        st.write('##### Teams Played')
        st.write(team_min_games)

    except:
        st.error("No data available with these parameters")

basic,shoot,advanced=st.tabs(['Basic Stats','Shooting Stats','Advanced Stats'])
try:
    with basic:
        st.write('### Basic Stats')
        basic_stats=computestats[['Player','Games','MIN','PTS', 'AS', 'TO', 'TR', 'DR', 'OR', 'BLK', 'BLKR', 'ST', 'PF', 'RF', 'PIR']].rename(columns={'PTS':'Points',
                                                                                                                                'AS':'Assists',
                                                                                                                                'TO':'Turnovers',
                                                                                                                                'TR':'Total Rebounds',
                                                                                                                                'OR':'Offensive Rebounds',
                                                                                                                                'DR':'Defensive Rebounds',
                                                                                                                                'BLK':'Blocks',
                                                                                                                                'BLKR':'Blocks Reversed',
                                                                                                                                'ST':'Steals',
                                                                                                                                'PF':'Personal Fouls',
                                                                                                                                'RF':'Fouls Drawn','MIN':'Minutes'})

        interactive_table(basic_stats.set_index('Player'),
                          paging=False, height=600, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])

        basic_player_ratings = players_ratings.loc[players_ratings['Player'] == search_player_player][
            ['Rating_PTS', 'Rating_AS', 'Rating_TO', 'Rating_TR', 'Rating_DR', 'Rating_OR', 'Rating_BLK', 'Rating_BLKR',
             'Rating_ST', 'Rating_PF', 'Rating_RF']].rename(columns={'Rating_PTS': 'Points',
                                                                     'Rating_AS': 'Assists',
                                                                     'Rating_TO': 'Turnovers',
                                                                     'Rating_TR': 'Total<br>Rebounds',
                                                                     'Rating_OR': 'Offensive<br>Rebounds',
                                                                     'Rating_DR': 'Defensive<br>Rebounds',
                                                                     'Rating_BLK': 'Blocks',
                                                                     'Rating_BLKR': 'Blocks<br>Reversed',
                                                                     'Rating_ST': 'Steals',
                                                                     'Rating_PF': 'Personal<br>Fouls',
                                                                     'Rating_RF': 'Fouls<br>Drawn'}).melt()
        basic_player_ratings['variable'] = basic_player_ratings['variable'].str.replace('Rating_', '')
        basic_ratings = go.Figure(go.Barpolar(
            r=basic_player_ratings['value'],
            theta=basic_player_ratings['variable'],
            marker_color='green',
            marker_line_color="black",
            marker_line_width=2,
            opacity=0.8,
            hovertemplate='%{theta} <br>Rating: %{r:.f}<extra></extra>'
        ))

        basic_ratings.update_layout(
            title='Basic Stats Ratings',
            template=None,
            polar=dict(
                radialaxis=dict(range=[0, 100], showticklabels=False, ticks=''),
                angularaxis=dict(showticklabels=True, ticks='')
            ))

        st.write(basic_ratings)

    with shoot:
        st.write('### Shooting Stats')
        shooting_stats=computestats[['Player','F2M', 'F2A', 'P2', 'F3M', 'F3A', 'P3', 'FTM', 'FTA', 'PFT', 'FTR', 'EFG', 'TS']].rename(columns={'F2M':'2P Made',
                                                                                                                                       'F2A':'2P Attempt',
                                                                                                                                       'P2':'2P(%)',
                                                                                                                                       'F3M': '3P Made',
                                                                                                                                       'F3A': '3P Attempt',
                                                                                                                                       'P3': '3P(%)',
                                                                                                                                       'FTM': 'FT Made',
                                                                                                                                       'FTA': 'FT Attempt',
                                                                                                                                       'PFT': 'FT(%)',
                                                                                                                                       'FTR':'FT Ratio',
                                                                                                                                       'EFG':'EFG(%)',
                                                                                                                                       'TS':'TS(%)'}).round(1)
        interactive_table(shooting_stats.set_index('Player'),
                                  paging=False, height=900, width=2000, showIndex=True,
                                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                                  columnDefs=[{"className": "dt-center", "targets": "_all"}])

        shoot_player_ratings = players_ratings.loc[players_ratings['Player'] == search_player_player][
            ['Rating_F2M', 'Rating_F2A', 'Rating_P2', 'Rating_F3M', 'Rating_F3A', 'Rating_P3', 'Rating_FTM', 'Rating_FTA',
             'Rating_PFT', 'Rating_FTR', 'Rating_EFG', 'Rating_TS']].rename(columns={'Rating_F2M': '2P Made',
                                                                                     'Rating_F2A': '2P Attempt',
                                                                                     'Rating_P2': '2P(%)',
                                                                                     'Rating_F3M': '3P Made',
                                                                                     'Rating_F3A': '3P Attempt',
                                                                                     'Rating_P3': '3P(%)',
                                                                                     'Rating_FTM': 'FT Made',
                                                                                     'Rating_FTA': 'FT Attempt',
                                                                                     'Rating_PFT': 'FT(%)',
                                                                                     'Rating_FTR': 'FT Ratio',
                                                                                     'Rating_EFG': 'EFG(%)',
                                                                                     'Rating_TS': 'TS(%)'}).melt()
        shoot_player_ratings['variable'] = shoot_player_ratings['variable'].str.replace('Rating_', '')
        shoot_ratings = go.Figure(go.Barpolar(
            r=shoot_player_ratings['value'],
            theta=shoot_player_ratings['variable'],
            marker_color='green',
            marker_line_color="black",
            marker_line_width=2,
            opacity=0.8,
            hovertemplate='%{theta} <br>Rating: %{r:.f}<extra></extra>'
        ))

        shoot_ratings.update_layout(
            title='Shooting Stats Ratings',
            template=None,
            hovermode="x",
            polar=dict(
                radialaxis=dict(range=[0, 100], showticklabels=False, ticks=''),
                angularaxis=dict(showticklabels=True, ticks='')
            ))

        st.write(shoot_ratings)


    with advanced:
        st.write('### Advanced Stats')
        advanced_stats = computestats[['Player','POS', 'ORA', 'ASTOR', 'TOR', 'ASR', 'USG', 'ORP']].rename(columns={'POS':'Possesions',
                                                                                                           'ORA':'Offensive Rating',
                                                                                                           'ASTOR':'Assists/Turnovers Ratio',
                                                                                                           'TOR':'Turnovers Ratio',
                                                                                                           'ASR':'Assists Ratio',
                                                                                                           'USG':'Usage(%)',
                                                                                                           'ORP':'OR(%)'}).round(1)

        interactive_table(advanced_stats.set_index('Player'),
                                  paging=False, height=900, width=2000, showIndex=True,
                                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                                  columnDefs=[{"className": "dt-center", "targets": "_all"}])

        adv_player_ratings = players_ratings.loc[players_ratings['Player'] == search_player_player][
                [ 'Rating_ORA', 'Rating_ASTOR', 'Rating_TOR', 'Rating_ASR', 'Rating_USG', 'Rating_ORP']].rename(columns={
                                                                                                               'Rating_ORA':'Offensive<br>Rating',
                                                                                                               'Rating_ASTOR':'Assists/Turnovers<br>Ratio',
                                                                                                               'Rating_TOR':'Turnovers<br>Ratio',
                                                                                                               'Rating_ASR':'Assists<br>Ratio',
                                                                                                               'Rating_USG':'Usage(%)',
                                                                                                               'Rating_ORP':'OR(%)'}).melt()
        adv_ratings = go.Figure(go.Barpolar(
            r=adv_player_ratings['value'],
            theta=adv_player_ratings['variable'],
            marker_color='green',
            marker_line_color="black",
            marker_line_width=2,
            opacity=0.8,
            hovertemplate='%{theta} <br>Rating: %{r:.f}<extra></extra>'
        ))

        adv_ratings.update_layout(
            title='Advanced Stats Ratings',
            template=None,
            polar=dict(
                radialaxis=dict(range=[0, 100], showticklabels=False, ticks=''),
                angularaxis=dict(showticklabels=True, ticks='')
            ))

        st.write(adv_ratings)
except:
    st.error("No data available with these parameters")
