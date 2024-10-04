
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






All_Seasons=pd.concat([euroleague_2016_2017_playerstats,euroleague_2017_2018_playerstats,euroleague_2018_2019_playerstats,euroleague_2019_2020_playerstats,euroleague_2020_2021_playerstats,euroleague_2021_2022_playerstats,euroleague_2022_2023_playerstats,euroleague_2023_2024_playerstats])

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





All_Seasons_filter['Player_Team']=All_Seasons_filter['Player']+"("+All_Seasons_filter['Team']+","+All_Seasons_filter['Season']+"-vs-"+All_Seasons_filter['Against']+")"

compute_player_mean_stats=All_Seasons_filter.groupby('Player')[['PTS','MIN','F2M', 'F2A','F3M', 'F3A','FTM', 'FTA','OR', 'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR','Team_PTS','Team_F2M', 'Team_F2A','Team_F3M', 'Team_F3A','Team_FTM', 'Team_FTA','Team_OR', 'Team_DR', 'Team_TR', 'Team_AS', 'Team_ST', 'Team_TO', 'Team_BLK', 'Team_PF','Team_opp_PTS','Team_opp_F2M', 'Team_opp_F2A','Team_opp_F3M', 'Team_opp_F3A','Team_opp_FTM', 'Team_opp_FTA','Team_opp_OR', 'Team_opp_DR', 'Team_opp_TR', 'Team_opp_AS', 'Team_opp_ST', 'Team_opp_TO', 'Team_opp_BLK', 'Team_opp_PF' ]].mean().reset_index()
compute_player_mean_stats['P2']=100*(compute_player_mean_stats['F2M']/compute_player_mean_stats['F2A'])
compute_player_mean_stats['P3']=100*(compute_player_mean_stats['F3M']/compute_player_mean_stats['F3A'])
compute_player_mean_stats['PFT']=100*(compute_player_mean_stats['FTM']/compute_player_mean_stats['FTA'])
compute_player_mean_stats['POS']=0.96*(compute_player_mean_stats['F2A']+compute_player_mean_stats['F3A']-compute_player_mean_stats['OR']+compute_player_mean_stats['TO']+0.44*compute_player_mean_stats['FTA'])
compute_player_mean_stats['ORA']=100*(compute_player_mean_stats['PTS']/compute_player_mean_stats['POS'])
compute_player_mean_stats['EFG']=100*(compute_player_mean_stats['F2M']+1.5*compute_player_mean_stats['F3M'])/(compute_player_mean_stats['F2A']+compute_player_mean_stats['F3A'])
compute_player_mean_stats['TS']=100*(compute_player_mean_stats['PTS'])/(2*(compute_player_mean_stats['F2A']+compute_player_mean_stats['F3A']+0.44*compute_player_mean_stats['FTA']))
compute_player_mean_stats['FTR']=compute_player_mean_stats['FTA']/(compute_player_mean_stats['F3A']+compute_player_mean_stats['F2A'])
compute_player_mean_stats['ASTOR']=compute_player_mean_stats['AS']/compute_player_mean_stats['TO']
compute_player_mean_stats['TOR']=100*(compute_player_mean_stats['TO']/compute_player_mean_stats['POS'])
compute_player_mean_stats['ASR']=100*(compute_player_mean_stats['AS']/compute_player_mean_stats['POS'])
compute_player_mean_stats['USG'] = 100 * (((compute_player_mean_stats['F3A'] + compute_player_mean_stats['F2A']) + 0.44 * compute_player_mean_stats['FTA'] + compute_player_mean_stats['TO']) * (40)) / (compute_player_mean_stats['MIN'] * (compute_player_mean_stats['Team_F2A'] +compute_player_mean_stats['Team_F3A'] + 0.44 * compute_player_mean_stats['Team_FTA'] + compute_player_mean_stats['Team_TO']))
compute_player_mean_stats['ORP'] = (100 * compute_player_mean_stats['OR']) / (compute_player_mean_stats['Team_OR'] + compute_player_mean_stats['Team_opp_OR'])
compute_player_total_stats=All_Seasons_filter.groupby('Player')[['PTS','MIN','F2M', 'F2A','F3M', 'F3A','FTM', 'FTA','OR', 'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR']].sum().reset_index()

compute_player_total_stats=(compute_player_total_stats.add_prefix('Total_')).rename(columns={'Total_Player':'Player'})
compute_player_games=All_Seasons_filter['Player'].value_counts().reset_index()
compute_player_games=compute_player_games.rename(columns={'count':'Games'})

compute_player_stats=pd.merge(compute_player_games,compute_player_mean_stats)
compute_player_stats=pd.merge(compute_player_stats,compute_player_total_stats)


compute_player_mean_stats_season=All_Seasons_filter.groupby(['Player','Season'])[['PTS','MIN','F2M', 'F2A','F3M', 'F3A','FTM', 'FTA','OR', 'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR','Team_PTS','Team_F2M', 'Team_F2A','Team_F3M', 'Team_F3A','Team_FTM', 'Team_FTA','Team_OR', 'Team_DR', 'Team_TR', 'Team_AS', 'Team_ST', 'Team_TO', 'Team_BLK', 'Team_PF','Team_opp_PTS','Team_opp_F2M', 'Team_opp_F2A','Team_opp_F3M', 'Team_opp_F3A','Team_opp_FTM', 'Team_opp_FTA','Team_opp_OR', 'Team_opp_DR', 'Team_opp_TR', 'Team_opp_AS', 'Team_opp_ST', 'Team_opp_TO', 'Team_opp_BLK', 'Team_opp_PF' ]].mean().reset_index()
compute_player_mean_stats_season['P2']=100*(compute_player_mean_stats_season['F2M']/compute_player_mean_stats_season['F2A'])
compute_player_mean_stats_season['P3']=100*(compute_player_mean_stats_season['F3M']/compute_player_mean_stats_season['F3A'])
compute_player_mean_stats_season['PFT']=100*(compute_player_mean_stats_season['FTM']/compute_player_mean_stats_season['FTA'])
compute_player_mean_stats_season['POS']=0.96*(compute_player_mean_stats_season['F2A']+compute_player_mean_stats_season['F3A']-compute_player_mean_stats_season['OR']+compute_player_mean_stats_season['TO']+0.44*compute_player_mean_stats_season['FTA'])
compute_player_mean_stats_season['ORA']=100*(compute_player_mean_stats_season['PTS']/compute_player_mean_stats_season['POS'])
compute_player_mean_stats_season['EFG']=100*(compute_player_mean_stats_season['F2M']+1.5*compute_player_mean_stats_season['F3M'])/(compute_player_mean_stats_season['F2A']+compute_player_mean_stats_season['F3A'])
compute_player_mean_stats_season['TS']=100*(compute_player_mean_stats_season['PTS'])/(2*(compute_player_mean_stats_season['F2A']+compute_player_mean_stats_season['F3A']+0.44*compute_player_mean_stats_season['FTA']))
compute_player_mean_stats_season['FTR']=compute_player_mean_stats_season['FTA']/(compute_player_mean_stats_season['F3A']+compute_player_mean_stats_season['F2A'])
compute_player_mean_stats_season['ASTOR']=compute_player_mean_stats_season['AS']/compute_player_mean_stats_season['TO']
compute_player_mean_stats_season['TOR']=100*(compute_player_mean_stats_season['TO']/compute_player_mean_stats_season['POS'])
compute_player_mean_stats_season['ASR']=100*(compute_player_mean_stats_season['AS']/compute_player_mean_stats_season['POS'])
compute_player_mean_stats_season['USG'] = 100 * (((compute_player_mean_stats_season['F3A'] + compute_player_mean_stats_season['F2A']) + 0.44 * compute_player_mean_stats_season['FTA'] + compute_player_mean_stats_season['TO']) * (40)) / (compute_player_mean_stats_season['MIN'] * (compute_player_mean_stats_season['Team_F2A'] +compute_player_mean_stats_season['Team_F3A'] + 0.44 * compute_player_mean_stats_season['Team_FTA'] + compute_player_mean_stats_season['Team_TO']))
compute_player_mean_stats_season['ORP'] = (100 * compute_player_mean_stats_season['OR']) / (compute_player_mean_stats_season['Team_OR'] + compute_player_mean_stats_season['Team_opp_OR'])

