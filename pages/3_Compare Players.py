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


st.set_page_config(layout='wide',page_title="Search a Player")
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
    if Fixture <= 15:
        return "First Round"
    elif Fixture > 15 and Fixture <= 34:
        return "Second Round"
def fixture_format4(Fixture):
    if Fixture <= 15:
        return "First Round"
    elif Fixture > 15 and Fixture <= 34:
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
        if Fixture <= 15:
            return "First Round"
        elif Fixture > 15 and Fixture <= 34:
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


All_Seasons=pd.concat([euroleague_2016_2017_playerstats,euroleague_2017_2018_playerstats,euroleague_2018_2019_playerstats,euroleague_2019_2020_playerstats,euroleague_2020_2021_playerstats,euroleague_2021_2022_playerstats,euroleague_2022_2023_playerstats,euroleague_2023_2024_playerstats])

st.sidebar.write("## Select First player filters")
search_player_player1=st.sidebar.selectbox("Choose First player:",All_Seasons['Player'].reset_index().sort_values('Player')['Player'].unique())
selected_ha_player1 = st.sidebar.selectbox("Home or Away games(First Player):",['A', 'H', 'All'],index=2)
selected_season_player1 = st.sidebar.selectbox("Season:",['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021','2021-2022', '2022-2023', '2023-2024','All'],index=8)
selected_phase_player1 = st.sidebar.selectbox("Phase(First Player):",['Regular Season', 'Play In','Play offs', 'Final Four','All'],index=4)
selected_wl_player1 = st.sidebar.selectbox("Result(First Player):",['W', 'L','All'],index=2)
selected_round_player1 = st.sidebar.selectbox("Round(First Player):",['First Round', 'Second Round','PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final', 'All'],index=12)

st.sidebar.write("## ______________________________")
st.sidebar.write("## Select Second player filters")
search_player_player2=st.sidebar.selectbox("Choose Second player:",All_Seasons['Player'].reset_index().sort_values('Player')['Player'].unique())
selected_ha_player2 = st.sidebar.selectbox("Home or Away games(Second Player):",['A', 'H', 'All'],index=2)
selected_season_player2 = st.sidebar.selectbox("Season(Second Player):",['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021',
       '2021-2022', '2022-2023', '2023-2024','All'],index=8)
selected_phase_player2 = st.sidebar.selectbox("Phase(Second Player):",['Regular Season', 'Play In','Play offs', 'Final Four','All'],index=4)
selected_wl_player2 = st.sidebar.selectbox("Result(Second Player):",['W', 'L','All'],index=2)
selected_round_player2 = st.sidebar.selectbox("Round(Second Player):",['First Round', 'Second Round', 'PI 1', 'PI 2','PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final', 'All'],index=12)


if "All" in selected_ha_player1:
    selected_ha_player1 = ['A', 'H']
    All_Seasons1=All_Seasons.loc[All_Seasons['HA'].isin(selected_ha_player1)]
    select_ha_player1=''
else:
    All_Seasons1=All_Seasons.loc[All_Seasons['HA']==selected_ha_player1]
    select_ha_player1 = selected_ha_player1

if "All" in selected_season_player1:
    selected_season_player1 = ['2016-2017', '2017-2018', '2018-2019', '2019-2020','2020-2021','2021-2022', '2022-2023','2023-2024']
    All_Seasons1=All_Seasons1.loc[All_Seasons1['Season'].isin(selected_season_player1)]
    select_season_player1 = ''
else:
    All_Seasons1=All_Seasons1.loc[All_Seasons1['Season']==selected_season_player1]
    select_season_player1 = selected_season_player1

if "All" in selected_wl_player1:
    selected_wl_player1 = ['W', 'L']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['results'].isin(selected_wl_player1)]
    select_wl_player1 = ''
else:
    All_Seasons1= All_Seasons1.loc[All_Seasons1['results'] == selected_wl_player1]
    select_wl_player1 = selected_wl_player1

if "All" in selected_phase_player1:
    selected_phase_player1 = ['Regular Season', 'Play In','Play offs', 'Final Four']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Phase'].isin(selected_phase_player1)]
    select_phase_player1 = ''
else:
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Phase'] == selected_phase_player1]
    select_phase_player1 = selected_phase_player1

if "All" in selected_round_player1:
    selected_round_player1 = ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Round'].isin(selected_round_player1)]
    select_round_player1 = ''
