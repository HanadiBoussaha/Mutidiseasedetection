# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:32:19 2024

@author: Chaima
"""
import streamlit as st
from connect import login_user 

from login import login
from signup import signup  
# Main page navigation
def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        st.write('Welcome to the Health Assistant app!')
    else:
        option = st.sidebar.selectbox('login/signup', ('login', 'signup'))

        if option == 'login':
            login()
        else:
            signup()

if __name__ == "__main__":
    main()
