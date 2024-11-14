
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

st.set_page_config(layout='wide',page_title="Player Stats",page_icon="🏀")
st.sidebar.write("If an error message appears, please refresh the page")
st.write("## Euroleague stats from 2017 to present")
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



selected_ha_player1 = st.sidebar.selectbox("Home or Away games:",['A', 'H', 'All'],index=2)
selected_season_player1 = st.sidebar.selectbox("Season:",['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021','2021-2022', '2022-2023', '2023-2024','2024-2025','All'],index=8)
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





All_Seasons_filter['Player(Team)']=All_Seasons_filter['Player']+" ("+All_Seasons_filter['Team']+","+All_Seasons_filter['Season']+" vs "+All_Seasons_filter['Against']+")"
All_Seasons_filter.rename(columns={'PTS':'Points','F2M':'2P Made','F3M':'3P Made','F2A':'2P Attempt',"F2GP":"2P%",'F3A':'3P Attempt',"F3GP":"3P%",'FTM':'FT Made', 'FTA':'FT Attempt',"FTP":"FT%",'OR':'Offensive Rebounds', 'DR':'Defensive Rebounds',
                                   'TR':'Total Rebounds', 'AS':'Assists', 'ST':'Steals', 'TO':"Turnovers", 'BLK':"Blocks Made", 'BLKR':'Blocks Reversed', 'PF':'Personal Fouls', 'RF':'Fouls Drawn'},inplace=True)
All_Seasons.rename(columns={'PTS':'Points','F2M':'2P Made','F3M':'3P Made','F2A':'2P Attempt','F3A':'3P Attempt','FTM':'FT Made', 'FTA':'FT Attempt','OR':'Offensive Rebounds', 'DR':'Defensive Rebounds',
                                   'TR':'Total Rebounds', 'AS':'Assists', 'ST':'Steals', 'TO':"Turnovers", 'BLK':"Blocks Made", 'BLKR':'Blocks Reversed', 'PF':'Personal Fouls', 'RF':'Fouls Drawn'},inplace=True)
All_Seasons_filter_sel=All_Seasons_filter[["Player(Team)",'Points','MIN','2P Made', '2P Attempt','3P Made', '3P Attempt','FT Made', 'FT Attempt','Offensive Rebounds', 'Defensive Rebounds', 'Total Rebounds',
                                                                'Assists', 'Steals', 'Turnovers', 'Blocks Made', 'Blocks Reversed', 'Personal Fouls', 'Fouls Drawn',"PIR",'2P%','3P%','FT%']]
All_Seasons_filter_sel['2P Made(%)']=All_Seasons_filter_sel['2P Made'].astype(str)+" ("+All_Seasons_filter_sel['2P%'].round(1).astype(str)+"%)"
All_Seasons_filter_sel['2P Attempt(%)']=All_Seasons_filter_sel['2P Attempt'].astype(str)+" ("+All_Seasons_filter_sel['2P%'].round(1).astype(str)+"%)"
All_Seasons_filter_sel['3P Made(%)']=All_Seasons_filter_sel['3P Made'].astype(str)+" ("+All_Seasons_filter_sel['3P%'].round(1).astype(str)+"%)"
All_Seasons_filter_sel['3P Attempt(%)']=All_Seasons_filter_sel['3P Attempt'].astype(str)+" ("+All_Seasons_filter_sel['3P%'].round(1).astype(str)+"%)"
All_Seasons_filter_sel['FT Made(%)']=All_Seasons_filter_sel['FT Made'].astype(str)+" ("+All_Seasons_filter_sel['FT%'].round(1).astype(str)+"%)"
All_Seasons_filter_sel['FT Attempt(%)']=All_Seasons_filter_sel['FT Attempt'].astype(str)+" ("+All_Seasons_filter_sel['FT%'].round(1).astype(str)+"%)"
compute_player_mean_stats=All_Seasons_filter.groupby('Player')[['Points','MIN','2P Made', '2P Attempt','3P Made', '3P Attempt','FT Made', 'FT Attempt','Offensive Rebounds', 'Defensive Rebounds', 'Total Rebounds',
                                                                'Assists', 'Steals', 'Turnovers', 'Blocks Made', 'Blocks Reversed', 'Personal Fouls', 'Fouls Drawn', 'PIR','Team_PTS','Team_F2M', 'Team_F2A','Team_F3M', 'Team_F3A','Team_FTM', 'Team_FTA','Team_OR', 'Team_DR', 'Team_TR', 'Team_AS', 'Team_ST', 'Team_TO', 'Team_BLK', 'Team_PF','Team_opp_PTS','Team_opp_F2M', 'Team_opp_F2A','Team_opp_F3M', 'Team_opp_F3A','Team_opp_FTM', 'Team_opp_FTA','Team_opp_OR', 'Team_opp_DR', 'Team_opp_TR', 'Team_opp_AS', 'Team_opp_ST', 'Team_opp_TO', 'Team_opp_BLK', 'Team_opp_PF' ]].mean().reset_index().round(1)
