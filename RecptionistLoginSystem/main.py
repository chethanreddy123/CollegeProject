import streamlit as st
import streamlit_authenticator as stauth
from pathlib import Path
import pickle
import datetime
from pymongo.mongo_client import MongoClient
import random as rd
from datetime import datetime

Data = MongoClient("mongodb://chethanreddy1234:chethan1234@ac-s9dsrxv-shard-00-00.yvbx0ko.mongodb.net:27017,ac-s9dsrxv-shard-00-01.yvbx0ko.mongodb.net:27017,ac-s9dsrxv-shard-00-02.yvbx0ko.mongodb.net:27017/?ssl=true&replicaSet=atlas-1ohy5i-shard-0&authSource=admin&retryWrites=true&w=majority")
ConnectData = Data['Test']['Test']


names = ["Chethan" , "Harry"]
usernames = ["chethan123", "harry123"]

st.title("Receptionist Dash-Board")

file_path = Path(__file__).parent / "hashed_pw.pkl"

with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

credentials = {
    "usernames":{
        usernames[0]:{
            "name":names[0],
            "password":hashed_passwords[0]
            },
        usernames[1]:{
            "name":names[1],
            "password":hashed_passwords[1]
            }            
        }
}

authenticator = stauth.Authenticate(credentials, 
                "my-DashBoard" , "abcdef", cookie_expiry_days=30)

name, authentication_status, usernames = authenticator.login("Login" , "main")

if authentication_status == True:
    authenticator.logout("Logout" , "sidebar")

    # Using object notation
    add_selectbox = st.sidebar.selectbox(
        "What would you like to do?",
        ("New Patient Registration", "Old-Patient Details")
    )

    st.sidebar.title('Developer\'s Contact')
    st.sidebar.markdown('[![Chethan-Reddy]'
                    '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                    '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

    st.sidebar.success("TIFAC - Maintained")

    if add_selectbox == "New Patient Registration":
        st.title("Patient Details Form")
        form = st.form(key="my-form" , clear_on_submit=True)
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
            Address = form.text_input("Enter the address")
        with c7:
            DateOfAsses = form.date_input("Enter the Data of Assessment",datetime.now())
        with c8:
            Complaint = form.text_area("Enter the Complaint")
        with c9:
            Past_History = form.text_input("Enter medical history")
        with c10:
            Surgical_History = form.text_input("Enter surgical history")
        with c11:
            Referal_Doctor = form.text_input("Enter the referal doctor")

        submit = form.form_submit_button("Click Here to upload the data!")

        if submit == True:
            Id_No = rd.randint(1,1000)
            Patient_Id = "ST" + str(Id_No)
            
            MyData = {
                "Patient_Id" : str(Patient_Id),
                "Patient_Name" :  str(Patient_Name),
                "Patient_Age" : str(Patient_Age),
                "Gender" : str(Gender),
                "contact_number": str(contact_number),
                "Occupation" : str(Occupation),
                "Address" : str(Address),
                "DateOfAsses" : str(DateOfAsses),
                "Complaint" : str(Complaint),
                "Past_History" : str(Past_History),
                "Surgical_History" : str(Surgical_History),
                "Referal_Doctor" : str(Referal_Doctor),
                "Patient_Documents" : [],
                "Senior_Doctors_Prescription" : [],
                "Junior_Doctors_Prescription": [],
                "Trainer_Prescription" : [],
                "Trainer_Suggestions" : [],
                "Tracker" : [(datetime.now() , "Filled the Form by %s"%name)]
            }


            with st.spinner('Wait for it...'):
                Check = ConnectData.insert_one(MyData)
                st.success("Data SuccessFully uploaded!")
                st.success(f"Patient_ID : {Patient_Id}")

    elif add_selectbox == "Old-Patient Details":
        form = st.form(key="my-form")
        c1, c2 = st.columns(2)
        with c1:
            sel1 = form.selectbox("Search By", ("ID", "Phone No"))
        with c2:
            track = form.text_input("Enter the ID/Phone").upper()
        submit = form.form_submit_button("Get the Details")
        if submit:
            if sel1 == "ID":
                Results = ConnectData.find({"Patient_Id" : track})
            else:
                Results = ConnectData.find({"contact_number" : track})

            for i in Results:
                st.json(i)
else:
    st.warning("Username/password Incorrect!")
   
