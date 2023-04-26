import streamlit as st


def get_prefixed_text(text, prefix):
    lines = text.strip().split("\n")
    count = 1
    indent = ""
    if isinstance(prefix, int):
        for i, line in enumerate(lines):
            if line.strip() == "":
                continue
            lines[i] = f"{count:02d}.{indent}{line}"
            count += 1
    else:
        for i, line in enumerate(lines):
            if line.strip() == "":
                continue
            lines[i] = f"{prefix}{indent}{line}"
    return "\n".join(lines)


def main():
    st.set_page_config(page_title="Add Prefix", page_icon=":pencil:")
    st.title("Add Prefix to Text")

    column1, column2, column3 = st.beta_columns((1, 1, 2))

    with column1:
        input_text = st.text_area("Enter Text")

    with column2:
        prefix_type = st.selectbox("Select Prefix Type", ("Number", "Symbol", "New Symbol 1", "New Symbol 2", "New Symbol 3"))
        if prefix_type == "Number":
            prefix_style = st.selectbox("Select Number Style", ("With dot", "With ()", "With []"))
        else:
            prefix_style = st.text_input("Enter Symbol Style")

        if prefix_type == "New Symbol 1":
            prefix_style = "●"
        elif prefix_type == "New Symbol 2":
            prefix_style = "■"
        elif prefix_type == "New Symbol 3":
            prefix_style = "▶"

    with column3:
        output_text = get_prefixed_text(input_text, 1)
        output_text_area = st.empty()
        copy_button = st.button("Copy")
        reset_button = st.button("Reset")

        if prefix_type == "Number":
            if prefix_style == "With dot":
                prefix = "1.2.3."
            elif prefix_style == "With ()":
                prefix = "(1)(2)(3)"
            else:
                prefix = "[1][2][3]"
        else:
            prefix = prefix_style

        if copy_button:
            st.write("Text copied to clipboard!")
            st.experimental_set_query_params(text=output_text)
        elif reset_button:
            input_text = ""
            output_text = ""
            output_text_area.text(output_text)
        else:
            if input_text.strip() != "":
                output_text = get_prefixed_text(input_text, prefix)
                output_text_area.text(output_text)


if __name__ == "__main__":
    main()