compute_player_mean_stats['2P%']=100*(compute_player_mean_stats['2P Made']/compute_player_mean_stats['2P Attempt'])
compute_player_mean_stats['2P Made(%)']=compute_player_mean_stats['2P Made'].astype(str)+" ("+compute_player_mean_stats['2P%'].round(1).astype(str)+"%)"
compute_player_mean_stats['2P Attempt(%)']=compute_player_mean_stats['2P Attempt'].astype(str)+" ("+compute_player_mean_stats['2P%'].round(1).astype(str)+"%)"
compute_player_mean_stats['3P%']=100*(compute_player_mean_stats['3P Made']/compute_player_mean_stats['3P Attempt'])
compute_player_mean_stats['3P Made(%)']=compute_player_mean_stats['3P Made'].astype(str)+" ("+compute_player_mean_stats['3P%'].round(1).astype(str)+"%)"
compute_player_mean_stats['3P Attempt(%)']=compute_player_mean_stats['3P Attempt'].astype(str)+" ("+compute_player_mean_stats['3P%'].round(1).astype(str)+"%)"
compute_player_mean_stats['FT%']=100*(compute_player_mean_stats['FT Made']/compute_player_mean_stats['FT Attempt'])
compute_player_mean_stats['FT Made(%)']=compute_player_mean_stats['FT Made'].astype(str)+" ("+compute_player_mean_stats['FT%'].round(1).astype(str)+"%)"
compute_player_mean_stats['FT Attempt(%)']=compute_player_mean_stats['FT Attempt'].astype(str)+" ("+compute_player_mean_stats['FT%'].round(1).astype(str)+"%)"
compute_player_mean_stats['Possesions']=0.96*(compute_player_mean_stats['2P Attempt']+compute_player_mean_stats['3P Attempt']+compute_player_mean_stats['Offensive Rebounds']+compute_player_mean_stats['Turnovers']+0.44*compute_player_mean_stats['FT Attempt'])
compute_player_mean_stats['Offensive Rating']=100*(compute_player_mean_stats['Points']/compute_player_mean_stats['Possesions'])
compute_player_mean_stats['EFG%']=100*(compute_player_mean_stats['2P Made']+1.5*compute_player_mean_stats['3P Made'])/(compute_player_mean_stats['2P Attempt']+compute_player_mean_stats['3P Attempt'])
compute_player_mean_stats['TS%']=100*(compute_player_mean_stats['Points'])/(2*(compute_player_mean_stats['2P Attempt']+compute_player_mean_stats['3P Attempt']+0.44*compute_player_mean_stats['FT Attempt']))
compute_player_mean_stats['FT Ratio']=compute_player_mean_stats['FT Attempt']/(compute_player_mean_stats['3P Attempt']+compute_player_mean_stats['2P Attempt'])
compute_player_mean_stats['AS-TO ratio']=compute_player_mean_stats['Assists']/compute_player_mean_stats['Turnovers']
compute_player_mean_stats['TO Ratio']=100*(compute_player_mean_stats['Turnovers']/compute_player_mean_stats['Possesions'])
compute_player_mean_stats['AS Ratio']=100*(compute_player_mean_stats['Assists']/compute_player_mean_stats['Possesions'])
compute_player_mean_stats['USG%'] = 100 * (((compute_player_mean_stats['3P Attempt'] + compute_player_mean_stats['2P Attempt']) + 0.44 * compute_player_mean_stats['FT Attempt'] + compute_player_mean_stats['Turnovers']) * (40)) / (compute_player_mean_stats['MIN'] * (compute_player_mean_stats['Team_F2A'] +compute_player_mean_stats['Team_F3A'] + 0.44 * compute_player_mean_stats['Team_FTA'] + compute_player_mean_stats['Team_TO']))
compute_player_mean_stats['OR%'] = (100 * compute_player_mean_stats['Offensive Rebounds']) / (compute_player_mean_stats['Team_OR'] + compute_player_mean_stats['Team_opp_OR'])
compute_player_total_stats=All_Seasons_filter.groupby('Player')[['Points','MIN','2P Made', '2P Attempt','3P Made', '3P Attempt','FT Made', 'FT Attempt','Offensive Rebounds', 'Defensive Rebounds', 'Total Rebounds',
                                                                'Assists', 'Steals', 'Turnovers', 'Blocks Made', 'Blocks Reversed', 'Personal Fouls', 'Fouls Drawn', 'PIR',
                                                                 'Team_PTS','Team_F2M', 'Team_F2A','Team_F3M', 'Team_F3A','Team_FTM', 'Team_FTA','Team_OR', 'Team_DR', 'Team_TR', 'Team_AS', 'Team_ST', 'Team_TO', 'Team_BLK', 'Team_PF','Team_opp_PTS',
                                                                 'Team_opp_F2M', 'Team_opp_F2A','Team_opp_F3M', 'Team_opp_F3A','Team_opp_FTM', 'Team_opp_FTA','Team_opp_OR', 'Team_opp_DR', 'Team_opp_TR', 'Team_opp_AS', 'Team_opp_ST', 'Team_opp_TO',
                                                                 'Team_opp_BLK', 'Team_opp_PF']].sum().reset_index()
