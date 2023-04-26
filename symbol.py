import streamlit as st 
 
# 初始化页面 
st.set_page_config(layout="wide") 
st.title("Add Prefix to Text") 
 
# 定义变量 
text_input = st.text_area("Input Text:", height=200) 
selected_format = st.selectbox("Select Format:", ["With dot 1.2.3.", "With () (1)(2)(3)", "With[] [1][2][3]", "●", "■", "▶", "Custom"]) 
 
# 根据选择的格式添加前缀 
output_text = "" 
if selected_format == "With dot 1.2.3.": 
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
         
elif selected_format in ["●", "■", "▶"]: 
    symbol = selected_format 
    lines = text_input.split("\n") 
    for line in lines: 
        if line.strip() == "": 
            continue 
        output_text += f"{symbol} {line.strip()}\n" 
         
elif selected_format == "Custom": 
    custom_prefix = st.text_input("Input Custom Prefix:") 
    lines = text_input.split("\n") 
    for line in lines: 
        if line.strip() == "": 
            continue 
        output_text += f"{custom_prefix} {line.strip()}\n" 
 
# 显示结果文本框 
col1, col2, col3 = st.columns(3) 
with col1: 
    st.text_area("Input Text:", text_input, height=200, key="my_unique_key") 
with col2: 
    st.write("") 
    st.selectbox("Select Format:", ["With dot 1.2.3.", "With () (1)(2)(3)", "With[] [1][2][3]", "●", "■", "▶", "Custom"]) 
with col3: 
    st.text_area("Output Text:", output_text, height=200, key="my_unique_key") 
 
# 显示复制按钮 
st.button("Copy Text")
