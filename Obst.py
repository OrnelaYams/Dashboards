import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Lieblingsobst der Klasse", layout="wide")

st.title("🍇 Lieblingsobst der Klasse 🍏")

# --- Datenbasis ---------------------------------------------------
df = pd.DataFrame({
    "Obst": ["Apfel", "Banane", "Erdbeere", "Orange", "Traube"],
    "Stimmen": [8, 5, 6, 4, 3],
    "Farbe": ["Rot", "Gelb", "Rot", "Orange", "Violett"],
    "Vitamin C (mg)": [12, 9, 60, 50, 4],
    "Herkunft": ["Deutschland", "Ecuador", "Spanien", "Italien", "Griechenland"],
    "Icon": ["🍎", "🍌", "🍓", "🍊", "🍇"],
    "Bild": [
        "https://example.com/apfel.png",
        "https://example.com/banane.png",
        "https://example.com/erdbeere.png",
        "https://example.com/orange.png",
        "https://example.com/traube.png",
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
    color="Obst",
    color_discrete_sequence=px.colors.sequential.Viridis
)

col1.plotly_chart(fig)
selected_obst = col1.selectbox("Wähle eine Obstsorte aus:", df["Obst"])

# --- Auswahl auswerten -------------------------------------------
with col2:
    if selected_obst:
        obst = df[df["Obst"] == selected_obst].iloc[0]
        st.subheader(f"Details zu {obst.Icon} {obst.Obst}")
        st.image(obst.Bild, width=150)
        with st.expander("Erfahre mehr"):
            st.markdown(f"""
            - **Farbe**: {obst.Farbe}  
            - **Vitamin C**: {obst['Vitamin C (mg)']} mg  
            - **Typische Herkunft**: {obst.Herkunft}
            - **Interessante Info**: Wussten Sie, dass {obst.Obst}s sehr gesund sind und oft als Teil einer ausgewogenen Ernährung empfohlen werden?
            """)

# --- Kreisdiagramm: Stimmenanteil --------------------------------
st.subheader("Stimmenanteil für jede Obstsorte")

pie_fig = px.pie(
    df,
    names="Obst",
    values="Stimmen",
    title="Stimmenverteilung je Obstsorte",
    color_discrete_sequence=px.colors.sequential.Viridis
)
st.plotly_chart(pie_fig)

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
st.plotly_chart(line_fig)