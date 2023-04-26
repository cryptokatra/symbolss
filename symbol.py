import streamlit as st

def add_prefix(text, prefix):
    lines = text.split('\n')
    if prefix == "With dot":
        prefix_list = [f"{i}." for i in range(1, len(lines) + 1)]
    elif prefix == "With ()":
        prefix_list = [f"({i})" for i in range(1, len(lines) + 1)]
    elif prefix == "With[]":
        prefix_list = [f"[{i}]" for i in range(1, len(lines) + 1)]
    elif prefix == "●":
        prefix_list = ["●"] * len(lines)
    elif prefix == "■":
        prefix_list = ["■"] * len(lines)
    elif prefix == "▶":
        prefix_list = ["▶"] * len(lines)
    else:
        prefix_list = [prefix] * len(lines)
    return "\n".join([f"{prefix_list[i]} {lines[i]}" for i in range(len(lines))])

def main():
    st.set_page_config(page_title="Add Prefix App")
    st.title("Add Prefix App")

    # Column 1
    st.sidebar.markdown("# Input Text")
    text_input = st.sidebar.text_area("Enter text here:", height=500)

    # Column 2
    st.sidebar.markdown("# Prefix Options")
    prefix_type = st.sidebar.selectbox("Select prefix type:", ["With dot", "With ()", "With[]", "●", "■", "▶", "Custom"])

    if prefix_type == "Custom":
        prefix = st.sidebar.text_input("Enter custom prefix here:")
    else:
        prefix = prefix_type

    # Column 3
    st.markdown("# Output Text")
    output_text = add_prefix(text_input, prefix)
    text_output = st.text_area("Result", value=output_text, height=500)

    if st.button("Copy"):
        st.experimental_set_query_params(text_output=text_output)

    if st.button("Clear"):
        text_input = ""
        text_output = ""
        st.experimental_set_query_params(text_input="", text_output="")
        
    st.write(" ")
    
    if st.button("Add Prefix"):
        output_text = add_prefix(text_input, prefix)

    st.radio("Select prefix type:", options=["With dot", "With ()", "With[]", "●", "■", "▶", "Custom"], key="options")

    if st.session_state.options == "Custom":
        prefix = st.text_input("Enter custom prefix here:", key="custom-prefix")
    else:
        prefix = st.session_state.options

    st.text_input("Enter text here:", value=text_input, key="input-text")

    output_text = add_prefix(text_input, prefix)
    st.code(output_text)

    st.empty()

if __name__ == "__main__":
    main()
