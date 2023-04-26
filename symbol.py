import streamlit as st

def add_prefix(input_text, prefix):
    lines = input_text.split("\n")
    output = []
    count = 1
    for line in lines:
        line = line.strip()
        if line:
            output.append(f"{prefix} {count}. {line}")
            count += 1
        else:
            output.append(line)
    return "\n".join(output)

def get_prefix_style(prefix_style):
    prefix = ""
    if prefix_style == "With dot":
        prefix = "."
    elif prefix_style == "With ()":
        prefix = "()"
    elif prefix_style == "With[]":
        prefix = "[]"
    elif prefix_style == "●":
        prefix = "●"
    elif prefix_style == "■":
        prefix = "■"
    elif prefix_style == "▶":
        prefix = "▶"
    return prefix

st.set_page_config(page_title="Prefix Adder")

st.title("Add Prefix to Each Line of Text")

input_text = st.text_area("Input Text", "", height=300)

prefix_style = st.selectbox("Select Prefix Style", 
    ["With dot", "With ()", "With[]", "●", "■", "▶"])

custom_prefix = st.text_input("Custom Prefix", "")

if custom_prefix:
    prefix = custom_prefix
else:
    prefix = get_prefix_style(prefix_style)

output_text = add_prefix(input_text, prefix)

st.text_area("Output Text", output_text, height=300)

if st.button("Copy"):
    st.write("Output text copied to clipboard!")
    st.experimental_set_query_params(output=output_text)

if "output" in st.experimental_get_query_params():
    copied_text = st.experimental_get_query_params()["output"]
    st.text_area("Copied Text", copied_text, height=300)
