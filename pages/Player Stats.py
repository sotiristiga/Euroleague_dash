
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

st.set_page_config(layout='wide',page_title="Player Stats")
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

All_Seasons=All_Seasons.rename(columns={'HA':'Home or Away','results':'Result'})

filters_playerstats = DynamicFilters(All_Seasons, filters=['Season','Round','Phase','Home or Away','Result'])
All_Seasons_filter = filters_playerstats .filter_df()

filters_playerstats.display_filters(location='sidebar')
All_Seasons_filter['Player_Team']=All_Seasons_filter['Player']+" ("+All_Seasons_filter['Team']+","+All_Seasons_filter['Season']+" vs "+All_Seasons_filter['Against']+")"

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
compute_player_mean_stats_season['Player_Season']=compute_player_mean_stats_season['Player']+" ("+compute_player_mean_stats_season['Season']+")"
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
            st.write("##### Average points per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_pts=compute_player_stats.loc[compute_player_stats['Games'] > games][['Player', 'PTS']].sort_values('PTS',
                                                                                                           ascending=False).head(
                10).round(1).reset_index().rename(columns={'PTS':'Points'})
            av_pts.drop("index",axis=1,inplace=True)
            av_pts=av_pts.reset_index()
            av_pts['No.']=av_pts['index']+1
            av_pts_fig = go.Figure(data=go.Table( columnwidth=[1,5,3],header=dict(
                                                         values=list(
                                                             av_pts[['No.','Player','Points']].columns),
                                                         align='center', font_size=18, height=30), cells=dict(
                    values=[av_pts['No.'],av_pts.Player, av_pts.Points],
                    align='center', font_size=16, height=30)))

            av_pts_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_pts_fig)
        with sum:
            st.write("##### Total points in Euroleague from 2016-2017 Season (Top 10)")
            tot_pts =compute_player_stats[['Player', 'Total_PTS']].sort_values('Total_PTS', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_PTS':'Total Points'})
            tot_pts.drop("index", axis=1, inplace=True)
            tot_pts = tot_pts.reset_index()
            tot_pts['No.'] = tot_pts['index'] + 1
            tot_pts_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    tot_pts[['No.', 'Player','Total Points']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_pts['No.'], tot_pts.Player, tot_pts['Total Points']],
                align='center', font_size=16, height=30)))

            tot_pts_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_pts_fig)
        with rec:
            st.write("##### Record points on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_pts =All_Seasons_filter[['Player_Team', 'PTS']].sort_values('PTS', ascending=False).head(10).round(
                1).reset_index().rename(columns={'PTS':'Record Points','Player_Team':'Player(Team)'})
            rec_pts.drop("index", axis=1, inplace=True)
            rec_pts = rec_pts.reset_index()
            rec_pts['No.'] = rec_pts['index'] + 1
            rec_pts_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    rec_pts[['No.', 'Player(Team)','Record Points']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_pts['No.'], rec_pts['Player(Team)'], rec_pts['Record Points']],
                align='center', font_size=16, height=30)))

            rec_pts_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_pts_fig)
        with bs:
             st.write("##### Best by Season on points in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
             bs_pts = compute_player_mean_stats_season[['Player_Season', 'PTS']].sort_values('PTS', ascending=False).head(10).round(
                 1).reset_index().rename(columns={'PTS': 'Average Points', 'Player_Season': 'Player(Season)'})
             bs_pts.drop("index", axis=1, inplace=True)
             bs_pts = bs_pts.reset_index()
             bs_pts['No.'] = bs_pts['index'] + 1
             bs_pts_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                 values=list(
                     bs_pts[['No.', 'Player(Season)', 'Average Points']].columns),
                 align='center', font_size=18, height=30), cells=dict(
                 values=[bs_pts['No.'], bs_pts['Player(Season)'], bs_pts['Average Points']],
                 align='center', font_size=16, height=30)))

             bs_pts_fig.update_layout(
                 autosize=True,
                 width=1000,
                 height=800,
                 margin=dict(
                     l=1,
                     r=1,
                     b=100,
                     t=80,
                     pad=10
                 ))

             st.write(bs_pts_fig)
    with ass:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best on Season'])
        with av:
            st.write("##### Average Assists per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_as = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','AS']].sort_values('AS',ascending=False).head(10).round(1).reset_index().rename(columns={'AS':'Assists'})
            av_as.drop("index", axis=1, inplace=True)
            av_as = av_as.reset_index()
            av_as['No.'] = av_as['index'] + 1
            av_as_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(av_as[['No.', 'Player', 'Assists']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_as['No.'], av_as.Player, av_as.Assists],
                align='center', font_size=16, height=30)))

            av_as_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_as_fig)
        with sum:
            st.write("##### Total assists in Euroleague from 2016-2017 Season (Top 10)")
            tot_as =compute_player_stats[['Player', 'Total_AS']].sort_values('Total_AS', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_AS':'Total Assists'})
            tot_as.drop("index", axis=1, inplace=True)
            tot_as = tot_as.reset_index()
            tot_as['No.'] = tot_as['index'] + 1
            tot_as_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    tot_as[['No.', 'Player','Total Assists']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_as['No.'], tot_as.Player, tot_as['Total Assists']],
                align='center', font_size=16, height=30)))

            tot_as_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_as_fig)
        with rec:
            st.write("##### Record points on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_as =All_Seasons_filter[['Player_Team', 'AS']].sort_values('AS', ascending=False).head(10).round(
                1).reset_index().rename(columns={'AS':'Record Assists','Player_Team':'Player(Team)'})
            rec_as.drop("index", axis=1, inplace=True)
            rec_as = rec_as.reset_index()
            rec_as['No.'] = rec_as['index'] + 1
            rec_as_fig = go.Figure(data=go.Table(columnwidth=[1,4,3],header=dict(
                values=list(
                    rec_as[['No.', 'Player(Team)','Record Assists']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_as['No.'], rec_as['Player(Team)'], rec_as['Record Assists']],
                align='center', font_size=16, height=30)))

            rec_as_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_as_fig)
        with bs:
            st.write("##### Best by Season on assists in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_as = compute_player_mean_stats_season[['Player_Season', 'AS']].sort_values('AS',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'AS': 'Average Assists', 'Player_Season': 'Player(Season)'})
            bs_as.drop("index", axis=1, inplace=True)
            bs_as = bs_as.reset_index()
            bs_as['No.'] = bs_as['index'] + 1
            bs_as_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    bs_as[['No.', 'Player(Season)', 'Average Assists']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_as['No.'], bs_as['Player(Season)'], bs_as['Average Assists']],
                align='center', font_size=16, height=30)))

            bs_as_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_as_fig)
    with tr:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best on Season'])
        with av:
            st.write("##### Average rebounds per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_tr = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','TR']].sort_values('TR',ascending=False).head(10).round(1).reset_index().rename(columns={'TR':'Rebounds'})
            av_tr.drop("index", axis=1, inplace=True)
            av_tr = av_tr.reset_index()
            av_tr['No.'] = av_tr['index'] + 1
            av_tr_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(av_tr[['No.', 'Player', 'Rebounds']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_tr['No.'], av_tr.Player, av_tr.Rebounds],
                align='center', font_size=16, height=30)))

            av_tr_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_tr_fig)
        with sum:
            st.write("##### Total rebounds in Euroleague from 2016-2017 Season (Top 10)")
            tot_tr =compute_player_stats[['Player', 'Total_TR']].sort_values('Total_TR', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_TR':'Total Rebounds'})
            tot_tr.drop("index", axis=1, inplace=True)
            tot_tr = tot_tr.reset_index()
            tot_tr['No.'] = tot_tr['index'] + 1
            tot_tr_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    tot_tr[['No.', 'Player','Total Rebounds']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_tr['No.'], tot_tr.Player, tot_tr['Total Rebounds']],
                align='center', font_size=16, height=30)))

            tot_tr_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_tr_fig)
        with rec:
            st.write("##### Record rebounds on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_tr =All_Seasons_filter[['Player_Team', 'TR']].sort_values('TR', ascending=False).head(10).round(
                1).reset_index().rename(columns={'TR':'Record Rebounds','Player_Team':'Player(Team)'})
            rec_tr.drop("index", axis=1, inplace=True)
            rec_tr = rec_tr.reset_index()
            rec_tr['No.'] = rec_tr['index'] + 1
            rec_tr_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    rec_tr[['No.', 'Player(Team)','Record Rebounds']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_tr['No.'], rec_tr['Player(Team)'], rec_tr['Record Rebounds']],
                align='center', font_size=16, height=30)))

            rec_tr_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_tr_fig)
        with bs:
            st.write("##### Best by Season on rebounds in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_tr = compute_player_mean_stats_season[['Player_Season', 'TR']].sort_values('TR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'TR': 'Average Rebounds', 'Player_Season': 'Player(Season)'})
            bs_tr.drop("index", axis=1, inplace=True)
            bs_tr = bs_tr.reset_index()
            bs_tr['No.'] = bs_tr['index'] + 1
            bs_tr_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    bs_tr[['No.', 'Player(Season)', 'Average Rebounds']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_tr['No.'], bs_tr['Player(Season)'], bs_tr['Average Rebounds']],
                align='center', font_size=16, height=30)))

            bs_tr_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_tr_fig)
    with ofr:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats',"Best on Season"])
        with av:
            st.write("##### Average offensive rebounds per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_or = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','OR']].sort_values('OR',ascending=False).head(10).round(1).reset_index().rename(columns={'OR':'Offensive Rebounds'})
            av_or.drop("index", axis=1, inplace=True)
            av_or = av_or.reset_index()
            av_or['No.'] = av_or['index'] + 1
            av_or_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(av_or[['No.', 'Player', 'Offensive Rebounds']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_or['No.'], av_or.Player, av_or['Offensive Rebounds']],
                align='center', font_size=16, height=30)))

            av_or_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_or_fig)
        with sum:
            st.write("##### Total offensive rebounds in Euroleague from 2016-2017 Season (Top 10)")
            tot_or =compute_player_stats[['Player', 'Total_OR']].sort_values('Total_OR', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_OR':'Total Offensive Rebounds'})
            tot_or.drop("index", axis=1, inplace=True)
            tot_or = tot_or.reset_index()
            tot_or['No.'] = tot_or['index'] + 1
            tot_or_fig = go.Figure(data=go.Table(columnwidth=[1,5,5],header=dict(
                values=list(
                    tot_or[['No.', 'Player','Total Offensive Rebounds']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_or['No.'], tot_or.Player, tot_or['Total Offensive Rebounds']],
                align='center', font_size=16, height=30)))

            tot_or_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_or_fig)
        with rec:
            st.write("##### Record offensive rebounds on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_or =All_Seasons_filter[['Player_Team', 'TR']].sort_values('TR', ascending=False).head(10).round(
                1).reset_index().rename(columns={'TR':'Record Offensive Rebounds','Player_Team':'Player(Team)'})
            rec_or.drop("index", axis=1, inplace=True)
            rec_or = rec_or.reset_index()
            rec_or['No.'] = rec_or['index'] + 1
            rec_or_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    rec_or[['No.', 'Player(Team)','Record Offensive Rebounds']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_or['No.'], rec_or['Player(Team)'], rec_or['Record Offensive Rebounds']],
                align='center', font_size=16, height=30)))

            rec_or_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_or_fig)
        with bs:
            st.write("##### Best by Season on offensive rebounds in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_or = compute_player_mean_stats_season[['Player_Season', 'OR']].sort_values('OR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'OR': 'Average Offensive Rebounds', 'Player_Season': 'Player(Season)'})
            bs_or.drop("index", axis=1, inplace=True)
            bs_or = bs_or.reset_index()
            bs_or['No.'] = bs_or['index'] + 1
            bs_or_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    bs_or[['No.', 'Player(Season)', 'Average Offensive Rebounds']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_or['No.'], bs_or['Player(Season)'], bs_or['Average Offensive Rebounds']],
                align='center', font_size=16, height=30)))

            bs_or_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_or_fig)
    with der:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best on Season'])
        with av:
            st.write("##### Average defensive rebounds per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_dr = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','DR']].sort_values('DR',ascending=False).head(10).round(1).reset_index().rename(columns={'DR':'Defensive Rebounds'})
            av_dr.drop("index", axis=1, inplace=True)
            av_dr = av_dr.reset_index()
            av_dr['No.'] = av_dr['index'] + 1
            av_dr_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(av_dr[['No.', 'Player', 'Defensive Rebounds']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_or['No.'], av_dr.Player, av_dr['Defensive Rebounds']],
                align='center', font_size=16, height=30)))

            av_dr_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_dr_fig)
        with sum:
            st.write("##### Total defensive rebounds in Euroleague from 2016-2017 Season (Top 10)")
            tot_dr =compute_player_stats[['Player', 'Total_DR']].sort_values('Total_DR', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_DR':'Total Defensive Rebounds'})
            tot_dr.drop("index", axis=1, inplace=True)
            tot_dr = tot_dr.reset_index()
            tot_dr['No.'] = tot_dr['index'] + 1
            tot_dr_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    tot_dr[['No.', 'Player','Total Defensive Rebounds']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_dr['No.'], tot_dr.Player, tot_dr['Total Defensive Rebounds']],
                align='center', font_size=16, height=30)))

            tot_dr_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_dr_fig)
        with rec:
            st.write("##### Record defensive rebounds on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_dr =All_Seasons_filter[['Player_Team', 'DR']].sort_values('DR', ascending=False).head(10).round(
                1).reset_index().rename(columns={'DR':'Record Defensive Rebounds','Player_Team':'Player(Team)'})
            rec_dr.drop("index", axis=1, inplace=True)
            rec_dr = rec_dr.reset_index()
            rec_dr['No.'] = rec_dr['index'] + 1
            rec_dr_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    rec_dr[['No.', 'Player(Team)','Record Defensive Rebounds']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_dr['No.'], rec_dr['Player(Team)'], rec_dr['Record Defensive Rebounds']],
                align='center', font_size=16, height=30)))

            rec_dr_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_dr_fig)
        with bs:
            st.write("##### Best by Season on defensive rebounds in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_dr = compute_player_mean_stats_season[['Player_Season', 'DR']].sort_values('DR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'DR': 'Average Defensive Rebounds', 'Player_Season': 'Player(Season)'})
            bs_dr.drop("index", axis=1, inplace=True)
            bs_dr = bs_dr.reset_index()
            bs_dr['No.'] = bs_dr['index'] + 1
            bs_dr_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    bs_dr[['No.', 'Player(Season)', 'Average Defensive Rebounds']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_dr['No.'], bs_dr['Player(Season)'], bs_dr['Average Defensive Rebounds']],
                align='center', font_size=16, height=30)))

            bs_dr_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_dr_fig)
    with ste:
        av, sum, rec, bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best on Season'])
        with av:
            st.write("##### Average steals per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_st = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','ST']].sort_values('ST',ascending=False).head(10).round(1).reset_index().rename(columns={'ST':'Steals'})
            av_st.drop("index", axis=1, inplace=True)
            av_st = av_st.reset_index()
            av_st['No.'] = av_st['index'] + 1
            av_st_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(av_st[['No.', 'Player', 'Steals']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_or['No.'], av_st.Player, av_st['Steals']],
                align='center', font_size=16, height=30)))

            av_st_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_st_fig)
        with sum:
            st.write("##### Total steals in Euroleague from 2016-2017 Season (Top 10)")
            tot_st =compute_player_stats[['Player', 'Total_ST']].sort_values('Total_ST', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_ST':'Total Steals'})
            tot_st.drop("index", axis=1, inplace=True)
            tot_st = tot_st.reset_index()
            tot_st['No.'] = tot_st['index'] + 1
            tot_st_fig = go.Figure(data=go.Table(columnwidth=[1,5,5],header=dict(
                values=list(
                    tot_st[['No.', 'Player','Total Steals']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_st['No.'], tot_st.Player, tot_st['Total Steals']],
                align='center', font_size=16, height=30)))

            tot_st_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_st_fig)
        with rec:
            st.write("##### Record steals on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_st =All_Seasons_filter[['Player_Team', 'ST']].sort_values('ST', ascending=False).head(10).round(
                1).reset_index().rename(columns={'ST':'Record Steals','Player_Team':'Player(Team)'})
            rec_st.drop("index", axis=1, inplace=True)
            rec_st = rec_st.reset_index()
            rec_st['No.'] = rec_st['index'] + 1
            rec_st_fig = go.Figure(data=go.Table(columnwidth=[1,4,3],header=dict(
                values=list(
                    rec_st[['No.', 'Player(Team)','Record Steals']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_st['No.'], rec_st['Player(Team)'], rec_st['Record Steals']],
                align='center', font_size=16, height=30)))

            rec_st_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_st_fig)
        with bs:
            st.write("##### Best by Season on steals in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_st = compute_player_mean_stats_season[['Player_Season', 'ST']].sort_values('ST',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'ST': 'Average Steals', 'Player_Season': 'Player(Season)'})
            bs_st.drop("index", axis=1, inplace=True)
            bs_st = bs_st.reset_index()
            bs_st['No.'] = bs_st['index'] + 1
            bs_st_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    bs_st[['No.', 'Player(Season)', 'Average Steals']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_st['No.'], bs_st['Player(Season)'], bs_st['Average Steals']],
                align='center', font_size=16, height=30)))

            bs_st_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_st_fig)
    with tur:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats',"Best by season"])
        with av:
            st.write("##### Average turnovers per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_to = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','TO']].sort_values('TO',ascending=False).head(10).round(1).reset_index().rename(columns={'TO':'Turnovers'})
            av_to.drop("index", axis=1, inplace=True)
            av_to = av_to.reset_index()
            av_to['No.'] = av_to['index'] + 1
            av_to_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(av_to[['No.', 'Player', 'Turnovers']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_to['No.'], av_to.Player, av_to['Turnovers']],
                align='center', font_size=16, height=30)))

            av_to_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_to_fig)
        with sum:
            st.write("##### Total turnovers in Euroleague from 2016-2017 Season (Top 10)")
            tot_to =compute_player_stats[['Player', 'Total_TO']].sort_values('Total_TO', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_TO':'Total Turnovers'})
            tot_to.drop("index", axis=1, inplace=True)
            tot_to = tot_to.reset_index()
            tot_to['No.'] = tot_to['index'] + 1
            tot_to_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    tot_to[['No.', 'Player','Total Turnovers']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_to['No.'], tot_to.Player, tot_to['Total Turnovers']],
                align='center', font_size=16, height=30)))

            tot_to_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_to_fig)
        with rec:
            st.write("##### Record turnovers on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_to =All_Seasons_filter[['Player_Team', 'TO']].sort_values('TO', ascending=False).head(10).round(
                1).reset_index().rename(columns={'TO':'Record Turnovers','Player_Team':'Player(Team)'})
            rec_to.drop("index", axis=1, inplace=True)
            rec_to = rec_to.reset_index()
            rec_to['No.'] = rec_to['index'] + 1
            rec_to_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    rec_to[['No.', 'Player(Team)','Record Turnovers']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_to['No.'], rec_to['Player(Team)'], rec_to['Record Turnovers']],
                align='center', font_size=16, height=30)))

            rec_to_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_to_fig)
        with bs:
            st.write("##### Best by Season on turnovers in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_to = compute_player_mean_stats_season[['Player_Season', 'TO']].sort_values('TO',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'TO': 'Average Turnovers', 'Player_Season': 'Player(Season)'})
            bs_to.drop("index", axis=1, inplace=True)
            bs_to = bs_to.reset_index()
            bs_to['No.'] = bs_to['index'] + 1
            bs_to_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    bs_to[['No.', 'Player(Season)', 'Average Turnovers']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_to['No.'], bs_to['Player(Season)'], bs_to['Average Turnovers']],
                align='center', font_size=16, height=30)))

            bs_to_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_to_fig)
    with blk:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average blocks per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_blk = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','BLK']].sort_values('BLK',ascending=False).head(10).round(1).reset_index().rename(columns={'BLK':'Blocks'})
            av_blk.drop("index", axis=1, inplace=True)
            av_blk = av_blk.reset_index()
            av_blk['No.'] = av_blk['index'] + 1
            av_blk_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(av_blk[['No.', 'Player', 'Blocks']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_blk['No.'], av_blk.Player, av_blk['Blocks']],
                align='center', font_size=16, height=30)))

            av_blk_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_blk_fig)
        with sum:
            st.write("##### Total blocks in Euroleague from 2016-2017 Season (Top 10)")
            tot_blk =compute_player_stats[['Player', 'Total_BLK']].sort_values('Total_BLK', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'Total_BLK':'Total Blocks'})
            tot_blk.drop("index", axis=1, inplace=True)
            tot_blk = tot_blk.reset_index()
            tot_blk['No.'] = tot_blk['index'] + 1
            tot_blk_fig = go.Figure(data=go.Table(columnwidth=[1,6,4],header=dict(
                values=list(
                    tot_blk[['No.', 'Player','Total Blocks']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_blk['No.'], tot_blk.Player, tot_blk['Total Blocks']],
                align='center', font_size=16, height=30)))

            tot_blk_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_blk_fig)
        with rec:
            st.write("##### Record blocks on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_blk =All_Seasons_filter[['Player_Team', 'BLK']].sort_values('BLK', ascending=False).head(10).round(
                1).reset_index().rename(columns={'BLK':'Record Blocks','Player_Team':'Player(Team)'})
            rec_blk.drop("index", axis=1, inplace=True)
            rec_blk = rec_blk.reset_index()
            rec_blk['No.'] = rec_blk['index'] + 1
            rec_blk_fig = go.Figure(data=go.Table(columnwidth=[1,6,4],header=dict(
                values=list(
                    rec_blk[['No.', 'Player(Team)','Record Blocks']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_blk['No.'], rec_blk['Player(Team)'], rec_blk['Record Blocks']],
                align='center', font_size=16, height=30)))

            rec_blk_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_blk_fig)
        with bs:
            st.write("##### Best by Season on blocks in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_blk = compute_player_mean_stats_season[['Player_Season', 'BLK']].sort_values('BLK',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'BLK': 'Average Blocks', 'Player_Season': 'Player(Season)'})
            bs_blk.drop("index", axis=1, inplace=True)
            bs_blk = bs_blk.reset_index()
            bs_blk['No.'] = bs_blk['index'] + 1
            bs_blk_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    bs_blk[['No.', 'Player(Season)', 'Average Blocks']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_blk['No.'], bs_blk['Player(Season)'], bs_blk['Average Blocks']],
                align='center', font_size=16, height=30)))

            bs_blk_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_blk_fig)
    with blkr:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average blocks reversed per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_blkr = compute_player_stats.loc[compute_player_stats['Games'] > games][['Player', 'BLKR']].sort_values(
                'BLKR', ascending=False).head(10).round(1).reset_index().rename(columns={'BLKR': 'Blocks Reversed'})
            av_blkr.drop("index", axis=1, inplace=True)
            av_blkr = av_blkr.reset_index()
            av_blkr['No.'] = av_blkr['index'] + 1
            av_blkr_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(av_blkr[['No.', 'Player', 'Blocks Reversed']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_blkr['No.'], av_blkr.Player, av_blkr['Blocks Reversed']],
                align='center', font_size=16, height=30)))

            av_blkr_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_blkr_fig)
        with sum:
            st.write("##### Total blocks reversed in Euroleague from 2016-2017 Season (Top 10)")
            tot_blkr = compute_player_stats[['Player', 'Total_BLKR']].sort_values('Total_BLKR', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_BLKR': 'Total Blocks Reversed'})
            tot_blkr.drop("index", axis=1, inplace=True)
            tot_blkr = tot_blkr.reset_index()
            tot_blkr['No.'] = tot_blkr['index'] + 1
            tot_blkr_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    tot_blkr[['No.', 'Player', 'Total Blocks Reversed']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_blkr['No.'], tot_blkr.Player, tot_blkr['Total Blocks Reversed']],
                align='center', font_size=16, height=30)))

            tot_blkr_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_blkr_fig)
        with rec:
            st.write("##### Record blocks reversed on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_blkr =All_Seasons_filter[['Player_Team', 'BLKR']].sort_values('BLKR', ascending=False).head(10).round(
                1).reset_index().rename(columns={'BLKR':'Record Blocks Reversed','Player_Team':'Player(Team)'})
            rec_blkr.drop("index", axis=1, inplace=True)
            rec_blkr = rec_blkr.reset_index()
            rec_blkr['No.'] = rec_blkr['index'] + 1
            rec_blkr_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    rec_blkr[['No.', 'Player(Team)','Record Blocks Reversed']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_blkr['No.'], rec_blkr['Player(Team)'], rec_blkr['Record Blocks Reversed']],
                align='center', font_size=16, height=30)))

            rec_blkr_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_blkr_fig)
        with bs:
            st.write("##### Best by Season on blocks in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_blkr = compute_player_mean_stats_season[['Player_Season', 'BLKR']].sort_values('BLKR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'BLKR': 'Average Blocks Reversed', 'Player_Season': 'Player(Season)'})
            bs_blkr.drop("index", axis=1, inplace=True)
            bs_blkr = bs_blkr.reset_index()
            bs_blkr['No.'] = bs_blkr['index'] + 1
            bs_blkr_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    bs_blkr[['No.', 'Player(Season)', 'Average Blocks Reversed']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_blkr['No.'], bs_blkr['Player(Season)'], bs_blkr['Average Blocks Reversed']],
                align='center', font_size=16, height=30)))

            bs_blkr_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_blkr_fig)
    with pf:
        av, sum,bs = st.tabs(['Average Stats', 'Total Stats',"Best by Season"])
        with av:
            st.write("##### Average personal fouls per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_pf = compute_player_stats.loc[compute_player_stats['Games'] > games][['Player', 'PF']].sort_values(
                'PF', ascending=False).head(10).round(1).reset_index().rename(columns={'PF': 'Personal Fouls'})
            av_pf.drop("index", axis=1, inplace=True)
            av_pf = av_pf.reset_index()
            av_pf['No.'] = av_pf['index'] + 1
            av_pf_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(av_pf[['No.', 'Player', 'Personal Fouls']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_pf['No.'], av_pf.Player, av_pf['Personal Fouls']],
                align='center', font_size=16, height=30)))

            av_pf_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_pf_fig)
        with sum:
            st.write("##### Total personal fouls in Euroleague from 2016-2017 Season (Top 10)")
            tot_pf = compute_player_stats[['Player', 'Total_PF']].sort_values('Total_PF', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_PF': 'Total Personal Fouls'})
            tot_pf.drop("index", axis=1, inplace=True)
            tot_pf = tot_pf.reset_index()
            tot_pf['No.'] = tot_pf['index'] + 1
            tot_pf_fig = go.Figure(data=go.Table(columnwidth=[1,5,5],header=dict(
                values=list(
                    tot_pf[['No.', 'Player', 'Total Personal Fouls']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_pf['No.'], tot_pf.Player, tot_pf['Total Personal Fouls']],
                align='center', font_size=16, height=30)))

            tot_pf_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_pf_fig)
        with bs:
            st.write("##### Best by Season on personal fouls in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_pf = compute_player_mean_stats_season[['Player_Season', 'PF']].sort_values('PF',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'PF': 'Average Personal Fouls', 'Player_Season': 'Player(Season)'})
            bs_pf.drop("index", axis=1, inplace=True)
            bs_pf = bs_pf.reset_index()
            bs_pf['No.'] = bs_pf['index'] + 1
            bs_pf_fig = go.Figure(data=go.Table(columnwidth=[1,5,5],header=dict(
                values=list(
                    bs_pf[['No.', 'Player(Season)', 'Average Personal Fouls']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_pf['No.'], bs_pf['Player(Season)'], bs_pf['Average Personal Fouls']],
                align='center', font_size=16, height=30)))

            bs_pf_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_pf_fig)
    with rf:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average fouls drawn per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_rf = compute_player_stats.loc[compute_player_stats['Games'] > games][['Player', 'RF']].sort_values(
                'RF', ascending=False).head(10).round(1).reset_index().rename(columns={'RF': 'Fouls Drawn'})
            av_rf.drop("index", axis=1, inplace=True)
            av_rf = av_rf.reset_index()
            av_rf['No.'] = av_rf['index'] + 1
            av_rf_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(av_rf[['No.', 'Player', 'Fouls Drawn']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_rf['No.'], av_rf.Player, av_rf['Fouls Drawn']],
                align='center', font_size=16, height=30)))

            av_rf_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_rf_fig)
        with sum:
            st.write("##### Total fouls drawn in Euroleague from 2016-2017 Season (Top 10)")
            tot_rf = compute_player_stats[['Player', 'Total_RF']].sort_values('Total_RF', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_RF': 'Total Fouls Drawn'})
            tot_rf.drop("index", axis=1, inplace=True)
            tot_rf = tot_rf.reset_index()
            tot_rf['No.'] = tot_rf['index'] + 1
            tot_rf_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    tot_rf[['No.', 'Player', 'Total Fouls Drawn']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_rf['No.'], tot_rf.Player, tot_rf['Total Fouls Drawn']],
                align='center', font_size=16, height=30)))

            tot_rf_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_rf_fig)
        with rec:
            st.write("##### Record fouls drawn on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_rf =All_Seasons_filter[['Player_Team', 'RF']].sort_values('RF', ascending=False).head(10).round(
                1).reset_index().rename(columns={'RF':'Record Fouls Drawn','Player_Team':'Player(Team)'})
            rec_rf.drop("index", axis=1, inplace=True)
            rec_rf = rec_rf.reset_index()
            rec_rf['No.'] = rec_rf['index'] + 1
            rec_rf_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    rec_rf[['No.', 'Player(Team)','Record Fouls Drawn']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_rf['No.'], rec_rf['Player(Team)'], rec_rf['Record Fouls Drawn']],
                align='center', font_size=16, height=30)))

            rec_rf_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_rf_fig)
        with bs:
            st.write("##### Best by Season on fouls drawn in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_rf = compute_player_mean_stats_season[['Player_Season', 'RF']].sort_values('RF',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'RF': 'Average Fouls Drawn', 'Player_Season': 'Player(Season)'})
            bs_rf.drop("index", axis=1, inplace=True)
            bs_rf = bs_rf.reset_index()
            bs_rf['No.'] = bs_rf['index'] + 1
            bs_rf_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    bs_rf[['No.', 'Player(Season)', 'Average Fouls Drawn']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_rf['No.'], bs_rf['Player(Season)'], bs_rf['Average Fouls Drawn']],
                align='center', font_size=16, height=30)))

            bs_rf_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_rf_fig)
