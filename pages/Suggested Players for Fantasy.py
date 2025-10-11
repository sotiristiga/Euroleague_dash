import pandas as pd
import numpy as np
import streamlit as st
import urllib.request
from PIL import Image

from itables.streamlit import interactive_table

from euroleague_api.boxscore_data import BoxScoreData

st.set_page_config(layout='wide',page_title="Euroleague fantasy",page_icon="🏀")
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



Positions=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/PlayersPositions.csv")
Players_CR=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/refs/heads/main/2025_2026_players.csv")

Fixtures=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/Euroleague_dash/refs/heads/main/Euroleague%20fixtures%202526.csv")

euroleague_2025_2026_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2025_2026_playerstats.csv")
euroleague_2025_2026_playerstats['idseason']=euroleague_2025_2026_playerstats['IDGAME'] + "_" + euroleague_2025_2026_playerstats['Season']
euroleague_2025_2026_playerstats[['Fixture', 'Game']] = euroleague_2025_2026_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2025_2026_playerstats['Fixture']=pd.to_numeric(euroleague_2025_2026_playerstats['Fixture'])
euroleague_2025_2026_playerstats['Round']=euroleague_2025_2026_playerstats['Fixture'].apply(fixture_format5)



All_Seasons=euroleague_2025_2026_playerstats

All_Seasons['Player']=All_Seasons['Player'].str.replace('Juan  Hernangomez','Juancho  Hernangomez')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Christ  Koumadje','Khalifa  Koumadje')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Nico  Mannion','Niccolo  Mannion')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Dan  Oturu','Daniel  Oturu')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Nikolaos  Rogkavopoulos','Nikos  Rogkavopoulos')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Aleksandr  Vezenkov','Sasha  Vezenkov')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Alberto  Abalde','Alberto  Abalde')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Wade  Baldwin Iv','Wade  Baldwin IV')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Devin  Booker','Devin  Booker')
All_Seasons['Player']=All_Seasons['Player'].str.replace('John  Brown II','John  Brown')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Jimmy  Clark Iii','Jimmy  Clark')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Oscar  da Silva','Oscar  Da Silva')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Nando  de Colo','Nando  De Colo')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Zach  LeDay','Zach  Leday')
All_Seasons['Player']=All_Seasons['Player'].str.replace('David  Mccormack','David  McCormack')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Codi  Miller-Mcintyre','Codi  Miller-McIntyre')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Alexandros  Samodurov','Alexandros  Samontourov')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Tj  Shorts','TJ  Shorts II')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Lonnie  Walker Iv','Lonnie  Walker IV')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Will  Rayman','William  Rayman')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Leopold  Cavaliere','Leo  Cavaliere')
All_Seasons['Player']=All_Seasons['Player'].str.replace('Nate  Reuvers','Nathan  Reuvers')
All_Seasons['Player']=All_Seasons['Player'].str.replace('David  Kraemer','David  Kramer')


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
    elif results=="L":
        return 0
All_Seasons["HA1"] = All_Seasons['HA'].apply(ha_against_format)
All_Seasons["Result1"] = All_Seasons['results'].apply(result_against_format)
All_Seasons["Win"]=All_Seasons['results'].apply(wins_against_format)

st.sidebar.markdown('''
  * ## [Filters](#filters)
  * ## [Teams PIR by Position](#teams-pir-by-position)
  * ## [Suggested Players by position](#suggested-players-by-position)
  * ## [Players PIR win and lose](#players-pir-win-and-lose)


''', unsafe_allow_html=True)
st.header("Filters")
f1, f2, f3, f4= st.columns(4)
with f1:
    search_team_phase_team1 = st.selectbox("Phase:",
                                           ['Regular Season', 'Play In', 'Play offs', 'Final Four', 'All'],
                                           index=4)
with f2:
    search_team_round_team1 = st.selectbox("Round:",
                                           ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2',
                                            'PO 3', 'PO 4', 'PO 5', 'Semi Final', 'Third Place', 'Final',
                                            'All'], index=12)
with f3:
    search_team_ha_team1 = st.selectbox("Home or Away games:", ['A', 'H', 'All'], index=2)
with f4:
    search_team_wl_team1 = st.selectbox("Result:", ['W', 'L', 'All'], index=2)



if "All" in search_team_ha_team1:
    search_team_ha_team1 = ['A', 'H']
    All_Seasons1=All_Seasons.loc[All_Seasons['HA'].isin(search_team_ha_team1)]

else:
    All_Seasons1=All_Seasons.loc[All_Seasons['HA']==search_team_ha_team1]


if "All" in search_team_wl_team1:
    search_team_wl_team1 = ['W', 'L']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['results'].isin(search_team_wl_team1)]


else:
    All_Seasons1= All_Seasons1.loc[All_Seasons1['results'] == search_team_wl_team1]


if "All" in search_team_phase_team1:
    search_team_phase_team1 = ['Regular Season', 'Play In','Play offs', 'Final Four']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Phase'].isin(search_team_phase_team1)]

