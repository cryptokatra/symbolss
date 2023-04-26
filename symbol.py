import streamlit as st
import pyperclip

# Define function to add prefix to each line
def add_prefix(text, prefix):
    lines = text.split('\n')
    new_lines = []
    for i, line in enumerate(lines):
        if prefix[0] == 'Number':
            new_line = prefix[1] + str(i+1) + prefix[2] + ' ' + line
        else:
            new_line = prefix[1] + ' ' + line
        new_lines.append(new_line)
    return '\n'.join(new_lines)

# Define Streamlit app
def app():
    st.title("Add Prefix to Each Line")

    # Sidebar
    st.sidebar.subheader("Prefix Style")
    prefix_type = st.sidebar.selectbox("Select Prefix Style", ["Numbered", "Symbol"])
    if prefix_type == "Numbered":
        number_style = st.sidebar.radio("Number Style", [("With dot", ".", "."), ("With ()", "(", ")"), ("With []", "[", "]")])
        prefix = ("Number", number_style[0], number_style[1])
    else:
        symbol_style = st.sidebar.radio("Symbol Style", ["●", "■", "▶", "Custom"])
        if symbol_style == "Custom":
            custom_symbol = st.sidebar.text_input("Enter Custom Symbol")
            if custom_symbol:
                prefix = ("Symbol", custom_symbol)
            else:
                st.sidebar.warning("Please enter a custom symbol")
                st.stop()
        else:
            prefix = ("Symbol", symbol_style)

    # Main Page
    st.subheader("Input Text")
    text_input = st.text_area("Enter Text Here")

    # Output for Number Prefix
    st.subheader("Output with Number Prefix")
    if text_input:
        text_with_number_prefix = add_prefix(text_input, prefix)
        st.code(text_with_number_prefix, language='text')
        # Copy Button
        if st.button("Copy to Clipboard"):
            pyperclip.copy(text_with_number_prefix)
            st.success("Text copied to clipboard")

    # Output for Symbol Prefix
    st.subheader("Output with Symbol Prefix")
    if text_input:
        symbol_prefix = ("Symbol", prefix[1])
        text_with_symbol_prefix = add_prefix(text_input, symbol_prefix)
        st.code(text_with_symbol_prefix, language='text')
        # Copy Button
        if st.button("Copy to Clipboard"):
            pyperclip.copy(text_with_symbol_prefix)
            st.success("Text copied to clipboard")

    # Reset Button
    if st.button("Reset"):
        st.experimental_rerun()
