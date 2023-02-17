import streamlit as st
import streamlit_authenticator as stauth
import matplotlib.pyplot as plt
from itertools import cycle
from pathlib import Path
import pickle
import datetime
from pymongo.mongo_client import MongoClient
import random as rd
from bson.binary import Binary
from PIL import Image
from streamlit_custom_notification_box import custom_notification_box
import io
import plotly.express as px
import numpy as np

Data = MongoClient("mongodb://chethanreddy1234:chethan1234@ac-s9dsrxv-shard-00-00.yvbx0ko.mongodb.net:27017,ac-s9dsrxv-shard-00-01.yvbx0ko.mongodb.net:27017,ac-s9dsrxv-shard-00-02.yvbx0ko.mongodb.net:27017/?ssl=true&replicaSet=atlas-1ohy5i-shard-0&authSource=admin&retryWrites=true&w=majority")
ConnectData = Data['Test']['Test']


names = ["parker" , "henry"]
usernames = ["parker123" , "henry123"]

st.title("Senior Doctor Dash-Board👨‍⚕️")

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
        ("Suggestions from Re-hab Trainer","Patient Prescription", "Past Prescription","X-Ray Analysis")
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
        
        st.title("Add your prescription here doctor!")
        form = st.form(key="your-form" , clear_on_submit=False)
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = st.columns(10)
        with c1:
            Id_Patient = form.text_input("Enter the Patient ID")
        with c2:
            S_Diagosis = form.text_input("Enter the Diagosis")
        with c3:
            Treatment = form.text_input("Enter the treatment prescription")
        with c4:
            Exercise = form.text_input("Enter the exercise recommendation")
        with c5:
            review = form.text_input("Enter the review")
        with c6:
            Home_Advice = form.text_input("Enter the home advice")
        with c7:
            Up_Treatment = form.text_input("Enter the follow up treatment")
        with c8:
            MRI_Impression = form.text_input("Enter the MRI_Impression")
        with c9:
            X_Ray = form.file_uploader("Choose a X-Ray file")
        with c10:
            X_Ray_Tags = form.text_input("Enter the X_Ray tags")


        submit = form.form_submit_button("Click Here to upload the data!")

        if submit == True:
            myData = {
                "S_Diagosis" : S_Diagosis,
                "Treatment" : Treatment,
                "Exercise" : Exercise,
                "review" : review,
                "Home_Advice" : Home_Advice,
                "Up_Treatment" : Up_Treatment,
                "MRI_Impression" : MRI_Impression
            }
            with st.spinner('Wait for it...'):

                ConnectData.update_one(
                        {"Patient_Id": Id_Patient},
                        {
                                "$set":{
                                        "Senior_Doctors_Prescription": myData
                                        }
                        }
                )

                images = Data['Images']['Images']

                im = Image.open(X_Ray)

                image_bytes = io.BytesIO()
                im.save(image_bytes, format='JPEG')


                XRayData = {
                    "Patient_Id" : str(Id_Patient),
                    "X_Ray" : image_bytes.getvalue(),
                    "X_Ray_Tags" : X_Ray_Tags 
                }

                image_id = images.insert_one(XRayData).inserted_id

                st.success("Data successfully uploaded to the cloud")

    elif add_selectbox == "X-Ray Analysis":
        st.title("X-Ray Analysis")

        Id_Patient = st.text_input("Enter the Patient ID")
        
        Check = st.button("Click here to get the X-ray")

        if Check == True:
            images = Data['Images']['Images']
            Results = images.find({"Patient_Id" : Id_Patient})

            Results = list(Results)

            pil_img = Image.open(io.BytesIO(Results[0]['X_Ray']))
            Caption=Results[0]["X_Ray_Tags"]
            fig = px.imshow(pil_img)
            st.plotly_chart(fig, )
            st.caption(Caption,)

    elif add_selectbox == "Suggestions from Re-hab Trainer":
        MyData = Data['Test']['PopUps']
        DataSearch1  = MyData.find({"Check" :  False})
        DataSearch2  = MyData.find({"Check" :  False})


        st.subheader("Important Notifications from Re-Hab Trainer")

        styles = {'material-icons':{'color': 'red'},
                'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'},
                'notification-text': {'':''},
                'close-button':{'':''},
                'link':{'':''}}

        Lenght = len(list(DataSearch1))
        stat = [0 for i in range(Lenght)]

        for i in DataSearch2:
            print(i)

            status = custom_notification_box(icon='info', 
                textDisplay=i["Suggestion"], 
                externalLink=i["Patient_Id"], url='none', styles=styles, key=i["Patient_Id"])
            print(status)

        

            if status != 0:
                x = ConnectData.update_many(
                {"Patient_Id":i['Patient_Id']},
                {
                        "$set":{
                                "Check":True
                                },
                        "$currentDate":{"lastModified":True}
                        
                        }
                )
                
        


        
  



elif authentication_status == False:
    st.warning("password wrong")
   
