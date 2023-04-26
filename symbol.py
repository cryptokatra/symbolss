import streamlit as st

# Define the prefix options
number_prefix = ["With dot 1.2.3.", "With () (1)(2)(3)", "With[] [1][2][3]"]
symbol_prefix = ["●", "■", "▶"]
custom_prefix = "Custom"

# Define the prefix style options
number_style = ["Default", "Custom"]
symbol_style = ["Default", "Custom"]

# Define the Streamlit app
def app():
    st.title("Add Prefix to Text")
    
    # Create the left column for user input
    left_col, mid_col, right_col = st.beta_columns([2,1,2])
    
    with left_col:
        # Get user input text
        user_input = st.text_area("Input Text Here:")
    
    with mid_col:
        # Select the prefix type (number or symbol)
        prefix_type = st.selectbox("Select Prefix Type:", ["Number", "Symbol", "Custom"])
        
        # Select the prefix style (default or custom)
        if prefix_type == "Number":
            prefix_style = st.selectbox("Select Prefix Style:", number_style)
        elif prefix_type == "Symbol":
            prefix_style = st.selectbox("Select Prefix Style:", symbol_style)
        elif prefix_type == "Custom":
            prefix_style = custom_prefix
    
    with right_col:
        # Create a button to add the prefix to the text
        if st.button("Add Prefix"):
            # Split the input text into lines
            lines = user_input.split("\n")
            
            # Create a counter for the prefix
            prefix_count = 1
            
            # Add the prefix to each line of text
            for i in range(len(lines)):
                if prefix_type == "Number" and prefix_style == "Default":
                    lines[i] = str(prefix_count) + ". " + lines[i]
                elif prefix_type == "Number" and prefix_style == "Custom":
                    prefix = st.text_input("Enter Custom Prefix for Line " + str(i+1) + ":", value=str(prefix_count) + ". ")
                    lines[i] = prefix + lines[i]
                elif prefix_type == "Symbol" and prefix_style == "Default":
                    lines[i] = symbol_prefix[prefix_count%len(symbol_prefix)] + " " + lines[i]
                elif prefix_type == "Symbol" and prefix_style == "Custom":
                    prefix = st.selectbox("Select Custom Prefix for Line " + str(i+1) + ":", symbol_prefix)
                    lines[i] = prefix + " " + lines[i]
                elif prefix_type == "Custom":
                    prefix = st.text_input("Enter Custom Prefix for Line " + str(i+1) + ":", value=prefix_style)
                    lines[i] = prefix + lines[i]
                prefix_count += 1
            
            # Join the lines back together with newline characters
            result = "\n".join(lines)
            
            # Display the result in the output text boxes
            st.text_area("Text with Number Prefix:", result)
            st.text_area("Text with Symbol Prefix:", result)

if __name__ == "__main__":
    app()