with shooting:
    f2m,f2a,p2,f3m,f3a,p3,ftm,fta,pft=st.tabs(['2P Made',"2P Attempt","2P(%)",'3P Made',"3P Attempt","3P(%)",'Free Throws Made',"Free Throws Attempt","FT(%)"])
    with f2m:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average 2p made per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_F2M = compute_player_stats.loc[compute_player_stats['Total_F2A']>Shoots][['Player','F2M']].sort_values('F2M',ascending=False).head(10).round(1).reset_index().rename(columns={'F2M': '2P Made'})
            av_F2M.drop("index", axis=1, inplace=True)
            av_F2M = av_F2M.reset_index()
            av_F2M['No.'] = av_F2M['index'] + 1
            av_F2M_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(av_F2M[['No.', 'Player', '2P Made']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_F2M['No.'], av_F2M.Player, av_F2M['2P Made']],
                align='center', font_size=16, height=30)))

            av_F2M_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_F2M_fig)
        with sum:
            st.write("##### Total 2p made in Euroleague from 2016-2017 Season (Top 10)")
            tot_f2m = compute_player_stats[['Player', 'Total_F2M']].sort_values('Total_F2M', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_F2M': 'Total 2P Made'})
            tot_f2m.drop("index", axis=1, inplace=True)
            tot_f2m = tot_f2m.reset_index()
            tot_f2m['No.'] = tot_f2m['index'] + 1
            tot_f2m_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    tot_f2m[['No.', 'Player', 'Total 2P Made']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_f2m['No.'], tot_f2m.Player, tot_f2m['Total 2P Made']],
                align='center', font_size=16, height=30)))

            tot_f2m_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_f2m_fig)
        with rec:
            st.write("##### Record 2p made on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_f2m =All_Seasons_filter[['Player_Team', 'F2M']].sort_values('F2M', ascending=False).head(10).round(
                1).reset_index().rename(columns={'F2M':'Record 2P Made','Player_Team':'Player(Team)'})
            rec_f2m.drop("index", axis=1, inplace=True)
            rec_f2m = rec_f2m.reset_index()
            rec_f2m['No.'] = rec_f2m['index'] + 1
            rec_f2m_fig = go.Figure(data=go.Table(columnwidth=[1,5,4],header=dict(
                values=list(
                    rec_f2m[['No.', 'Player(Team)','Record 2P Made']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_f2m['No.'], rec_f2m['Player(Team)'], rec_f2m['Record 2P Made']],
                align='center', font_size=16, height=30)))

            rec_f2m_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_f2m_fig)
        with bs:
            st.write("##### Best by Season on 2p made in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_f2m = compute_player_mean_stats_season[['Player_Season', 'F2M']].sort_values('F2M',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'F2M': 'Average 2P Made', 'Player_Season': 'Player(Season)'})
            bs_f2m.drop("index", axis=1, inplace=True)
            bs_f2m = bs_f2m.reset_index()
            bs_f2m['No.'] = bs_f2m['index'] + 1
            bs_f2m_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    bs_f2m[['No.', 'Player(Season)', 'Average 2P Made']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_f2m['No.'], bs_f2m['Player(Season)'], bs_f2m['Average 2P Made']],
                align='center', font_size=16, height=30)))

            bs_f2m_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_f2m_fig)
    with f2a:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average 2p attempt per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_F2A = compute_player_stats.loc[compute_player_stats['Total_F2A']>Shoots][['Player','F2A']].sort_values('F2A',ascending=False).head(10).round(1).reset_index().rename(columns={'F2A': '2P Attempt'})
            av_F2A.drop("index", axis=1, inplace=True)
            av_F2A = av_F2A.reset_index()
            av_F2A['No.'] = av_F2A['index'] + 1
            av_F2A_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_F2A[['No.', 'Player', '2P Attempt']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_F2A['No.'], av_F2A.Player, av_F2A['2P Attempt']],
                align='center', font_size=16, height=30)))

            av_F2A_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_F2A_fig)

        with sum:
            st.write("##### Total 2p attempt in Euroleague from 2016-2017 Season (Top 10)")
            tot_f2a = compute_player_stats[['Player', 'Total_F2A']].sort_values('Total_F2A', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_F2A': 'Total 2P Attempt'})
            tot_f2a.drop("index", axis=1, inplace=True)
            tot_f2a = tot_f2a.reset_index()
            tot_f2a['No.'] = tot_f2a['index'] + 1
            tot_f2a_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    tot_f2a[['No.', 'Player', 'Total 2P Attempt']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_f2a['No.'], tot_f2a.Player, tot_f2a['Total 2P Attempt']],
                align='center', font_size=16, height=30)))

            tot_f2a_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_f2a_fig)
        with rec:
            st.write("##### Record 2p attempt on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_f2a =All_Seasons_filter[['Player_Team', 'F2A']].sort_values('F2A', ascending=False).head(10).round(
                1).reset_index().rename(columns={'F2A':'Record 2P Attempt','Player_Team':'Player(Team)'})
            rec_f2a.drop("index", axis=1, inplace=True)
            rec_f2a = rec_f2a.reset_index()
            rec_f2a['No.'] = rec_f2a['index'] + 1
            rec_f2a_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    rec_f2a[['No.', 'Player(Team)','Record 2P Attempt']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_f2a['No.'], rec_f2a['Player(Team)'], rec_f2a['Record 2P Attempt']],
                align='center', font_size=16, height=30)))

            rec_f2a_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_f2a_fig)
        with bs:
            st.write("##### Best by Season on 2p attempt in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_f2a = compute_player_mean_stats_season[['Player_Season', 'F2A']].sort_values('F2A',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'F2A': 'Average 2P Attempt', 'Player_Season': 'Player(Season)'})
            bs_f2a.drop("index", axis=1, inplace=True)
            bs_f2a = bs_f2a.reset_index()
            bs_f2a['No.'] = bs_f2a['index'] + 1
            bs_f2a_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_f2a[['No.', 'Player(Season)', 'Average 2P Attempt']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_f2a['No.'], bs_f2a['Player(Season)'], bs_f2a['Average 2P Attempt']],
                align='center', font_size=16, height=30)))

            bs_f2a_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_f2a_fig)
    with p2:
        av,  bs = st.tabs(['Total Stats', 'Best by Season'])
        with av:

            st.write("##### Percentage of 2p per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_P2 = compute_player_stats.loc[compute_player_stats['Total_F2A']>Shoots][['Player','P2']].sort_values('P2',ascending=False).head(10).round(1).reset_index().rename(columns={'P2': '2P(%)'})
            av_P2.drop("index", axis=1, inplace=True)
            av_P2 = av_P2.reset_index()
            av_P2['No.'] = av_P2['index'] + 1
            av_P2_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(av_P2[['No.', 'Player', '2P(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_P2['No.'], av_P2.Player, av_P2['2P(%)']],
                align='center', font_size=16, height=30)))

            av_P2_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_P2_fig)

        with bs:
            st.write(
                "##### Best by Season on 2P percentage in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games  & at least 100 of 2P attempts in the season)")
            bs_P2 = compute_player_mean_stats_season.loc[ compute_player_mean_stats_season['Total_F2A']>=100][['Player_Season', 'P2']].sort_values('P2',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'P2': '2P(%)', 'Player_Season': 'Player(Season)'})
            bs_P2.drop("index", axis=1, inplace=True)
            bs_P2 = bs_P2.reset_index()
            bs_P2['No.'] = bs_P2['index'] + 1
            bs_P2_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(
                    bs_P2[['No.', 'Player(Season)', '2P(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_P2['No.'], bs_P2['Player(Season)'], bs_P2['2P(%)']],
                align='center', font_size=16, height=30)))

            bs_P2_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_P2_fig)

    with f3m:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average 3p made per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_F3M = compute_player_stats.loc[compute_player_stats['Total_F3A']>Shoots][['Player','F3M']].sort_values('F3M',ascending=False).head(10).round(1).reset_index().rename(columns={'F3M': '3P Made'})
            av_F3M.drop("index", axis=1, inplace=True)
            av_F3M = av_F3M.reset_index()
            av_F3M['No.'] = av_F3M['index'] + 1
            av_F3M_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_F3M[['No.', 'Player', '3P Made']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_F3M['No.'], av_F3M.Player, av_F3M['3P Made']],
                align='center', font_size=16, height=30)))

            av_F3M_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_F3M_fig)

            with sum:
                st.write("##### Total 3p made in Euroleague from 2016-2017 Season (Top 10)")
                tot_f3m = compute_player_stats[['Player', 'Total_F3M']].sort_values('Total_F3M', ascending=False).head(
                    10).round(
                    1).reset_index().rename(columns={'Total_F3M': 'Total 3P Made'})
                tot_f3m.drop("index", axis=1, inplace=True)
                tot_f3m = tot_f3m.reset_index()
                tot_f3m['No.'] = tot_f3m['index'] + 1
                tot_f3m_fig = go.Figure(data=go.Table(header=dict(
                    values=list(
                        tot_f3m[['No.', 'Player', 'Total 3P Made']].columns),
                    align='center', font_size=18, height=30), cells=dict(
                    values=[tot_f3m['No.'], tot_f3m.Player, tot_f3m['Total 3P Made']],
                    align='center', font_size=16, height=30)))

                tot_f3m_fig.update_layout(
                    autosize=True,
                    width=600,
                    height=550,
                    margin=dict(
                        l=30,
                        r=50,
                        b=100,
                        t=80,
                        pad=10
                    ))

                st.write(tot_f3m_fig)
            with rec:
                st.write("##### Record 3p made on a game in Euroleague from 2016-2017 Season (Top 10)")
                rec_f3m = All_Seasons_filter[['Player_Team', 'F3M']].sort_values('F3M', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'F3M': 'Record 3P Made', 'Player_Team': 'Player(Team)'})
                rec_f3m.drop("index", axis=1, inplace=True)
                rec_f3m = rec_f3m.reset_index()
                rec_f3m['No.'] = rec_f3m['index'] + 1
                rec_f3m_fig = go.Figure(data=go.Table(header=dict(
                    values=list(
                        rec_f3m[['No.', 'Player(Team)', 'Record 3P Made']].columns),
                    align='center', font_size=18, height=30), cells=dict(
                    values=[rec_f3m['No.'], rec_f3m['Player(Team)'], rec_f3m['Record 3P Made']],
                    align='center', font_size=16, height=30)))

                rec_f3m_fig.update_layout(
                    autosize=True,
                    width=1000,
                    height=800,
                    margin=dict(
                        l=1,
                        r=1,
                        b=100,
                        t=80,
                        pad=10
                    ))

                st.write(rec_f3m_fig)

        with bs:
            st.write("##### Best by Season on 3p made in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_f3m = compute_player_mean_stats_season[['Player_Season', 'F3M']].sort_values('F3M',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'F3M': 'Average 3P Made', 'Player_Season': 'Player(Season)'})
            bs_f3m.drop("index", axis=1, inplace=True)
            bs_f3m = bs_f3m.reset_index()
            bs_f3m['No.'] = bs_f3m['index'] + 1
            bs_f3m_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_f3m[['No.', 'Player(Season)', 'Average 3P Made']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_f3m['No.'], bs_f3m['Player(Season)'], bs_f3m['Average 3P Made']],
                align='center', font_size=16, height=30)))

            bs_f3m_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_f3m_fig)
    with f3a:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average 3p attempt per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_F3A = compute_player_stats.loc[compute_player_stats['Total_F3A']>Shoots][['Player','F3A']].sort_values('F3A',ascending=False).head(10).round(1).reset_index().rename(columns={'F3A': '3P Attempt'})
            av_F3A.drop("index", axis=1, inplace=True)
            av_F3A = av_F3A.reset_index()
            av_F3A['No.'] = av_F3A['index'] + 1
            av_F3A_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_F3A[['No.', 'Player', '3P Attempt']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_F3A['No.'], av_F3A.Player, av_F3A['3P Attempt']],
                align='center', font_size=16, height=30)))

            av_F3A_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_F3A_fig)

            with sum:
                st.write("##### Total 3p attempt in Euroleague from 2016-2017 Season (Top 10)")
                tot_f3a = compute_player_stats[['Player', 'Total_F3A']].sort_values('Total_F3A', ascending=False).head(
                    10).round(
                    1).reset_index().rename(columns={'Total_F3A': 'Total 3P Attempt'})
                tot_f3a.drop("index", axis=1, inplace=True)
                tot_f3a = tot_f3a.reset_index()
                tot_f3a['No.'] = tot_f3a['index'] + 1
                tot_f3a_fig = go.Figure(data=go.Table(header=dict(
                    values=list(
                        tot_f3a[['No.', 'Player', 'Total 3P Attempt']].columns),
                    align='center', font_size=18, height=30), cells=dict(
                    values=[tot_f3a['No.'], tot_f3a.Player, tot_f3a['Total 3P Attempt']],
                    align='center', font_size=16, height=30)))

                tot_f3a_fig.update_layout(
                    autosize=True,
                    width=600,
                    height=550,
                    margin=dict(
                        l=30,
                        r=50,
                        b=100,
                        t=80,
                        pad=10
                    ))

                st.write(tot_f3a_fig)
            with rec:
                st.write("##### Record 3p attempt on a game in Euroleague from 2016-2017 Season (Top 10)")
                rec_f3a =All_Seasons_filter[['Player_Team', 'F3A']].sort_values('F3A', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'F3A':'Record 3P Attempt','Player_Team':'Player(Team)'})
                rec_f3a.drop("index", axis=1, inplace=True)
                rec_f3a = rec_f3a.reset_index()
                rec_f3a['No.'] = rec_f3a['index'] + 1
                rec_f3a_fig = go.Figure(data=go.Table(header=dict(
                    values=list(
                        rec_f3a[['No.', 'Player(Team)','Record 3P Attempt']].columns),
                    align='center', font_size=18, height=30), cells=dict(
                    values=[rec_f3a['No.'], rec_f3a['Player(Team)'], rec_f3a['Record 3P Attempt']],
                    align='center', font_size=16, height=30)))

                rec_f3a_fig.update_layout(
                    autosize=True,
                    width=1000,
                    height=800,
                    margin=dict(
                        l=1,
                        r=1,
                        b=100,
                        t=80,
                        pad=10
                    ))

                st.write(rec_f3a_fig)
            with bs:
                st.write(
                    "##### Best by Season on 3p attempt in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
                bs_f3a = compute_player_mean_stats_season[['Player_Season', 'F3A']].sort_values('F3A',
                                                                                                ascending=False).head(
                    10).round(
                    1).reset_index().rename(columns={'F3A': 'Average 3P Attempt', 'Player_Season': 'Player(Season)'})
                bs_f3a.drop("index", axis=1, inplace=True)
                bs_f3a = bs_f3a.reset_index()
                bs_f3a['No.'] = bs_f3a['index'] + 1
                bs_f3a_fig = go.Figure(data=go.Table(header=dict(
                    values=list(
                        bs_f3a[['No.', 'Player(Season)', 'Average 3P Attempt']].columns),
                    align='center', font_size=18, height=30), cells=dict(
                    values=[bs_f3a['No.'], bs_f3a['Player(Season)'], bs_f3a['Average 3P Attempt']],
                    align='center', font_size=16, height=30)))

                bs_f3a_fig.update_layout(
                    autosize=True,
                    width=1000,
                    height=800,
                    margin=dict(
                        l=1,
                        r=1,
                        b=100,
                        t=80,
                        pad=10
                    ))

                st.write(bs_f3a_fig)
    with p3:
        av, bs = st.tabs(['Total Stats', 'Best by Season'])
        with av:
            st.write("##### Percentage of 3p per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_P3 = compute_player_stats.loc[compute_player_stats['Total_F3A']>Shoots][['Player','P3']].sort_values('P3',ascending=False).head(10).round(1).reset_index().rename(columns={'P3': '3P(%)'})
            av_P3.drop("index", axis=1, inplace=True)
            av_P3 = av_P3.reset_index()
            av_P3['No.'] = av_P3['index'] + 1
            av_P3_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_P3[['No.', 'Player', '3P(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_P3['No.'], av_P3.Player, av_P3['3P(%)']],
                align='center', font_size=16, height=30)))

            av_P3_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_P3_fig)

        with bs:
            st.write(
                "##### Best by Season on 3P percentage in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games  & at least 100 of 3P attempts in the season)")
            bs_P3 = compute_player_mean_stats_season.loc[ compute_player_mean_stats_season['Total_F3A']>=100][['Player_Season', 'P3']].sort_values('P3',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'P3': '3P(%)', 'Player_Season': 'Player(Season)'})
            bs_P3.drop("index", axis=1, inplace=True)
            bs_P3 = bs_P3.reset_index()
            bs_P3['No.'] = bs_P3['index'] + 1
            bs_P3_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_P3[['No.', 'Player(Season)', '3P(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_P3['No.'], bs_P3['Player(Season)'], bs_P3['3P(%)']],
                align='center', font_size=16, height=30)))

            bs_P3_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_P3_fig)

    with ftm:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average free throws made per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_FTM = compute_player_stats.loc[compute_player_stats['Total_FTA']>Shoots][['Player','FTM']].sort_values('FTM',ascending=False).head(10).round(1).reset_index().rename(columns={'FTM': 'Free Throws Made'})
            av_FTM.drop("index", axis=1, inplace=True)
            av_FTM = av_FTM.reset_index()
            av_FTM['No.'] = av_FTM['index'] + 1
            av_FTM_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_FTM[['No.', 'Player', 'Free Throws Made']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_FTM['No.'], av_FTM.Player, av_FTM['Free Throws Made']],
                align='center', font_size=16, height=30)))

            av_FTM_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_FTM_fig)

            st.write('For better results move the Shoots slider')
            with sum:
                st.write("##### Total free throws made in Euroleague from 2016-2017 Season (Top 10)")
                tot_ftm = compute_player_stats[['Player', 'Total_FTM']].sort_values('Total_FTM', ascending=False).head(
                    10).round(
                    1).reset_index().rename(columns={'Total_FTM': 'Total Free throws Made'})
                tot_ftm.drop("index", axis=1, inplace=True)
                tot_ftm = tot_ftm.reset_index()
                tot_ftm['No.'] = tot_ftm['index'] + 1
                tot_ftm_fig = go.Figure(data=go.Table(header=dict(
                    values=list(
                        tot_ftm[['No.', 'Player', 'Total Free throws Made']].columns),
                    align='center', font_size=18, height=30), cells=dict(
                    values=[tot_ftm['No.'], tot_ftm.Player, tot_ftm['Total Free throws Made']],
                    align='center', font_size=16, height=30)))

                tot_ftm_fig.update_layout(
                    autosize=True,
                    width=600,
                    height=550,
                    margin=dict(
                        l=30,
                        r=50,
                        b=100,
                        t=80,
                        pad=10
                    ))

                st.write(tot_ftm_fig)

            with rec:
                st.write("##### Record free throws made on a game in Euroleague from 2016-2017 Season (Top 10)")
                rec_ftm = All_Seasons_filter[['Player_Team', 'FTM']].sort_values('FTM', ascending=False).head(10).round(
                    1).reset_index().rename(columns={'FTM': 'Record Free throws Made', 'Player_Team': 'Player(Team)'})
                rec_ftm.drop("index", axis=1, inplace=True)
                rec_ftm = rec_ftm.reset_index()
                rec_ftm['No.'] = rec_ftm['index'] + 1
                rec_ftm_fig = go.Figure(data=go.Table(header=dict(
                    values=list(
                        rec_ftm[['No.', 'Player(Team)', 'Record Free throws Made']].columns),
                    align='center', font_size=18, height=30), cells=dict(
                    values=[rec_ftm['No.'], rec_ftm['Player(Team)'], rec_ftm['Record Free throws Made']],
                    align='center', font_size=16, height=30)))

                rec_ftm_fig.update_layout(
                    autosize=True,
                    width=1000,
                    height=800,
                    margin=dict(
                        l=1,
                        r=1,
                        b=100,
                        t=80,
                        pad=10
                    ))

                st.write(rec_ftm_fig)
            with bs:
                st.write(
                    "##### Best by Season on Free throws made in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
                bs_ftm = compute_player_mean_stats_season[['Player_Season', 'FTM']].sort_values('FTM',
                                                                                                ascending=False).head(
                    10).round(
                    1).reset_index().rename(columns={'FTM': 'Average Free Throws Made', 'Player_Season': 'Player(Season)'})
                bs_ftm.drop("index", axis=1, inplace=True)
                bs_ftm = bs_ftm.reset_index()
                bs_ftm['No.'] = bs_ftm['index'] + 1
                bs_ftm_fig = go.Figure(data=go.Table(header=dict(
                    values=list(
                        bs_ftm[['No.', 'Player(Season)', 'Average Free Throws Made']].columns),
                    align='center', font_size=18, height=30), cells=dict(
                    values=[bs_ftm['No.'], bs_ftm['Player(Season)'], bs_ftm['Average Free Throws Made']],
                    align='center', font_size=16, height=30)))

                bs_ftm_fig.update_layout(
                    autosize=True,
                    width=1000,
                    height=800,
                    margin=dict(
                        l=1,
                        r=1,
                        b=100,
                        t=80,
                        pad=10
                    ))

                st.write(bs_ftm_fig)
    with fta:
        av, sum, rec,bs = st.tabs(['Average Stats', 'Total Stats', 'Record Stats','Best by Season'])
        with av:
            st.write("##### Average free throws attempt per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_FTA = compute_player_stats.loc[compute_player_stats['Total_FTA']>Shoots][['Player','FTA']].sort_values('FTA',ascending=False).head(10).round(1).reset_index().rename(columns={'FTA': 'Free Throws Attempt'})
            av_FTA.drop("index", axis=1, inplace=True)
            av_FTA = av_FTA.reset_index()
            av_FTA['No.'] = av_FTA['index'] + 1
            av_FTA_fig = go.Figure(data=go.Table(columnwidth=[1,5,3],header=dict(
                values=list(av_FTA[['No.', 'Player', 'Free Throws Attempt']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_FTA['No.'], av_FTA.Player, av_FTA['Free Throws Attempt']],
                align='center', font_size=16, height=30)))

            av_FTA_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_FTA_fig)
        with sum:
            st.write("##### Total free throws attempt in Euroleague from 2016-2017 Season (Top 10)")
            tot_fta = compute_player_stats[['Player', 'Total_FTA']].sort_values('Total_FTA', ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'Total_FTA': 'Total Free throws Attempt'})
            tot_fta.drop("index", axis=1, inplace=True)
            tot_fta = tot_fta.reset_index()
            tot_fta['No.'] = tot_fta['index'] + 1
            tot_fta_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    tot_fta[['No.', 'Player', 'Total Free throws Attempt']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[tot_fta['No.'], tot_fta.Player, tot_fta['Total Free throws Attempt']],
                align='center', font_size=16, height=30)))

            tot_fta_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(tot_fta_fig)
        with rec:
            st.write("##### Record free throws attempt on a game in Euroleague from 2016-2017 Season (Top 10)")
            rec_fta = All_Seasons_filter[['Player_Team', 'FTA']].sort_values('FTA', ascending=False).head(10).round(
                1).reset_index().rename(columns={'FTA': 'Record Free throws Attempt', 'Player_Team': 'Player(Team)'})
            rec_fta.drop("index", axis=1, inplace=True)
            rec_fta = rec_fta.reset_index()
            rec_fta['No.'] = rec_fta['index'] + 1
            rec_fta_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    rec_fta[['No.', 'Player(Team)', 'Record Free throws Attempt']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[rec_fta['No.'], rec_fta['Player(Team)'], rec_fta['Record Free throws Attempt']],
                align='center', font_size=16, height=30)))

            rec_fta_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(rec_fta_fig)
        with bs:
            st.write(
                "##### Best by Season on Free throws attempt in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_fta = compute_player_mean_stats_season[['Player_Season', 'FTA']].sort_values('FTA',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'FTA': 'Average Free Throws Attempt', 'Player_Season': 'Player(Season)'})
            bs_fta.drop("index", axis=1, inplace=True)
            bs_fta = bs_fta.reset_index()
            bs_fta['No.'] = bs_fta['index'] + 1
            bs_fta_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_fta[['No.', 'Player(Season)', 'Average Free Throws Attempt']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_fta['No.'], bs_fta['Player(Season)'], bs_fta['Average Free Throws Attempt']],
                align='center', font_size=16, height=30)))

            bs_fta_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_fta_fig)
    with pft:
        av, bs = st.tabs(['Total Stats', 'Best by Season'])
        with av:
            st.write("##### Percentage of free throws per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_PFT = compute_player_stats.loc[compute_player_stats['Total_FTA']>Shoots][['Player','PFT']].sort_values('PFT',ascending=False).head(10).round(1).reset_index().rename(columns={'PFT': 'FT(%)'})
            av_PFT.drop("index", axis=1, inplace=True)
            av_PFT = av_PFT.reset_index()
            av_PFT['No.'] = av_PFT['index'] + 1
            av_PFT_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_PFT[['No.', 'Player', 'FT(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_PFT['No.'], av_PFT.Player, av_PFT['FT(%)']],
                align='center', font_size=16, height=30)))

            av_PFT_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_PFT_fig)
        with bs:
            st.write(
                "##### Best by Season on FT percentage in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games  & at least 100 of FT attempts in the season)")
            bs_PFT = compute_player_mean_stats_season.loc[ compute_player_mean_stats_season['Total_FTA']>=100][['Player_Season', 'PFT']].sort_values('PFT',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'PFT': 'FT(%)', 'Player_Season': 'Player(Season)'})
            bs_PFT.drop("index", axis=1, inplace=True)
            bs_PFT = bs_PFT.reset_index()
            bs_PFT['No.'] = bs_PFT['index'] + 1
            bs_PFT_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_PFT[['No.', 'Player(Season)', 'FT(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_PFT['No.'], bs_PFT['Player(Season)'], bs_PFT['FT(%)']],
                align='center', font_size=16, height=30)))

            bs_PFT_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_PFT_fig)



