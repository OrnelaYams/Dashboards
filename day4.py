import streamlit as st
 
st.title("Überweisung durchführen")
 
if "step" not in st.session_state:
    st.session_state.step = "Daten aufnehmen"
 
 
if st.session_state.step == "Daten aufnehmen":
    st.write("Bitte geben Sie die Überweisungsdaten an:")
    c1, c2 = st.columns(2)
    c1.text_input("IBAN")
    c2.number_input("Betrag")
 
    b1 = st.button("Bestätigung starten")
   # if b1:
    #    st.session_state.step = "Daten bestätigen"
 
if st.session_state.step == "Daten bestätigen":
    st.write("Bestätigen Sie bitte die folgenden Eingaben:")
   