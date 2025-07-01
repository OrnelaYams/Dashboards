import streamlit as st
import pandas as pd

# CSV-Datei laden
csv_url = "Python_Dashboards/teams.csv"
data = pd.read_csv(csv_url)

# App-Titel
st.title("NHL Teams")

# Seitenleiste für Filters
st.sidebar.header("Filter Options")

# Multiselect für Teamnamen
team_names = data['Team'].unique()
selected_teams = st.sidebar.multiselect('Select Teams', team_names, default=team_names)

# Filtere die Daten basierend auf der Auswahl
filtered_data = data[data['Team'].isin(selected_teams)]

# Auswahl des Jahresbereichs
year_range = st.sidebar.slider('Select Year Range', int(data['Jahr'].min()), int(data['Jahr'].max()), 
                               (int(data['Jahr'].min()), int(data['Jahr'].max())))

# Filtere die Daten basierend auf dem Jahresbereich
filtered_data = filtered_data[(filtered_data['Jahr'] >= year_range[0]) & (filtered_data['Jahr'] <= year_range[1])]

# Anzeige der Daten
st.write(filtered_data)