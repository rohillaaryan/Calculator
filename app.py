import streamlit as st #st is the streamlit library we impoerted    

st.title("My Calculator")
num1 = st.number_input("Enter first number: ") #number_input() is a Streamlit function that creates a number-entry box
operator = st.selectbox("Operation: ", options=['+','-','*','/','%']) # selectbox widget creates a drop down menu
num2 = st.number_input("Enter second number: ")

if st.button("Calculate"):  # but creates a clickable button that works on boolean logic
    st.write(num1)    #write is fxn to simply see output
    st.write("OPERATOR IS: ", operator)
    st.write(num2)