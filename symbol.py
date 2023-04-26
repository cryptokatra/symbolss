import streamlit as st 
 
# 初始化页面 
st.title("Add Prefix to Text") 
 
# 定义变量 
text_input = st.text_area("Input Text:",height=200) 
selected_format = st.selectbox("Select Format:", ["With dot  1.2.3.", "With () (1)(2)(3)", "With[] [1][2][3]", "●", "■", "▶", "Custom"]) 
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
    custom_prefix = st.text_input("Input Custom Prefix:") 
    lines = text_input.split("\n") 
    for line in lines: 
        if line.strip() == "": 
            continue 
        output_text += f"{custom_prefix} {line.strip()}\n" 
 
# 显示结果文本框 
output_text = output_text.strip() 
if output_text: 
     st.markdown(f"**Output Text:**", unsafe_allow_html=True) 
    
 
# 显示复制按钮 
if st.button("Copy Text"): 
    st.write("Text Copied to Clipboard!") 
    st.text(output_text)  # 显示结果 
 
# 显示清空按钮 
if st.button("Clear All Content"): 
    text_input = "" 
    selected_format = "" 
    output_text = "" 
    st.text_area("Input Text:", value=text_input, height=300, key="input_text") 
    st.text_area("Output Text:", value=output_text, height=300, key="output_text")