compute_player_total_stats['2P%']=100*(compute_player_total_stats['2P Made']/compute_player_total_stats['2P Attempt'])
compute_player_total_stats['2P Made(%)']=compute_player_total_stats['2P Made'].astype(str)+" ("+compute_player_total_stats['2P%'].round(1).astype(str)+"%)"
compute_player_total_stats['2P Attempt(%)']=compute_player_total_stats['2P Attempt'].astype(str)+" ("+compute_player_total_stats['2P%'].round(1).astype(str)+"%)"
compute_player_total_stats['3P%']=100*(compute_player_total_stats['3P Made']/compute_player_total_stats['3P Attempt'])
compute_player_total_stats['3P Made(%)']=compute_player_total_stats['3P Made'].astype(str)+" ("+compute_player_total_stats['3P%'].round(1).astype(str)+"%)"
compute_player_total_stats['3P Attempt(%)']=compute_player_total_stats['3P Attempt'].astype(str)+" ("+compute_player_total_stats['3P%'].round(1).astype(str)+"%)"
compute_player_total_stats['FT%']=100*(compute_player_total_stats['FT Made']/compute_player_total_stats['FT Attempt'])
compute_player_total_stats['FT Made(%)']=compute_player_total_stats['FT Made'].astype(str)+" ("+compute_player_total_stats['FT%'].round(1).astype(str)+"%)"
compute_player_total_stats['FT Attempt(%)']=compute_player_total_stats['FT Attempt'].astype(str)+" ("+compute_player_total_stats['FT%'].round(1).astype(str)+"%)"
compute_player_total_stats['Possesions']=0.96*(compute_player_total_stats['2P Attempt']+compute_player_total_stats['3P Attempt']-compute_player_total_stats['Offensive Rebounds']+compute_player_total_stats['Turnovers']+0.44*compute_player_total_stats['FT Attempt'])
compute_player_total_stats['Offensive Rating']=100*(compute_player_total_stats['Points']/compute_player_total_stats['Possesions'])
compute_player_total_stats['EFG%']=100*(compute_player_total_stats['2P Made']+1.5*compute_player_total_stats['3P Made'])/(compute_player_total_stats['2P Attempt']+compute_player_total_stats['3P Attempt'])
compute_player_total_stats['TS%']=100*(compute_player_total_stats['Points'])/(2*(compute_player_total_stats['2P Attempt']+compute_player_total_stats['3P Attempt']+0.44*compute_player_total_stats['FT Attempt']))
compute_player_total_stats['FT Ratio']=compute_player_total_stats['FT Attempt']/(compute_player_total_stats['3P Attempt']+compute_player_total_stats['2P Attempt'])
compute_player_total_stats['AS-TO ratio']=compute_player_total_stats['Assists']/compute_player_total_stats['Turnovers']
compute_player_total_stats['TO Ratio']=100*(compute_player_total_stats['Turnovers']/compute_player_total_stats['Possesions'])
compute_player_total_stats['AS Ratio']=100*(compute_player_total_stats['Assists']/compute_player_total_stats['Possesions'])
compute_player_total_stats['USG(%)'] = 100 * (((compute_player_total_stats['3P Attempt'] + compute_player_total_stats['2P Attempt']) + 0.44 * compute_player_total_stats['FT Attempt'] + compute_player_total_stats['Turnovers']) * (40)) / (compute_player_total_stats['MIN'] * (compute_player_total_stats['Team_F2A'] +compute_player_total_stats['Team_F3A'] + 0.44 * compute_player_total_stats['Team_FTA'] + compute_player_total_stats['Team_TO']))
compute_player_total_stats['ΟR(%)'] = (100 * compute_player_total_stats['Offensive Rebounds']) / (compute_player_total_stats['Team_OR'] + compute_player_total_stats['Team_opp_OR'])




