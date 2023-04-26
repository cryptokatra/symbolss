import uuid 
import streamlit as st

# 初始化页面 
st.title("Add Prefix to Text") 
 
# 定义变量 
text_input = st.text_area("Input Text:", height=200, key=str(uuid.uuid4())) 
selected_format = st.selectbox("Select Format:", ["With dot  1.2.3.", "With () (1)(2)(3)", "With[] [1][2][3]", "●", "■", "▶", "Custom"],key=str(uuid.uuid4())) 
output_text = "" 
 
# 根据选择的格式添加前缀 
if selected_format == "With dot  1.2.3.": 
    lines = text_input.split("\n") 
    count = 1 
    for line in lines: 
        if line.strip() == "": 
            continue 
        output_text += f"{count}. {line.strip()}\n" 
        count += 1 
elif selected_format == "With () (1)(2)(3)": 
    lines = text_input.split("\n") 
    count = 1 
    for line in lines: 
        if line.strip() == "": 
            continue 
        output_text += f"({count}) {line.strip()}\n" 
        count += 1 
elif selected_format == "With[] [1][2][3]": 
    lines = text_input.split("\n") 
    count = 1 
    for line in lines: 
        if line.strip() == "": 
            continue 
        output_text += f"[{count}] {line.strip()}\n" 
        count += 1 
elif selected_format == "●": 
    symbol = "●" 
    lines = text_input.split("\n") 
    for line in lines: 
        if line.strip() == "": 
            continue 
        output_text += f"{symbol} {line.strip()}\n" 
elif selected_format == "■": 
    symbol = "■" 
    lines = text_input.split("\n") 
    for line in lines: 
        if line.strip() == "": 
            continue 
        output_text += f"{symbol} {line.strip()}\n" 
elif selected_format == "▶": 
    symbol = "▶" 
    lines = text_input.split("\n") 
    for line in lines: 
        if line.strip() == "": 
            continue 
        output_text += f"{symbol} {line.strip()}\n" 
elif selected_format == "Custom": 
    custom_prefix = st.text_input("Input Custom Prefix:", key=str(uuid.uuid4())) 
    lines = text_input.split("\n") 
    for line in lines: 
        if line.strip() == "": 
            continue 
        output_text += f"{custom_prefix} {line.strip()}\n" 
 
# 显示结果文本框 
if output_text: 
    st.text_area("Output Text:", output_text, height=200, key=str(uuid.uuid4())) 
 
# 添加Copy和Clear按钮 
col1, col2 = st.beta_columns(2) 
if col1.button("Copy"): 
    if output_text: 
        st.write("Copied!") 
        st.clipboard_copy(output_text) 
if col2.button("Clear"): 
    st.text_area("Input Text:", value="", height=200, key=str(uuid.uuid4())) 
    st.text_area("Output Text:", value="", height=200, key=str(uuid.uuid4()))
