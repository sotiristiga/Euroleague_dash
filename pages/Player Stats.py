
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
st.set_page_config(layout='wide',page_title="Euroleague")
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


All_Seasons=pd.concat([euroleague_2016_2017_playerstats,euroleague_2017_2018_playerstats,euroleague_2018_2019_playerstats,euroleague_2019_2020_playerstats,euroleague_2020_2021_playerstats,euroleague_2021_2022_playerstats,euroleague_2022_2023_playerstats,euroleague_2023_2024_playerstats])

All_Seasons_res=pd.concat([euroleague_2016_2017_results,euroleague_2017_2018_results,euroleague_2018_2019_results,euroleague_2019_2020_results,euroleague_2020_2021_results,euroleague_2021_2022_results,euroleague_2022_2023_results,euroleague_2023_2024_results])

filters_playerstats = DynamicFilters(All_Seasons, filters=['Season','Round','Phase','HA','results'])
All_Seasons_filter = filters_playerstats .filter_df()

filters_playerstats.display_filters(location='sidebar')

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

games = st.sidebar.slider("Pick Number of games", 0, 1000)
Shoots = st.sidebar.slider("Pick Number of Shoots", 0, 2000)

av,sum,rec=st.tabs(['Average Stats','Total Stats','Record Stats'])

