import streamlit as st
import pyperclip

st.set_page_config(page_title="Prefixer", layout="wide")

# Define function for copying to clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)
    st.sidebar.text("Copied to clipboard!")
    
# Define function for resetting the app
def reset_app():
    text_input.text("")
    dropdown_num.selectbox("Select prefix style:", prefix_options)
    dropdown_symbol.selectbox("Select symbol:", symbol_options)
    custom_prefix_text.empty()
    custom_symbol_text.empty()
    output_text_B.empty()
    output_text_C.empty()

# Define prefix options
prefix_options = ["With dot", "With ()", "With []", "Custom"]

# Define symbol options
symbol_options = ["●", "■", "▶", "Custom"]

# Define streamlit widgets
text_input = st.sidebar.text_area("Enter Text:")
prefix_choice = st.sidebar.selectbox("Select prefix style:", prefix_options)
dropdown_num = None
custom_prefix_text = None
if prefix_choice == "Custom":
    custom_prefix_text = st.sidebar.text_input("Enter custom prefix:")
else:
    dropdown_num = st.sidebar.selectbox("", ["1. 2. 3.", "(1)(2)(3)", "[1][2][3]"])

symbol_choice = st.sidebar.selectbox("Select symbol:", symbol_options)
dropdown_symbol = None
custom_symbol_text = None
if symbol_choice == "Custom":
    custom_symbol_text = st.sidebar.text_input("Enter custom symbol:")
else:
    dropdown_symbol = st.sidebar.selectbox("", ["●", "■", "▶"])

output_text_B = st.empty()
output_text_C = st.empty()

# Create buttons for copying the output
if st.sidebar.button('Copy B'):
    copy_to_clipboard(output_text_B.to_dict()['children'][0])
if st.sidebar.button('Copy C'):
    copy_to_clipboard(output_text_C.to_dict()['children'][0])
if st.sidebar.button('Reset'):
    reset_app()

# Get text input and split into lines
text = text_input.splitlines()

# Create new lines with prefixes based on user input
new_lines_B = []
prefix_num = 1
for line in text:
    prefix = ""
    if prefix_choice == "With dot":
        prefix = f"{prefix_num}. "
    elif prefix_choice == "With ()":
        prefix = f"({prefix_num})"
    elif prefix_choice == "With []":
        prefix = f"[{prefix_num}]"
    else:
        prefix = f"{custom_prefix_text.value} "
    new_line = f"{prefix}{line}"
    new_lines_B.append(new_line)
    prefix_num += 1

# Join new lines and write to output text box B
if len(new_lines_B) > 0:
    output_text_B.markdown("\n".join(new_lines_B))

# Create new lines with suffixes based on user input
new_lines_C = []
for line in text:
    if symbol_choice == "●":
        suffix = " ●"
    elif symbol_choice == "■":
        suffix = " ■"
    elif symbol_choice == "▶":
        suffix = " ▶"
    else:
        suffix = f" {custom_symbol_text.value}"
    new_line = f"{line}{suffix}"
    new_lines_C.append(new_line)

# Join new lines and write to output text box C
if len(new_lines_C) > 0:
    output_text_C.markdown("\n".join(new_lines_C))
