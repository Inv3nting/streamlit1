import streamlit as st

#Writes Hello World on Webpage
#st.write('Hello World!') Day 1,2

#Creating A button

st.header('st.button')

if st.button('Say hello'):
    st.write('why hello there')
else:
    st.write('Goodbye')
    