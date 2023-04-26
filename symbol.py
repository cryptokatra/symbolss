import streamlit as st

def main():
    st.set_page_config(page_title="Prefix Tool", page_icon=":pencil2:")
    st.title("Prefix Tool")

    # 文本框A
    st.subheader("Input Text")
    input_text = st.text_area("Enter text here", height=150)

    # 文本框B + 選擇數字
    st.subheader("Add Prefix Number")
    prefix_num = st.selectbox("Select number style", options=["With dot 1.2.3.", "With () (1)(2)(3)", "With[] [1][2][3]", "Custom"], index=0)
    if prefix_num == "Custom":
        custom_num = st.text_input("Enter custom number style")
        prefix_num = custom_num

    with_num = ""
    if prefix_num.startswith("With dot"):
        with_num = "1. "
    elif prefix_num.startswith("With ()"):
        with_num = "(1) "
    elif prefix_num.startswith("With[]"):
        with_num = "[1] "
    else:
        with_num = prefix_num + " "

    text_with_prefix_num = ""
    text_lines = input_text.split("\n")
    for index, line in enumerate(text_lines):
        text_with_prefix_num += f"{with_num}{line}\n"

    st.text_area("Text with Prefix Number", value=text_with_prefix_num, height=150)

    # 文本框C + 選擇符號
    st.subheader("Add Prefix Symbol")
    prefix_sym = st.selectbox("Select symbol style", options=["BLACK CIRCLE ●", "BLACK SQUARE ■", "BLACK RIGHT-POINTING TRIANGLE ▶", "Custom"], index=0)
    if prefix_sym == "Custom":
        custom_sym = st.text_input("Enter custom symbol style")
        prefix_sym = custom_sym

    text_with_prefix_sym = ""
    text_lines = input_text.split("\n")
    for index, line in enumerate(text_lines):
        text_with_prefix_sym += f"{prefix_sym} {line}\n"

    st.text_area("Text with Prefix Symbol", value=text_with_prefix_sym, height=150)

    # 清除所有
    if st.button("Clear All"):
        input_text = ""
        text_with_prefix_num = ""
        text_with_prefix_sym = ""

    # 複製到剪貼板
    if st.button("Copy Text with Prefix Number"):
        st.write("Copied to clipboard!")
        st.experimental_set_query_params(text_with_prefix_num=text_with_prefix_num)

    if st.button("Copy Text with Prefix Symbol"):
        st.write("Copied to clipboard!")
        st.experimental_set_query_params(text_with_prefix_sym=text_with_prefix_sym)

if __name__ == "__main__":
    main()
