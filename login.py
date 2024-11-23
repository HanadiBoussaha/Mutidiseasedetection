# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:29:52 2024

@author: Chaima
"""
import streamlit as st
from connect import login_user 

def login():
    st.title('Login')
    name = st.text_input('Name')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if login_user(name, password):
            st.session_state.logged_in = True  # Set logged_in to True
            st.success('Login successful!')
            st.rerun()  # Refresh the app to update the UI
        else:
            st.error('Invalid credentials')
