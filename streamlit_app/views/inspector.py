import streamlit as st

def show_memory_inspector():
    st.header("🕵️ Memory Inspector")
    st.info("Inspect a single memory entry by ID.")

    memory_id = st.text_input("Enter Memory ID to inspect", "")
    
    if memory_id:
        st.write(f"Showing details for memory ID: `{memory_id}`")
        st.json({
            "type": "episodic",
            "timestamp": "2025-05-10T12:34:56",
            "tags": ["daily", "important"],
            "summary": "This is a placeholder summary.",
            "full_text": "This is the full text of the memory entry."
        })
    else:
        st.warning("Enter a memory ID above to begin inspection.")
