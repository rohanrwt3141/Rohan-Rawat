import streamlit as st
import pandas as pd
def show_LogIn():
    c=0
    st.title("Log In")
    username=st.text_input("Username")
    Password=st.text_input("Password",type="password")
    if(st.button("Log In")):
        data=pd.read_csv("SignIn.csv")
        df=pd.DataFrame(data)
        for i in range(5):
            if(df["Username"].loc[i]==username):
                if(df["Password"].loc[i]==Password):
                    st.success("Log In Successful")
                    c+=1
                    break
        if(c==0):
            st.write("Invalid Username and Password")  
show_LogIn()