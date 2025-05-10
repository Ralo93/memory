import streamlit as st

def show_metadata_stats():
    st.header("📊 Metadata & Memory Stats")
    st.info("This page will show aggregate memory usage, tag frequency, and stale memory counts.")

    # Placeholder stats
    st.metric(label="Total Memories", value="0")
    st.metric(label="Tagged as 'important'", value="0")
    st.metric(label="Stale / Unused", value="0")

    st.write("Memory usage heatmaps, tag charts, etc. will go here.")