with av:
    basic,shooting,advanced=st.tabs(['Basic Stats','Shooting Stats','Advanced Stats'])
    with basic:
        tab1a,tab2a,tab3a,tab4a,tab5a,tab6a,tab7a,tab8a,tab9a,tab10a,tab11a=st.tabs(['Points',"Assists","Total Reb","Off Reb",'Def Reb',"Steals",'Turnovers','Blocks','Blocks Reversed','Fouls Made',"Fouls Drawn"])
        with tab1a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','PTS']].sort_values('PTS',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab2a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','AS']].sort_values('AS',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab3a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','TR']].sort_values('TR',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab4a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','OR']].sort_values('OR',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab5a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','DR']].sort_values('DR',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab6a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','ST']].sort_values('ST',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab7a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','TO']].sort_values('TO',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab8a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','BLK']].sort_values('BLK',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab9a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','BLKR']].sort_values('BLKR',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab10a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player', 'PF']].sort_values('PF', ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab11a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player', 'RF']].sort_values('RF', ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
    with shooting:

        tab12a,tab13a,tab14a,tab15a,tab16a,tab17a,tab18a,tab19a,tab20a=st.tabs(['2P Made',"2P Attempt","2P(%)",'3P Made',"3P Attempt","3P(%)",'Free Throws Made',"Free Throws Attempt","FT(%)"])
        with tab12a:
            st.write(compute_player_stats.loc[compute_player_stats['Total_F2A']>Shoots][['Player','F2M']].sort_values('F2M',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Shoots slider')
        with tab13a:
            st.write(compute_player_stats.loc[compute_player_stats['Total_F2A']>Shoots][['Player','F2A']].sort_values('F2A',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Shoots slider')
        with tab14a:
            st.write(compute_player_stats.loc[compute_player_stats['Total_F2A']>Shoots][['Player','P2']].sort_values('P2',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Shoots slider')
        with tab15a:
            st.write(compute_player_stats.loc[compute_player_stats['Total_F3A']>Shoots][['Player','F3M']].sort_values('F3M',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Shoots slider')
        with tab16a:
            st.write(compute_player_stats.loc[compute_player_stats['Total_F3A']>Shoots][['Player','F3A']].sort_values('F3A',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Shoots slider')
        with tab17a:
            st.write(compute_player_stats.loc[compute_player_stats['Total_F3A']>Shoots][['Player','P3']].sort_values('P3',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Shoots slider')
        with tab18a:
            st.write(compute_player_stats.loc[compute_player_stats['Total_FTA']>Shoots][['Player','FTM']].sort_values('FTM',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Shoots slider')
        with tab19a:
            st.write(compute_player_stats.loc[compute_player_stats['Total_FTA']>Shoots][['Player','FTA']].sort_values('FTA',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Shoots slider')
        with tab20a:
            st.write(compute_player_stats.loc[compute_player_stats['Total_F3A']>Shoots][['Player','PFT']].sort_values('PFT',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Shoots slider')

    with advanced:
        tab21a, tab22a, tab23a, tab24a, tab25a, tab26a, tab27a, tab28a, tab29a,tab30a = st.tabs(
            ['Possessions', "Offensive Rating", "EFG(%)", 'TS(%)', "Free Throw Ratio", "Assists - Turnover Ratio", 'Turnover Ratio',
             "Assists Ratio", "Usage(%)",'OR(%)'])
        with tab21a:
            st.write(compute_player_stats[['Player','POS']].sort_values('POS',ascending=False).head(10).round(1).set_index('Player'))
        with tab22a:
            st.write(compute_player_stats.loc[compute_player_stats['POS']>10][['Player','ORA']].sort_values('ORA',ascending=False).head(10).round(1).set_index('Player'))
        with tab23a:
            st.write(compute_player_stats.loc[(compute_player_stats['Total_F2A']>Shoots) |(compute_player_stats['Total_F3A']>Shoots)][['Player','EFG']].sort_values('EFG',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Shoots slider')
        with tab24a:
            st.write(compute_player_stats.loc[(compute_player_stats['Total_F2A']>Shoots) |(compute_player_stats['Total_F3A']>Shoots)][['Player','TS']].sort_values('TS',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Shoots slider')
        with tab25a:
            st.write(compute_player_stats.loc[compute_player_stats['Total_FTA']>Shoots][['Player','FTR']].sort_values('FTR',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Shoots slider')
        with tab26a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','ASTOR']].sort_values('ASTOR',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab27a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','TOR']].sort_values('TOR',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab28a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','ASR']].sort_values('ASR',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab29a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','USG']].sort_values('USG',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
        with tab30a:
            st.write(compute_player_stats.loc[compute_player_stats['Games']>games][['Player','ORP']].sort_values('ORP',ascending=False).head(10).round(1).set_index('Player'))
            st.write('For better results move the Games slider')
with sum:
    basic, shooting= st.tabs(['Basic Stats', 'Shooting Stats'])
    with basic:
        tab1t, tab2t, tab3t, tab4t, tab5t, tab6t, tab7t, tab8t, tab9t, tab10t, tab11t = st.tabs(
            ['Points', "Assists", "Total Reb", "Off Reb", 'Def Reb', "Steals", 'Turnovers', 'Blocks', 'Blocks Reversed',
             'Fouls Made', "Fouls Drawn"])
        with tab1t:
            st.write(compute_player_stats[['Player', 'Total_PTS']].sort_values('Total_PTS', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab2t:
            st.write(compute_player_stats[['Player', 'Total_AS']].sort_values('Total_AS', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab3t:
            st.write(compute_player_stats[['Player', 'Total_TR']].sort_values('Total_TR', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab4t:
            st.write(compute_player_stats[['Player', 'Total_OR']].sort_values('Total_OR', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab5t:
            st.write(compute_player_stats[['Player', 'Total_DR']].sort_values('Total_DR', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab6t:
            st.write(compute_player_stats[['Player', 'Total_ST']].sort_values('Total_ST', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab7t:
            st.write(compute_player_stats[['Player', 'Total_TO']].sort_values('Total_TO', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab8t:
            st.write(compute_player_stats[['Player', 'Total_BLK']].sort_values('Total_BLK', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab9t:
            st.write(compute_player_stats[['Player', 'Total_BLKR']].sort_values('Total_BLKR', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab10t:
            st.write(compute_player_stats[['Player', 'Total_PF']].sort_values('Total_PF', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab11t:
            st.write(compute_player_stats[['Player', 'Total_RF']].sort_values('Total_RF', ascending=False).head(10).round(
                1).set_index('Player'))
    with shooting:

        tab12t, tab13t, tab14t, tab15t, tab16t, tab17t = st.tabs(
            ['2P Made', "2P Attempt", '3P Made', "3P Attempt",  'Free Throws Made',
             "Free Throws Attempt"])
        with tab12t:
            st.write(compute_player_stats[['Player', 'Total_F2M']].sort_values('Total_F2M', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab13t:
            st.write(compute_player_stats[['Player', 'Total_F2A']].sort_values('Total_F2A', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab14t:
            st.write(compute_player_stats[['Player', 'Total_F3M']].sort_values('Total_F3M', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab15t:
            st.write(compute_player_stats[['Player', 'Total_F3A']].sort_values('Total_F3A', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab16t:
            st.write(compute_player_stats[['Player', 'Total_FTM']].sort_values('Total_FTM', ascending=False).head(10).round(
                1).set_index('Player'))
        with tab17t:
            st.write(compute_player_stats[['Player', 'Total_FTA']].sort_values('Total_FTA', ascending=False).head(10).round(
                1).set_index('Player'))


with rec:
    basic, shooting = st.tabs(['Basic Stats', 'Shooting Stats'])
    with basic:
        tab1r, tab2r, tab3r, tab4r, tab5r, tab6r, tab7r, tab8r, tab9r, tab10r, tab11r = st.tabs(
            ['Points', "Assists", "Total Reb", "Off Reb", 'Def Reb', "Steals", 'Turnovers', 'Blocks', 'Blocks Reversed',
             'Fouls Made', "Fouls Drawn"])
        All_Seasons_filter['Player_Team']=All_Seasons_filter['Player']+"("+All_Seasons_filter['Team']+","+All_Seasons_filter['Season']+" vs "+All_Seasons_filter['Against']+")"
        with tab1r:
            st.write(All_Seasons_filter[['Player_Team', 'PTS']].sort_values('PTS', ascending=False).head(10).round(
                1).set_index('Player_Team'))
        with tab2r:
            st.write(All_Seasons_filter[['Player_Team', 'AS']].sort_values('AS', ascending=False).head(10).round(
                1).set_index('Player_Team'))
        with tab3r:
            st.write(All_Seasons_filter[['Player_Team', 'TR']].sort_values('TR', ascending=False).head(10).round(
                1).set_index('Player_Team'))
        with tab4r:
            st.write(All_Seasons_filter[['Player_Team', 'OR']].sort_values('OR', ascending=False).head(10).round(
                1).set_index('Player_Team'))
        with tab5r:
            st.write(All_Seasons_filter[['Player_Team', 'DR']].sort_values('DR', ascending=False).head(10).round(
                1).set_index('Player_Team'))
        with tab6r:
            st.write(All_Seasons_filter[['Player_Team', 'ST']].sort_values('ST', ascending=False).head(10).round(
                1).set_index('Player_Team'))
        with tab7r:
            st.write(All_Seasons_filter[['Player_Team', 'TO']].sort_values('TO', ascending=False).head(10).round(
                1).set_index('Player_Team'))
        with tab8r:
            st.write(All_Seasons_filter[['Player_Team', 'BLK']].sort_values('BLK', ascending=False).head(10).round(
                1).set_index('Player_Team'))
        with tab9r:
            st.write(
                All_Seasons_filter[['Player_Team', 'BLKR']].sort_values('BLKR', ascending=False).head(10).round(
                    1).set_index('Player_Team'))
        with tab10r:
            st.write(All_Seasons_filter[['Player_Team', 'PF']].sort_values('PF', ascending=False).head(10).round(
                1).set_index('Player_Team'))
        with tab11r:
            st.write(All_Seasons_filter[['Player_Team', 'RF']].sort_values('RF', ascending=False).head(10).round(
                1).set_index('Player_Team'))
    with shooting:
        tab12r, tab13r, tab14r, tab15r, tab16r, tab17r = st.tabs(
            ['2P Made', "2P Attempt", '3P Made', "3P Attempt", 'Free Throws Made',
             "Free Throws Attempt"])
        with tab12r:
            st.write(
                All_Seasons_filter[['Player_Team', 'F2M']].sort_values('F2M', ascending=False).head(10).round(
                    1).set_index('Player_Team'))
        with tab13r:
            st.write(
                All_Seasons_filter[['Player_Team', 'F2A']].sort_values('F2A', ascending=False).head(10).round(
                    1).set_index('Player_Team'))
        with tab14r:
            st.write(
                All_Seasons_filter[['Player_Team', 'F3M']].sort_values('F3M', ascending=False).head(10).round(
                    1).set_index('Player_Team'))
        with tab15r:
            st.write(
                All_Seasons_filter[['Player_Team', 'F3A']].sort_values('F3A', ascending=False).head(10).round(
                    1).set_index('Player_Team'))
        with tab16r:
            st.write(
                All_Seasons_filter[['Player_Team', 'FTM']].sort_values('FTM', ascending=False).head(10).round(
                    1).set_index('Player_Team'))
        with tab17r:
            st.write(
                All_Seasons_filter[['Player_Team', 'FTA']].sort_values('FTA', ascending=False).head(10).round(
                    1).set_index('Player_Team'))