compute_player_games=All_Seasons_filter['Player'].value_counts().reset_index()
compute_player_games=compute_player_games.rename(columns={'count':'Games'})

compute_player_mean_stats=pd.merge(compute_player_games,compute_player_mean_stats)
compute_player_total_stats=pd.merge(compute_player_games,compute_player_total_stats)


compute_player_mean_stats_season=All_Seasons.groupby(['Player','Season'])[['Points','MIN','2P Made', '2P Attempt','3P Made', '3P Attempt','FT Made', 'FT Attempt','Offensive Rebounds', 'Defensive Rebounds', 'Total Rebounds',
                                                                'Assists', 'Steals', 'Turnovers', 'Blocks Made', 'Blocks Reversed', 'Personal Fouls', 'Fouls Drawn', 'PIR','Team_PTS','Team_F2M', 'Team_F2A','Team_F3M', 'Team_F3A','Team_FTM', 'Team_FTA','Team_OR', 'Team_DR', 'Team_TR', 'Team_AS', 'Team_ST', 'Team_TO', 'Team_BLK', 'Team_PF','Team_opp_PTS','Team_opp_F2M', 'Team_opp_F2A','Team_opp_F3M', 'Team_opp_F3A','Team_opp_FTM', 'Team_opp_FTA','Team_opp_OR', 'Team_opp_DR', 'Team_opp_TR', 'Team_opp_AS', 'Team_opp_ST', 'Team_opp_TO', 'Team_opp_BLK', 'Team_opp_PF' ]].mean().reset_index().round(1)
