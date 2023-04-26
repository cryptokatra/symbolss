import streamlit as st

def add_prefix(prefix, lines, style):
    prefix_lines = []
    if style == "With dot":
        for i, line in enumerate(lines):
            prefix_lines.append(f"{i+1}{prefix}{line}")
    elif style == "With ()":
        for i, line in enumerate(lines):
            prefix_lines.append(f"({i+1}){prefix}{line}")
    elif style == "With[]":
        for i, line in enumerate(lines):
            prefix_lines.append(f"[{i+1}]{prefix}{line}")
    elif style == "Custom":
        for i, line in enumerate(lines):
            prefix_lines.append(f"{prefix+{i+1}}{line}")
    return prefix_lines

st.title("Add Prefix Tool")

# Define the text input box for the user
text_input = st.text_area("Enter Text Here:")

# Define the prefix style dropdown for the user
prefix_style = st.selectbox("Select Prefix Style:", ("With dot", "With ()", "With[]", "Custom"))

# Define the prefix input box for the user
prefix_input = st.text_input("Enter Prefix Here:", "")

# Define the symbol style dropdown for the user
symbol_style = st.selectbox("Select Symbol Style:", ("●", "■", "▶", "Custom"))

# Define the symbol input box for the user
symbol_input = st.text_input("Enter Symbol Here:", "●")

# Define the buttons
if st.button("Add Prefix"):
    lines = text_input.split("\n")
    prefix_lines = add_prefix(prefix_input, lines, prefix_style)
    prefix_text = "\n".join(prefix_lines)
    st.text_area("Prefixed Text:", value=prefix_text)
    
if st.button("Add Symbol"):
    lines = text_input.split("\n")
    symbol_lines = [f"{symbol_input} {line}" for line in lines]
    symbol_text = "\n".join(symbol_lines)
    st.text_area("Symbolized Text:", value=symbol_text)

if st.button("Clear All"):
    st.text_input("Enter Text Here:", value="")
    st.text_input("Enter Prefix Here:", value="")
    st.text_input("Enter Symbol Here:", value="")