else:
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Phase'] == search_team_phase_team1]



if "All" in search_team_round_team1:
    search_team_round_team1 = ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final']
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Round'].isin(search_team_round_team1)]

else:
    All_Seasons1 = All_Seasons1.loc[All_Seasons1['Round'] == search_team_round_team1]



All_seasons_pos=pd.merge(All_Seasons1,Positions,on='Player')
teams_pir=All_seasons_pos.groupby(['Team','idseason'])['PIR'].sum().round(1).reset_index().groupby('Team')['PIR'].mean().round(1).reset_index().rename(columns={'PIR':"Team's PIR"})
against_pir=All_seasons_pos.groupby(['Against','idseason'])['PIR'].sum().round(1).reset_index().groupby('Against')['PIR'].mean().round(1).reset_index().rename(columns={'Against':'Team','PIR':"Opp.'s PIR"})
teams_pir=pd.merge(teams_pir,against_pir,on='Team')


stats_by_pos = All_seasons_pos.groupby(['Team', 'Position', 'idseason']).sum()['PIR'].groupby(
        ['Team', 'Position']).mean().reset_index().round(1).sort_values('Position')

stats_by_pos_c=stats_by_pos.loc[stats_by_pos.Position=='C'].rename(columns={'PIR':"Team's Centers PIR"})
stats_by_pos_c.drop('Position',axis=1,inplace=True)
stats_by_pos_f=stats_by_pos.loc[stats_by_pos.Position=='F'].rename(columns={'PIR':"Team's Forwards PIR"})
stats_by_pos_f.drop('Position',axis=1,inplace=True)
stats_by_pos_g=stats_by_pos.loc[stats_by_pos.Position=='G'].rename(columns={'PIR':"Team's Guards PIR"})
stats_by_pos_g.drop('Position',axis=1,inplace=True)

teams_pir_by_pos=pd.merge(stats_by_pos_g,stats_by_pos_f,on='Team')
teams_pir_by_pos=pd.merge(teams_pir_by_pos,stats_by_pos_c,on='Team')


stats_by_pos_opp = All_seasons_pos.groupby(['Against', 'Position', 'idseason']).sum()['PIR'].groupby(
        ['Against', 'Position']).mean().reset_index().round(1).sort_values('Position')

stats_by_pos_c_opp=stats_by_pos_opp.loc[stats_by_pos_opp.Position=='C'].rename(columns={'PIR':"Opp.'s Centers PIR","Against":'Team'})
stats_by_pos_c_opp.drop('Position',axis=1,inplace=True)
stats_by_pos_f_opp=stats_by_pos_opp.loc[stats_by_pos_opp.Position=='F'].rename(columns={'PIR':"Opp.'s Forwards PIR","Against":'Team'})
stats_by_pos_f_opp.drop('Position',axis=1,inplace=True)
stats_by_pos_g_opp=stats_by_pos_opp.loc[stats_by_pos_opp.Position=='G'].rename(columns={'PIR':"Opp.'s Guards PIR","Against":'Team'})
stats_by_pos_g_opp.drop('Position',axis=1,inplace=True)
opp_pir_by_pos=pd.merge(stats_by_pos_g_opp,stats_by_pos_f_opp,on='Team')
opp_pir_by_pos=pd.merge(opp_pir_by_pos,stats_by_pos_c_opp,on='Team')
pir_by_pos=pd.merge(teams_pir_by_pos,opp_pir_by_pos)
pir_by_pos=pd.merge(pir_by_pos,teams_pir)


st.header("Suggested Players by position")

now_fixture=euroleague_2025_2026_playerstats['Fixture'].max()
select_position=st.selectbox("Position:",['Guards', 'Forwards','Centers'],index=2)
Fixtures_test=Fixtures.loc[Fixtures['Fixture']==now_fixture+1][["Home_Team","Away_Team"]]

take_home_teams=Fixtures_test.rename(columns={"Home_Team":"Team","Away_Team":"Against"})
take_home_teams["HA"]="H"

take_away_teams=Fixtures_test.rename(columns={"Home_Team":"Against","Away_Team":"Team"})
take_away_teams["HA"]="A"

take_teams=pd.concat([take_home_teams,take_away_teams])

next_fixtures_opp=pd.merge(take_teams.rename(columns={"Home_Team":"Team","Away_Team":"Against"}),pir_by_pos[['Team',"Opp.'s Guards PIR","Opp.'s Forwards PIR","Opp.'s Centers PIR"]].rename(columns={"Team":"Against"}),how="outer")
select_guard=next_fixtures_opp[['Team',"Against","Opp.'s Guards PIR",'HA']].sort_values("Opp.'s Guards PIR",ascending=False).head(8)
select_forward=next_fixtures_opp[['Team',"Against","Opp.'s Forwards PIR",'HA']].sort_values("Opp.'s Forwards PIR",ascending=False).head(8)
select_center=next_fixtures_opp[['Team',"Against","Opp.'s Centers PIR",'HA']].sort_values("Opp.'s Centers PIR",ascending=False).head(8)

