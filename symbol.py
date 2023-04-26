import streamlit as st

def add_prefix(text, prefix):
    prefix_list = []
    if prefix == "With dot  1.2.3.":
        for i in range(1, len(text) + 1):
            prefix_list.append(str(i) + ".")
    elif prefix == "With () (1)(2)(3)":
        for i in range(1, len(text) + 1):
            prefix_list.append("(" + str(i) + ")")
    elif prefix == "With[] [1][2][3]":
        for i in range(1, len(text) + 1):
            prefix_list.append("[" + str(i) + "]")
    else:
        prefix_list = [prefix] * len(text)
    return [prefix_list[i] + text[i] for i in range(len(text))]

st.title("Add Prefix to Lines")

# Define columns
col1, col2, col3 = st.beta_columns(3)

# Column 1: Text Input
text_input = col1.text_area("Input Text:")

# Column 2: Prefix Options and Input
with col2.beta_form("options_form"):
    prefix_type = st.selectbox("Select Prefix Type:", ["Numeric", "Symbolic"])
    if prefix_type == "Numeric":
        prefix = st.selectbox("Select Numeric Prefix Style:", ["With dot  1.2.3.", "With () (1)(2)(3)", "With[] [1][2][3]"])
        text_input2 = st.text_input("Input Custom Numeric Prefix Style:")
    else:
        prefix = st.selectbox("Select Symbolic Prefix Style:", ["●", "■", "▶"])
        text_input2 = st.text_input("Input Custom Symbolic Prefix Style:")

# Column 3: Processed Text and Buttons
converted_text = add_prefix(text_input.split("\n"), prefix) if prefix_type == "Numeric" else [prefix + line for line in text_input.split("\n")]
output_text = "\n".join(converted_text)
col3.text_area("Output Text:", output_text)
if col3.button("Copy"):
    st.experimental_set_query_params(text=output_text)
    st.success("Copied to Clipboard!")
if col3.button("Reset"):
    st.experimental_set_query_params()
    st.experimental_rerun()
