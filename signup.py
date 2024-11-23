# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:23:19 2024

@author: Chaima
"""
import streamlit as st
from connect import signup_user 

def signup():
    st.title('Signup')
    name = st.text_input('name')
    email = st.text_input('email')
    password= st.text_input('password', type='password')

    if st.button('Signup'):
        if name and email and password:  # Ensure all fields are filled
            signup_user(name, email, password)
            st.success('User signed up successfully!')
        else:
            st.error('Please fill in all fields.')
