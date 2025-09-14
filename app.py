import streamlit as st
import os

# File to store the visitor count
VISITOR_COUNT_FILE = "visitor_count.txt"

def load_visitor_count():
    if os.path.exists(VISITOR_COUNT_FILE):
        with open(VISITOR_COUNT_FILE, "r") as f:
            return int(f.read().strip())
    return 0

def save_visitor_count(count):
    with open(VISITOR_COUNT_FILE, "w") as f:
        f.write(str(count))

# Initialize session state for visitor count if it doesn't exist
if 'visitor_count' not in st.session_state:
    # Load the existing count from file
    count = load_visitor_count()
    # Increment the count for this visit
    count += 1
    # Save the new count
    save_visitor_count(count)
    # Store in session state
    st.session_state.visitor_count = count

# Display the visitor count
st.title("Welcome to Our App!")
st.write(f"You are visitor number: {st.session_state.visitor_count}")

# Add some additional information
st.info("""
This counter tracks unique visits by:
- Initial app load
- Page reloads
The count is persisted to a file, so it maintains state between app restarts.
""")