import streamlit as st

# Set default values for customization options
number_style = '1'
symbol_style = '● BLACK CIRCLE'

# Define the HTML symbols
number_symbols = {'1': '1.', '2': '2.', '3': '3.', 'Custom': ''}
symbol_symbols = {'● BLACK CIRCLE': '●', '◘ INVERSE BULLET': '◘', '‣ TRIANGULAR BULLET': '‣', 'Custom': ''}

# Define the functions for adding the number or symbol
def add_number(text):
    if number_style == 'Custom':
        return text
    else:
        return number_symbols[number_style] + ' ' + text

def add_symbol(text):
    if symbol_style == 'Custom':
        return text
    else:
        return symbol_symbols[symbol_style] + ' ' + text

# Define the Streamlit app
def app():
    st.title('List Item Adder')

    # Input text box
    text = st.text_area('Input Text')

    # Number customization option
    st.subheader('Number Style')
    number_style = st.selectbox('Select a number style', list(number_symbols.keys()))
    if number_style == 'Custom':
        custom_number = st.text_input('Enter a custom number', value='')
        number_symbols[number_style] = custom_number

    # Symbol customization option
    st.subheader('Symbol Style')
    symbol_style = st.selectbox('Select a symbol style', list(symbol_symbols.keys()))
    if symbol_style == 'Custom':
        custom_symbol = st.text_input('Enter a custom symbol', value='')
        symbol_symbols[symbol_style] = custom_symbol

    # Add number and symbol to text
    add_number_button = st.button('Add Number')
    add_symbol_button = st.button('Add Symbol')

    if add_number_button:
        text = add_number(text)

    if add_symbol_button:
        text = add_symbol(text)

    # Output text box
    st.subheader('Output Text')
    st.text(text)

    # Copy to clipboard buttons
    col1, col2 = st.beta_columns(2)
    with col1:
        if st.button('Copy Numbered Text'):
            st.write('Copied!')
            st.text_to_copy(add_number(text))

    with col2:
        if st.button('Copy Symbolled Text'):
            st.write('Copied!')
            st.text_to_copy(add_symbol(text))

    # Clear all button
    if st.button('CLEAR ALL'):
        text = ''