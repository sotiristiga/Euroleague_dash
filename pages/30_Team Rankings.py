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


st.set_page_config(layout='wide',page_title="Team Rankings",page_icon="🏀")
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

def games_format(HA,Fixture,Season,Team,Against):
    if HA == "H":
        return Fixture + " / " +Season + ' / ' + Team + ' - ' + Against
    elif HA == "A":
        return Fixture + " / " + Season + ' / ' + Against + ' - ' + Team


def result_format(Win):
    if Win == 1:
        return "W"
    elif Win == 0:
        return "L"

def period_win_format(S,C):
    if S>C:
        return 1
    else:
        return 0

def result_format(Win):
    if Win == 1:
        return "W"
    elif Win == 0:
        return "L"

def period_win_res_win_format(S,C,result):
    if S>C and result=="W":
        return 1
    else:
        return 0

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
period_points['Q1W']=period_points.apply(lambda x: period_win_format(x['Q1S'],x['Q1C']),axis=1)
period_points['Q2W']=period_points.apply(lambda x: period_win_format(x['Q2S'],x['Q2C']),axis=1)
period_points['FHW']=period_points.apply(lambda x: period_win_format(x['FHS'],x['FHC']),axis=1)
period_points['Q3W']=period_points.apply(lambda x: period_win_format(x['Q3S'],x['Q3C']),axis=1)
period_points['Q4W']=period_points.apply(lambda x: period_win_format(x['Q4S'],x['Q4C']),axis=1)
period_points['SHW']=period_points.apply(lambda x: period_win_format(x['SHS'],x['SHC']),axis=1)
period_points['EXW']=period_points.apply(lambda x: period_win_format(x['EXS'],x['EXC']),axis=1)
period_points['Q1W_W']=period_points.apply(lambda x: period_win_res_win_format(x['Q1S'],x['Q1C'],x['results']),axis=1)
period_points['Q2W_W']=period_points.apply(lambda x: period_win_res_win_format(x['Q2S'],x['Q2C'],x['results']),axis=1)
period_points['FHW_W']=period_points.apply(lambda x: period_win_res_win_format(x['FHS'],x['FHC'],x['results']),axis=1)
period_points['Q3W_W']=period_points.apply(lambda x: period_win_res_win_format(x['Q3S'],x['Q3C'],x['results']),axis=1)
period_points['Q4W_W']=period_points.apply(lambda x: period_win_res_win_format(x['Q4S'],x['Q4C'],x['results']),axis=1)
period_points['SHW_W']=period_points.apply(lambda x: period_win_res_win_format(x['SHS'],x['SHC'],x['results']),axis=1)
period_points['EXW_W']=period_points.apply(lambda x: period_win_res_win_format(x['EXS'],x['EXC'],x['results']),axis=1)
team_ranking_season = st.sidebar.selectbox("Season:",['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021','2021-2022', '2022-2023', '2023-2024','2024-2025','All'],index=8)
team_ranking_phase = st.sidebar.selectbox("Phase:",['Regular Season', 'Play In','Play offs', 'Final Four','All'],index=4)
team_ranking_round = st.sidebar.selectbox("Round:",['First Round', 'Second Round','PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final', 'All'],index=12)
team_ranking_ha = st.sidebar.selectbox("Home or Away games:",['A', 'H', 'All'],index=2)
team_ranking_wl = st.sidebar.selectbox("Result:",['W', 'L','All'],index=2)







finalstats=All_Seasons.groupby(['idseason','Team','HA','results'])[['PTS','F2M',
                              'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                              'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF',
                              'PIR','Possesions']].sum().reset_index()
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
finalstats=finalstats[['idseason','Team','HA','results','PTS','F2M','F2A', '2P(%)','F3M', 'F3A','3P(%)', 'FTM', 'FTA','FT(%)', 'OR','DR', 'TR',
                       'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF','PIR','Possesions','Offensive Rating','EFG(%)',
                       'TS(%)','FT Ratio','AS-TO Ratio','TO Ratio','AS Ratio']].round(1)

finalstats_opp=All_Seasons.groupby(['idseason','Against'])[['PTS','F2M',
                              'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                              'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF',
                              'PIR','Possesions']].sum().reset_index()


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
finalstats_opp=finalstats_opp[['idseason','Against','PTS','F2M','F2A', '2P(%)','F3M', 'F3A','3P(%)', 'FTM', 'FTA','FT(%)', 'OR','DR', 'TR',
                       'AS', 'ST', 'TO', 'BLK', 'BLKR','PF', 'RF','PIR','Possesions','Offensive Rating','EFG(%)',
                       'TS(%)','FT Ratio','AS-TO Ratio','TO Ratio','AS Ratio']].round(1)
finalstats_opp=finalstats_opp.add_prefix('opp ').rename(columns={'opp Against':'Team','opp idseason':'idseason'})

gamesstats=pd.merge(finalstats,finalstats_opp)
allstats_in_a_game=pd.merge(period_points,gamesstats,on=['idseason','Team','HA','results'])

