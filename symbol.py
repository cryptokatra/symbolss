import streamlit as st

def add_prefix(text_list, prefix):
    return [f"{prefix}{line.strip()}" for line in text_list]

def add_number_prefix(text_list):
    return [f"{i + 1}. {line.strip()}" for i, line in enumerate(text_list)]

def add_symbol_prefix(text_list, symbol):
    return [f"{symbol} {line.strip()}" for line in text_list]

def remove_empty_lines(text_list):
    return [line for line in text_list if line.strip()]

def format_text(text_list, prefix):
    if prefix.startswith("With dot"):
        return add_number_prefix(text_list)
    elif prefix.startswith("With ()"):
        return add_prefix(text_list, "(")
    elif prefix.startswith("With[]"):
        return add_prefix(text_list, "[")
    elif prefix.startswith("●"):
        return add_symbol_prefix(text_list, "●")
    elif prefix.startswith("■"):
        return add_symbol_prefix(text_list, "■")
    elif prefix.startswith("▶"):
        return add_symbol_prefix(text_list, "▶")
    else:
        return add_prefix(text_list, prefix)

st.set_page_config(layout="wide")
col1, col2, col3 = st.beta_columns(3)

with col1:
    input_text = st.text_area("Column1: Input text")

with col2:
    format_options = [
        "With dot",
        "With ()",
        "With[]",
        "●",
        "■",
        "▶",
        "Custom",
    ]
    selected_format = st.selectbox("Column2: Select format", format_options)
    if selected_format == "Custom":
        custom_prefix = st.text_input("Enter custom prefix")
    else:
        custom_prefix = ""

with col3:
    output_text = st.text_area("Column3: Output text")

    if st.button("Copy output"):
        st.experimental_set_query_params(text="\n".join(remove_empty_lines(output_text.split("\n"))))
        st.success("Output copied to clipboard")

    if selected_format != st.session_state.get("selected_format", ""):
        st.session_state.selected_format = selected_format
        st.session_state.custom_prefix = custom_prefix
        input_text_list = remove_empty_lines(input_text.split("\n"))
        output_text_list = format_text(input_text_list, selected_format if selected_format != "Custom" else custom_prefix)
        st.session_state.output_text = "\n".join(remove_empty_lines(output_text_list))
        output_text = st.session_state.output_text

    if input_text and output_text:
        st.write("Adding prefix...")
        input_text_list = remove_empty_lines(input_text.split("\n"))
        output_text_list = format_text(input_text_list, selected_format if selected_format != "Custom" else custom_prefix)
        st.session_state.output_text = "\n".join(remove_empty_lines(output_text_list))
        st.write(st.session_state.output_text.strip())
