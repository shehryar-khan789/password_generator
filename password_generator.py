import streamlit as st #importing the stramlit library for creating the web app
import random #importing th random library for generating random characters
import string #importing th string library for generating string characters
#function  to generate a password based on user preference

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation
    #generates a random password of the specified length using the characters defined above
    return ''.join(random.choice(characters) for _ in range(length) )  

st.title ("Password Generator")
length = st.slider("Select password length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include digits")
use_special = st.checkbox("Include special characters")

if st.button("Generate password"):
    password =  generate_password(length, use_digits, use_special)
    st.write(f"Generated password:`{password}`")

st.write("-----------------------------")
st.write("Build with 💖 by [Shehryar Ali](https://github.com/shehryar-khan789)")
