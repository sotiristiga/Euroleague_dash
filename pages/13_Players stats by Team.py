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


st.set_page_config(layout='wide',page_title="Players stats by Team",page_icon="🏀")
st.sidebar.write("If an error message appears, please refresh the page")
def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)

download_image('https://raw.githubusercontent.com/sotiristiga/Euroleague_dash/refs/heads/main/eurologo.png','eurologo.png')
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

def ha_against_format(HA):
    if HA == "A":
        return "H"
    elif HA=="H":
        return "A"
    
def result_against_format(results):
    if results == "W":
        return "L"
    elif results=="L":
        return "W"

lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'

def metrics_customize(red,green,blue,iconname,sline,i):

    htmlstr = f"""<p style='background-color: rgb({red},{green},{blue}, 0.75); 
                        color: rgb(0,0,0, 0.75); 
                        font-size: 20px; 
                        border-radius: 120px; 
                        padding-left: 20px; 
                        padding-top: 0px; 
                        padding-bottom: 50px; 
                        line-height:60px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 30px; 
                        margin-top: 0;'>{sline}</style></span></p>"""
    return htmlstr
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
All_Seasons["HA1"]=All_Seasons['HA'].apply(ha_against_format)
All_Seasons["Result1"]=All_Seasons['results'].apply(result_against_format)
player_stats_by_team_team=st.sidebar.selectbox("Choose Team:",All_Seasons['Team'].reset_index().sort_values('Team')['Team'].unique())
player_stats_by_team_ha = st.sidebar.selectbox("Home or Away games:",['A', 'H', 'All'],index=2)
player_stats_by_team_season = st.sidebar.selectbox("Season:",['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021','2021-2022', '2022-2023', '2023-2024','2024-2025','All'],index=8)
player_stats_by_team_phase = st.sidebar.selectbox("Phase:",['Regular Season', 'Play In','Play offs', 'Final Four','All'],index=4)
player_stats_by_team_wl = st.sidebar.selectbox("Result:",['W', 'L','All'],index=2)
player_stats_by_team_round = st.sidebar.selectbox("Round:",['First Round', 'Second Round','PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final', 'All'],index=12)



if "All" in player_stats_by_team_ha:
    player_stats_by_team_ha = ['A', 'H']
    All_Seasons1=All_Seasons.loc[All_Seasons['HA'].isin(player_stats_by_team_ha)]
    select_ha_player1=''
else:
    All_Seasons1=All_Seasons.loc[All_Seasons['HA']==player_stats_by_team_ha]
    select_ha_player1 = player_stats_by_team_ha

if "All" in player_stats_by_team_season:
    player_stats_by_team_season = ['2016-2017', '2017-2018', '2018-2019', '2019-2020','2020-2021','2021-2022', '2022-2023','2023-2024','2024-2025']
    All_Seasons1=All_Seasons1.loc[All_Seasons1['Season'].isin(player_stats_by_team_season)]
    select_season_player1 = ''
else:
    All_Seasons1=All_Seasons1.loc[All_Seasons1['Season']==player_stats_by_team_season]
    select_season_player1 = player_stats_by_team_season

if "All" in player_stats_by_team_wl:
    player_stats_by_team_wl = ['W', 'L']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['results'].isin(player_stats_by_team_wl)]
    select_wl_player1 = ''
else:
    All_Seasons1= All_Seasons1.loc[All_Seasons1['results'] == player_stats_by_team_wl]
    select_wl_player1 = player_stats_by_team_wl

if "All" in player_stats_by_team_phase:
    player_stats_by_team_phase = ['Regular Season', 'Play In','Play offs', 'Final Four']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Phase'].isin(player_stats_by_team_phase)]
    select_phase_player1 = ''
else:
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Phase'] == player_stats_by_team_phase]
    select_phase_player1 = player_stats_by_team_phase

if "All" in player_stats_by_team_round:
    player_stats_by_team_round = ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Round'].isin(player_stats_by_team_round)]
    select_round_player1 = ''
else:
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Round'] == player_stats_by_team_round]
    select_round_player1 = player_stats_by_team_round

def compute_player_stats_by_team(dataset,Team):
    computestats=dataset.groupby(['Player','Team'])[['PTS','MIN','F2M', 'F2A','F3M', 'F3A','FTM', 'FTA','OR', 'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR','Team_PTS','Team_F2M', 'Team_F2A','Team_F3M', 'Team_F3A','Team_FTM', 'Team_FTA','Team_OR', 'Team_DR', 'Team_TR', 'Team_AS', 'Team_ST', 'Team_TO', 'Team_BLK', 'Team_PF','Team_opp_PTS','Team_opp_F2M', 'Team_opp_F2A','Team_opp_F3M', 'Team_opp_F3A','Team_opp_FTM', 'Team_opp_FTA','Team_opp_OR', 'Team_opp_DR', 'Team_opp_TR', 'Team_opp_AS', 'Team_opp_ST', 'Team_opp_TO', 'Team_opp_BLK', 'Team_opp_PF']].mean().round(1).reset_index()
    computestats['P2']=100*(computestats['F2M']/computestats['F2A'])
    computestats['P3']=100*(computestats['F3M']/computestats['F3A'])
    computestats['PFT']=100*(computestats['FTM']/computestats['FTA'])
    computestats['POS']=0.96*(computestats['F2A']+computestats['F3A']-computestats['OR']+computestats['TO']+0.44*computestats['FTA'])
    computestats['ORA']=100*(computestats['PTS']/computestats['POS'])
    computestats['EFG']=100*(computestats['F2M']+1.5*computestats['F3M'])/(computestats['F2A']+computestats['F3A'])
    computestats['TS']=100*(computestats['PTS'])/(2*(computestats['F2A']+computestats['F3A']+0.44*computestats['FTA']))
    computestats['FTR']=computestats['FTA']/(computestats['F3A']+computestats['F2A'])
    computestats['ASTOR']=computestats['AS']/computestats['TO']
    computestats['TOR']=100*(computestats['TO']/computestats['POS'])
    computestats['ASR']=100*(computestats['AS']/computestats['POS'])
    computestats['USG'] = 100 * (((computestats['F3A'] + computestats['F2A']) + 0.44 * computestats['FTA'] + computestats['TO']) * (40)) / (computestats['MIN'] * (computestats['Team_F2A'] +computestats['Team_F3A'] + 0.44 * computestats['Team_FTA'] + computestats['Team_TO']))
    computestats['ORP'] = (100 * computestats['OR']) / (computestats['Team_OR'] + computestats['Team_opp_OR'])

    computestatsfinal = computestats.loc[computestats['Team'] == Team]
    computestatsfinal.drop('Team',axis=1,inplace=True)
    computestatsfinal=computestatsfinal.set_index('Player').round(1)
    computestatsfinal=computestatsfinal[['PTS', 'MIN', 'F2M', 'F2A','P2', 'F3M', 'F3A', 'P3','FTM', 'FTA', 'PFT','OR',
                                         'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR','POS','ORA','EFG','TS','FTR','ASTOR','TOR','ASR','USG','ORP']]
    return computestatsfinal


interactive_table(compute_player_stats_by_team(All_Seasons1,player_stats_by_team_team),
                      paging=False,height=960,width=20000,showIndex=True,classes="display order-column nowrap table_with_monospace_font",searching=False,fixedColumns=True,select=True,info=False,scrollCollapse=True,
        scrollX=True,scrollY=1000,fixedHeader=True,scroller=True,columnDefs=[{"className": "dt-center", "targets": "_all"}])
