import streamlit as st

def add_prefix(input_text, prefix):
    lines = input_text.split("\n")
    prefix_lines = []
    for i, line in enumerate(lines):
        line = line.strip()
        if line:
            prefix_line = f"{prefix}{line}"
            prefix_lines.append(prefix_line)
    return "\n".join(prefix_lines)

def main():
    st.title("Add Prefix to Text")

    # Column 1
    input_text = st.text_area("Enter Text")

    # Column 2
    format_options = ["With dot", "With ()", "With []", "●", "■", "▶", "Custom"]
    format_option = st.selectbox("Select Format", format_options)
    if format_option == "Custom":
        prefix = st.text_input("Enter Custom Prefix")
    else:
        if format_option == "With dot":
            prefix = "1."
        elif format_option == "With ()":
            prefix = "(1)"
        elif format_option == "With []":
            prefix = "[1]"
        else:
            prefix = format_option

    # Column 3
    if st.button("Add Prefix"):
        output_text = add_prefix(input_text, prefix)
        st.text_area("Result", output_text)

    if st.button("Copy"):
        output_text = add_prefix(input_text, prefix)
        st.write(output_text)
        st.text_input("", value=output_text)

if __name__ == "__main__":
    main()