if "All" in team_ranking_ha:
    team_ranking_ha = ['A', 'H']
    allstats_in_a_game1=allstats_in_a_game.loc[allstats_in_a_game['HA'].isin(team_ranking_ha)]
else:
    allstats_in_a_game1=allstats_in_a_game.loc[allstats_in_a_game['HA']==team_ranking_ha]


if "All" in team_ranking_season:
    team_ranking_season = ['2016-2017', '2017-2018', '2018-2019', '2019-2020','2020-2021','2021-2022', '2022-2023','2023-2024','2024-2025']
    allstats_in_a_game1=allstats_in_a_game1.loc[allstats_in_a_game1['Season'].isin(team_ranking_season)]

else:
    allstats_in_a_game1=allstats_in_a_game1.loc[allstats_in_a_game1['Season']==team_ranking_season]


if "All" in team_ranking_wl:
    team_ranking_wl = ['W', 'L']
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['results'].isin(team_ranking_wl)]

else:
    allstats_in_a_game1= allstats_in_a_game1.loc[allstats_in_a_game1['results'] == team_ranking_wl]


if "All" in team_ranking_phase:
    team_ranking_phase = ['Regular Season', 'Play In','Play offs', 'Final Four']
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Phase'].isin(team_ranking_phase)]

else:
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Phase'] == team_ranking_phase]


if "All" in team_ranking_round:
    team_ranking_round = ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final']
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Round'].isin(team_ranking_round)]

else:
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Round'] == team_ranking_round]


teamranking,teampointsinaperiod,teamwinsbyperiod,teambasicstats,teamsshootstats,teamadvstats=st.tabs(["Team Ranking(Wins-Loses)",'Team Points by period','Team Wins by Period','Team Basic Stats','Team Shooting Stats',"Team Advanced Stats"])
with teamranking:
    try:

        games=allstats_in_a_game1['Team'].value_counts().reset_index().rename(columns={'count':'Games'})
        wins=allstats_in_a_game1.groupby('Team')["Win"].sum().reset_index()
        gameswins=pd.merge(games,wins)
        points=allstats_in_a_game1.groupby('Team')[['Scored',"Conceed"]].mean().reset_index()
        ranking=pd.merge(games,points)
        ranking["Diff"]=ranking['Scored']-ranking['Conceed']
        ranking=pd.merge(ranking,wins)
        ranking['Loses']=ranking['Games']-ranking['Win']
        ranking['Win(%)']=(100*ranking['Win']/ranking['Games']).round(1)
        interactive_table(ranking.round(1).set_index('Team').sort_values('Win(%)'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=False,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True,filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])

    except:
        st.error('No data available with these parameters')


with teampointsinaperiod:
    periods = allstats_in_a_game1.groupby('Team')[['Q1S','Q1C','Q2S','Q2C',"FHS","FHC",'Q3S','Q3C','Q4S','Q4C','SHS','SHC','EXS','EXC']].mean().reset_index()
    interactive_table(periods.round(1).set_index('Team'),
                          paging=False, height=900, width=2000, showIndex=True,
                          classes="display order-column nowrap table_with_monospace_font", searching=False,
                          fixedColumns=True, select=True, info=False, scrollCollapse=True,
                          scrollX=True, scrollY=1000, fixedHeader=True, scroller=True,filter='bottom',
                          columnDefs=[{"className": "dt-center", "targets": "_all"}])

with teamwinsbyperiod:
    periodwins=allstats_in_a_game1.groupby('Team')[['Q1W','Q1W_W','Q2W','Q2W_W','FHW','FHW_W','Q3W','Q3W_W',"Q4W",'Q4W_W','SHW','SHW_W','EXW','EXW_W']].sum().reset_index()
    periodwins=pd.merge(gameswins,periodwins)
    interactive_table(periodwins.set_index('Team'),
                      paging=False, height=900, width=2000, showIndex=True,
                      classes="display order-column nowrap table_with_monospace_font", searching=False,
                      fixedColumns=True, select=True, info=False, scrollCollapse=True,
                      scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                      columnDefs=[{"className": "dt-center", "targets": "_all"}])

with teambasicstats:
    basicstats=allstats_in_a_game1.groupby('Team')[['AS','opp AS','OR', 'opp OR','DR','opp DR', 'TR','opp TR','ST','opp ST', 'TO', 'opp TO','BLK', 'BLKR','PF', 'RF']].mean().reset_index().round(1)
    interactive_table(basicstats.set_index('Team'),
                      paging=False, height=900, width=2000, showIndex=True,
                      classes="display order-column nowrap table_with_monospace_font", searching=False,
                      fixedColumns=True, select=True, info=False, scrollCollapse=True,
                      scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                      columnDefs=[{"className": "dt-center", "targets": "_all"}])