compute_player_mean_stats_season['2P%']=100*(compute_player_mean_stats_season['2P Made']/compute_player_mean_stats_season['2P Attempt'])
compute_player_mean_stats_season['2P Made(%)']=compute_player_mean_stats_season['2P Made'].astype(str)+" ("+compute_player_mean_stats_season['2P%'].round(1).astype(str)+"%)"
compute_player_mean_stats_season['2P Attempt(%)']=compute_player_mean_stats_season['2P Attempt'].astype(str)+" ("+compute_player_mean_stats_season['2P%'].round(1).astype(str)+"%)"
compute_player_mean_stats_season['3P%']=100*(compute_player_mean_stats_season['3P Made']/compute_player_mean_stats_season['3P Attempt'])
compute_player_mean_stats_season['3P Made(%)']=compute_player_mean_stats_season['3P Made'].astype(str)+" ("+compute_player_mean_stats_season['3P%'].round(1).astype(str)+"%)"
compute_player_mean_stats_season['3P Attempt(%)']=compute_player_mean_stats_season['3P Attempt'].astype(str)+" ("+compute_player_mean_stats_season['3P%'].round(1).astype(str)+"%)"
compute_player_mean_stats_season['FT%']=100*(compute_player_mean_stats_season['FT Made']/compute_player_mean_stats_season['FT Attempt'])
compute_player_mean_stats_season['FT Made(%)']=compute_player_mean_stats_season['FT Made'].astype(str)+" ("+compute_player_mean_stats_season['FT%'].round(1).astype(str)+"%)"
compute_player_mean_stats_season['FT Attempt(%)']=compute_player_mean_stats_season['FT Attempt'].astype(str)+" ("+compute_player_mean_stats_season['FT%'].round(1).astype(str)+"%)"
compute_player_mean_stats_season['Possesions']=0.96*(compute_player_mean_stats_season['2P Attempt']+compute_player_mean_stats_season['3P Attempt']-compute_player_mean_stats_season['Offensive Rebounds']+compute_player_mean_stats_season['Turnovers']+0.44*compute_player_mean_stats_season['FT Attempt'])
compute_player_mean_stats_season['Offensive Rating']=100*(compute_player_mean_stats_season['Points']/compute_player_mean_stats_season['Possesions'])
compute_player_mean_stats_season['EFG%']=100*(compute_player_mean_stats_season['2P Made']+1.5*compute_player_mean_stats_season['3P Made'])/(compute_player_mean_stats_season['2P Attempt']+compute_player_mean_stats_season['3P Attempt'])
compute_player_mean_stats_season['TS%']=100*(compute_player_mean_stats_season['Points'])/(2*(compute_player_mean_stats_season['2P Attempt']+compute_player_mean_stats_season['3P Attempt']+0.44*compute_player_mean_stats_season['FT Attempt']))
compute_player_mean_stats_season['FT Ratio']=compute_player_mean_stats_season['FT Attempt']/(compute_player_mean_stats_season['3P Attempt']+compute_player_mean_stats_season['2P Attempt'])
compute_player_mean_stats_season['AS-TO ratio']=compute_player_mean_stats_season['Assists']/compute_player_mean_stats_season['Turnovers']
compute_player_mean_stats_season['TO Ratio']=100*(compute_player_mean_stats_season['Turnovers']/compute_player_mean_stats_season['Possesions'])
compute_player_mean_stats_season['AS Ratio']=100*(compute_player_mean_stats_season['Assists']/compute_player_mean_stats_season['Possesions'])
compute_player_mean_stats_season['USG%'] = 100 * (((compute_player_mean_stats_season['3P Attempt'] + compute_player_mean_stats_season['2P Attempt']) + 0.44 * compute_player_mean_stats_season['FT Attempt'] + compute_player_mean_stats_season['Turnovers']) * (40)) / (compute_player_mean_stats_season['MIN'] * (compute_player_mean_stats_season['Team_F2A'] +compute_player_mean_stats_season['Team_F3A'] + 0.44 * compute_player_mean_stats_season['Team_FTA'] + compute_player_mean_stats_season['Team_TO']))
compute_player_mean_stats_season['OR%'] = (100 * compute_player_mean_stats_season['Offensive Rebounds']) / (compute_player_mean_stats_season['Team_OR'] + compute_player_mean_stats['Team_opp_OR'])


compute_player_games_season=All_Seasons[['Player','Season']].value_counts().reset_index()
compute_player_games_season=compute_player_games_season.rename(columns={'count':'Games'})
compute_player_mean_stats_season=pd.merge(compute_player_mean_stats_season,compute_player_games_season,on=['Player','Season'])
compute_player_mean_stats_season['Player']=compute_player_mean_stats_season['Player']+" ("+compute_player_mean_stats_season['Season']+")"
compute_player_total_stats_season=All_Seasons_filter.groupby(['Player','Season'])[['Points','MIN','2P Made', '2P Attempt','3P Made', '3P Attempt','FT Made', 'FT Attempt','Offensive Rebounds', 'Defensive Rebounds', 'Total Rebounds',
                                                                'Assists', 'Steals', 'Turnovers', 'Blocks Made', 'Blocks Reversed', 'Personal Fouls', 'Fouls Drawn', 'PIR']].sum().reset_index()