players_pir_guard=All_seasons_pos.loc[All_seasons_pos.Position=='G'].groupby(['Player','Team'])['PIR'].mean().round(1).reset_index().rename(columns={'PIR':"Player's PIR"})
players_pir_guard_ha=All_seasons_pos.loc[All_seasons_pos.Position=='G'].groupby(['Player','Team','HA'])['PIR'].mean().round(1).reset_index().rename(columns={'PIR':"Player's PIR at HA"})
Guards=pd.merge(select_guard,players_pir_guard,how="outer").sort_values(["Opp.'s Guards PIR","Player's PIR"],ascending=False).rename(columns={"Opp.'s Guards PIR":"Opp.'s "+select_position+" PIR"}).merge(players_pir_guard_ha,how="outer")
Guards["Position"]="Guards"

players_pir_forw=All_seasons_pos.loc[All_seasons_pos.Position=='F'].groupby(['Player','Team'])['PIR'].mean().round(1).reset_index().rename(columns={'PIR':"Player's PIR"})
players_pir_forw_ha=All_seasons_pos.loc[All_seasons_pos.Position=='F'].groupby(['Player','Team','HA'])['PIR'].mean().round(1).reset_index().rename(columns={'PIR':"Player's PIR at HA"})
Forwards=pd.merge(select_forward,players_pir_forw,how="outer").sort_values(["Opp.'s Forwards PIR","Player's PIR"],ascending=False).rename(columns={"Opp.'s Forwards PIR":"Opp.'s "+select_position+" PIR"}).merge(players_pir_forw_ha)
Forwards["Position"]="Forwards"

players_pir_cent=All_seasons_pos.loc[All_seasons_pos.Position=='C'].groupby(['Player','Team'])['PIR'].mean().round(1).reset_index().rename(columns={'PIR':"Player's PIR"})
players_pir_cent_ha=All_seasons_pos.loc[All_seasons_pos.Position=='C'].groupby(['Player','Team','HA'])['PIR'].mean().round(1).reset_index().rename(columns={'PIR':"Player's PIR at HA"})
Centers=pd.merge(select_center,players_pir_cent,how="outer").sort_values(["Opp.'s Centers PIR","Player's PIR"],ascending=False).rename(columns={"Opp.'s Centers PIR":"Opp.'s "+select_position+" PIR"}).merge(players_pir_cent_ha)
Centers["Position"]="Centers"

suggested_players=pd.concat([Guards,Forwards,Centers])

suggested_players_fil=suggested_players.loc[(suggested_players["Player's PIR"]>6) &(suggested_players["Position"]==select_position)].rename(columns={'HA':"Played"})
suggested_players_fil.drop('Position',axis=1,inplace=True)



url = "https://www.basketstories.net/datacenter/players_fdr.php"
tables = pd.read_html(url)
values=pd.DataFrame(tables[0].iloc[3:,:3].set_axis(['Player1', 'Team','CR'], axis=1))
values.columns=['Player1', 'Team','CR']


credits_data=pd.merge(Players_CR,values,on="Player1",how="outer")
credits_data['Player'] = credits_data['First Name'] + "  " + credits_data['Last Name']
credits_data['Player']=credits_data['Player'].fillna(credits_data["Player1"])
credits_data['Player']=credits_data['Player'].str.replace("Dan  Oturu","Daniel  Oturu")
credits_data['Player']=credits_data['Player'].str.replace("Codi  Miller-Mcintyre","Codi  Miller-McIntyre")
credits_data['Player']=credits_data['Player'].str.replace("Wade  Baldwin Iv","Wade  Baldwin IV")
credits_data['Player']=credits_data['Player'].str.replace("Lonnie  Walker Iv","Lonnie  Walker IV")
credits_data['Player']=credits_data['Player'].str.replace("Lonnie  Walker Iv","Lonnie  Walker IV")

suggest=pd.merge(suggested_players_fil,credits_data[["Player","CR"]],on="Player",how="left")
suggest["Player's PIR at HA"]=suggest["Player's PIR at HA"].replace(np.nan,0)
suggest=suggest[['Player','Team',"Player's PIR","Against","Opp.'s "+select_position+" PIR","Played","Player's PIR at HA","CR"]].set_index('Player')
suggest["CR"]=suggest["CR"].astype(float)
suggest["Eff PIR"]=(suggest["Player's PIR"]/suggest["CR"]).round(2)
interactive_table(suggest,
                      paging=False, height=900, width=2000, showIndex=True,
                      classes="display order-column nowrap table_with_monospace_font", searching=True,
                      fixedColumns=True, select=True, info=False, scrollCollapse=True,
                      scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                      columnDefs=[{"className": "dt-center", "targets": "_all"}])
