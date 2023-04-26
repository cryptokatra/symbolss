import streamlit as st
import re

# Define functions to add prefixes
def add_number_prefix(text, prefix):
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = f"{prefix}{i+1}. {lines[i]}"
    return '\n'.join(lines)

def add_symbol_prefix(text, prefix):
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = f"{prefix} {lines[i]}"
    return '\n'.join(lines)

# Define Streamlit app
def app():
    st.title("Add Prefixes to Text")
    
    # Define UI components
    col1, col2, col3 = st.columns(3)
    
    # Column 1: Input text box
    with col1:
        st.header("Input Text")
        input_text = st.text_area("Enter text")
        
    # Column 2: Prefix options
    with col2:
        st.header("Prefix Options")
        prefix_type = st.selectbox(
            "Select prefix type",
            ("Number", "Symbol")
        )
        if prefix_type == "Number":
            prefix_options = ("With dot  1.2.3.", "With () (1)(2)(3)", "With [] [1][2][3]")
        else:
            prefix_options = ("●", "■", "▶")
        prefix = st.selectbox("Select prefix", prefix_options)
        custom_prefix = st.text_input("Enter custom prefix (optional)")
        
    # Column 3: Output text box, copy and reset buttons
    with col3:
        st.header("Output Text")
        if prefix_type == "Number":
            if prefix == "With dot  1.2.3.":
                prefix = "."
            elif prefix == "With () (1)(2)(3)":
                prefix = ")"
            else:
                prefix = "]"
            output_text = add_number_prefix(input_text, prefix)
        else:
            output_text = add_symbol_prefix(input_text, prefix)
        if custom_prefix:
            output_text = add_symbol_prefix(input_text, custom_prefix)
        st.text_area("Output", value=output_text)
        if st.button("Copy"):
            st.write("Copied to clipboard!")
        st.button("Reset")
