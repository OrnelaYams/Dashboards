import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Beispielhafter Obst-Datensatz
data = {
    "Obstart": ["Apfel", "Banane", "Kirsche", "Mango", "Orange"],
    "Kalorien": [52, 89, 63, 60, 47],
    "Vitamin C (mg)": [4.6, 8.7, 7, 36.4, 53.2],
    "Ballaststoffe (g)": [2.4, 2.6, 1.5, 1.6, 2.2]
}

df = pd.DataFrame(data)

st.title("🍎 Obst-Informationsseite")

st.write("""
**Willkommen auf der Obst-Informationsseite! Hier finden Sie interessante Fakten 
zu verschiedenen Obstsorten und können sich über deren Nährstoffgehalt informieren.**
""")

# Auswahl eines Obstes
obst_auswahl = st.selectbox("Wählen Sie eine Obstsorte:", df["Obstart"])

# Anzeige der Informationen
obst_info = df[df["Obstart"] == obst_auswahl]
st.subheader(f"Informationen zu {obst_auswahl}")
st.write(obst_info)

# Diagramm der Nährwerte
st.subheader("Nährwertdiagramm")
fig, ax = plt.subplots()
obst_info.plot(kind="bar", x="Obstart", y=["Kalorien", "Vitamin C (mg)", "Ballaststoffe (g)"], ax=ax)
st.pyplot(fig)

st.write("")

# Weitere Informationen
st.header("Allgemeine Tipps und Wissenswertes")
st.write("""
- **Äpfel** sind gut für die Herzgesundheit.
- **Bananen** sind eine hervorragende Kaliumquelle.
- **Kirschen** enthalten Antioxidantien, die Entzündungen bekämpfen.
- **Mangofrüchte** können die Hautgesundheit verbessern.
- **Orangen** liefern eine hohe Dosis an Vitamin C.
""")