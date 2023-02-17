import streamlit as st
import streamlit_authenticator as stauth
from pathlib import Path
import pickle
import datetime
from pymongo.mongo_client import MongoClient
import random as rd
import pandas as pd
import os


Data = MongoClient("mongodb://chethanreddy1234:chethan1234@ac-s9dsrxv-shard-00-00.yvbx0ko.mongodb.net:27017,ac-s9dsrxv-shard-00-01.yvbx0ko.mongodb.net:27017,ac-s9dsrxv-shard-00-02.yvbx0ko.mongodb.net:27017/?ssl=true&replicaSet=atlas-1ohy5i-shard-0&authSource=admin&retryWrites=true&w=majority")
ConnectData = Data['Test']['Test']


names = ["parker" , "henry"]
usernames = ["parker123" , "henry123"]

st.title("Junior Doctor Dash-Board👨‍⚕️")

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
        ("Patient Prescription", "Past Prescription" , "Emergency Review", "Suggestion" , "Track Exercise")
    )

    st.sidebar.title('Developer\'s Contact')
    st.sidebar.markdown('[![Chethan-Reddy]'
                    '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                    '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

    st.sidebar.success("TIFAC - Maintained")



    if add_selectbox == "Past Prescription":

        st.subheader("Search for the Patient")

        form = st.form(key="my-form")
        c1, c2= st.columns(2)
        with c1:
            Id_Patient = form.selectbox("Search By", ("ID", "Phone No"))
        with c2:
            track = str(form.text_input("Enter The Patient ID"))

        submit = form.form_submit_button("Get the Details")


        if submit == True:
        
            Results = ConnectData.find({"Patient_Id" : track})
            for i in Results:
                st.json(i)

    elif add_selectbox == "Patient Prescription":
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
            
        Click = st.button("Click Here to Add Prescription")

        if Click == True:
            st.title("Patient Details Form")
            form = st.form(key="your-form")
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
                DateOfAsses = form.date_input("Enter the Data of Assessment",datetime.date.today())
            with c8:
                Complaint = form.text_area("Enter the Complaint")
            with c9:
                Past_History = form.text_input("Enter medical history")
            with c10:
                Surgical_History = form.text_input("Enter surgical history")
            with c11:
                Referal_Doctor = form.text_input("Enter the referal doctor")

            submit = form.form_submit_button("Click Here to upload the data!")
    elif add_selectbox == "Track Exercise":
        st.title("Exerice and Training Tracker")
        patient = st.text_input("Enter the Patient_ID")

        if patient == "":
            st.caption("Details Not Found, put the patient_Id")
        else:

            Results = ConnectData.find_one({"Patient_Id" : patient})
            SearchData = dict(Results)

            if SearchData == dict():
                st.caption("Details Not Found, put the patient_Id")

            else:
                with st.expander("View Updated Data 💫"	, expanded=True):
                    Day_Wise = list(SearchData["Junior_Doctors_Prescription"])
                    print(Day_Wise)
                    clean_df = pd.DataFrame(Day_Wise,columns=["Date","Discription","Pain Scale"])
                    st.dataframe(clean_df)


            st.subheader("Add the Exerise")
            col1,col2 = st.columns(2)

            with col1:
                Disc = st.text_area("Enter the Description of the Exericse")

            with col2:
                pain_scale = st.selectbox("Enter the Pain Scale out of 10",[i for i in range(1,11)])
                date = st.date_input("Enter the date")

            if st.button("Click Here👨‍💻"):
                myquery = { "Patient_Id" : patient }
                Day_Wise.append([str(date),Disc,pain_scale])
                newvalues = { "$set": { "Junior_Doctors_Prescription":Day_Wise } }

                ConnectData.update_one(myquery, newvalues)
                st.success("Exercise Added ✅")
                    
            with st.expander("Current Data"):
                print(Day_Wise)
                clean_df = pd.DataFrame(Day_Wise,columns=["Date","Discription","Pain Scale"])
                st.dataframe(clean_df)
                st.bar_chart(clean_df, x="Date" , y="Pain Scale")

    elif add_selectbox == "Suggestions":
        form = st.form(key="my-form" , clear_on_submit=True)
        c1, c2 = st.columns(2)
        with c1:
            p_i = form.text_input("Enter the patient id")
        with c2:
            suggestion = form.text_input("Enter the Suggestion for this patient")
        submit = form.form_submit_button("Suggest!!")

        if submit == True:
            ConnectData = Data['Test']['PopUps']
            status = ConnectData.insert_one({"Patient_Id" : p_i , "Suggestion" : suggestion , "Check" : False})
            if status:
                st.success("Suggestion sent successfully to the Senior Doctor")
            st.success("Suggestion sent successfully to the Senior Doctor")
    elif add_selectbox == "Emergency Review":
        st.subheader("Emergency Review")
        form = st.form(key="my-form" , clear_on_submit=True)
        c1, c2 = st.columns(2)
        with c1:
            p_i = form.text_input("Enter the patient id")
        with c2:
            suggestion = form.text_input("Enter the information for emergency Review")
        submit = form.form_submit_button("Raise an Emergency Review")

        if submit == True:
            ConnectData = Data['Test']['PopUps']
            status = ConnectData.insert_one({"Patient_Id" : p_i , "Suggestion" : suggestion , "Check" : False})
            if status:
                st.success("Suggestion sent successfully to the Senior Doctor")
            st.success("Suggestion sent successfully to the Senior Doctor")

elif authentication_status == False:
    st.warning("password wrong")
   

# added 
# added 2