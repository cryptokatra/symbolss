import streamlit as st

def add_prefix(text_lines, prefix):
    prefixed_lines = []
    for i, line in enumerate(text_lines):
        prefixed_line = f"{prefix}{line}"
        if i != len(text_lines) - 1:
            prefixed_line += "\n"
        prefixed_lines.append(prefixed_line)
    return "".join(prefixed_lines)

def add_numbers(text):
    lines = text.split("\n")
    numbered_lines = add_prefix(lines, f"{st.session_state['number_style']}")
    st.session_state["number_output"] = numbered_lines

def add_symbols(text):
    lines = text.split("\n")
    symbol_lines = add_prefix(lines, f"{st.session_state['symbol_style']}")
    st.session_state["symbol_output"] = symbol_lines

def reset():
    st.session_state["text_input"] = ""
    st.session_state["number_output"] = ""
    st.session_state["symbol_output"] = ""

if "text_input" not in st.session_state:
    st.session_state["text_input"] = ""
if "number_style" not in st.session_state:
    st.session_state["number_style"] = "1."
if "symbol_style" not in st.session_state:
    st.session_state["symbol_style"] = "●"
if "number_output" not in st.session_state:
    st.session_state["number_output"] = ""
if "symbol_output" not in st.session_state:
    st.session_state["symbol_output"] = ""

st.sidebar.markdown("# 左面")
text_input = st.sidebar.text_area("請輸入任何文字", value=st.session_state["text_input"], height=200)
st.session_state["text_input"] = text_input

st.sidebar.markdown("# 中間")
number_style = st.sidebar.selectbox("選擇加入什麼數字", options=["1.2.3.", "(1)(2)(3)", "[1][2][3]", "自定義"])
if number_style == "自定義":
    number_style = st.sidebar.text_input("自定義數字 style")
st.session_state["number_style"] = number_style

symbol_style = st.sidebar.selectbox("選擇加入什麼符號", options=["●", "■", "▶", "自定義"])
if symbol_style == "自定義":
    symbol_style = st.sidebar.text_input("自定義符號 style")
st.session_state["symbol_style"] = symbol_style

st.sidebar.markdown("# 右面")
st.sidebar.markdown("## 文本框 B")
number_output = st.sidebar.text_area("每一行文字的前綴加入數字", value=st.session_state["number_output"], height=200, readonly=True)

st.sidebar.markdown("## 文本框 C")
symbol_output = st.sidebar.text_area("每一行文字的前綴加入符號", value=st.session_state["symbol_output"], height=200, readonly=True)

st.sidebar.button("Copy 文本框 B 內容", to_copy=st.session_state["number_output"])
st.sidebar.button("Copy 文本框 C 內容", to_copy=st.session_state["symbol_output"])
st.sidebar.button("Reset", on_click=reset)

st.title("文本前綴加入數字或符號")
add_numbers(text_input)
add_symbols(text_input)
st.write(f"加入數字的結果：\n{st.session_state['number_output']}")
st.write(f"加入符號的結果：\n{st.session_state['symbol_output']}")
