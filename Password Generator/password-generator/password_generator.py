import streamlit as st
import random
import string

# Function to generate the password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Page configuration
st.set_page_config(page_title='Password Generator', page_icon='🔐', layout='centered')

# Custom CSS for background and styling
st.markdown(
    '''
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stButton button {
        background-color: #1f77b4;
        color: white;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Title and UI elements with icons
st.title('🔐 Password Generator')
length = st.slider('📏 Select Password Length', min_value=6, max_value=32, value=12)
use_digits = st.checkbox('🔢 Include Digits')
use_special = st.checkbox('✨ Include Special Characters')

# Generate password button
if st.button('Generate Password 💡'):
    password = generate_password(length, use_digits, use_special)
    st.success(f'Generated Password: {password}')

# Footer
st.write('--------------------------')
st.write('🛠️ Thank you for using Password Generator!')
