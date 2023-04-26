import streamlit as st

def add_prefix(text, prefix):
    prefix_text = ""
    if prefix == "With dot":
        prefix_text = "{}. ".format(text[0])
    elif prefix == "With ()":
        prefix_text = "({}) ".format(text[0])
    elif prefix == "With[]":
        prefix_text = "[{}] ".format(text[0])
    elif prefix == "●":
        prefix_text = "● "
    elif prefix == "■":
        prefix_text = "■ "
    elif prefix == "▶":
        prefix_text = "▶ "
    return prefix_text + text[1:]

def add_line_numbers(text):
    lines = text.split("\n")
    numbered_lines = [add_prefix((str(i+1), line), st.session_state.prefix) for i, line in enumerate(lines)]
    return "\n".join(numbered_lines)

def copy_to_clipboard(text):
    st.experimental_set_query_params(text=text)
    st.info("You can now copy the text from the URL")

def reset():
    st.session_state.textbox = ""
    st.session_state.prefix = "With dot"
    st.session_state.custom_style = ""

st.title("Add Prefix to Each Line of Text")

st.sidebar.title("Options")

st.sidebar.markdown("### Select Prefix Style")
prefix_options = ["With dot", "With ()", "With[]", "●", "■", "▶"]
st.sidebar.selectbox("", prefix_options, key="prefix", index=0)
if st.session_state.prefix != st.session_state.prefix_changed:
    st.session_state.prefix = st.session_state.prefix_changed

st.sidebar.markdown("### Custom Style")
custom_style = st.sidebar.text_input("", max_chars=1, key="custom_style")
if st.session_state.custom_style != st.session_state.custom_style_changed:
    st.session_state.custom_style = st.session_state.custom_style_changed

st.sidebar.markdown("### Reset")
if st.sidebar.button("Reset"):
    reset()

st.sidebar.markdown("---")

st.markdown("### Enter Text")
textbox = st.text_area(" ", key="textbox")
if st.session_state.textbox != st.session_state.textbox_changed:
    st.session_state.textbox = st.session_state.textbox_changed

prefix = st.session_state.prefix
if st.session_state.custom_style:
    prefix = st.session_state.custom_style

if st.session_state.textbox:
    st.write("### Output Text")
    output_text = add_line_numbers(st.session_state.textbox)
    st.text_area(" ", value=output_text, key="output_text")
    if st.button("Copy to Clipboard"):
        copy_to_clipboard(output_text)
else:
    st.write("Please enter some text in the textbox above.")