with advanced:
    pos, ora, efg, ts, ftr, astor, tor, asr, usg,orp = st.tabs(
        ['Possessions', "Offensive Rating", "EFG(%)", 'TS(%)', "Free Throw Ratio", "Assists - Turnover Ratio", 'Turnover Ratio',
         "Assists Ratio", "Usage(%)",'OR(%)'])
    with pos:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Average possesions per game in Euroleague from 2016-2017 Season (Top 10)")
            av_POS = compute_player_stats[['Player','POS']].sort_values('POS',ascending=False).head(10).round(1).reset_index().rename(columns={'POS': 'Possesions'})
            av_POS.drop("index", axis=1, inplace=True)
            av_POS = av_POS.reset_index()
            av_POS['No.'] = av_POS['index'] + 1
            av_POS_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_POS[['No.', 'Player', 'Possesions']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_POS['No.'], av_POS.Player, av_POS['Possesions']],
                align='center', font_size=16, height=30)))

            av_POS_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_POS_fig)
        with bs:
            st.write(
                "##### Best by Season on average possesions per game in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_POS = compute_player_mean_stats_season[['Player_Season', 'POS']].sort_values('POS',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'POS': 'Possesions', 'Player_Season': 'Player(Season)'})
            bs_POS.drop("index", axis=1, inplace=True)
            bs_POS = bs_POS.reset_index()
            bs_POS['No.'] = bs_POS['index'] + 1
            bs_POS_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_POS[['No.', 'Player(Season)', 'Possesions']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_POS['No.'], bs_POS['Player(Season)'], bs_POS['Possesions']],
                align='center', font_size=16, height=30)))

            bs_POS_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_POS_fig)

    with ora:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Offensive Rating per game in Euroleague from 2016-2017 Season (Top 10)")
            av_ORA = compute_player_stats.loc[compute_player_stats['POS']>10][['Player','ORA']].sort_values('ORA',ascending=False).head(10).round(1).reset_index().rename(columns={'ORA': 'Offensive Rating'})
            av_ORA.drop("index", axis=1, inplace=True)
            av_ORA = av_ORA.reset_index()
            av_ORA['No.'] = av_ORA['index'] + 1
            av_ORA_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_ORA[['No.', 'Player', 'Offensive Rating']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_ORA['No.'], av_ORA.Player, av_ORA['Offensive Rating']],
                align='center', font_size=16, height=30)))

            av_ORA_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_ORA_fig)
        with bs:
            st.write(
                "##### Best by Season on offensive rating per game in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games & over 10 possesions per game in the season)")
            bs_ORA = compute_player_mean_stats_season.loc[compute_player_mean_stats_season['POS']>10][['Player_Season', 'ORA']].sort_values('ORA',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'ORA': 'Offensive Rating', 'Player_Season': 'Player(Season)'})
            bs_ORA.drop("index", axis=1, inplace=True)
            bs_ORA = bs_ORA.reset_index()
            bs_ORA['No.'] = bs_ORA['index'] + 1
            bs_ORA_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_ORA[['No.', 'Player(Season)', 'Offensive Rating']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_ORA['No.'], bs_ORA['Player(Season)'], bs_ORA['Offensive Rating']],
                align='center', font_size=16, height=30)))

            bs_ORA_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_ORA_fig)

    with efg:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Effective Field Goal per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_EFG = compute_player_stats.loc[(compute_player_stats['Total_F2A']>Shoots) |(compute_player_stats['Total_F3A']>Shoots)][['Player','EFG']].sort_values('EFG',ascending=False).head(10).round(1).reset_index().rename(columns={'EFG': 'EFG(%)'})
            av_EFG.drop("index", axis=1, inplace=True)
            av_EFG = av_EFG.reset_index()
            av_EFG['No.'] = av_EFG['index'] + 1
            av_EFG_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_EFG[['No.', 'Player', 'EFG(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_EFG['No.'], av_EFG.Player, av_EFG['EFG(%)']],
                align='center', font_size=16, height=30)))

            av_EFG_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_EFG_fig)

        with bs:
            st.write(
                "##### Best by Season on effective field goal in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games & at least 100 2p or 3P Attempts in the season)")
            bs_EFG = compute_player_mean_stats_season.loc[(compute_player_mean_stats_season['Total_F2A']>=100) | (compute_player_mean_stats_season['Total_F3A']>=100)][['Player_Season', 'EFG']].sort_values('EFG',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'EFG': 'EFG(%)', 'Player_Season': 'Player(Season)'})
            bs_EFG.drop("index", axis=1, inplace=True)
            bs_EFG = bs_EFG.reset_index()
            bs_EFG['No.'] = bs_EFG['index'] + 1
            bs_EFG_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_EFG[['No.', 'Player(Season)', 'EFG(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_EFG['No.'], bs_EFG['Player(Season)'], bs_EFG['EFG(%)']],
                align='center', font_size=16, height=30)))

            bs_EFG_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_EFG_fig)
    with ts:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### True Shooting percentage per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_TS = compute_player_stats.loc[(compute_player_stats['Total_F2A']>Shoots) |(compute_player_stats['Total_F3A']>Shoots)][['Player','TS']].sort_values('TS',ascending=False).head(10).round(1).reset_index().rename(columns={'TS': 'TS(%)'})
            av_TS.drop("index", axis=1, inplace=True)
            av_TS = av_TS.reset_index()
            av_TS['No.'] = av_TS['index'] + 1
            av_TS_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_TS[['No.', 'Player', 'TS(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_TS['No.'], av_TS.Player, av_TS['TS(%)']],
                align='center', font_size=16, height=30)))

            av_TS_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_TS_fig)
        with bs:
            st.write(
                "##### Best by Season on true shoting in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games & at least 100 2p or 3P Attempts in the season)")
            bs_TS = compute_player_mean_stats_season.loc[(compute_player_mean_stats_season['Total_F2A']>=100) | (compute_player_mean_stats_season['Total_F3A']>=100)][['Player_Season', 'TS']].sort_values('TS',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'TS': 'TS(%)', 'Player_Season': 'Player(Season)'})
            bs_TS.drop("index", axis=1, inplace=True)
            bs_TS = bs_TS.reset_index()
            bs_TS['No.'] = bs_TS['index'] + 1
            bs_TS_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_TS[['No.', 'Player(Season)', 'TS(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_TS['No.'], bs_TS['Player(Season)'], bs_TS['TS(%)']],
                align='center', font_size=16, height=30)))

            bs_TS_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_TS_fig)

    with ftr:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Free Throw Ratio per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Shoots slider)')
            av_FTR = compute_player_stats.loc[(compute_player_stats['Total_FTA'] > Shoots)][
                ['Player', 'FTR']].sort_values('FTR', ascending=False).round(1)
            av_FTR=av_FTR.loc[av_FTR.FTR<100].reset_index()
            av_FTR = av_FTR.head(10).rename(columns={'FTR': 'Free Throws Ratio'})
            av_FTR.drop("index", axis=1, inplace=True)
            av_FTR = av_FTR.reset_index()
            av_FTR['No.'] = av_FTR['index'] + 1
            av_FTR_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_FTR[['No.', 'Player', 'Free Throws Ratio']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_FTR['No.'], av_FTR.Player, av_FTR['Free Throws Ratio']],
                align='center', font_size=16, height=30)))

            av_FTR_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_FTR_fig)
        with bs:
            st.write(
                "##### Best by Season on free throw ratio in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games & at least 100 Free throw Attempts in the season)")
            bs_FTR = compute_player_mean_stats_season.loc[(compute_player_mean_stats_season['Total_FTA']>=100) ][['Player_Season', 'FTR']].sort_values('FTR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'FTR': 'Free Throws Ratio', 'Player_Season': 'Player(Season)'})
            bs_FTR.drop("index", axis=1, inplace=True)
            bs_FTR = bs_FTR.reset_index()
            bs_FTR['No.'] = bs_FTR['index'] + 1
            bs_FTR_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_FTR[['No.', 'Player(Season)', 'Free Throws Ratio']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_FTR['No.'], bs_FTR['Player(Season)'], bs_FTR['Free Throws Ratio']],
                align='center', font_size=16, height=30)))

            bs_FTR_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_FTR_fig)

    with astor:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Assists-Turnovers Ratio per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_ASTOR = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','ASTOR']].sort_values('ASTOR',ascending=False).head(10).round(1).reset_index().rename(columns={'ASTOR': 'Assists-Turnovers Ratio'})
            av_ASTOR.drop("index", axis=1, inplace=True)
            av_ASTOR = av_ASTOR.reset_index()
            av_ASTOR['No.'] = av_ASTOR['index'] + 1
            av_ASTOR_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_ASTOR[['No.', 'Player', 'Assists-Turnovers Ratio']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_ASTOR['No.'], av_ASTOR.Player, av_ASTOR['Assists-Turnovers Ratio']],
                align='center', font_size=16, height=30)))

            av_ASTOR_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_ASTOR_fig)
        with bs:
            st.write(
                "##### Best by Season on Assists-Turnover ratio in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_ASTOR = compute_player_mean_stats_season[['Player_Season', 'ASTOR']].sort_values('ASTOR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index()
            bs_ASTOR=bs_ASTOR.loc[bs_ASTOR.ASTOR<100].rename(columns={'ASTOR': 'Assists-Turnover ratio', 'Player_Season': 'Player(Season)'})
            bs_ASTOR.drop("index", axis=1, inplace=True)
            bs_ASTOR = bs_ASTOR.reset_index()
            bs_ASTOR['No.'] = bs_ASTOR['index'] + 1
            bs_ASTOR_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_ASTOR[['No.', 'Player(Season)', 'Assists-Turnover ratio']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_ASTOR['No.'], bs_ASTOR['Player(Season)'], bs_ASTOR['Assists-Turnover ratio']],
                align='center', font_size=16, height=30)))

            bs_ASTOR_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_ASTOR_fig)
    with tor:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Turnovers Ratio per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_TOR = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','TOR']].sort_values('TOR',ascending=False).head(10).round(1).reset_index().rename(
                columns={'TOR': 'Turnovers Ratio'})
            av_TOR.drop("index", axis=1, inplace=True)
            av_TOR = av_TOR.reset_index()
            av_TOR['No.'] = av_TOR['index'] + 1
            av_TOR_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_TOR[['No.', 'Player', 'Turnovers Ratio']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_TOR['No.'], av_TOR.Player, av_TOR['Turnovers Ratio']],
                align='center', font_size=16, height=30)))

            av_TOR_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_TOR_fig)
        with bs:
            st.write(
                "##### Best by Season onTurnover ratio in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_TOR = compute_player_mean_stats_season[
                ['Player_Season', 'TOR']].sort_values('TOR',
                                                        ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'TOR': 'Turnover ratio', 'Player_Season': 'Player(Season)'})
            bs_TOR.drop("index", axis=1, inplace=True)
            bs_TOR = bs_TOR.reset_index()
            bs_TOR['No.'] = bs_TOR['index'] + 1
            bs_TOR_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_TOR[['No.', 'Player(Season)', 'Turnover ratio']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_TOR['No.'], bs_TOR['Player(Season)'], bs_TOR['Turnover ratio']],
                align='center', font_size=16, height=30)))

            bs_TOR_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_TOR_fig)

    with asr:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Assists Ratio per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_ASR = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','ASR']].sort_values('ASR',ascending=False).head(10).round(1).reset_index().rename(
                columns={'ASR': 'Assists Ratio'})
            av_ASR.drop("index", axis=1, inplace=True)
            av_ASR = av_ASR.reset_index()
            av_ASR['No.'] = av_ASR['index'] + 1
            av_ASR_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_ASR[['No.', 'Player', 'Assists Ratio']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_ASR['No.'], av_ASR.Player, av_ASR['Assists Ratio']],
                align='center', font_size=16, height=30)))

            av_ASR_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_ASR_fig)
        with bs:
            st.write(
                "##### Best by Season on Assists ratio in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_ASR = compute_player_mean_stats_season[['Player_Season', 'ASR']].sort_values('ASR',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'ASR': 'Assists ratio', 'Player_Season': 'Player(Season)'})
            bs_ASR.drop("index", axis=1, inplace=True)
            bs_ASR = bs_ASR.reset_index()
            bs_ASR['No.'] = bs_ASR['index'] + 1
            bs_ASR_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_ASR[['No.', 'Player(Season)', 'Assists ratio']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_ASR['No.'], bs_ASR['Player(Season)'], bs_ASR['Assists ratio']],
                align='center', font_size=16, height=30)))

            bs_ASR_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_ASR_fig)

    with usg:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Usage(%) per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_USG = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','USG']].sort_values('USG',ascending=False).head(10).round(1).reset_index().rename(
                columns={'USG': 'Usage(%)'})
            av_USG.drop("index", axis=1, inplace=True)
            av_USG = av_USG.reset_index()
            av_USG['No.'] = av_USG['index'] + 1
            av_USG_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_USG[['No.', 'Player', 'Usage(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_USG['No.'], av_USG.Player, av_USG['Usage(%)']],
                align='center', font_size=16, height=30)))

            av_USG_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_USG_fig)
        with bs:
            st.write(
                "##### Best by Season on Usage in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_USG = compute_player_mean_stats_season[['Player_Season', 'USG']].sort_values('USG',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'USG': 'Usage(%)', 'Player_Season': 'Player(Season)'})
            bs_USG.drop("index", axis=1, inplace=True)
            bs_USG = bs_USG.reset_index()
            bs_USG['No.'] = bs_USG['index'] + 1
            bs_USG_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_USG[['No.', 'Player(Season)', 'Usage(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_USG['No.'], bs_USG['Player(Season)'], bs_USG['Usage(%)']],
                align='center', font_size=16, height=30)))

            bs_USG_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_USG_fig)
    with orp:
        av, bs = st.tabs(['Average Stats', 'Best by Season'])
        with av:
            st.write("##### Percentage of Offensive Rebounds per game in Euroleague from 2016-2017 Season (Top 10)")
            st.write('(For better results move the Games slider)')
            av_ORP = compute_player_stats.loc[compute_player_stats['Games']>games][['Player','ORP']].sort_values('ORP',ascending=False).head(10).round(1).reset_index().rename(
                columns={'ORP': 'OR(%)'})
            av_ORP.drop("index", axis=1, inplace=True)
            av_ORP = av_ORP.reset_index()
            av_ORP['No.'] = av_ORP['index'] + 1
            av_ORP_fig = go.Figure(data=go.Table(header=dict(
                values=list(av_ORP[['No.', 'Player', 'OR(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[av_ORP['No.'], av_ORP.Player, av_ORP['OR(%)']],
                align='center', font_size=16, height=30)))

            av_ORP_fig.update_layout(
                autosize=True,
                width=600,
                height=550,
                margin=dict(
                    l=30,
                    r=50,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(av_ORP_fig)

        with bs:
            st.write(
                "##### Best by Season on percentage of Offensive Rebounds in Euroleague from 2016-2017 Season (Top 10 - played at least 15 games in the season)")
            bs_ORP = compute_player_mean_stats_season[['Player_Season', 'ORP']].sort_values('ORP',
                                                                                            ascending=False).head(
                10).round(
                1).reset_index().rename(columns={'ORP': 'OR(%)', 'Player_Season': 'Player(Season)'})
            bs_ORP.drop("index", axis=1, inplace=True)
            bs_ORP = bs_ORP.reset_index()
            bs_ORP['No.'] = bs_ORP['index'] + 1
            bs_ORP_fig = go.Figure(data=go.Table(header=dict(
                values=list(
                    bs_ORP[['No.', 'Player(Season)', 'OR(%)']].columns),
                align='center', font_size=18, height=30), cells=dict(
                values=[bs_ORP['No.'], bs_ORP['Player(Season)'], bs_ORP['OR(%)']],
                align='center', font_size=16, height=30)))

            bs_ORP_fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(
                    l=1,
                    r=1,
                    b=100,
                    t=80,
                    pad=10
                ))

            st.write(bs_ORP_fig)
