import streamlit as st

# Define the functions to add prefix to the text
def add_prefix_with_dot(text):
    lines = text.split("\n")
    prefix = ""
    new_lines = []
    for i, line in enumerate(lines):
        new_lines.append(f"{prefix}{i+1}. {line}")
    return "\n".join(new_lines)

def add_prefix_with_parenthesis(text):
    lines = text.split("\n")
    prefix = ""
    new_lines = []
    for i, line in enumerate(lines):
        new_lines.append(f"{prefix}({i+1}){line}")
    return "\n".join(new_lines)

def add_prefix_with_bracket(text):
    lines = text.split("\n")
    prefix = ""
    new_lines = []
    for i, line in enumerate(lines):
        new_lines.append(f"{prefix}[{i+1}]{line}")
    return "\n".join(new_lines)

# Define the Streamlit app
def app():
    st.set_page_config(page_title="Prefix Adder")

    st.title("Prefix Adder")

    # Define the input text box
    st.sidebar.header("Input Text")
    text = st.sidebar.text_area("Enter text here", height=300)

    # Define the prefix selection widgets
    st.sidebar.header("Prefix Options")
    prefix_type = st.sidebar.selectbox("Select prefix type", ["Numbers", "Symbols", "Custom"])
    if prefix_type == "Numbers":
        prefix_value = st.sidebar.selectbox("Select prefix value", ["1.2.3.", "(1)(2)(3)", "[1][2][3]"])
    elif prefix_type == "Symbols":
        prefix_value = st.sidebar.selectbox("Select prefix value", ["●", "■", "▶"])
    else:
        prefix_value = st.sidebar.text_input("Enter custom prefix value")

    # Define the output text boxes
    st.header("Output Text")
    st.subheader("Text with numbered prefix")
    if prefix_type == "Numbers":
        output_text = add_prefix_with_dot(text) if prefix_value == "1.2.3." else \
                      add_prefix_with_parenthesis(text) if prefix_value == "(1)(2)(3)" else \
                      add_prefix_with_bracket(text) if prefix_value == "[1][2][3]" else ""
    else:
        output_text = f"{prefix_value}\n{text}".replace("\n", f"\n{prefix_value}")
    st.text_area("Text with numbered prefix", value=output_text, height=300)
    st.subheader("Text with symbol prefix")
    if prefix_type == "Numbers":
        st.text_area("Text with symbol prefix", value="")
    else:
        output_text = f"{prefix_value}\n{text}".replace("\n", f"\n{prefix_value}")
        st.text_area("Text with symbol prefix", value=output_text, height=300)

    # Define the copy and reset buttons
    if st.button("Copy text with numbered prefix"):
        st.write("Text copied to clipboard!")
        st.experimental_set_query_params(output_text=output_text)
    if st.button("Copy text with symbol prefix"):
        st.write("Text copied to clipboard!")
        st.experimental_set_query_params(output_text=output_text)
    if st.button("Reset"):
        st.experimental_set_query_params(output_text="")
        
if __name__ == "__main__":
    app()