with teamsshootstats:
    shootstats=allstats_in_a_game1.groupby('Team')[['F2M','F2A', 'F3M', 'F3A', 'FTM', 'FTA','opp F2M','opp F2A', 'opp F3M', 'opp F3A', 'opp FTM', 'opp FTA']].mean().reset_index()
    shootstats['2P(%)'] = 100 * (shootstats['F2M'] / shootstats['F2A'])
    shootstats['3P(%)'] = 100 * (shootstats['F3M'] / shootstats['F3A'])
    shootstats['FT(%)'] = 100 * (shootstats['FTM'] / shootstats['FTA'])
    shootstats['opp 2P(%)'] = 100 * (shootstats['opp F2M'] / shootstats['opp F2A'])
    shootstats['opp 3P(%)'] = 100 * (shootstats['opp F3M'] / shootstats['opp F3A'])
    shootstats['opp FT(%)'] = 100 * (shootstats['opp FTM'] / shootstats['opp FTA'])
    interactive_table(shootstats[['Team','F2M','F2A', '2P(%)','opp F2M','opp F2A','opp 2P(%)',
                                  'F3M', 'F3A','3P(%)', 'opp F3M', 'opp F3A', 'opp 3P(%)',
                                  'FTM', 'FTA','FT(%)', 'opp FTM', 'opp FTA','opp FT(%)']].round(1).set_index('Team'),
                      paging=False, height=900, width=2000, showIndex=True,
                      classes="display order-column nowrap table_with_monospace_font", searching=False,
                      fixedColumns=True, select=True, info=False, scrollCollapse=True,
                      scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                      columnDefs=[{"className": "dt-center", "targets": "_all"}])

with teamadvstats:
    computestatsadv=allstats_in_a_game1.groupby('Team')[['F2M','F2A', 'F3M', 'F3A', 'FTM', 'FTA',
                                              'opp F2M','opp F2A', 'opp F3M', 'opp F3A',
                                              'opp FTM', 'opp FTA','AS','opp AS','OR',
                                              'opp OR','DR','opp DR', 'TR','opp TR','ST',
                                              'opp ST', 'TO', 'opp TO','BLK', 'BLKR','PF', 'RF',
                                             'PTS','opp PTS','Possesions','opp Possesions']].mean().reset_index()
    computestatsadv['Offensive Rating'] = 100 * (computestatsadv['PTS'] / computestatsadv['Possesions'])
    computestatsadv['EFG(%)'] = 100 * (computestatsadv['F2M'] + 1.5 * computestatsadv['F3M']) / (
            computestatsadv['F2A'] + computestatsadv['F3A'])
    computestatsadv['TS(%)'] = 100 * (computestatsadv['PTS']) / (
            2 * (computestatsadv['F2A'] + computestatsadv['F3A'] + 0.44 * computestatsadv['FTA']))
    computestatsadv['FT Ratio'] = computestatsadv['FTA'] / (computestatsadv['F3A'] + computestatsadv['F2A'])
    computestatsadv['AS-TO Ratio'] = computestatsadv['AS'] / computestatsadv['TO']
    computestatsadv['TO Ratio'] = 100 * (computestatsadv['TO'] / computestatsadv['Possesions'])
    computestatsadv['AS Ratio'] = 100 * (computestatsadv['AS'] / computestatsadv['Possesions'])
    computestatsadv['Defensive Rating'] = 100 * (computestatsadv['opp PTS'] / computestatsadv['opp Possesions'])
    computestatsadv['Net Rating'] = (computestatsadv['Offensive Rating'] - computestatsadv['Defensive Rating'])
    computestatsadv['opp EFG(%)'] = 100 * (computestatsadv['opp F2M'] + 1.5 * computestatsadv['opp F3M']) / (
                computestatsadv['opp F2A'] + computestatsadv['opp F3A'])
    computestatsadv['opp TS(%)'] = 100 * (computestatsadv['opp PTS']) / (
                2 * (computestatsadv['opp F2A'] + computestatsadv['opp F3A'] + 0.44 * computestatsadv['opp FTA']))
    computestatsadv['opp FT Ratio'] = computestatsadv['opp FTA'] / (computestatsadv['opp F3A'] + computestatsadv['opp F2A'])
    computestatsadv['opp AS-TO Ratio'] = computestatsadv['opp AS'] / computestatsadv['opp TO']
    computestatsadv['opp TO Ratio'] = 100 * (computestatsadv['opp TO'] / computestatsadv['opp Possesions'])
    computestatsadv['opp AS Ratio'] = 100 * (computestatsadv['opp AS'] / computestatsadv['opp Possesions'])
    advstats=computestatsadv[['Team','Possesions','opp Possesions','Offensive Rating','Defensive Rating','Net Rating',
                         'EFG(%)','opp EFG(%)','TS(%)','opp TS(%)','FT Ratio','opp FT Ratio','AS-TO Ratio',
                         'opp AS-TO Ratio','TO Ratio','opp TO Ratio','AS Ratio','opp AS Ratio']].round(2)

    interactive_table(advstats.set_index('Team'),
                      paging=False, height=900, width=2000, showIndex=True,
                      classes="display order-column nowrap table_with_monospace_font", searching=False,
                      fixedColumns=True, select=True, info=False, scrollCollapse=True,
                      scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                      columnDefs=[{"className": "dt-center", "targets": "_all"}])
