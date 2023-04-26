import streamlit as st

def add_prefix_text(text, prefix):
    lines = text.split("\n")
    output = ""
    for i, line in enumerate(lines):
        if prefix.isdigit():
            prefix_text = prefix + ". "
            prefix = str(int(prefix) + 1)
        else:
            prefix_text = prefix + " "
        output += prefix_text + line + "\n"
    return output

def main():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        text_input = st.text_area("Enter your text here:", height=300)

    with col2:
        st.write("Select prefix type:")
        prefix_type = st.radio("", ["Number", "Symbol"])
        if prefix_type == "Number":
            prefix_options = ["With dot 1.2.3.", "With () (1)(2)(3)", "With[] [1][2][3]"]
        else:
            prefix_options = ["●", "■", "▶"]
        prefix = st.selectbox("Select prefix option:", prefix_options)
        custom_prefix = st.text_input("Or enter a custom prefix:")

    with col3:
        if st.button("Add Prefix"):
            if custom_prefix:
                prefix = custom_prefix
            if prefix_type == "Number":
                prefix = prefix.split(".")[0]
            output = add_prefix_text(text_input, prefix)
            output_area = st.empty()
            output_area.text_area("Output:", value=output, height=300)

        if st.button("Copy Output"):
            output_area = st.empty()
            output_area.text_area("Output:", value=output, height=300)
            output_area.text_input("Copy the text below:")
        
        if st.button("Reset"):
            st.experimental_rerun()

if __name__ == "__main__":
    main()
