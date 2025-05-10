import streamlit as st
from views.memory_table import show_memory_table
from views.context_trace import show_context_trace
from views.metadata_stats import show_metadata_stats
from views.inspector import show_memory_inspector

st.set_page_config(page_title="Memory Assistant", layout="wide")

# Sidebar navigation
st.sidebar.title("🧠 Memory Debugger")
page = st.sidebar.radio("Go to", [
    "📄 Memory Table",
    "🔍 Context Trace",
    "📊 Metadata & Stats",
    "🕵️ Inspect Memory"
])

# Page routing
if page == "📄 Memory Table":
    show_memory_table()
elif page == "🔍 Context Trace":
    show_context_trace()
elif page == "📊 Metadata & Stats":
    show_metadata_stats()
elif page == "🕵️ Inspect Memory":
    show_memory_inspector()
