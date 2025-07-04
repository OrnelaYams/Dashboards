import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Lieblingsobst der Klasse", layout="wide")

st.title("🍇Lieblingsobst der Klasse🍏")

# --- Datenbasis ---------------------------------------------------
df = pd.DataFrame({
    "Obst": ["Apfel", "Banane", "Erdbeere", "Orange", "Traube"],
    "Stimmen": [8, 5, 6, 4, 3],
    "Farbe": ["Rot", "Gelb", "Rot", "Orange", "Violett"],
    "Vitamin C (mg)": [12, 9, 60, 50, 4],
    "Herkunft": ["Deutschland", "Ecuador", "Spanien", "Italien", "Griechenland"],
    "Icon": ["🍎", "🍌", "🍓", "🍊", "🍇"],
    "InteressanteInfo": ["ist gut für die Herzgesundheit.","ist eine hervorragende Kaliumquelle.","wirkt harntreibend und blutreinigend","liefert eine hohe Dosis an Vitamin C","hilft bei Müdigkeit und heilt Nierenkrankheiten"],

    "Bild": [
        "https://tse1.mm.bing.net/th/id/OIP.WQ58YvuDt-x7TcDTF-uILQAAAA?rs=1&pid=ImgDetMain&o=7&rm=3",
        "https://foto.wuestenigel.com/wp-content/uploads/api/bananen.jpeg",
        "https://img.freepik.com/fotos-premium/reife-ernte-von-bio-erdbeeren-nahaufnahme-ansicht-von-oben_752567-316.jpg",
        "https://das-ernaehrungshandbuch.de/wp-content/uploads/2016/01/shutterstock_342874121-Orangen.jpg",
        "https://www.as-garten.de/media/image/a7/6f/45/41582_rosella_1000x1000_2.jpg",
    ]
 
})

col1, col2 = st.columns([2, 1])

# --- Interaktives Balkendiagramm ----------------------------------
fig = px.bar(
    df,
    x="Obst",
    y="Stimmen",
    hover_data=["Farbe", "Vitamin C (mg)", "Herkunft"],
    title="Stimmen für Lieblingsobst",
    #color="Obst",
    color_discrete_sequence=px.colors.sequential.Viridis
)


selected = col1.plotly_chart(fig, on_select="rerun")

# --- Auswahl auswerten -------------------------------------------
indices = selected["selection"]["point_indices"]

with col2:
    if not indices:
        st.info("👉 Klicke auf eine Obstsorte im Diagramm, um mehr zu erfahren.")
    else:
        obst = df.iloc[indices[0]]
        st.subheader(f"Details zu {obst.Icon} {obst.Obst}")
        st.image(obst.Bild, width=150)
       # with st.expander("Erfahren Sie mehr"):
        st.markdown(f"""
            - **Farbe**: {obst.Farbe}  
            - **Vitamin C**: {obst['Vitamin C (mg)']} mg  
            - **Typische Herkunft**: {obst.Herkunft}
            - **Interessante Info**: {obst.InteressanteInfo}
            """)



# --- Interaktives Kreisdiagramm --------------------------------
st.subheader("Stimmenanteil für jede Obstsorte")

pie_fig = px.pie(
    df,
    names="Obst",
    values="Stimmen",
    title="Stimmenverteilung je Obstsorte",
    color_discrete_sequence=px.colors.sequential.Viridis
)
st.plotly_chart(pie_fig, use_container_width=True)



# --- Interaktives Liniendiagramm ---------------------------------
st.subheader("Vitamin C Gehalt in verschiedenen Obstarten")

line_fig = px.line(
    df,
    x="Obst",
    y="Vitamin C (mg)",
    title="Vitamin C Gehalt je Obstsorte",
    markers=True,
    color_discrete_sequence=px.colors.sequential.Plasma
)
st.plotly_chart(line_fig, use_container_width=True)