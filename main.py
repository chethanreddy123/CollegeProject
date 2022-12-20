import streamlit as st
from pymongo.mongo_client import MongoClient
import requests
import json 
import datetime

import time


from pymongo.mongo_client import MongoClient
Data = MongoClient("mongodb+srv://chethanreddy1234:chethan1234@cluster0.yvbx0ko.mongodb.net/?retryWrites=true&w=majority")
ConnectData = Data['Test']['Test']


st.sidebar.title('Developer\'s Contact')
st.sidebar.markdown('[![Chethan-Reddy]'
                  '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                  '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

st.sidebar.success("Guided By Vijaya Priay R")

st.title("Patient Details Form")




form = st.form(key="my-form")
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11 = st.columns(11)
with c1:
    Patient_Name = form.text_input("Enter the name of patient")
with c2:
    Patient_Age = form.text_input("Enter the age: ")
with c3:
    Gender = form.selectbox("Enter the Gender" , ["Male" , "Female" , "Trans"])
with c4:
    contact_number = form.text_input("Enter the Phone Number")
with c5:
    Occupation = form.text_input("Enter the Occupation")
with c6:
    DataOfAsses = form.date_input("Enter the Data of Assessment",datetime.date.today())
with c7:
    Complaint = form.text_area("Enter the Complaint")
with c8:
    Past_History = form.text_input("Enter medical history")
with c9:
    y_cor5 = form.text_input("Enter the y - coordinate:5 ")
with c10:
    y_cor6 = form.text_input("Enter the y - coordinate:6 ")
with c11:
    y_cor7 = form.text_input("Enter the y - coordinate:7 ")

submit = form.form_submit_button("Click Here to upload the data!")


if submit == True:
    MyData = {
        "Patient_Name" :  Patient_Name,
        "Patient_Age" : Patient_Age,
        "Gender" : Gender
    }

    Check = ConnectData.insert_one(MyData)

    if Check:
        st.success("Data SuccessFully uploaded!!")

