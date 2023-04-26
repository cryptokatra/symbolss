import streamlit as st

def add_prefix(text, prefix):
    lines = text.split("\n")
    output = ""
    counter = 1
    for line in lines:
        line = line.strip()
        if line != "":
            output += f"{prefix}{counter}. {line}\n"
            counter += 1
    return output.strip()

def add_number_prefix(text):
    return add_prefix(text, "")

def add_dot_prefix(text):
    return add_prefix(text, "●")

def add_parenthesis_prefix(text):
    return add_prefix(text, "(%d)")

def add_square_bracket_prefix(text):
    return add_prefix(text, "[%d]")

def add_custom_symbol_prefix(text, symbol):
    return add_prefix(text, symbol)

prefix_options = ["With dot", "With ()", "With[]", "●", "■", "▶", "Custom symbol"]
symbol_options = ["%", "$", "@"]

st.set_page_config(page_title="Text Prefixer", page_icon=":memo:", layout="wide")

# Define layout
col1, col2, col3 = st.columns([1, 2, 1])

# Column 1: Text Input
with col1:
    st.write("### Text Input")
    text_input = st.text_area("", height=400)

# Column 2: Prefix Options
with col2:
    st.write("### Prefix Options")
    prefix_choice = st.selectbox("Choose a prefix option", prefix_options)
    if prefix_choice == "With dot":
        prefix_func = add_dot_prefix
    elif prefix_choice == "With ()":
        prefix_func = add_parenthesis_prefix
    elif prefix_choice == "With[]":
        prefix_func = add_square_bracket_prefix
    elif prefix_choice == "●":
        prefix_func = add_custom_symbol_prefix(text_input, "●")
    elif prefix_choice == "■":
        prefix_func = add_custom_symbol_prefix(text_input, "■")
    elif prefix_choice == "▶":
        prefix_func = add_custom_symbol_prefix(text_input, "▶")
    else:
        symbol_choice = st.selectbox("Choose a custom symbol", symbol_options)
        prefix_func = add_custom_symbol_prefix(text_input, symbol_choice)

    custom_prefix = st.text_input("Enter a custom prefix", value="", max_chars=10)
    if custom_prefix:
        prefix_func = add_custom_symbol_prefix(text_input, custom_prefix)

# Column 3: Text Output
with col3:
    st.write("### Text Output")
    if st.button("Add Prefix"):
        output = prefix_func(text_input)
        output = output.replace("\n\n", "\n").strip()
        st.text_area("", value=output, height=400)
    if st.button("Copy"):
        st.write("Copied to Clipboard!")
        st.write(output)
    if st.button("Reset"):
        st.experimental_rerun()

st.write("---")
