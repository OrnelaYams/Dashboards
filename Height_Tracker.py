import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from random import randint

st.set_page_config(page_title="Height Tracker", layout="centered", initial_sidebar_state="expanded")

# Initialize session-state storage
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame({
        "Name": ["Alice", "Bob", "Clara"],
        "Height (cm)": [172.5, 165.0, 180.3]
    })

if "highlight_value" not in st.session_state:
    st.session_state.highlight_value = None

st.title("📏 Height Tracker")

# Input sidebar
with st.sidebar:
    st.header("Add a new person")
    name = st.text_input("Name", key="name_input")
    height = st.number_input("Height (cm)", min_value=0.0, step=0.1, key="height_input")
    if st.button("Save"):
        if name and height:
            df = st.session_state.data
            st.session_state.data = pd.concat(
                [df, pd.DataFrame({"Name": [name], "Height (cm)": [height]})],
                ignore_index=True,
            )
            st.toast(f"Gespeichert: {name} - {height:.1f} cm", icon="✅")
        else:
            st.toast("Bitte sowohl Namen als auch Größe eingeben!", icon="⚠️")

    st.markdown("---")
    st.header("Datenoptionen")
    uploaded_file = st.file_uploader("CSV-Datei hochladen", type="csv")
    if uploaded_file is not None:
        try:
            df_upload = pd.read_csv(uploaded_file)
            if set(["Name", "Height (cm)"]).issubset(df_upload.columns):
                st.session_state.data = df_upload
                st.toast("Datei erfolgreich geladen!", icon="📄")
            else:
                st.warning("Die Datei muss die Spalten 'Name' und 'Height (cm)' enthalten.")
        except Exception as e:
            st.error(f"Fehler beim Laden der Datei: {e}")
    if st.button("🗑️ Datensatz leeren"):
        st.session_state.data = pd.DataFrame({"Name": [], "Height (cm)": []})
        st.toast("Daten wurden zurückgesetzt.", icon="🗑️")
    st.download_button(
        label="📥 CSV herunterladen",
        data=st.session_state.data.to_csv(index=False).encode("utf-8"),
        file_name="height_data.csv",
        mime="text/csv"
    )

# Editable table
st.subheader("Datensatz (bearbeitbar)")
edited_df = st.data_editor(
    st.session_state.data,
    num_rows="dynamic",
    use_container_width=True,
    key="data_editor",
)

# Persist edits back to session_state
after_edit = edited_df.copy()
st.session_state.data = after_edit

# Visualisierung: Histogramm
if not after_edit.empty:
    st.subheader("Höhenverteilung")
    plt.figure(figsize=(10, 4))
    sns.histplot(after_edit['Height (cm)'], bins=10, kde=True)
    plt.xlabel("Height (cm)")
    plt.title("Höhenverteilung")
    st.pyplot(plt)

# Metrics
if not after_edit.empty:
    max_height = after_edit["Height (cm)"].max()
    min_height = after_edit["Height (cm)"].min()
    avg_height = after_edit["Height (cm)"].mean()
    tallest_name = after_edit.loc[after_edit["Height (cm)"] == max_height, "Name"].values[0]
    shortest_name = after_edit.loc[after_edit["Height (cm)"] == min_height, "Name"].values[0]
    
    # Highlight Neue höchste oder niedrigste Höhe
    if st.session_state.highlight_value is None or max_height != st.session_state.highlight_value:
        st.balloons()
        st.session_state.highlight_value = max_height

    st.divider()
    st.subheader("Kennzahlen")
    col1, col2, col3 = st.columns(3)
    col1.metric("Größte Größe", f"{max_height:.1f} cm", f"von {tallest_name}")
    col2.metric("Kleinste Größe", f"{min_height:.1f} cm", f"von {shortest_name}")
    col3.metric("Durchschnitt", f"{avg_height:.1f} cm")
else:
    st.info("Füge Daten hinzu, um Kennzahlen zu sehen.")
