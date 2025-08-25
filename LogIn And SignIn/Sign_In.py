import streamlit as st
import pandas as pd
def show_Sighin():
    st.title("Sign In")
    # st.write("Username")
    Username=st.text_input("Username")
    Password=st.text_input("Password")
    # df1=pd.DataFrame(columns=["Username","Password"])
    # df1.to_csv("LogIn1.csv" , mode='w+')
    # df=pd.DataFrame([[Username, Password]] ,columns=["Username","Password"])
    # df.to_csv("LogIn1.csv",mode='w')
    # st.success("Login Successful")
    if st.button("Sign In"):
        df=pd.DataFrame([[Username, Password]] ,columns=["Username","Password"])
        df.to_csv("SignIn.csv",mode='a',header=False ,index=False)
        st.success("Sign In Successful")
    # if st.button("Login"):
    #     df = pd.DataFrame([[Username, Password]], columns=["Username", "Password"])
    #     df.to_csv("LogIn1.csv", mode='a', header=False, index=False)
    #     st.success("Login Successful")
show_Sighin()