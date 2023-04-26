import streamlit as st

def add_prefix(text, prefix):
    lines = text.split("\n")
    formatted_lines = []
    i = 0
    for line in lines:
        line = line.strip()
        if line == "":
            formatted_lines.append(line)
        else:
            formatted_lines.append(f"{prefix}{i+1}. {line}")
            i += 1
    return "\n".join(formatted_lines)

def main():
    st.title("Add Prefix to Text")
    c_text = st.empty()
    format_option = st.selectbox(
        "Choose a Format",
        [
            "With dot  1.2.3.",
            "With () (1)(2)(3)",
            "With[] [1][2][3]",
            "●",
            "■",
            "▶",
            "Custom"
        ]
    )
    if format_option == "Custom":
        custom_format = st.text_input("Enter Custom Prefix")
        prefix = custom_format if custom_format != "" else "Custom"
    else:
        prefix = format_option
    text = st.text_area("Enter Text Here")
    if st.button("Add Prefix"):
        text = add_prefix(text, prefix)
        text = text.strip()
        c_text.value = text
    if st.button("Copy Text"):
        st.write("Copied to Clipboard!")


if __name__ == "__main__":
    main()