else:
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Round'] == selected_round_player1]
    select_round_player1 = selected_round_player1


if "All" in selected_ha_player2:
    selected_ha_player2 = ['A', 'H']
    All_Seasons2=All_Seasons.loc[All_Seasons['HA'].isin(selected_ha_player2)]
    select_ha_player2 = ''
else:
    All_Seasons2=All_Seasons.loc[All_Seasons['HA']==selected_ha_player2]
    select_ha_player2 = selected_ha_player2

if "All" in selected_season_player2:
    selected_season_player2 = ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021',
       '2021-2022', '2022-2023', '2023-2024']
    All_Seasons2=All_Seasons2.loc[All_Seasons2['Season'].isin(selected_season_player2)]
    select_season_player2 = ''
else:
    All_Seasons2=All_Seasons2.loc[All_Seasons2['Season']==selected_season_player2]
    select_season_player2 = selected_season_player2

if "All" in selected_wl_player2:
    selected_wl_player2 = ['W', 'L']
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['results'].isin(selected_wl_player2)]
    select_wl_player2 = ''
else:
    All_Seasons2= All_Seasons2.loc[All_Seasons2['results'] == selected_wl_player2]
    select_wl_player2 = selected_wl_player2

if "All" in selected_phase_player2:
    selected_phase_player2 = ['Regular Season', 'Play In','Play offs', 'Final Four']
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['Phase'].isin(selected_phase_player2)]
    select_phase_player2 = ''
else:
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['Phase'] == selected_phase_player2]
    select_phase_player2 = selected_phase_player2

if "All" in selected_round_player2:
    selected_round_player2 = ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final']
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['Round'].isin(selected_round_player2)]
    select_round_player2 = ''
else:
    All_Seasons2 = All_Seasons2.loc[All_Seasons2['Round'] == selected_round_player2]
    select_round_player2 = selected_round_player2

def player_rating_stat_higher(dataset,stat):
    dataset1=dataset[["Player",stat]].sort_values(stat).reset_index()
    dataset1.drop("index",axis=1,inplace=True)
    final_dataset=dataset1.reset_index() >> mutate(Rating=(100*(X.index+1)/X.Player.nunique()),Rating1=X.Rating.round(0))
    final_dataset.rename(columns={'Rating1':'Rating_'+ stat},inplace=True)
    final_dataset.drop(["index","Rating",stat],axis=1,inplace=True)
    return final_dataset

def player_rating_stat_lower(dataset,stat):
    dataset1=dataset[["Player",stat]].sort_values(stat).reset_index()
    dataset1.drop("index",axis=1,inplace=True)
    final_dataset=dataset1.reset_index() >> mutate(Rating=(100*(X.index+1)/X.Player.nunique()),Rating1=X.Rating.round(0))
    final_dataset.rename(columns={'Rating1':'Rating_'+ stat},inplace=True)
    final_dataset.drop(["index","Rating",stat],axis=1,inplace=True)
    return final_dataset
def compute_player_stats(dataset,Player):
    computestats=dataset.groupby('Player')[['PTS','MIN','F2M', 'F2A','F3M', 'F3A','FTM', 'FTA','OR', 'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR','Team_PTS','Team_F2M', 'Team_F2A','Team_F3M', 'Team_F3A','Team_FTM', 'Team_FTA','Team_OR', 'Team_DR', 'Team_TR', 'Team_AS', 'Team_ST', 'Team_TO', 'Team_BLK', 'Team_PF','Team_opp_PTS','Team_opp_F2M', 'Team_opp_F2A','Team_opp_F3M', 'Team_opp_F3A','Team_opp_FTM', 'Team_opp_FTA','Team_opp_OR', 'Team_opp_DR', 'Team_opp_TR', 'Team_opp_AS', 'Team_opp_ST', 'Team_opp_TO', 'Team_opp_BLK', 'Team_opp_PF']].mean().round(1).reset_index()
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
    colsplus = ['AS', 'F2M', 'F2A', 'F3M', 'F3A', 'FTM',
                'FTA', 'OR', 'DR', 'TR', 'BLK', 'RF', 'ST', 'P2', 'P3', 'PFT', 'ORA', 'EFG', 'TS', 'FTR', 'ASTOR',
                'ASR', 'USG', 'ORP']
    colsminus = ['BLKR',
                 'PF', 'TOR']

    players_ratings1 = player_rating_stat_higher(computestats, "PTS")
    for i in colsplus:
        df2 = player_rating_stat_higher(computestats, i)
        players_ratings1 = pd.merge(players_ratings1, df2)
    players_ratings2 = player_rating_stat_lower(computestats, "TO")
    for i in colsminus:
        df3 = player_rating_stat_lower(computestats, i)
        players_ratings2 = pd.merge(players_ratings2, df3)

    players_ratings = pd.merge(players_ratings1, players_ratings2)
    computestatsfinal=pd.merge(computestats,players_ratings)
    computestatsfinal = computestatsfinal.loc[computestatsfinal['Player'] == Player]
    return computestatsfinal


