import streamlit as st
import pyperclip

def add_prefix(input_text, prefix):
    output_text = []
    for index, line in enumerate(input_text.splitlines(), start=1):
        output_text.append(f"{prefix}{index}. {line}")
    return '\n'.join(output_text)

def add_prefix_with_symbol(input_text, symbol):
    output_text = []
    for line in input_text.splitlines():
        output_text.append(f"{symbol} {line}")
    return '\n'.join(output_text)

def get_number_style(style):
    if style == "With dot":
        return "."
    elif style == "With ()":
        return "()"
    elif style == "With []":
        return "[]"

def get_symbol_style(style):
    if style == "●":
        return "●"
    elif style == "■":
        return "■"
    elif style == "▶":
        return "▶"

def copy_to_clipboard(text):
    pyperclip.copy(text)

# Create the Streamlit web app
def main():
    st.title("Add Prefix to Text")
    text_input = st.text_area("Enter Text:")
    number_style = st.selectbox(
        "Select Number Style:",
        ("With dot", "With ()", "With []")
    )
    symbol_style = st.selectbox(
        "Select Symbol Style:",
        ("●", "■", "▶")
    )
    custom_style = st.text_input("Enter Custom Style:")
    number_prefix = get_number_style(number_style)
    symbol_prefix = get_symbol_style(symbol_style)
    if custom_style:
        number_prefix = custom_style
        symbol_prefix = custom_style
    text_output_number = add_prefix(text_input, number_prefix)
    text_output_symbol = add_prefix_with_symbol(text_input, symbol_prefix)
    st.subheader("Output with Numbers:")
    st.text_area("Output with Numbers:", text_output_number)
    st.subheader("Output with Symbols:")
    st.text_area("Output with Symbols:", text_output_symbol)
    if st.button("Copy Output with Numbers"):
        copy_to_clipboard(text_output_number)
        st.success("Output with Numbers copied to clipboard!")
    if st.button("Copy Output with Symbols"):
        copy_to_clipboard(text_output_symbol)
        st.success("Output with Symbols copied to clipboard!")
    if st.button("Reset"):
        st.text_input("Enter Text:")
        st.empty()

if __name__ == "__main__":
    main()