compute_player_mean_stats_season['Player_Season']=compute_player_mean_stats_season['Player']+"("+compute_player_mean_stats_season['Season']+")"
compute_player_games_season=All_Seasons_filter[['Player','Season']].value_counts().reset_index()
compute_player_games_season=compute_player_games_season.rename(columns={'count':'Games'})
compute_player_total_stats_season=All_Seasons_filter.groupby(['Player','Season'])[['PTS','MIN','F2M', 'F2A','F3M', 'F3A','FTM', 'FTA','OR', 'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR']].sum().reset_index()

compute_player_total_stats_season=(compute_player_total_stats_season.add_prefix('Total_')).rename(columns={'Total_Player':'Player','Total_Season':'Season'})
compute_player_mean_stats_season=pd.merge(compute_player_mean_stats_season,compute_player_games_season,on=['Player','Season'])
compute_player_mean_stats_season=pd.merge(compute_player_mean_stats_season,compute_player_total_stats_season,on=['Player','Season'])
compute_player_mean_stats_season=compute_player_mean_stats_season.loc[compute_player_mean_stats_season['Games']>15]
games = st.sidebar.slider("Pick Number of games", 0, 200,value=17)
Shoots = st.sidebar.slider("Pick Number of Shoots", 0, 200,value=100)



basic, shooting, advanced = st.tabs(['Basic Stats', 'Shooting Stats', 'Advanced Stats'])
with basic:
    pts, ass, tr, ofr, der, ste, tur, blk, blkr, pf, rf = st.tabs(
        ['Points', "Assists", "Total Reb", "Off Reb", 'Def Reb', "Steals", 'Turnovers', 'Blocks', 'Blocks Reversed',
         'Fouls Made', "Fouls Drawn"])
    with pts:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best on Season'])
        with av:
            st.write("##### Average points per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_pts=compute_player_stats.loc[compute_player_stats['Games'] > games][['Player', 'PTS']].sort_values('PTS',
                                                                                                           ascending=False).head(
                10).round(1).reset_index().rename(columns={'PTS':'Points'})
            av_pts.drop("index",axis=1,inplace=True)
            av_pts=av_pts.reset_index()
            av_pts['No.']=av_pts['index']+1
            av_pts.drop('index',axis=1,inplace=True)
            interactive_table(av_pts.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])

        with sum:

            st.write("##### Total points in Euroleague (Top 10)")
            tot_pts =compute_player_stats[['Player', 'Total_PTS']].sort_values('Total_PTS', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_PTS':'Total Points'})
            tot_pts.drop("index", axis=1, inplace=True)
            tot_pts = tot_pts.reset_index()
            tot_pts['No.'] = tot_pts['index'] + 1
            tot_pts.drop('index', axis=1, inplace=True)
            interactive_table(tot_pts.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record points on a game in Euroleague (Top 10)")
            rec_pts =All_Seasons_filter[['Player_Team', 'PTS']].sort_values('PTS', ascending=False).head(10).round(
                1).reset_index().rename(columns={'PTS':'Record Points','Player_Team':'Player(Team)'})
            rec_pts.drop("index", axis=1, inplace=True)
            rec_pts = rec_pts.reset_index()
            rec_pts['No.'] = rec_pts['index'] + 1
            rec_pts.drop('index', axis=1, inplace=True)
            interactive_table(rec_pts.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
             st.write("##### Best by Season on points in Euroleague (Top 10 - played at least 15 games in the season)")
             bs_pts = compute_player_mean_stats_season[['Player_Season', 'PTS']].sort_values('PTS', ascending=False).head(10).round(
                 1).reset_index().rename(columns={'PTS': 'Average Points', 'Player_Season': 'Player(Season)'})
             bs_pts.drop("index", axis=1, inplace=True)
             bs_pts = bs_pts.reset_index()
             bs_pts['No.'] = bs_pts['index'] + 1
             bs_pts.drop('index', axis=1, inplace=True)
             interactive_table(bs_pts.set_index('No.'),
                               paging=False, height=900, width=2000, showIndex=True,
                               classes="display order-column nowrap table_with_monospace_font", searching=True,
                               fixedColumns=True, select=True, info=False, scrollCollapse=True,
                               scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                               columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with ass:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best on Season'])
        with av:
            st.write("##### Average Assists per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_as = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','AS']].sort_values('AS',ascending=False).head(10).round(1).reset_index().rename(columns={'AS':'Assists'})
            av_as.drop("index", axis=1, inplace=True)
            av_as = av_as.reset_index()
            av_as['No.'] = av_as['index'] + 1
            av_as.drop('index', axis=1, inplace=True)
            interactive_table(av_as.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total assists in Euroleague (Top 10)")
            tot_as =compute_player_stats[['Player', 'Total_AS']].sort_values('Total_AS', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_AS':'Total Assists'})
            tot_as.drop("index", axis=1, inplace=True)
            tot_as = tot_as.reset_index()
            tot_as['No.'] = tot_as['index'] + 1
            tot_as.drop('index', axis=1, inplace=True)
            interactive_table(tot_as.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record points on a game in Euroleague (Top 10)")
            rec_as =All_Seasons_filter[['Player_Team', 'AS']].sort_values('AS', ascending=False).head(10).round(
                1).reset_index().rename(columns={'AS':'Record Assists','Player_Team':'Player(Team)'})
            rec_as.drop("index", axis=1, inplace=True)
            rec_as = rec_as.reset_index()
            rec_as['No.'] = rec_as['index'] + 1
            rec_as.drop('index', axis=1, inplace=True)
            interactive_table(rec_as.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on assists in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_as = compute_player_mean_stats_season[['Player_Season', 'AS']].sort_values('AS',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'AS': 'Average Assists', 'Player_Season': 'Player(Season)'})
            bs_as.drop("index", axis=1, inplace=True)
            bs_as = bs_as.reset_index()
            bs_as['No.'] = bs_as['index'] + 1
            bs_as.drop('index', axis=1, inplace=True)
            interactive_table(bs_as.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with tr:
        av,sum,rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best on Season'])
        with av:
            st.write("##### Average rebounds per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_tr = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','TR']].sort_values('TR',ascending=False).head(10).round(1).reset_index().rename(columns={'TR':'Rebounds'})
            av_tr.drop("index", axis=1, inplace=True)
            av_tr = av_tr.reset_index()
            av_tr['No.'] = av_tr['index'] + 1
            av_tr.drop('index', axis=1, inplace=True)
            interactive_table(av_tr.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total rebounds in Euroleague (Top 10)")
            tot_tr =compute_player_stats[['Player', 'Total_TR']].sort_values('Total_TR', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_TR':'Total Rebounds'})
            tot_tr.drop("index", axis=1, inplace=True)
            tot_tr = tot_tr.reset_index()
            tot_tr['No.'] = tot_tr['index'] + 1
            tot_tr.drop('index', axis=1, inplace=True)
            interactive_table(tot_tr.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record rebounds on a game in Euroleague (Top 10)")
            rec_tr =All_Seasons_filter[['Player_Team', 'TR']].sort_values('TR', ascending=False).head(10).round(
                1).reset_index().rename(columns={'TR':'Record Rebounds','Player_Team':'Player(Team)'})
            rec_tr.drop("index", axis=1, inplace=True)
            rec_tr = rec_tr.reset_index()
            rec_tr['No.'] = rec_tr['index'] + 1
            rec_tr.drop('index', axis=1, inplace=True)
            interactive_table(rec_tr.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on rebounds in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_tr = compute_player_mean_stats_season[['Player_Season', 'TR']].sort_values('TR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'TR': 'Average Rebounds', 'Player_Season': 'Player(Season)'})
            bs_tr.drop("index", axis=1, inplace=True)
            bs_tr = bs_tr.reset_index()
            bs_tr['No.'] = bs_tr['index'] + 1
            bs_tr.drop('index', axis=1, inplace=True)
            interactive_table(bs_tr.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with ofr:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats',"Best on Season"])
        with av:
            st.write("##### Average offensive rebounds per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_or = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','OR']].sort_values('OR',ascending=False).head(10).round(1).reset_index().rename(columns={'OR':'Offensive Rebounds'})
            av_or.drop("index", axis=1, inplace=True)
            av_or = av_or.reset_index()
            av_or['No.'] = av_or['index'] + 1
            av_or.drop('index', axis=1, inplace=True)
            interactive_table(av_or.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total offensive rebounds in Euroleague (Top 10)")
            tot_or =compute_player_stats[['Player', 'Total_OR']].sort_values('Total_OR', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_OR':'Total Offensive Rebounds'})
            tot_or.drop("index", axis=1, inplace=True)
            tot_or = tot_or.reset_index()
            tot_or['No.'] = tot_or['index'] + 1
            tot_or.drop('index', axis=1, inplace=True)
            interactive_table(tot_or.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record offensive rebounds on a game in Euroleague (Top 10)")
            rec_or =All_Seasons_filter[['Player_Team', 'OR']].sort_values('OR', ascending=False).head(10).round(
                1).reset_index().rename(columns={'OR':'Record Offensive Rebounds','Player_Team':'Player(Team)'})
            rec_or.drop("index", axis=1, inplace=True)
            rec_or = rec_or.reset_index()
            rec_or['No.'] = rec_or['index'] + 1
            rec_or.drop('index', axis=1, inplace=True)
            interactive_table(rec_or.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on offensive rebounds in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_or = compute_player_mean_stats_season[['Player_Season', 'OR']].sort_values('OR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'OR': 'Average Offensive Rebounds', 'Player_Season': 'Player(Season)'})
            bs_or.drop("index", axis=1, inplace=True)
            bs_or = bs_or.reset_index()
            bs_or['No.'] = bs_or['index'] + 1
            bs_or.drop('index', axis=1, inplace=True)
            interactive_table(bs_or.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with der:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best on Season'])
        with av:
            st.write("##### Average defensive rebounds per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_dr = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','DR']].sort_values('DR',ascending=False).head(10).round(1).reset_index().rename(columns={'DR':'Defensive Rebounds'})
            av_dr.drop("index", axis=1, inplace=True)
            av_dr = av_dr.reset_index()
            av_dr['No.'] = av_dr['index'] + 1
            av_dr.drop('index', axis=1, inplace=True)
            interactive_table(av_dr.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total defensive rebounds in Euroleague (Top 10)")
            tot_dr =compute_player_stats[['Player', 'Total_DR']].sort_values('Total_DR', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_DR':'Total Defensive Rebounds'})
            tot_dr.drop("index", axis=1, inplace=True)
            tot_dr = tot_dr.reset_index()
            tot_dr['No.'] = tot_dr['index'] + 1
            tot_dr.drop('index', axis=1, inplace=True)
            interactive_table(tot_dr.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record defensive rebounds on a game in Euroleague (Top 10)")
            rec_dr =All_Seasons_filter[['Player_Team', 'DR']].sort_values('DR', ascending=False).head(10).round(
                1).reset_index().rename(columns={'DR':'Record Defensive Rebounds','Player_Team':'Player(Team)'})
            rec_dr.drop("index", axis=1, inplace=True)
            rec_dr = rec_dr.reset_index()
            rec_dr['No.'] = rec_dr['index'] + 1
            rec_dr.drop('index', axis=1, inplace=True)
            interactive_table(rec_dr.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on defensive rebounds in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_dr = compute_player_mean_stats_season[['Player_Season', 'DR']].sort_values('DR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'DR': 'Average Defensive Rebounds', 'Player_Season': 'Player(Season)'})
            bs_dr.drop("index", axis=1, inplace=True)
            bs_dr = bs_dr.reset_index()
            bs_dr['No.'] = bs_dr['index'] + 1
            bs_dr.drop('index', axis=1, inplace=True)
            interactive_table(bs_dr.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with ste:
        av, sum, rec, bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best on Season'])
        with av:
            st.write("##### Average steals per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_st = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','ST']].sort_values('ST',ascending=False).head(10).round(1).reset_index().rename(columns={'ST':'Steals'})
            av_st.drop("index", axis=1, inplace=True)
            av_st = av_st.reset_index()
            av_st['No.'] = av_st['index'] + 1
            av_st.drop('index', axis=1, inplace=True)
            interactive_table(av_st.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total steals in Euroleague (Top 10)")
            tot_st =compute_player_stats[['Player', 'Total_ST']].sort_values('Total_ST', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_ST':'Total Steals'})
            tot_st.drop("index", axis=1, inplace=True)
            tot_st = tot_st.reset_index()
            tot_st['No.'] = tot_st['index'] + 1
            tot_st.drop('index', axis=1, inplace=True)
            interactive_table(tot_st.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record steals on a game in Euroleague (Top 10)")
            rec_st =All_Seasons_filter[['Player_Team', 'ST']].sort_values('ST', ascending=False).head(10).round(
                1).reset_index().rename(columns={'ST':'Record Steals','Player_Team':'Player(Team)'})
            rec_st.drop("index", axis=1, inplace=True)
            rec_st = rec_st.reset_index()
            rec_st['No.'] = rec_st['index'] + 1
            rec_st.drop('index', axis=1, inplace=True)
            interactive_table(rec_st.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on steals in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_st = compute_player_mean_stats_season[['Player_Season', 'ST']].sort_values('ST',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'ST': 'Average Steals', 'Player_Season': 'Player(Season)'})
            bs_st.drop("index", axis=1, inplace=True)
            bs_st = bs_st.reset_index()
            bs_st['No.'] = bs_st['index'] + 1
            bs_st.drop('index', axis=1, inplace=True)
            interactive_table(bs_st.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with tur:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats',"Best by season"])
        with av:
            st.write("##### Average turnovers per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_to = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','TO']].sort_values('TO',ascending=False).head(10).round(1).reset_index().rename(columns={'TO':'Turnovers'})
            av_to.drop("index", axis=1, inplace=True)
            av_to = av_to.reset_index()
            av_to['No.'] = av_to['index'] + 1
            av_to.drop('index', axis=1, inplace=True)
            interactive_table(av_to.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total turnovers in Euroleague (Top 10)")
            tot_to =compute_player_stats[['Player', 'Total_TO']].sort_values('Total_TO', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_TO':'Total Turnovers'})
            tot_to.drop("index", axis=1, inplace=True)
            tot_to = tot_to.reset_index()
            tot_to['No.'] = tot_to['index'] + 1
            tot_to.drop('index', axis=1, inplace=True)
            interactive_table(tot_to.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record turnovers on a game in Euroleague (Top 10)")
            rec_to =All_Seasons_filter[['Player_Team', 'TO']].sort_values('TO', ascending=False).head(10).round(
                1).reset_index().rename(columns={'TO':'Record Turnovers','Player_Team':'Player(Team)'})
            rec_to.drop("index", axis=1, inplace=True)
            rec_to = rec_to.reset_index()
            rec_to['No.'] = rec_to['index'] + 1
            rec_to.drop('index', axis=1, inplace=True)
            interactive_table(rec_to.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on turnovers in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_to = compute_player_mean_stats_season[['Player_Season', 'TO']].sort_values('TO',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'TO': 'Average Turnovers', 'Player_Season': 'Player(Season)'})
            bs_to.drop("index", axis=1, inplace=True)
            bs_to = bs_to.reset_index()
            bs_to['No.'] = bs_to['index'] + 1
            bs_to.drop('index', axis=1, inplace=True)
            interactive_table(bs_to.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with blk:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average blocks per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_blk = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','BLK']].sort_values('BLK',ascending=False).head(10).round(1).reset_index().rename(columns={'BLK':'Blocks'})
            av_blk.drop("index", axis=1, inplace=True)
            av_blk = av_blk.reset_index()
            av_blk['No.'] = av_blk['index'] + 1
            av_blk.drop('index', axis=1, inplace=True)
            interactive_table(av_blk.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total blocks in Euroleague (Top 10)")
            tot_blk =compute_player_stats[['Player', 'Total_BLK']].sort_values('Total_BLK', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_BLK':'Total Blocks'})
            tot_blk.drop("index", axis=1, inplace=True)
            tot_blk = tot_blk.reset_index()
            tot_blk['No.'] = tot_blk['index'] + 1
            tot_blk.drop('index', axis=1, inplace=True)
            interactive_table(tot_blk.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record blocks on a game in Euroleague (Top 10)")
            rec_blk =All_Seasons_filter[['Player_Team', 'BLK']].sort_values('BLK', ascending=False).head(10).round(
                1).reset_index().rename(columns={'BLK':'Record Blocks','Player_Team':'Player(Team)'})
            rec_blk.drop("index", axis=1, inplace=True)
            rec_blk = rec_blk.reset_index()
            rec_blk['No.'] = rec_blk['index'] + 1
            rec_blk.drop('index', axis=1, inplace=True)
            interactive_table(rec_blk.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on blocks in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_blk = compute_player_mean_stats_season[['Player_Season', 'BLK']].sort_values('BLK',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'BLK': 'Average Blocks', 'Player_Season': 'Player(Season)'})
            bs_blk.drop("index", axis=1, inplace=True)
            bs_blk = bs_blk.reset_index()
            bs_blk['No.'] = bs_blk['index'] + 1
            bs_blk.drop('index', axis=1, inplace=True)
            interactive_table(bs_blk.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with blkr:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average blocks reversed per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_blkr = compute_player_stats.loc[compute_player_stats['Games'] > games][['Player', 'BLKR']].sort_values(
                'BLKR', ascending=False).head(10).round(1).reset_index().rename(columns={'BLKR': 'Blocks Reversed'})
            av_blkr.drop("index", axis=1, inplace=True)
            av_blkr = av_blkr.reset_index()
            av_blkr['No.'] = av_blkr['index'] + 1
            av_blkr.drop('index', axis=1, inplace=True)
            interactive_table(av_blkr.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total blocks reversed in Euroleague (Top 10)")
            tot_blkr = compute_player_stats[['Player', 'Total_BLKR']].sort_values('Total_BLKR', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_BLKR': 'Total Blocks Reversed'})
            tot_blkr.drop("index", axis=1, inplace=True)
            tot_blkr = tot_blkr.reset_index()
            tot_blkr['No.'] = tot_blkr['index'] + 1
            tot_blkr.drop('index', axis=1, inplace=True)
            interactive_table(tot_blkr.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record blocks reversed on a game in Euroleague (Top 10)")
            rec_blkr =All_Seasons_filter[['Player_Team', 'BLKR']].sort_values('BLKR', ascending=False).head(10).round(
                1).reset_index().rename(columns={'BLKR':'Record Blocks Reversed','Player_Team':'Player(Team)'})
            rec_blkr.drop("index", axis=1, inplace=True)
            rec_blkr = rec_blkr.reset_index()
            rec_blkr['No.'] = rec_blkr['index'] + 1
            rec_blkr.drop('index', axis=1, inplace=True)
            interactive_table(rec_blkr.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on blocks reversed in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_blkr = compute_player_mean_stats_season[['Player_Season', 'BLKR']].sort_values('BLKR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'BLKR': 'Average Blocks Reversed', 'Player_Season': 'Player(Season)'})
            bs_blkr.drop("index", axis=1, inplace=True)
            bs_blkr = bs_blkr.reset_index()
            bs_blkr['No.'] = bs_blkr['index'] + 1
            bs_blkr.drop('index', axis=1, inplace=True)
            interactive_table(bs_blkr.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with pf:
        av, sum,bs = st.tabs(['Average Stats', 'Total Stats',"Best by Season"])
        with av:
            st.write("##### Average personal fouls per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_pf = compute_player_stats.loc[compute_player_stats['Games'] > games][['Player', 'PF']].sort_values(
                'PF', ascending=False).head(10).round(1).reset_index().rename(columns={'PF': 'Personal Fouls'})
            av_pf.drop("index", axis=1, inplace=True)
            av_pf = av_pf.reset_index()
            av_pf['No.'] = av_pf['index'] + 1
            av_pf.drop('index', axis=1, inplace=True)
            interactive_table(av_pf.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total personal fouls in Euroleague (Top 10)")
            tot_pf = compute_player_stats[['Player', 'Total_PF']].sort_values('Total_PF', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_PF': 'Total Personal Fouls'})
            tot_pf.drop("index", axis=1, inplace=True)
            tot_pf = tot_pf.reset_index()
            tot_pf['No.'] = tot_pf['index'] + 1
            tot_pf.drop('index', axis=1, inplace=True)
            interactive_table(tot_pf.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on personal fouls in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_pf = compute_player_mean_stats_season[['Player_Season', 'PF']].sort_values('PF',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'PF': 'Average Personal Fouls', 'Player_Season': 'Player(Season)'})
            bs_pf.drop("index", axis=1, inplace=True)
            bs_pf = bs_pf.reset_index()
            bs_pf['No.'] = bs_pf['index'] + 1
            bs_pf.drop('index', axis=1, inplace=True)
            interactive_table(bs_pf.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with rf:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average fouls drawn per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_rf = compute_player_stats.loc[compute_player_stats['Games'] > games][['Player', 'RF']].sort_values(
                'RF', ascending=False).head(10).round(1).reset_index().rename(columns={'RF': 'Fouls Drawn'})
            av_rf.drop("index", axis=1, inplace=True)
            av_rf = av_rf.reset_index()
            av_rf['No.'] = av_rf['index'] + 1
            av_rf.drop('index', axis=1, inplace=True)
            interactive_table(av_rf.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total fouls drawn in Euroleague (Top 10)")
            tot_rf = compute_player_stats[['Player', 'Total_RF']].sort_values('Total_RF', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_RF': 'Total Fouls Drawn'})
            tot_rf.drop("index", axis=1, inplace=True)
            tot_rf = tot_rf.reset_index()
            tot_rf['No.'] = tot_rf['index'] + 1
            tot_rf.drop('index', axis=1, inplace=True)
            interactive_table(tot_rf.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record fouls drawn on a game in Euroleague (Top 10)")
            rec_rf =All_Seasons_filter[['Player_Team', 'RF']].sort_values('RF', ascending=False).head(10).round(
                1).reset_index().rename(columns={'RF':'Record Fouls Drawn','Player_Team':'Player(Team)'})
            rec_rf.drop("index", axis=1, inplace=True)
            rec_rf = rec_rf.reset_index()
            rec_rf['No.'] = rec_rf['index'] + 1
            rec_rf.drop('index', axis=1, inplace=True)
            interactive_table(rec_rf.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on fouls drawn in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_rf = compute_player_mean_stats_season[['Player_Season', 'RF']].sort_values('RF',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'RF': 'Average Fouls Drawn', 'Player_Season': 'Player(Season)'})
            bs_rf.drop("index", axis=1, inplace=True)
            bs_rf = bs_rf.reset_index()
            bs_rf['No.'] = bs_rf['index'] + 1
            bs_rf.drop('index', axis=1, inplace=True)
            interactive_table(bs_rf.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
with shooting:
    f2m,f2a,p2,f3m,f3a,p3,ftm,fta,pft=st.tabs(['2P Made',"2P Attempt","2P(%)",'3P Made',"3P Attempt","3P(%)",'Free Throws Made',"Free Throws Attempt","FT(%)"])
    with f2m:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average 2p made per game in Euroleague (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_F2M = compute_player_stats.loc[compute_player_stats['Total_F2A']>Shoots][['Player','F2M']].sort_values('F2M',ascending=False).head(10).round(1).reset_index().rename(columns={'F2M': '2P Made'})
            av_F2M.drop("index", axis=1, inplace=True)
            av_F2M = av_F2M.reset_index()
            av_F2M['No.'] = av_F2M['index'] + 1
            av_F2M.drop('index', axis=1, inplace=True)
            interactive_table(av_F2M.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total 2p made in Euroleague (Top 10)")
            tot_f2m = compute_player_stats[['Player', 'Total_F2M']].sort_values('Total_F2M', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_F2M': 'Total 2P Made'})
            tot_f2m.drop("index", axis=1, inplace=True)
            tot_f2m = tot_f2m.reset_index()
            tot_f2m['No.'] = tot_f2m['index'] + 1
            tot_f2m.drop('index', axis=1, inplace=True)
            interactive_table(tot_f2m.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record 2p made on a game in Euroleague (Top 10)")
            rec_f2m =All_Seasons_filter[['Player_Team', 'F2M']].sort_values('F2M', ascending=False).head(10).round(
                1).reset_index().rename(columns={'F2M':'Record 2P Made','Player_Team':'Player(Team)'})
            rec_f2m.drop("index", axis=1, inplace=True)
            rec_f2m = rec_f2m.reset_index()
            rec_f2m['No.'] = rec_f2m['index'] + 1
            rec_f2m.drop('index', axis=1, inplace=True)
            interactive_table(rec_f2m.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on 2p made in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_f2m = compute_player_mean_stats_season[['Player_Season', 'F2M']].sort_values('F2M',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'F2M': 'Average 2P Made', 'Player_Season': 'Player(Season)'})
            bs_f2m.drop("index", axis=1, inplace=True)
            bs_f2m = bs_f2m.reset_index()
            bs_f2m['No.'] = bs_f2m['index'] + 1
            bs_f2m.drop('index', axis=1, inplace=True)
            interactive_table(bs_f2m.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with f2a:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average 2p attempt per game in Euroleague (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_F2A = compute_player_stats.loc[compute_player_stats['Total_F2A']>Shoots][['Player','F2A']].sort_values('F2A',ascending=False).head(10).round(1).reset_index().rename(columns={'F2A': '2P Attempt'})
            av_F2A.drop("index", axis=1, inplace=True)
            av_F2A = av_F2A.reset_index()
            av_F2A['No.'] = av_F2A['index'] + 1
            av_F2A.drop('index', axis=1, inplace=True)
            interactive_table(av_F2A.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total 2p attempt in Euroleague (Top 10)")
            tot_f2a = compute_player_stats[['Player', 'Total_F2A']].sort_values('Total_F2A', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_F2A': 'Total 2P Attempt'})
            tot_f2a.drop("index", axis=1, inplace=True)
            tot_f2a = tot_f2a.reset_index()
            tot_f2a['No.'] = tot_f2a['index'] + 1
            tot_f2a.drop('index', axis=1, inplace=True)
            interactive_table(tot_f2a.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record 2p attempt on a game in Euroleague (Top 10)")
            rec_f2a =All_Seasons_filter[['Player_Team', 'F2A']].sort_values('F2A', ascending=False).head(10).round(
                1).reset_index().rename(columns={'F2A':'Record 2P Attempt','Player_Team':'Player(Team)'})
            rec_f2a.drop("index", axis=1, inplace=True)
            rec_f2a = rec_f2a.reset_index()
            rec_f2a['No.'] = rec_f2a['index'] + 1
            rec_f2a.drop('index', axis=1, inplace=True)
            interactive_table(rec_f2a.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on 2p attempt in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_f2a = compute_player_mean_stats_season[['Player_Season', 'F2A']].sort_values('F2A',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'F2A': 'Average 2P Attempt', 'Player_Season': 'Player(Season)'})
            bs_f2a.drop("index", axis=1, inplace=True)
            bs_f2a = bs_f2a.reset_index()
            bs_f2a['No.'] = bs_f2a['index'] + 1
            bs_f2a.drop('index', axis=1, inplace=True)
            interactive_table(bs_f2a.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with p2:
        av,  bs = st.tabs(['Total Stats', 'Best by Season'])
        with av:

            st.write("##### Percentage of 2p per game in Euroleague (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_P2 = compute_player_stats.loc[compute_player_stats['Total_F2A']>Shoots][['Player','P2']].sort_values('P2',ascending=False).head(10).round(1).reset_index().rename(columns={'P2': '2P(%)'})
            av_P2.drop("index", axis=1, inplace=True)
            av_P2 = av_P2.reset_index()
            av_P2['No.'] = av_P2['index'] + 1
            av_P2.drop('index', axis=1, inplace=True)
            interactive_table(av_P2.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on 2P percentage in Euroleague (Top 10 - played at least 15 games  & at least 100 of 2P attempts in the season)")
            bs_P2 = compute_player_mean_stats_season.loc[ compute_player_mean_stats_season['Total_F2A']>=100][['Player_Season', 'P2']].sort_values('P2',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'P2': '2P(%)', 'Player_Season': 'Player(Season)'})
            bs_P2.drop("index", axis=1, inplace=True)
            bs_P2 = bs_P2.reset_index()
            bs_P2['No.'] = bs_P2['index'] + 1
            bs_P2.drop('index', axis=1, inplace=True)
            interactive_table(bs_P2.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with f3m:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average 3p made per game in Euroleague (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_F3M = compute_player_stats.loc[compute_player_stats['Total_F3A']>Shoots][['Player','F3M']].sort_values('F3M',ascending=False).head(10).round(1).reset_index().rename(columns={'F3M': '3P Made'})
            av_F3M.drop("index", axis=1, inplace=True)
            av_F3M = av_F3M.reset_index()
            av_F3M['No.'] = av_F3M['index'] + 1
            av_F3M.drop('index', axis=1, inplace=True)
            interactive_table(av_F3M.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total 3p made in Euroleague (Top 10)")
            tot_f3m = compute_player_stats[['Player', 'Total_F3M']].sort_values('Total_F3M', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_F3M': 'Total 3P Made'})
            tot_f3m.drop("index", axis=1, inplace=True)
            tot_f3m = tot_f3m.reset_index()
            tot_f3m['No.'] = tot_f3m['index'] + 1
            tot_f3m.drop('index', axis=1, inplace=True)
            interactive_table(tot_f3m.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record 3p made on a game in Euroleague (Top 10)")
            rec_f3m = All_Seasons_filter[['Player_Team', 'F3M']].sort_values('F3M', ascending=False).head(10).round(
                1).reset_index().rename(columns={'F3M': 'Record 3P Made', 'Player_Team': 'Player(Team)'})
            rec_f3m.drop("index", axis=1, inplace=True)
            rec_f3m = rec_f3m.reset_index()
            rec_f3m['No.'] = rec_f3m['index'] + 1
            rec_f3m.drop('index', axis=1, inplace=True)
            interactive_table(rec_f3m.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write("##### Best by Season on 3p made in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_f3m = compute_player_mean_stats_season[['Player_Season', 'F3M']].sort_values('F3M',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'F3M': 'Average 3P Made', 'Player_Season': 'Player(Season)'})
            bs_f3m.drop("index", axis=1, inplace=True)
            bs_f3m = bs_f3m.reset_index()
            bs_f3m['No.'] = bs_f3m['index'] + 1
            bs_f3m.drop('index', axis=1, inplace=True)
            interactive_table(bs_f3m.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with f3a:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average 3p attempt per game in Euroleague (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_F3A = compute_player_stats.loc[compute_player_stats['Total_F3A']>Shoots][['Player','F3A']].sort_values('F3A',ascending=False).head(10).round(1).reset_index().rename(columns={'F3A': '3P Attempt'})
            av_F3A.drop("index", axis=1, inplace=True)
            av_F3A = av_F3A.reset_index()
            av_F3A['No.'] = av_F3A['index'] + 1
            av_F3A.drop('index', axis=1, inplace=True)
            interactive_table(av_F3A.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total 3p attempt in Euroleague (Top 10)")
            tot_f3a = compute_player_stats[['Player', 'Total_F3A']].sort_values('Total_F3A', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_F3A': 'Total 3P Attempt'})
            tot_f3a.drop("index", axis=1, inplace=True)
            tot_f3a = tot_f3a.reset_index()
            tot_f3a['No.'] = tot_f3a['index'] + 1
            tot_f3a.drop('index', axis=1, inplace=True)
            interactive_table(tot_f3a.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record 3p attempt on a game in Euroleague (Top 10)")
            rec_f3a =All_Seasons_filter[['Player_Team', 'F3A']].sort_values('F3A', ascending=False).head(10).round(
                1).reset_index().rename(columns={'F3A':'Record 3P Attempt','Player_Team':'Player(Team)'})
            rec_f3a.drop("index", axis=1, inplace=True)
            rec_f3a = rec_f3a.reset_index()
            rec_f3a['No.'] = rec_f3a['index'] + 1
            rec_f3a.drop('index', axis=1, inplace=True)
            interactive_table(rec_f3a.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on 3p attempt in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_f3a = compute_player_mean_stats_season[['Player_Season', 'F3A']].sort_values('F3A',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'F3A': 'Average 3P Attempt', 'Player_Season': 'Player(Season)'})
            bs_f3a.drop("index", axis=1, inplace=True)
            bs_f3a = bs_f3a.reset_index()
            bs_f3a['No.'] = bs_f3a['index'] + 1
            bs_f3a.drop('index', axis=1, inplace=True)
            interactive_table(bs_f3a.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with p3:
        av, bs = st.tabs(['Total Stats', 'Best by Season'])
        with av:
            st.write("##### Percentage of 3p per game in Euroleague (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_P3 = compute_player_stats.loc[compute_player_stats['Total_F3A']>Shoots][['Player','P3']].sort_values('P3',ascending=False).head(10).round(1).reset_index().rename(columns={'P3': '3P(%)'})
            av_P3.drop("index", axis=1, inplace=True)
            av_P3 = av_P3.reset_index()
            av_P3['No.'] = av_P3['index'] + 1
            av_P3.drop('index', axis=1, inplace=True)
            interactive_table(av_P3.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on 3P percentage in Euroleague (Top 10 - played at least 15 games  & at least 100 of 3P attempts in the season)")
            bs_P3 = compute_player_mean_stats_season.loc[ compute_player_mean_stats_season['Total_F3A']>=100][['Player_Season', 'P3']].sort_values('P3',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'P3': '3P(%)', 'Player_Season': 'Player(Season)'})
            bs_P3.drop("index", axis=1, inplace=True)
            bs_P3 = bs_P3.reset_index()
            bs_P3['No.'] = bs_P3['index'] + 1
            bs_P3.drop('index', axis=1, inplace=True)
            interactive_table(bs_P3.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with ftm:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average free throws made per game in Euroleague (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_FTM = compute_player_stats.loc[compute_player_stats['Total_FTA']>Shoots][['Player','FTM']].sort_values('FTM',ascending=False).head(10).round(1).reset_index().rename(columns={'FTM': 'Free Throws Made'})
            av_FTM.drop("index", axis=1, inplace=True)
            av_FTM = av_FTM.reset_index()
            av_FTM['No.'] = av_FTM['index'] + 1
            av_FTM.drop('index', axis=1, inplace=True)
            interactive_table(av_FTM.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with sum:
            st.write("##### Total free throws made in Euroleague (Top 10)")
            tot_ftm = compute_player_stats[['Player', 'Total_FTM']].sort_values('Total_FTM', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_FTM': 'Total Free Throws Made'})
            tot_ftm.drop("index", axis=1, inplace=True)
            tot_ftm = tot_ftm.reset_index()
            tot_ftm['No.'] = tot_ftm['index'] + 1
            tot_ftm.drop('index', axis=1, inplace=True)
            interactive_table(tot_ftm.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record free throws made on a game in Euroleague (Top 10)")
            rec_ftm = All_Seasons_filter[['Player_Team', 'FTM']].sort_values('FTM', ascending=False).head(10).round(
                1).reset_index().rename(columns={'FTM': 'Record Free Throws Made', 'Player_Team': 'Player(Team)'})
            rec_ftm.drop("index", axis=1, inplace=True)
            rec_ftm = rec_ftm.reset_index()
            rec_ftm['No.'] = rec_ftm['index'] + 1
            rec_ftm.drop('index', axis=1, inplace=True)
            interactive_table(rec_ftm.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on Free throws made in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_ftm = compute_player_mean_stats_season[['Player_Season', 'FTM']].sort_values('FTM',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'FTM': 'Average Free Throws Made', 'Player_Season': 'Player(Season)'})
            bs_ftm.drop("index", axis=1, inplace=True)
            bs_ftm = bs_ftm.reset_index()
            bs_ftm['No.'] = bs_ftm['index'] + 1
            bs_ftm.drop('index', axis=1, inplace=True)
            interactive_table(bs_ftm.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with fta:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average free throws attempt per game in Euroleague (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_FTA = compute_player_stats.loc[compute_player_stats['Total_FTA']>Shoots][['Player','FTA']].sort_values('FTA',ascending=False).head(10).round(1).reset_index().rename(columns={'FTA': 'Free Throws Attempt'})
            av_FTA.drop("index", axis=1, inplace=True)
            av_FTA = av_FTA.reset_index()
            av_FTA['No.'] = av_FTA['index'] + 1
            av_FTA.drop('index', axis=1, inplace=True)
            interactive_table(av_FTA.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt center", "targets": "_all"}])
        with sum:
            st.write("##### Total Free Throws Attempt in Euroleague (Top 10)")
            tot_fta = compute_player_stats[['Player', 'Total_FTA']].sort_values('Total_FTA', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_FTA': 'Total Free Throws Attempt'})
            tot_fta.drop("index", axis=1, inplace=True)
            tot_fta = tot_fta.reset_index()
            tot_fta['No.'] = tot_fta['index'] + 1
            tot_fta.drop('index', axis=1, inplace=True)
            interactive_table(tot_fta.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with rec:
            st.write("##### Record free throws attempt on a game in Euroleague (Top 10)")
            rec_fta = All_Seasons_filter[['Player_Team', 'FTA']].sort_values('FTA', ascending=False).head(10).round(
                1).reset_index().rename(columns={'FTA': 'Record Free Throws Attempt', 'Player_Team': 'Player(Team)'})
            rec_fta.drop("index", axis=1, inplace=True)
            rec_fta = rec_fta.reset_index()
            rec_fta['No.'] = rec_fta['index'] + 1
            rec_fta.drop('index', axis=1, inplace=True)
            interactive_table(rec_fta.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on Free throws attempt in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_fta = compute_player_mean_stats_season[['Player_Season', 'FTA']].sort_values('FTA',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'FTA': 'Average Free Throws Attempt', 'Player_Season': 'Player(Season)'})
            bs_fta.drop("index", axis=1, inplace=True)
            bs_fta = bs_fta.reset_index()
            bs_fta['No.'] = bs_fta['index'] + 1
            bs_fta.drop('index', axis=1, inplace=True)
            interactive_table(bs_fta.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with pft:
        av, bs = st.tabs(['Total Stats', 'Best by Season'])
        with av:
            st.write("##### Percentage of free throws per game in Euroleague (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_PFT = compute_player_stats.loc[compute_player_stats['Total_FTA']>Shoots][['Player','PFT']].sort_values('PFT',ascending=False).head(10).round(1).reset_index().rename(columns={'PFT': 'FT(%)'})
            av_PFT.drop("index", axis=1, inplace=True)
            av_PFT = av_PFT.reset_index()
            av_PFT['No.'] = av_PFT['index'] + 1
            av_PFT.drop('index', axis=1, inplace=True)
            interactive_table(av_PFT.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on FT percentage in Euroleague (Top 10 - played at least 15 games  & at least 100 of FT attempts in the season)")
            bs_PFT = compute_player_mean_stats_season.loc[ compute_player_mean_stats_season['Total_FTA']>=100][['Player_Season', 'PFT']].sort_values('PFT',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'PFT': 'FT(%)', 'Player_Season': 'Player(Season)'})
            bs_PFT.drop("index", axis=1, inplace=True)
            bs_PFT = bs_PFT.reset_index()
            bs_PFT['No.'] = bs_PFT['index'] + 1
            bs_PFT.drop('index', axis=1, inplace=True)
            interactive_table(bs_PFT.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
with advanced:
    pos, ora, efg, ts, ftr, astor, tor, asr, usg,orp = st.tabs(
        ['Possessions', "Offensive Rating", "EFG(%)", 'TS(%)', "Free Throw Ratio", "Assists - Turnover Ratio", 'Turnover Ratio',
         "Assists Ratio", "Usage(%)",'OR(%)'])
    with pos:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Average possesions per game in Euroleague (Top 10)")
            av_POS = compute_player_stats[['Player','POS']].sort_values('POS',ascending=False).head(10).round(1).reset_index().rename(columns={'POS': 'Possesions'})
            av_POS.drop("index", axis=1, inplace=True)
            av_POS = av_POS.reset_index()
            av_POS['No.'] = av_POS['index'] + 1
            av_POS.drop('index', axis=1, inplace=True)
            interactive_table(av_POS.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on average possesions per game in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_POS = compute_player_mean_stats_season[['Player_Season', 'POS']].sort_values('POS',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'POS': 'Possesions', 'Player_Season': 'Player(Season)'})
            bs_POS.drop("index", axis=1, inplace=True)
            bs_POS = bs_POS.reset_index()
            bs_POS['No.'] = bs_POS['index'] + 1
            bs_POS.drop('index', axis=1, inplace=True)
            interactive_table(bs_POS.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with ora:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Offensive Rating per game in Euroleague (Top 10)")
            av_ORA = compute_player_stats.loc[compute_player_stats['POS']>10][['Player','ORA']].sort_values('ORA',ascending=False).head(10).round(1).reset_index().rename(columns={'ORA': 'Offensive Rating'})
            av_ORA.drop("index", axis=1, inplace=True)
            av_ORA = av_ORA.reset_index()
            av_ORA['No.'] = av_ORA['index'] + 1
            av_ORA.drop('index', axis=1, inplace=True)
            interactive_table(av_ORA.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on offensive rating per game in Euroleague (Top 10 - played at least 15 games & over 10 possesions per game in the season)")
            bs_ORA = compute_player_mean_stats_season.loc[compute_player_mean_stats_season['POS']>10][['Player_Season', 'ORA']].sort_values('ORA',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'ORA': 'Offensive Rating', 'Player_Season': 'Player(Season)'})
            bs_ORA.drop("index", axis=1, inplace=True)
            bs_ORA = bs_ORA.reset_index()
            bs_ORA['No.'] = bs_ORA['index'] + 1
            bs_ORA.drop('index', axis=1, inplace=True)
            interactive_table(bs_ORA.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with efg:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Effective Field Goal per game in Euroleague (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_EFG = compute_player_stats.loc[(compute_player_stats['Total_F2A']>Shoots) |(compute_player_stats['Total_F3A']>Shoots)][['Player','EFG']].sort_values('EFG',ascending=False).head(10).round(1).reset_index().rename(columns={'EFG': 'EFG(%)'})
            av_EFG.drop("index", axis=1, inplace=True)
            av_EFG = av_EFG.reset_index()
            av_EFG['No.'] = av_EFG['index'] + 1
            av_EFG.drop('index', axis=1, inplace=True)
            interactive_table(av_EFG.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on effective field goal in Euroleague (Top 10 - played at least 15 games & at least 100 2p or 3P Attempts in the season)")
            bs_EFG = compute_player_mean_stats_season.loc[(compute_player_mean_stats_season['Total_F2A']>=100) | (compute_player_mean_stats_season['Total_F3A']>=100)][['Player_Season', 'EFG']].sort_values('EFG',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'EFG': 'EFG(%)', 'Player_Season': 'Player(Season)'})
            bs_EFG.drop("index", axis=1, inplace=True)
            bs_EFG = bs_EFG.reset_index()
            bs_EFG['No.'] = bs_EFG['index'] + 1
            bs_EFG.drop('index', axis=1, inplace=True)
            interactive_table(bs_EFG.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with ts:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### True Shooting percentage per game in Euroleague (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_TS = compute_player_stats.loc[(compute_player_stats['Total_F2A']>Shoots) |(compute_player_stats['Total_F3A']>Shoots)][['Player','TS']].sort_values('TS',ascending=False).head(10).round(1).reset_index().rename(columns={'TS': 'TS(%)'})
            av_TS.drop("index", axis=1, inplace=True)
            av_TS = av_TS.reset_index()
            av_TS['No.'] = av_TS['index'] + 1
            av_TS.drop('index', axis=1, inplace=True)
            interactive_table(av_TS.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on true shoting in Euroleague (Top 10 - played at least 15 games & at least 100 2p or 3P Attempts in the season)")
            bs_TS = compute_player_mean_stats_season.loc[(compute_player_mean_stats_season['Total_F2A']>=100) | (compute_player_mean_stats_season['Total_F3A']>=100)][['Player_Season', 'TS']].sort_values('TS',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'TS': 'TS(%)', 'Player_Season': 'Player(Season)'})
            bs_TS.drop("index", axis=1, inplace=True)
            bs_TS = bs_TS.reset_index()
            bs_TS['No.'] = bs_TS['index'] + 1
            bs_TS.drop('index', axis=1, inplace=True)
            interactive_table(bs_TS.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with ftr:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Free Throw Ratio per game in Euroleague (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_FTR = compute_player_stats.loc[(compute_player_stats['Total_FTA'] > Shoots)][
                ['Player', 'FTR']].sort_values('FTR', ascending=False).round(1)
            av_FTR=av_FTR.loc[av_FTR.FTR<100].reset_index()
            av_FTR = av_FTR.head(10).rename(columns={'FTR': 'Free Throws Ratio'})
            av_FTR.drop("index", axis=1, inplace=True)
            av_FTR = av_FTR.reset_index()
            av_FTR['No.'] = av_FTR['index'] + 1
            av_FTR.drop('index', axis=1, inplace=True)
            interactive_table(av_FTR.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on free throw ratio in Euroleague (Top 10 - played at least 15 games & at least 100 Free throw Attempts in the season)")
            bs_FTR = compute_player_mean_stats_season.loc[(compute_player_mean_stats_season['Total_FTA']>=100) ][['Player_Season', 'FTR']].sort_values('FTR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'FTR': 'Free Throws Ratio', 'Player_Season': 'Player(Season)'})
            bs_FTR.drop("index", axis=1, inplace=True)
            bs_FTR = bs_FTR.reset_index()
            bs_FTR['No.'] = bs_FTR['index'] + 1
            bs_FTR.drop('index', axis=1, inplace=True)
            interactive_table(bs_FTR.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with astor:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Assists-Turnovers Ratio per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_ASTOR = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','ASTOR']].sort_values('ASTOR',ascending=False).head(10).round(1).reset_index().rename(columns={'ASTOR': 'Assists-Turnovers ratio'})
            av_ASTOR.drop("index", axis=1, inplace=True)
            av_ASTOR = av_ASTOR.reset_index()
            av_ASTOR['No.'] = av_ASTOR['index'] + 1
            av_ASTOR.drop('index', axis=1, inplace=True)
            interactive_table(av_ASTOR.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on Assists-Turnover ratio in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_ASTOR = compute_player_mean_stats_season[['Player_Season', 'ASTOR']].sort_values('ASTOR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index()
            bs_ASTOR=bs_ASTOR.loc[bs_ASTOR.ASTOR<100].rename(columns={'ASTOR': 'Assists-Turnover ratio', 'Player_Season': 'Player(Season)'})
            bs_ASTOR.drop("index", axis=1, inplace=True)
            bs_ASTOR = bs_ASTOR.reset_index()
            bs_ASTOR['No.'] = bs_ASTOR['index'] + 1
            bs_ASTOR.drop('index', axis=1, inplace=True)
            interactive_table(bs_ASTOR.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with tor:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Turnovers Ratio per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_TOR = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','TOR']].sort_values('TOR',ascending=False).head(10).round(1).reset_index().rename(
                columns={'TOR': 'Turnovers ratio'})
            av_TOR.drop("index", axis=1, inplace=True)
            av_TOR = av_TOR.reset_index()
            av_TOR['No.'] = av_TOR['index'] + 1
            av_TOR.drop('index', axis=1, inplace=True)
            interactive_table(av_TOR.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season onTurnover ratio in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_TOR = compute_player_mean_stats_season[
                ['Player_Season', 'TOR']].sort_values('TOR',
                                                        ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'TOR': 'Turnover ratio', 'Player_Season': 'Player(Season)'})
            bs_TOR.drop("index", axis=1, inplace=True)
            bs_TOR = bs_TOR.reset_index()
            bs_TOR['No.'] = bs_TOR['index'] + 1
            bs_TOR.drop('index', axis=1, inplace=True)
            interactive_table(bs_TOR.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with asr:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Assists Ratio per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_ASR = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','ASR']].sort_values('ASR',ascending=False).head(10).round(1).reset_index().rename(
                columns={'ASR': 'Assists Ratio'})
            av_ASR.drop("index", axis=1, inplace=True)
            av_ASR = av_ASR.reset_index()
            av_ASR['No.'] = av_ASR['index'] + 1
            av_ASR.drop('index', axis=1, inplace=True)
            interactive_table(av_ASR.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on Assists ratio in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_ASR = compute_player_mean_stats_season[['Player_Season', 'ASR']].sort_values('ASR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'ASR': 'Assists Ratio', 'Player_Season': 'Player(Season)'})
            bs_ASR.drop("index", axis=1, inplace=True)
            bs_ASR = bs_ASR.reset_index()
            bs_ASR['No.'] = bs_ASR['index'] + 1
            bs_ASR.drop('index', axis=1, inplace=True)
            interactive_table(bs_ASR.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])

    with usg:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Usage(%) per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_USG = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','USG']].sort_values('USG',ascending=False).head(10).round(1).reset_index().rename(
                columns={'USG': 'Usage(%)'})
            av_USG.drop("index", axis=1, inplace=True)
            av_USG = av_USG.reset_index()
            av_USG['No.'] = av_USG['index'] + 1
            av_USG.drop('index', axis=1, inplace=True)
            interactive_table(av_USG.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
        with bs:
            st.write(
                "##### Best by Season on Usage in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_USG = compute_player_mean_stats_season[['Player_Season', 'USG']].sort_values('USG',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'USG': 'Usage(%)', 'Player_Season': 'Player(Season)'})
            bs_USG.drop("index", axis=1, inplace=True)
            bs_USG = bs_USG.reset_index()
            bs_USG['No.'] = bs_USG['index'] + 1
            bs_USG.drop('index', axis=1, inplace=True)
            interactive_table(bs_USG.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
    with orp:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Percentage of Offensive Rebounds per game in Euroleague (Top 10)")
            st.write('(For better results move the Games slider)')
            av_ORP = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','ORP']].sort_values('ORP',ascending=False).head(10).round(1).reset_index().rename(
                columns={'ORP': 'OR(%)'})
            av_ORP.drop("index", axis=1, inplace=True)
            av_ORP = av_ORP.reset_index()
            av_ORP['No.'] = av_ORP['index'] + 1
            av_ORP.drop('index', axis=1, inplace=True)
            interactive_table(av_ORP.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])

        with bs:
            st.write(
                "##### Best by Season on percentage of Offensive Rebounds in Euroleague (Top 10 - played at least 15 games in the season)")
            bs_ORP = compute_player_mean_stats_season[['Player_Season', 'ORP']].sort_values('ORP',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'ORP': 'OR(%)', 'Player_Season': 'Player(Season)'})
            bs_ORP.drop("index", axis=1, inplace=True)
            bs_ORP = bs_ORP.reset_index()
            bs_ORP['No.'] = bs_ORP['index'] + 1
            bs_ORP.drop('index', axis=1, inplace=True)
            interactive_table(bs_ORP.set_index('No.'),
                              paging=False, height=900, width=2000, showIndex=True,
                              classes="display order-column nowrap table_with_monospace_font", searching=True,
                              fixedColumns=True, select=True, info=False, scrollCollapse=True,
                              scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                              columnDefs=[{"className": "dt-center", "targets": "_all"}])