player1_stats=compute_player_stats(All_Seasons1,search_player_player1)
player2_stats=compute_player_stats(All_Seasons2,search_player_player2)

p1, p2,stats=st.columns([1,1,2])




with p1:
    st.write('### Player 1')
    st.markdown("#### " + search_player_player1)
    st.write('Season: '+select_season_player1)
    st.write('Phase: '+select_phase_player1)
    st.write('Round: '+select_round_player1)
    st.write('Home or away: '+select_ha_player1)
    st.write('Result: '+select_wl_player1)

    offense_rating_data=player1_stats.loc[player1_stats['Player'] == search_player_player1][
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
        height=150,
        margin=dict(
            l=30,
            r=50,
            b=10,
            t=40,
            pad=0
        ))

    st.write(off)
    defense_ratings = player1_stats.loc[player1_stats['Player'] == search_player_player1][
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
        height=150,
        margin=dict(
            l=30,
            r=50,
            b=10,
            t=40,
            pad=0
        )
    )

    st.write(defe)

    total_ratings = player1_stats.loc[player1_stats['Player'] == search_player_player1][
        ['Player','Rating_PTS', 'Rating_AS', 'Rating_TO', 'Rating_OR', 'Rating_BLKR', 'Rating_RF', 'Rating_F2M', 'Rating_F2A',
         'Rating_P2', 'Rating_F3M', 'Rating_F3A', 'Rating_P3',
         'Rating_FTM', 'Rating_FTA', 'Rating_PFT', 'Rating_FTR', 'Rating_EFG', 'Rating_TS', "Rating_ORA",
         'Rating_ASTOR', "Rating_TOR", "Rating_ASR", 'Rating_USG', 'Rating_ORP','Rating_ST', 'Rating_DR', 'Rating_PF', 'Rating_BLK']].melt(id_vars='Player')[
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

    teams_min_games_played1 = pd.merge(
        All_Seasons1.loc[All_Seasons1['Player'] == search_player_player1].groupby(["Player", 'Team'])[
            'MIN'].mean().round(1).reset_index(),
        All_Seasons1.loc[All_Seasons1['Player'] == search_player_player1][
            ["Player", 'Team']].value_counts().reset_index()).rename(columns={'count': 'Games'})

    team_min_games = go.Figure(data=go.Table(columnwidth=[1, 1, 1],
                                             header=dict(
                                                 values=list(teams_min_games_played1[['Team', 'MIN', 'Games']].columns),
                                                 align='center', font_size=18, height=30), cells=dict(
            values=[teams_min_games_played1.Team, teams_min_games_played1.MIN, teams_min_games_played1.Games],
            align='center', font_size=16, height=30)))

    team_min_games.update_layout(
        autosize=True,
        width=300,
        height=350,
        margin=dict(
            l=20,
            r=20,
            b=100,
            t=40,
            pad=10
        ))
    st.write(team_min_games)





with p2:
    st.write('### Player 2')
    st.markdown("#### " + search_player_player2)
    st.write('Season: ' + select_season_player2)
    st.write('Phase: ' + select_phase_player2)
    st.write('Round: ' + select_round_player2)
    st.write('Home or away: ' + select_ha_player2)
    st.write('Result: ' + select_wl_player2)

    offense_rating_data=player2_stats.loc[player2_stats['Player'] == search_player_player2][
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
        height=150,
        margin=dict(
            l=30,
            r=50,
            b=10,
            t=40,
            pad=0
        ))

    st.write(off)



    defense_ratings = player2_stats.loc[player2_stats['Player'] == search_player_player2][
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
        height=150,
        margin=dict(
            l=30,
            r=50,
            b=10,
            t=40,
            pad=0
        )
    )

    st.write(defe)



    total_ratings = player2_stats.loc[player2_stats['Player'] == search_player_player2][
        ['Player','Rating_PTS', 'Rating_AS', 'Rating_TO', 'Rating_OR', 'Rating_BLKR', 'Rating_RF', 'Rating_F2M', 'Rating_F2A',
         'Rating_P2', 'Rating_F3M', 'Rating_F3A', 'Rating_P3',
         'Rating_FTM', 'Rating_FTA', 'Rating_PFT', 'Rating_FTR', 'Rating_EFG', 'Rating_TS', "Rating_ORA",
         'Rating_ASTOR', "Rating_TOR", "Rating_ASR", 'Rating_USG', 'Rating_ORP','Rating_ST', 'Rating_DR', 'Rating_PF', 'Rating_BLK']].melt(id_vars='Player')[
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

    teams_min_games_played2 = pd.merge(
        All_Seasons2.loc[All_Seasons2['Player'] == search_player_player2].groupby(["Player", 'Team'])[
            'MIN'].mean().round(1).reset_index(),
        All_Seasons2.loc[All_Seasons2['Player'] == search_player_player2][
            ["Player", 'Team']].value_counts().reset_index()).rename(columns={'count': 'Games'})

    team_min_games = go.Figure(data=go.Table(columnwidth=[1, 1, 1],
                                             header=dict(
                                                 values=list(teams_min_games_played2[['Team', 'MIN', 'Games']].columns),
                                                 align='center', font_size=18, height=30), cells=dict(
            values=[teams_min_games_played2.Team, teams_min_games_played2.MIN, teams_min_games_played2.Games],
            align='center', font_size=16, height=30)))

    team_min_games.update_layout(
        autosize=True,
        width=300,
        height=350,
        margin=dict(
            l=20,
            r=20,
            b=100,
            t=40,
            pad=10
        ))
    st.write(team_min_games)
with stats:
    basic,shooting,advanced=st.tabs(['Basic Stats','Shooting Stats','Advanced Stats'])
    with basic:
        basic_stats1=player1_stats[['PTS', 'AS', 'TO', 'TR', 'DR', 'OR', 'BLK', 'BLKR', 'ST', 'PF', 'RF', 'PIR']].rename(columns={'PTS':'Points',
                                                                                                                                    'AS':'Assists',
                                                                                                                                    'TO':'Turnovers',
                                                                                                                                    'TR':'Total Rebounds',
                                                                                                                                    'OR':'Offensive Rebounds',
                                                                                                                                    'DR':'Defensive Rebounds',
                                                                                                                                    'BLK':'Blocks',
                                                                                                                                    'BLKR':'Blocks Reversed',
                                                                                                                                    'ST':'Steals',
                                                                                                                                    'PF':'Personal Fouls',
                                                                                                                                    'RF':'Fouls Drawn'}).round(1)
        basic_stats1=basic_stats1.melt().rename(columns={"variable": "Basic Stats", "value": "Player 1"})
        basic_stats2= player2_stats[['PTS', 'AS', 'TO', 'TR', 'DR', 'OR', 'BLK', 'BLKR', 'ST', 'PF', 'RF', 'PIR']].rename(columns={'PTS': 'Points','AS': 'Assists','TO': 'Turnovers','TR': 'Total Rebounds','OR': 'Offensive Rebounds','DR': 'Defensive Rebounds','BLK': 'Blocks','BLKR': 'Blocks Reversed','ST': 'Steals','PF': 'Personal Fouls','RF': 'Fouls Drawn'}).round(1)
        basic_stats2=basic_stats2.melt().rename(columns={"variable":"Basic Stats","value":"Player 2"})
        basic_stats_data=pd.merge(basic_stats1,basic_stats2)
        basic_stats_fig=go.Figure(data=go.Table(header=dict(values=list(basic_stats_data.columns),align='center',font_size=18,height=30),
                        cells=dict(values=[basic_stats_data['Basic Stats'],basic_stats_data['Player 1'],basic_stats_data['Player 2']],align='center',font_size=15.5,height=30)))
        basic_stats_fig.update_layout(
            autosize=False,
            width=600,
            height=450,
            margin=dict(
            l=0,
            r=10,
            b=40,
            t=0,
            pad=40
            ))
        st.write(basic_stats_fig)
        basic_player_ratings1 = player1_stats.loc[player1_stats['Player'] == search_player_player1][
            ['Player','Rating_PTS', 'Rating_AS', 'Rating_TO', 'Rating_TR', 'Rating_DR', 'Rating_OR', 'Rating_BLK', 'Rating_BLKR',
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
                                                                     'Rating_RF': 'Fouls<br>Drawn'}).melt(id_vars='Player')
        basic_player_ratings1['variable'] = basic_player_ratings1['variable'].str.replace('Rating_', '')

        basic_player_ratings2 = player2_stats.loc[player2_stats['Player'] == search_player_player2][
            ['Player','Rating_PTS', 'Rating_AS', 'Rating_TO', 'Rating_TR', 'Rating_DR', 'Rating_OR', 'Rating_BLK', 'Rating_BLKR',
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
                                                                     'Rating_RF': 'Fouls<br>Drawn'}).melt(id_vars='Player')
        basic_player_ratings2['variable'] = basic_player_ratings2['variable'].str.replace('Rating_', '')
        basic_player_ratings_data=pd.concat([basic_player_ratings1,basic_player_ratings2])
        basic_ratings=make_subplots(rows=2, cols=1,specs=[[{"type": "barpolar"}],[{"type": "barpolar"}]])
        basic_ratings.add_trace(go.Barpolar(
            r=basic_player_ratings1['value'],
            theta=basic_player_ratings1['variable'],
            marker_color='green',
            marker_line_color="black",
            marker_line_width=2,
            opacity=0.8,
            name='Player 1',
            hovertemplate='%{theta} <br>Rating: %{r:.f}<extra></extra>'
            ),row=1, col=1)
        basic_ratings.add_trace(go.Barpolar(
            r=basic_player_ratings2['value'],
            theta=basic_player_ratings2['variable'],
            marker_color='blue',
            marker_line_color="black",
            marker_line_width=2,
            opacity=0.8,
            name='Player 2',
            hovertemplate='%{theta} <br>Rating: %{r:.f}<extra></extra>'
            ),row=2, col=1)
        basic_ratings.update_layout(
            title='Basic Stats Ratings',
            template=None,
            height=650,
            polar=dict(
                radialaxis=dict(range=[0, 100], showticklabels=False, ticks=''),
                angularaxis=dict(showticklabels=True, ticks='')
            ))

        st.write(basic_ratings)
    with shooting:
        shooting_stats1=player1_stats[['F2M', 'F2A', 'P2', 'F3M', 'F3A', 'P3', 'FTM', 'FTA', 'PFT', 'FTR', 'EFG', 'TS']].rename(columns={'F2M':'2P Made',
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
                                                                                                                                       'TS':'TS(%)'})
        shooting_stats1=shooting_stats1.round(1).melt().rename(columns={"variable":"Shooting Stats","value":"Player 1"})
        shooting_stats2 = player2_stats[
            ['F2M', 'F2A', 'P2', 'F3M', 'F3A', 'P3', 'FTM', 'FTA', 'PFT', 'FTR', 'EFG', 'TS']].rename(
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
        shooting_stats2 = shooting_stats2.round(1).melt().rename(
            columns={"variable": "Shooting Stats", "value": "Player 2"})
        shooting_stats_data=pd.merge(shooting_stats1,shooting_stats2)
        shooting_stats_fig=go.Figure(data=go.Table(header=dict(values=list(shooting_stats_data.columns),align='center',font_size=18,height=30),
                        cells=dict(values=[shooting_stats_data['Shooting Stats'],shooting_stats_data['Player 1'],shooting_stats_data['Player 2']],align='center',font_size=16,height=30)))
        shooting_stats_fig.update_layout(
        autosize=False,
        width=8000,
        height=460,
        margin=dict(
            l=0,
            r=10,
            b=40,
            t=0,
            pad=40
        ))
        st.write(shooting_stats_fig)

        shoot_player_ratings1 = player1_stats.loc[player1_stats['Player'] == search_player_player1][
            ['Player','Rating_F2M', 'Rating_F2A', 'Rating_P2', 'Rating_F3M', 'Rating_F3A', 'Rating_P3', 'Rating_FTM',
             'Rating_FTA', 'Rating_PFT', 'Rating_FTR', 'Rating_EFG', 'Rating_TS']].rename(
            columns={'Rating_F2M': '2P Made',
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
                     'Rating_TS': 'TS(%)'}).melt(id_vars='Player')
        shoot_player_ratings1['variable'] = shoot_player_ratings1['variable'].str.replace('Rating_', '')
        shoot_player_ratings2 = player2_stats.loc[player2_stats['Player'] == search_player_player2][
            ['Player','Rating_F2M', 'Rating_F2A', 'Rating_P2', 'Rating_F3M', 'Rating_F3A', 'Rating_P3', 'Rating_FTM',
             'Rating_FTA', 'Rating_PFT', 'Rating_FTR', 'Rating_EFG', 'Rating_TS']].rename(
            columns={'Rating_F2M': '2P Made',
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
                     'Rating_TS': 'TS(%)'}).melt(id_vars='Player')
        shoot_player_ratings2['variable'] = shoot_player_ratings2['variable'].str.replace('Rating_', '')
        shoot_ratings = make_subplots(rows=2, cols=1, specs=[[{"type": "barpolar"}], [{"type": "barpolar"}]])
        shoot_ratings.add_trace(go.Barpolar(
            r=shoot_player_ratings1['value'],
            theta=shoot_player_ratings1['variable'],
            marker_color='green',
            marker_line_color="black",
            marker_line_width=2,
            name='Player 1',
            opacity=0.8,
            hovertemplate='%{theta} <br>Rating: %{r:.f}<extra></extra>'
            ),row=1, col=1)
        shoot_ratings.add_trace(go.Barpolar(
            r=shoot_player_ratings2['value'],
            theta=shoot_player_ratings2['variable'],
            marker_color='blue',
            marker_line_color="black",
            marker_line_width=2,
            name='Player 2',
            opacity=0.8,
            hovertemplate='%{theta} <br>Rating: %{r:.f}<extra></extra>'
        ),row=2, col=1)

        shoot_ratings.update_layout(
            title='Shooting Stats Ratings',
            template=None,
            hovermode="x",
            height=650,
            polar=dict(
                radialaxis=dict(range=[0, 100], showticklabels=False, ticks=''),
                angularaxis=dict(showticklabels=True, ticks='')
            ))
        st.write(shoot_ratings)

    with advanced:
        advanced_stats1 = player1_stats[['POS', 'ORA', 'ASTOR', 'TOR', 'ASR', 'USG', 'ORP']].rename(
            columns={'POS': 'Possesions',
                     'ORA': 'Offensive Rating',
                     'ASTOR': 'Assists/Turnovers Ratio',
                     'TOR': 'Turnovers Ratio',
                     'ASR': 'Assists Ratio',
                     'USG': 'Usage(%)',
                     'ORP': 'OR(%)'})
        advanced_stats1 = advanced_stats1.round(1).melt().rename(
            columns={"variable": "Advanced Stats", "value": "Player 1"})
        advanced_stats2 = player2_stats[['POS', 'ORA', 'ASTOR', 'TOR', 'ASR', 'USG', 'ORP']].rename(
            columns={'POS': 'Possesions',
                     'ORA': 'Offensive Rating',
                     'ASTOR': 'Assists/Turnovers Ratio',
                     'TOR': 'Turnovers Ratio',
                     'ASR': 'Assists Ratio',
                     'USG': 'Usage(%)',
                     'ORP': 'OR(%)'})
        advanced_stats2 = advanced_stats2.round(1).melt().rename(
            columns={"variable": "Advanced Stats", "value": "Player 2"})
        advanced_stats_data=pd.merge(advanced_stats1,advanced_stats2)
        advanced_stats_fig = go.Figure(data=go.Table(
            header=dict(values=list(advanced_stats_data.columns), align='center', font_size=18, height=30),
            cells=dict(values=[advanced_stats_data['Advanced Stats'], advanced_stats_data['Player 1'], advanced_stats_data['Player 2']], align='center',
                       font_size=15, height=30)))
        advanced_stats_fig.update_layout(
            autosize=False,
            width=8000,
            height=500,
            margin=dict(
                l=1,
                r=1,
                b=100,
                t=80,
                pad=25
            ))
        st.write(advanced_stats_fig)

rat_basic, rat_shoot, rat_adv = st.columns(3)
