import streamlit as st

TITLE_DE = "Die Schnellen und die Wilden"
TITLE_EN = "The Fast and the Furious"
POSTER_URL = "https://i-viaplay-com.akamaized.net/viaplay-prod/177/164/1696334760-d8639e086e3f7530974d6edf0331eb85f9f020f8.jpg?width=400&height=600"
YOUTUBE_INTRO = "https://www.youtube.com/watch?v=6PHqjitVyXw"

INFO = {
    "Jahre": "2001 - 2023",
    "Staffeln": 10,
    "Laufzeit": "ca. 136 Min./Staffeln",
    "IMDb Rating": "6.5 / 10",
    "Stimmen": "ca. 324799",
}

CAST_MAIN = [
    "Vin Diesel - Dominic Toretto",
    "Paul Walker - Brian O´Conner",
    "MichellenRodriguez - Letty",
    "Jordana Brewster - Mia Toretto",
    "Rick Yune - Johnny Tran",

]

SUMMARY = (
    "**Fast & Furious**, auch bekannt als **The Fast and the Furious**, ist ein amerikanisches Action-Medien-Franchise, das auf einer Reihe von Filmen basiert, die sich um Straßenrennen, Raubüberfälle und Spione drehen. Das Franchise umfasst auch Kurzfilme, eine Fernsehserie, Spielzeug, Videospiele, Live-Shows und Themenpark-Attraktionen."
)

# ------------------------------------------------------------
# Layout : Header + Metrics
# ------------------------------------------------------------
with st.container():
    col_poster, col_title = st.columns([1, 2], gap="large")

    with col_poster:
        st.image(POSTER_URL, use_container_width=True)

    with col_title:
        st.title(f"{TITLE_EN} - {TITLE_DE}")
        st.caption(INFO["Jahre"] + " | " + INFO["Laufzeit"])

        m1, m2,  = st.columns(2)
        m1.metric("IMDb Rating", INFO["IMDb Rating"], None)
        m2.metric("Staffeln", INFO["Staffeln"])
       

        st.write(SUMMARY)

# ------------------------------------------------------------
# Tabs Section
# ------------------------------------------------------------

overview_tab, cast_tab, media_tab = st.tabs(["Überblick", "Hauptcast", "Media"])

with overview_tab:
    st.subheader("Kurzer Inhalt")


with cast_tab:
    st.subheader("Besetzung - Hauptrollen")
    st.write("\n".join([f"- {member}" for member in CAST_MAIN]))

with media_tab:
    st.subheader("Serien-Intro (Video)")
    st.video(YOUTUBE_INTRO)

# ------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------
with st.sidebar:
    st.header("📈 Statistik")
    st.metric("IMDb Rating", INFO["IMDb Rating"])

    st.header("🔗 Links")
    st.markdown("* [IMDb-Seite](https://www.imdb.com/de/title/tt5433140/?ref_=fn_all_ttl_2)\n* [Wikipedia-Artikel (de)](https://de.wikipedia.org/wiki/Fast_%26_Furious_(Filmreihe)#%C3%9Cberblick)")



# Datenstrukturen für Filme/Serien
series = {
    "Fast and Furious": {
        "director": "Rob Cohen",
        "year": 2001,
        "genre": "Action, Crime, Thriller",
        "synopsis": "An undercover cop becomes caught up in the thrilling world of street racing.",
    },
    "Breaking Bad": {
        "creator": "Vince Gilligan",
        "year": 2008,
        "genre": "Crime, Drama, Thriller",
        "synopsis": "A high school chemistry teacher turned methamphetamine manufacturer partners with a former student.",
    },
    "Inception": {
        "director": "Christopher Nolan",
        "year": 2010,
        "genre": "Science Fiction",
        "synopsis": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
    }
}

# Layout
st.title("Mehrfilm Serien Auswahl")
st.sidebar.title("Wähle eine Film/Serie")

# Auswahlbox
selected_item = st.sidebar.selectbox("Film/Serie", list(series.keys()))

# Anzeige der gewählten Optionen
st.header(selected_item)
st.subheader("Details")
if selected_item:
    info = series[selected_item]
    st.text(f"Regie/Ersteller: {info.get('director', info.get('creator'))}")
    st.text(f"Jahr: {info['year']}")
    st.text(f"Genre: {info['genre']}")
    st.text(f"Synopsis: {info['synopsis']}")



# Funktion, um benutzerdefiniertes CSS hinzuzufügen
def add_bg_color():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #FFCCCC; /* Helles Rot */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    add_bg_color()
    
    # Hauptinhalte der Webseite
    st.title("Fast and Furious Selektion")
    options = ["Film 1", "Film 2", "Film 3"]
    choice = st.selectbox("Wähle einen Film aus:", options)
    st.write(f"Sie haben {choice} ausgewählt.")

if __name__ == "__main__":
    main()
    