
import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

# CSV-Datei laden
csv_url = "Python_Dashboards/teams.csv"
data  = pd.read_csv(csv_url)

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





# # CSV laden
# df = pd.read_csv("Python_Dashboards/teams.csv")

# st.title("NHL Teams")

# # Jahr sicherstellen als int
# df["Jahr"] = df["Jahr"].astype(int)

# # Seitenleiste: Multiselect für Teamnamen
# team_names = sorted(df["Team"].unique())
# selected_teams = st.multiselect(
#     "Wähle Teamnamen",
#     options=team_names,
#     default=team_names[:3] 
# )

# # Seitenleiste: Jahresbereich mit Slider
# min_year = df["Jahr"].min()
# max_year = df["Jahr"].max()
# year_range = st.slider(
#     "Jahresbereich filtern",
#     min_value=min_year,
#     max_value=max_year,
#     value=(min_year, max_year),
#     step=1
# )

# Filter anwenden
df_filtered = data[
    (data["Team"].isin(selected_teams)) &
    (data["Jahr"].between(year_range[0], year_range[1]))
]

# # Tabelle anzeigen
# st.expander("Datensatz anzeigen").dataframe(df_filtered, use_container_width=True)




# Dropdown für die Metrikauswahl
st.markdown("## Trendanalyse als Liniendiagramm")
metric_options = ["GF", "AF", "Siege", "Niederlagen"]
selected_metric = st.selectbox(
    "Wähle die Metrik für das Liniendiagramm",
    options=metric_options,
)

import plotly.express as px
# Liniendiagramm mit Plotly
if df_filtered.empty:
    st.info("Keine Daten für die gewählten Filter.")
else:
    fig = px.line(
        df_filtered,
        x="Jahr",
        y=selected_metric,
        color="Team",
        markers=True,
        title=f"Verlauf von {selected_metric}"
    )
    fig.update_layout(legend_title_text='Team')
    st.plotly_chart(fig, use_container_width=True)

# CSS für den Hintergrund
def add_bg_color():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ADD8E6;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
def main():
    add_bg_color()

if __name__ == "__main__":
    main()