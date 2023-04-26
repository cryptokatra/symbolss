import streamlit as st
from streamlit_bokeh_events import streamlit_bokeh_events


def add_prefix_with_number(prefix, number_style):
    return f"{number_style}{prefix}"


def add_prefix_with_symbol(prefix, symbol):
    return f"{symbol} {prefix}"


def main():
    st.set_page_config(page_title="Prefix Adder", page_icon=":pencil2:")

    st.title("Prefix Adder")

    # Left-hand side: input text box
    input_text = st.text_area("Enter text here")

    # Middle: select number style and symbol style
    number_style = st.selectbox("Select number style", options=["With dot  1.2.3.", "With () (1)(2)(3)", "With[] [1][2][3]"])
    symbol_style = st.selectbox("Select symbol style", options=["●", "■", "▶", "Custom"])

    if symbol_style == "Custom":
        custom_symbol = st.text_input("Enter custom symbol here")
    else:
        custom_symbol = symbol_style

    # Right-hand side: output text boxes
    output_with_number = st.text_area("Output with number prefix")
    output_with_symbol = st.text_area("Output with symbol prefix")

    # Add prefixes to input text when button is clicked
    if streamlit_bokeh_events("Add prefixes", key="add_button"):
        input_lines = input_text.split("\n")
        for i, line in enumerate(input_lines):
            output_with_number.write(add_prefix_with_number(line, i+1))
            output_with_number.write("\n")

            output_with_symbol.write(add_prefix_with_symbol(line, custom_symbol))
            output_with_symbol.write("\n")

    # Buttons to copy output text and reset
    col1, col2, col3 = st.beta_columns([1, 1, 1])

    if col1.button("Copy output with number prefix"):
        st.experimental_set_query_params(output_with_number.to_dataframe().to_csv(index=False), key="number-output")
    if col2.button("Copy output with symbol prefix"):
        st.experimental_set_query_params(output_with_symbol.to_dataframe().to_csv(index=False), key="symbol-output")
    if col3.button("Reset"):
        output_with_number.empty()
        output_with_symbol.empty()

    # Display output text if query parameter is present
    if "number-output" in st.experimental_get_query_params():
        output_with_number.write(st.experimental_get_query_params()["number-output"][0])
    if "symbol-output" in st.experimental_get_query_params():
        output_with_symbol.write(st.experimental_get_query_params()["symbol-output"][0])


if __name__ == "__main__":
    main()