compute_player_total_stats_season=(compute_player_total_stats_season.add_prefix('Total_')).rename(columns={'Total_Player':'Player','Total_Season':'Season'})
compute_player_total_stats_season=pd.merge(compute_player_total_stats_season,compute_player_games_season,on=['Player','Season'])
compute_player_mean_stats_season=compute_player_mean_stats_season.loc[compute_player_mean_stats_season['Games']>15]
games = st.sidebar.slider("Pick Number of games", 0, 200,value=0)



basic, shooting, advanced = st.tabs(['Basic Stats', 'Shooting Stats', 'Advanced Stats'])
with basic:
    basicstatselect = st.selectbox('Stat:',
        ['Points', "Assists", "Total Rebounds", "Offensive Rebounds", 'Defensive Rebounds', "Steals", 'Turnovers', 'Blocks Made', 'Blocks Reversed',
         'Personal Fouls', "Fouls Drawn",'PIR'])
    regex1 = 'Player|' + basicstatselect
    av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best on Season'])
    with av:
        st.write("##### Average "+basicstatselect+ " per game in Euroleague (Top 10)")
        st.write('(For better results move the Games slider)')

        av=compute_player_mean_stats.loc[compute_player_mean_stats['Games'] > games].filter(regex=regex1).sort_values(basicstatselect,
                                                                                                       ascending=False).head(
            10).round(1).reset_index()
        av.drop("index",axis=1,inplace=True)
        av=av.reset_index()
        av['No.']=av['index']+1
        av.drop('index',axis=1,inplace=True)
        interactive_table(av.set_index('No.'),
                          paging=False, height=1200, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])

    with sum:

        st.write("##### Total "+ basicstatselect+" in Euroleague (Top 10)")
        tot =compute_player_total_stats.filter(regex=regex1).sort_values(basicstatselect, ascending=False).head(10).round(
                1).reset_index()
        tot.drop("index", axis=1, inplace=True)
        tot = tot.reset_index()
        tot['No.'] = tot['index'] + 1
        tot.drop('index', axis=1, inplace=True)
        interactive_table(tot.set_index('No.'),
                          paging=False, height=1200, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with rec:
        st.write("##### Record "+basicstatselect+" on a game in Euroleague (Top 10)")
        rec =All_Seasons_filter_sel.filter(regex=regex1).sort_values(basicstatselect, ascending=False).head(10).round(
            1).reset_index()
        rec.drop("index", axis=1, inplace=True)
        rec = rec.reset_index()
        rec['No.'] = rec['index'] + 1
        rec.drop('index', axis=1, inplace=True)
        interactive_table(rec.set_index('No.'),
                          paging=False, height=1200, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
             st.write("##### Best by Season on "+ basicstatselect+" in Euroleague (Top 10 - played at least 15 games in the season)")
             bs = compute_player_mean_stats_season.filter(regex=regex1).sort_values(basicstatselect, ascending=False).head(10).round(
                1).reset_index()
             bs.drop("index", axis=1, inplace=True)
             bs = bs.reset_index()
             bs['No.'] = bs['index'] + 1
             bs.drop('index', axis=1, inplace=True)
             interactive_table(bs.set_index('No.'),
                               paging=False, height=1200, width=2000, showIndex=True,
                               classes="display order-column nowrap table_with_monospace_font", searching=True,
                               fixedColumns=True, select=True, info=False, scrollCollapse=True,
                               scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                               columnDefs=[{"className": "dt-center", "targets": "_all"}])

with shooting:
    shootstatselect=st.selectbox('Stat:',['2P Made',"2P Attempt",'3P Made',"3P Attempt",'FT Made',"FT Attempt"])
    regex1 = 'Player|' + shootstatselect

    av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
    with av:
        st.write("##### Average "+ shootstatselect+" per game in Euroleague (Top 10)")
        st.write('(For better results move the Games slider)')

        av_shoot = compute_player_mean_stats.loc[compute_player_mean_stats['Games'] > games].filter(regex=regex1).sort_values(shootstatselect,ascending=False).head(10).round(1).reset_index()
        av_shoot.drop(["index",shootstatselect], axis=1, inplace=True)
        av_shoot = av_shoot.reset_index()
        av_shoot['No.'] = av_shoot['index'] + 1
        av_shoot.drop('index', axis=1, inplace=True)
        interactive_table(av_shoot.set_index('No.'),
                          paging=False, height=1200, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with sum:
        st.write("##### Total "+ shootstatselect +" in Euroleague (Top 10)")
        tot_shoot = compute_player_total_stats.filter(regex=regex1).sort_values(shootstatselect,ascending=False).head(10).round(1).reset_index()
        tot_shoot.drop(["index",shootstatselect], axis=1, inplace=True)
        tot_shoot = tot_shoot.reset_index()
        tot_shoot['No.'] = tot_shoot['index'] + 1
        tot_shoot.drop('index', axis=1, inplace=True)
        interactive_table(tot_shoot.set_index('No.'),
                          paging=False, height=1200, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with rec:
        st.write("##### Record "+shootstatselect+" on a game in Euroleague (Top 10)")
        rec_shoot =All_Seasons_filter_sel.filter(regex=regex1).sort_values(shootstatselect,ascending=False).head(10).round(1).reset_index()
        rec_shoot.drop(["index",shootstatselect], axis=1, inplace=True)
        rec_shoot = rec_shoot.reset_index()
        rec_shoot['No.'] = rec_shoot['index'] + 1
        rec_shoot.drop('index', axis=1, inplace=True)
        interactive_table(rec_shoot.set_index('No.'),
                          paging=False, height=1200, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with bs:
        st.write("##### Best by Season on "+ shootstatselect+" in Euroleague (Top 10 - played at least 15 games in the season)")
        bs_shoot = compute_player_mean_stats_season.filter(regex=regex1).sort_values(shootstatselect,ascending=False).head(10).round(1).reset_index()
        bs_shoot.drop(["index",shootstatselect], axis=1, inplace=True)
        bs_shoot = bs_shoot.reset_index()
        bs_shoot['No.'] = bs_shoot['index'] + 1
        bs_shoot.drop('index', axis=1, inplace=True)
        interactive_table(bs_shoot.set_index('No.'),
                          paging=False, height=1200, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])

with advanced:
    advancedstatselect = st.selectbox("Stat:",
        ['Possesions', "Offensive Rating", "EFG%", 'TS%', "FT Ratio", "AS-TO ratio", 'TO Ratio',
         "AS Ratio", "USG%",'OR%'])
    regex1 = 'Player|' + advancedstatselect
    av, bs = st.tabs(['Average Stats', 'Best by Season'])
    with av:
        st.write("##### Average possesions per game in Euroleague (Top 10)")
        av_adv = compute_player_mean_stats.loc[(compute_player_mean_stats['Games'] > games)&(compute_player_mean_stats[advancedstatselect]<100)].filter(regex=regex1).sort_values(advancedstatselect,ascending=False).head(10).round(1).reset_index()
        av_adv.drop("index", axis=1, inplace=True)
        av_adv = av_adv.reset_index()
        av_adv['No.'] = av_adv['index'] + 1
        av_adv.drop('index', axis=1, inplace=True)
        interactive_table(av_adv.set_index('No.'),
                          paging=False, height=1200, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with bs:
        st.write(
            "##### Best by Season on average possesions per game in Euroleague (Top 10 - played at least 15 games in the season)")
        bs_adv = compute_player_mean_stats_season.loc[compute_player_mean_stats_season[advancedstatselect]<100].filter(regex=regex1).sort_values(advancedstatselect,ascending=False).head(10).round(1).reset_index()
        bs_adv.drop("index", axis=1, inplace=True)
        bs_adv = bs_adv.reset_index()
        bs_adv['No.'] = bs_adv['index'] + 1
        bs_adv.drop('index', axis=1, inplace=True)
        interactive_table(bs_adv.set_index('No.'),
                          paging=False, height=1200, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=True,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])
