import streamlit as st
import pickle
from typing import List

def add_prefix(text: str, prefix: str) -> str:
    return prefix + text

def add_number_prefix(text: str, start: int, step: int, with_dot: bool = True) -> str:
    if with_dot:
        prefix = f'{start}.'
    else:
        prefix = f'({start})'
    return add_prefix(text, prefix)

def add_symbol_prefix(text: str, symbol: str) -> str:
    return add_prefix(text, symbol)

def add_custom_prefix(text: str, prefix: str) -> str:
    return add_prefix(text, prefix)

def add_prefix_to_lines(lines: List[str], prefix_func, *args, **kwargs) -> List[str]:
    result = []
    count = 0
    for line in lines:
        count += 1
        prefix = prefix_func(line, count, *args, **kwargs)
        result.append(add_prefix(line, prefix))
    return result

def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_from_pickle(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

def main():
    st.title('Add prefix to text lines')

    # Create input widgets
    input_text = st.text_area('Input text', height=200)
    with_number_dropdown = st.selectbox('With number', ['With dot', 'With ()', 'With []'])
    symbol_dropdown = st.selectbox('Symbol', ['●', '■', '▶'])
    custom_input = st.text_input('Custom prefix')
    
    # Create output widgets
    number_output = st.empty()
    symbol_output = st.empty()

    # Create buttons
    copy_number_button = st.button('Copy number output')
    copy_symbol_button = st.button('Copy symbol output')
    reset_button = st.button('Reset')

    # Process input text
    if input_text:
        lines = input_text.split('\n')
        if with_number_dropdown == 'With dot':
            prefix_func = add_number_prefix
            prefix_args = (1, 1, True)
        elif with_number_dropdown == 'With ()':
            prefix_func = add_number_prefix
            prefix_args = (1, 1, False)
        elif with_number_dropdown == 'With []':
            prefix_func = add_number_prefix
            prefix_args = (1, 1, False)
        if custom_input:
            prefix_func = add_custom_prefix
            prefix_args = (custom_input,)
        symbol = symbol_dropdown or ' '
        number_lines = add_prefix_to_lines(lines, prefix_func, *prefix_args)
        symbol_lines = add_prefix_to_lines(lines, add_symbol_prefix, symbol)
        number_output.text('\n'.join(number_lines))
        symbol_output.text('\n'.join(symbol_lines))

    # Handle button clicks
    if copy_number_button:
        st.experimental_set_query_params(output=number_output.text())
    if copy_symbol_button:
        st.experimental_set_query_params(output=symbol_output.text())
    if reset_button:
        st.experimental_set_query_params(output='')

if __name__ == '__main__':
    main()
