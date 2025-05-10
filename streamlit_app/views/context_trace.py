import streamlit as st

def show_context_trace():
    st.header("🔍 Context Trace")
    st.info("This page will show which memory entries were used to generate a specific assistant response.")

    # Placeholder for future selection
    st.selectbox("Choose a past query or session ID", ["(none available yet)"])
    st.write("Memory trace for selected query will appear here.")
