import streamlit as st
import streamlit_authenticator as stauth
from pathlib import Path
import pickle
import datetime
from pymongo.mongo_client import MongoClient
import random as rd
import datetime
import numpy
from dateutil import parser


Data = MongoClient("mongodb://localhost:27017/")


ConnectData = Data['Test']['Test']


names = ["Chethan" , "Harry"]
usernames = ["chethan123", "harry123"]

st.title("Receptionist Dash-Board 💁")

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
        ("New Patient Registration", "Old-Patient Veiw \ Update" , "Old Patient Re-Visit Again" , "Payment Details" , "Feedback")
    )

    st.sidebar.title('Developer\'s Contact')
    st.sidebar.markdown('[![Chethan-Reddy]'
                    '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                    '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

    st.sidebar.success("TIFAC - Maintained")

    if add_selectbox == "New Patient Registration":
        st.title("Initial Evaluation Form for the New Patient 📝")
        form = st.form(key="my-form" , clear_on_submit=True)
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36 = st.columns(36)
        with c12:
            form.subheader('Patient Information')
        with c1:
            Patient_Name = form.text_input("Enter the name of patient *")
        with c2:
            Patient_Age = form.text_input("Enter the age *")
        with c14:
            Patient_Height = form.text_input("Enter the Height(cm)")
        with c15:
            Patient_Weight = form.text_input("Enter the Weight(kg)")
        with c3:
            GenderOptions = ("Male" , "Female" , "Trans")
            Gender = form.selectbox("Enter the Gender *" , GenderOptions)
        with c4:
            contact_number = form.text_input("Enter the Phone Number *")
        with c13:
            EmployedOptions = ("Yes" , "No")
            Employed =  form.radio(
                            "Currently Employed?",
                            EmployedOptions)
        with c5:
            Occupation = form.text_input("Enter the Occupation")
        with c6:
            Address = form.text_input("Enter the address")
        with c7:
            DateOfAsses = form.date_input("Enter the Data of Assessment *",(datetime.datetime.today().replace(microsecond=0)))
        with c16:
            form.subheader("Basic Assesment")
        with c8:
            Complaint = form.text_area("Chief Complaint *")
        with c17:
            Injury = form.text_input("Enter if any injury")
        with c18:
            DateOfInjury = form.date_input("Enter the Data of injury",(datetime.datetime.today().replace(microsecond=0)))
        with c9:
            DateOfInjuryforSurgery = form.date_input("Enter the date of surgery", (datetime.datetime.today().replace(microsecond=0)))
        with c19:
            DecriptionOfSurgery = form.text_area("Briefly Describe how you were injured")
        with c20:
            RecievedTherapyOptions = ["Yes" , "No"]
            RecievedTherapy = form.selectbox("Have recieved the therapy for this condition" , RecievedTherapyOptions)
        with c36:
            WhatTherapy = form.text_input("Enter if therapy taken") # backend 
        with c21:
            DateofTherapy = form.date_input("Enter the data of therapy taken", (datetime.datetime.today().replace(microsecond=0)))
        with c22:
            CurrentConditionOptions = ["Worse" , "Same" , "Better"]
            CurrentCondition = form.radio("The present condition is getting" , CurrentConditionOptions)
        with c23:
            currentStatusSymptomsOptions = ["Constant" , "Intermittent" ]
            currentStatusSymptoms = form.radio("Are the symptoms" , currentStatusSymptomsOptions)
        with c24:
            form.caption("Mark the number that best corresponds to the pain *")
        with c26:
            AtWorstPain = form.slider("Enter At Worst" , 1, 10, 1)
        with c10:
            Surgical_History = form.text_input("Enter surgical history")
        with c11:
            Referal_Doctor = form.text_input("Enter the referal doctor")
        with c27:
            MakesConditionBetter = form.multiselect("What decreases/makes the condition better", ["Bending" , "Sitting"
                                                                        , "Rising", "Changing Positions" , "Movement" ,  "Rest"
                                                                        "Standing" , "Walking" , "Lying" , "Heat" , "Ice",
                                                                        "Medication" , "Better In Am" , "Better as Day Progresses" 
                                                                        ,"Better in PM", "N/A Cast Just Remove"])
        with c28:
            MakesConditionBetterWorse = form.multiselect("What increases/makes the condtition worse" , ["Bending" , 'Sitting' , "Rising"
                                                        "Prolonged Positioning", "Worse as day progresses" , "Movement" , "Standing",
                                                        "Walking" , "Lying" , "N/A Cast Just Removed",
                                                        "Rest" , "Stairs" , "Cough" , "Worse In AM" , "Sneeze" , "Deep Breath"
                                                        , "Medication", "Worse in PM" ])
        with c29:
            MedicalIntervention = form.multiselect("Previous Medical Investigation" , ["X-Ray" , "Catscan" , "Injections" , "MRI", "Others"])
        with c30:
            GoalsAfterTreat = form.text_input("What are the Goals to be Achieved by End of the therapy")
        with c31:
            MedicalInformation = form.multiselect("Medical Information" , ["Difficulty Swallowing", "Arthritis"
                    , "High Blood Pressure" , "Heart Trouble" , "Pacemaker" , "Epilepsy/Seizures" , "History of Drug Abuse"
                    , "Myofascial Pain" , "Cancer" , "Motion Sickness" , "Fever/Chills/Sweats" , "Unexplainable Weight Loss"
                    , "Blood Clots" , "Shortness of Breath" ,  "History of Smoking" , "Diabetes" , "Fibromyalgia"
                    , "Stroke" , "Osteoporous" , "Anemia" , "Bleeding Problem" , "HIV/Hepatitis" , "History of Alcohol Abuse",
                    "Depression/Anxiety" , "Pregnancy"])
        with c32:
            PrevSurger = form.text_input("Enter if any Previous Surgeries")
        with c33:
            OtherInfo = form.text_input("Enter if any other information")
        with c34:
            Medications = form.text_input("Enter if any medications are taken")
        with c35:
            Allergies = form.text_input("Enter if any Allergies")
         
        submit = form.form_submit_button("Click Here to upload the data!")



        ########################    Form #####################

        if submit == True:
            Patient_Id = "23ST" + str(rd.randint(1,1001))
            CurrentData = {
                "Patient_Id" : Patient_Id,
                "Patient_Name" : Patient_Name,
                "Patient_Age" : Patient_Age,
                "Patient_Gender" : GenderOptions.index(Gender),
                "Patient_Height" : Patient_Height,
                "Patient_Weight" : Patient_Weight,
                "Patient_Contact_No" : contact_number,
                "Employed" : EmployedOptions.index(Employed),
                "Occupation" : Occupation,
                "Address" : Address,
                "DateOfAsses" : [DateOfAsses.isoformat( )],
                "Complaint" : [Complaint],
                "Injury" : [Injury],
                "DateOfInjury" : [DateOfInjury.isoformat( ) ],
                "DateOfInjuryforSurgery" : [DateOfInjuryforSurgery.isoformat( )],
                "DecriptionOfSurgery" : [DecriptionOfSurgery],
                "RecievedTherapy" : [RecievedTherapyOptions.index(RecievedTherapy)],
                "DateofTherapy" : [DateofTherapy.isoformat( )],
                "CurrentCondition" : [CurrentConditionOptions.index(CurrentCondition)],
                "currentStatusSymptoms" : [currentStatusSymptomsOptions.index(currentStatusSymptoms)],
            
                "AtWorstPain" : [AtWorstPain],
                "Surgical_History" : [Surgical_History],
                "Referal_Doctor" : [Referal_Doctor],
                "MakesConditionBetter" : [MakesConditionBetter],
                "MakesConditionBetterWorse" : [MakesConditionBetterWorse],
                "MedicalIntervention" : [MedicalIntervention],
                "GoalsAfterTreat" : [GoalsAfterTreat],
                "MedicalInformation" : [MedicalInformation],
                "PrevSurger" : [PrevSurger],
                "OtherInfo" : [OtherInfo],
                "Medications" : [Medications],
                "Allergies" : [Allergies],
                "Feedback" : None
            }

            with st.spinner('Wait for it...'):
                Check = ConnectData.insert_one(CurrentData)
                st.success("Data SuccessFully uploaded!")
                st.success(f"Patient_ID : {Patient_Id}")

    elif add_selectbox == "Old-Patient Veiw \ Update":
        if "button_clicked" not in st.session_state:
            st.session_state.button_clicked = False
        def callback():
            st.session_state.button_clicked = True
        form = st.form(key="my-form")
        c1, c2 = st.columns(2)
        with c1:
            sel1 = form.selectbox("Search By", ("ID", "Phone No"))
        with c2:
            track = form.text_input("Enter the ID/Phone").upper()
        submit = form.form_submit_button("Get the Details" , on_click = callback)
        if submit or st.session_state.button_clicked:
            if sel1 == "ID":
                Results = ConnectData.find_one({"Patient_Id" : track})
            else:
                Results = ConnectData.find_one({"contact_number" : track})
            
            if Results != None:
                myData = Results  
                AllDate = tuple(myData['DateOfAsses'])
                DisplayDate = st.selectbox("Select Date of Visit",AllDate)
                mainDate = AllDate.index(DisplayDate)

                if DisplayDate:
                    st.subheader("Patient View 🔍 Or Update ⌨️")
                    TypeOption = st.select_slider("Select to View or Edict" , ["View" , "Edit"])
                    Optiontype = True
                    if TypeOption == "Edit":
                        Optiontype = False
                    else:
                        Optiontype = True
                    print(TypeOption) 
                    
                    form = st.form(key="Edit-form" , clear_on_submit=True)
                    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35 = st.columns(35)
                    with c12:
                        form.subheader('Patient Information')
                    with c1:
                        Patient_Name = form.text_input("Enter the name of patient *",myData["Patient_Name"],disabled = Optiontype)
                    with c2:
                        Patient_Age = form.text_input("Enter the age *", myData["Patient_Age"] , disabled = Optiontype)
                    with c14:
                        Patient_Height = form.text_input("Enter the Height(cm)", myData["Patient_Height"], disabled = Optiontype)
                    with c15:
                        Patient_Weight = form.text_input("Enter the Weight(kg)", myData["Patient_Height"], disabled = Optiontype)
                    with c3:
                        GenderOptions = ["Male" , "Female" , "Trans"]
                        Gender = form.selectbox("Enter the Gender *" , GenderOptions, index = (myData['Patient_Gender']), disabled = Optiontype)
                    with c4:
                        contact_number = form.text_input("Enter the Phone Number *", myData["Patient_Contact_No"], disabled = Optiontype)
                    with c13:
                        EmployedOptions = ("Yes" , "No")
                        Employed =  form.radio(
                                        "Currently Employed?",
                                        EmployedOptions , index = int(myData['Employed']), disabled = Optiontype)
                    with c5:
                        Occupation = form.text_input("Enter the Occupation", myData["Occupation"], disabled = Optiontype)
                    with c6:
                        Address = form.text_input("Enter the address", myData["Address"], disabled = Optiontype)
                    with c7:
                        DateOfAsses = form.date_input("Enter the Data of Assessment *" , parser.parse(myData['DateOfAsses'][mainDate]) ,disabled = Optiontype)
                    with c16:
                        form.subheader("Basic Assesment")
                    with c8:
                        Complaint = form.text_area("Chief Complaint *" , myData["Complaint"][mainDate] , disabled = Optiontype)
                    with c17:
                        Injury = form.text_input("Enter if any injury" , myData["Injury"][mainDate] , disabled = Optiontype)
                    with c18:
                        DateOfInjury = form.date_input("Enter the Data of injury", parser.parse(myData['DateOfInjury'][mainDate]), disabled = Optiontype)
                    with c9:
                        DateOfInjuryforSurgery = form.date_input("Enter the date of surgery", parser.parse(myData['DateOfInjuryforSurgery'][mainDate]), disabled = Optiontype )
                    with c19:
                        DecriptionOfSurgery = form.text_area("Briefly Describe how you were injured" , disabled = Optiontype)
                    with c20:
                        RecievedTherapyOptions =  ["Yes" , "No"] 
                        RecievedTherapy = form.selectbox("Have recieved the therapy for this condition" ,RecievedTherapyOptions, index = myData['RecievedTherapy'][mainDate] ,  disabled = Optiontype)
                    with c21:
                        DateofTherapy = form.date_input("Enter the data of therapy taken", parser.parse(myData['DateofTherapy'][mainDate]) , disabled = Optiontype)
                    with c22:
                        CurrentConditionOptions = ["Worse" , "Same" , "Better"] 
                        CurrentCondition = form.radio("The condition is getting" , CurrentConditionOptions, index =  int(myData['CurrentCondition'][mainDate]), disabled = Optiontype)
                    with c23:
                        currentStatusSymptomsOptions = ["Constant" , "Intermittent" ] 
                        currentStatusSymptoms = form.radio("Are the symptoms" , currentStatusSymptomsOptions, index = myData['currentStatusSymptoms'][mainDate], disabled = Optiontype)
                    with c24:
                        form.caption("Mark the number that best corresponds to the pain *")
                    with c26:
                        AtWorstPain = form.slider("Enter At Worst" , min_value = 0, max_value = 10,step = 1, value = myData["AtWorstPain"][mainDate], disabled = Optiontype)
                    with c10:
                        Surgical_History = form.text_input("Enter surgical history", myData["Surgical_History"][mainDate] , disabled = Optiontype)
                    with c11:
                        Referal_Doctor = form.text_input("Enter the referal doctor", myData["Referal_Doctor"][mainDate] , disabled = Optiontype)
                    with c27:
                        MakesConditionBetter = form.multiselect("What decreases/makes the condition better", ["Bending" , "Sitting"
                                                                                    , "Rising", "Changing Positions" , "Movement" ,  "Rest"
                                                                                    "Standing" , "Walking" , "Lying" , "Heat" , "Ice",
                                                                                    "Medication" , "Better In Am" , "Better as Day Progresses" 
                                                                                    ,"Better in PM", "N/A Cast Just Remove"], myData["MakesConditionBetter"][mainDate] , disabled = Optiontype)
                    with c28:
                        MakesConditionBetterWorse = form.multiselect("What increases/makes the condtition worse" , ["Bending" , 'Sitting' , "Rising"
                                                                    "Prolonged Positioning", "Worse as day progresses" , "Movement" , "Standing",
                                                                    "Walking" , "Lying" , "N/A Cast Just Removed",
                                                                    "Rest" , "Stairs" , "Cough" , "Worse In AM" , "Sneeze" , "Deep Breath"
                                                                    , "Medication", "Worse in PM"] , myData["MakesConditionBetterWorse"][mainDate], disabled = Optiontype)
                        
                    with c29:
                        MedicalIntervention = form.multiselect("Previous Medical Interventions" , ["X-Ray MRI" , "Catscan" , "Injections" , "Others"], myData["MedicalIntervention"][mainDate] , disabled = Optiontype)
                    with c30:
                        GoalsAfterTreat = form.text_input("What are the Goals to be Achieved by End of the therapy", myData["GoalsAfterTreat"][mainDate] , disabled = Optiontype)
                    with c31:
                        MedicalInformation = form.multiselect("Medical Information" , ["Difficulty Swallowing", "Arthritis"
                                , "High Blood Pressure" , "Heart Trouble" , "Pacemaker" , "Epilepsy/Seizures" , "History of Drug Abuse"
                                , "Myofascial Pain" , "Cancer" , "Motion Sickness" , "Fever/Chills/Sweats" , "Unexplainable Weight Loss"
                                , "Blood Clots" , "Shortness of Breath" ,  "History of Smoking" , "Diabetes" , "Fibromyalgia"
                                , "Stroke" , "Osteoporous" , "Anemia" , "Bleeding Problem" , "HIV/Hepatitis" , "History of Alcohol Abuse",
                                "Depression/Anxiety" , "Pregnancy"], myData["MedicalInformation"][mainDate] , disabled = Optiontype)
                    with c32:
                        PrevSurger = form.text_input("Enter if any Previous Surgeries", myData["PrevSurger"][mainDate] , disabled = Optiontype)
                    with c33:
                        OtherInfo = form.text_input("Enter if any other information", myData["OtherInfo"][mainDate], disabled = Optiontype)
                    with c34:
                        Medications = form.text_input("Enter if any medications are taken", myData["Medications"][mainDate],disabled = Optiontype)
                    with c35:
                        Allergies = form.text_input("Enter if any Allergies", myData["Allergies"][mainDate] , disabled = Optiontype)
                    
                    submit = form.form_submit_button("Click Here to update the Data!" , disabled = Optiontype)

                    if submit == True:
                        NewMydata = myData.copy()
                        NewMydata['Patient_Name'] = Patient_Name
                        NewMydata['Patient_Age'] = Patient_Age
                        NewMydata['Patient_Gender'] = GenderOptions.index(Gender)
                        NewMydata['Patient_Contact_No'] = contact_number
                        NewMydata['Employed'] = EmployedOptions.index(Employed)
                        NewMydata['Occupation'] = Occupation
                        NewMydata['Address'] = Address
                        NewMydata['DateOfAsses'][mainDate] = DateOfAsses.isoformat( )
                        NewMydata['Complaint'][mainDate] = Complaint
                        NewMydata['Injury'][mainDate] = Injury
                        NewMydata['DateOfInjury'][mainDate] = DateOfInjury.isoformat( )
                        NewMydata['DateOfInjuryforSurgery'][mainDate] = DateOfInjuryforSurgery.isoformat( )

                        NewMydata['DecriptionOfSurgery'][mainDate] = DecriptionOfSurgery,
                        NewMydata['RecievedTherapy'][mainDate] = RecievedTherapyOptions.index(RecievedTherapy)
                        NewMydata['DateofTherapy'][mainDate] = DateofTherapy.isoformat( )
                        NewMydata['CurrentCondition'][mainDate] = CurrentConditionOptions.index(CurrentCondition)
                        NewMydata['currentStatusSymptoms'][mainDate] = currentStatusSymptomsOptions.index(currentStatusSymptoms)
                    
                        NewMydata['AtWorstPain'][mainDate] = AtWorstPain
                        NewMydata['Surgical_History'][mainDate] = Surgical_History
                        NewMydata['Referal_Doctor'][mainDate] = Referal_Doctor
                        NewMydata['MakesConditionBetter'][mainDate] = MakesConditionBetter
                        NewMydata['MakesConditionBetterWorse'][mainDate] = MakesConditionBetterWorse
                        NewMydata['MedicalIntervention'][mainDate] = MedicalIntervention
                        NewMydata['GoalsAfterTreat'][mainDate] = GoalsAfterTreat
                        NewMydata['MedicalInformation'][mainDate] = MedicalInformation
                        NewMydata['PrevSurger'][mainDate] = PrevSurger
                        NewMydata['OtherInfo'][mainDate] = OtherInfo
                        NewMydata['Medications'][mainDate] = Medications
                        NewMydata['Allergies'][mainDate] = Allergies



                        myquery = { "Patient_Id": track}
                        newvalues = { "$set": NewMydata}

                        ConnectData.update_one(myquery, newvalues)

                        st.success("Data Successfully Updated")
        



    elif add_selectbox == "Old Patient Re-Visit Again":

        c1, c2 = st.columns(2)
        with c1:
            sel1 = st.selectbox("Search By", ("ID", "Phone No"))
        with c2:
            track = st.text_input("Enter the ID/Phone").upper()

        if sel1 != None and track != None:
            print("bad")
            if sel1 == "ID":
                Results = ConnectData.find_one({"Patient_Id" : track})
            else:
                Results = ConnectData.find_one({"contact_number" : track})
                
            if Results != None:
                myData = Results
                st.subheader("Add the information for new treatment")
                
                Optiontype = False
                
                form = st.form(key="Edit-form" , clear_on_submit=True)
                c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35 = st.columns(35)
                with c12:
                    form.subheader('Patient Information')
                with c1:
                    Patient_Name = form.text_input("Enter the name of patient *",myData["Patient_Name"],disabled = True)
                with c2:
                    Patient_Age = form.text_input("Enter the age *", myData["Patient_Age"] , disabled = True)
                with c14:
                    Patient_Height = form.text_input("Enter the Height(cm)", myData["Patient_Height"], disabled = True)
                with c15:
                    Patient_Weight = form.text_input("Enter the Weight(kg)", myData["Patient_Height"], disabled = True)
                with c3:
                    GenderOptions = ["Male" , "Female" , "Trans"]
                    Gender = form.selectbox("Enter the Gender *" , GenderOptions, index = (myData['Patient_Gender']), disabled = True)
                with c4:
                    contact_number = form.text_input("Enter the Phone Number *", myData["Patient_Contact_No"], disabled = True)
                with c13:
                    EmployedOptions = ("Yes" , "No")
                    Employed =  form.radio(
                                    "Currently Employed?",
                                    EmployedOptions , index = int(myData['Employed']), disabled = True)
                with c5:
                    Occupation = form.text_input("Enter the Occupation", myData["Occupation"], disabled = True)
                with c6:
                    Address = form.text_input("Enter the address", myData["Address"], disabled = True)
                with c7:
                    DateOfAsses = form.date_input("Enter the Data of Assessment *" , (datetime.datetime.today().replace(microsecond=0))  ,disabled = Optiontype)
                with c16:
                    form.subheader("Basic Assesment")
                with c8:
                    Complaint = form.text_area("Chief Complaint *" , disabled = Optiontype)
                with c17:
                    Injury = form.text_input("Enter if any injury"  , disabled = Optiontype)
                with c18:
                    DateOfInjury = form.date_input("Enter the Data of injury",(datetime.datetime.today().replace(microsecond=0)), disabled = Optiontype)
                with c9:
                    DateOfInjuryforSurgery = form.date_input("Enter the date of surgery", (datetime.datetime.today().replace(microsecond=0)) , disabled = Optiontype )
                with c19:
                    DecriptionOfSurgery = form.text_area("Briefly Describe how you were injured" , disabled = Optiontype)
                with c20:
                    RecievedTherapyOptions =  ["Yes" , "No"] 
                    RecievedTherapy = form.selectbox("Have recieved the therapy for this condition" ,RecievedTherapyOptions ,  disabled = Optiontype)
                with c21:
                    DateofTherapy = form.date_input("Enter the data of therapy taken", (datetime.datetime.today().replace(microsecond=0)) , disabled = Optiontype)
                with c22:
                    CurrentConditionOptions = ["Worse" , "Same" , "Better"] 
                    CurrentCondition = form.radio("The condition is getting" , CurrentConditionOptions , disabled = Optiontype)
                with c23:
                    currentStatusSymptomsOptions = ["Constant" , "Intermittent" ] 
                    currentStatusSymptoms = form.radio("Are the symptoms" , currentStatusSymptomsOptions , disabled = Optiontype)
                with c24:
                    form.caption("Mark the number that best corresponds to the pain *")
                with c26:
                    AtWorstPain = form.slider("Enter At Worst" , min_value = 0, max_value = 10,step = 1, disabled = Optiontype)
                with c10:
                    Surgical_History = form.text_input("Enter surgical history" , disabled = Optiontype)
                with c11:
                    Referal_Doctor = form.text_input("Enter the referal doctor" , disabled = Optiontype)
                with c27:
                    MakesConditionBetter = form.multiselect("What decreases/makes the condition better", ["Bending" , "Sitting"
                                                                                , "Rising", "Changing Positions" , "Movement" ,  "Rest"
                                                                                "Standing" , "Walking" , "Lying" , "Heat" , "Ice",
                                                                                "Medication" , "Better In Am" , "Better as Day Progresses" 
                                                                                ,"Better in PM", "N/A Cast Just Remove"] , disabled = Optiontype)
                with c28:
                    MakesConditionBetterWorse = form.multiselect("What increases/makes the condtition worse" , ["Bending" , 'Sitting' , "Rising"
                                                                "Prolonged Positioning", "Worse as day progresses" , "Movement" , "Standing",
                                                                "Walking" , "Lying" , "N/A Cast Just Removed",
                                                                "Rest" , "Stairs" , "Cough" , "Worse In AM" , "Sneeze" , "Deep Breath"
                                                                , "Medication", "Worse in PM"] , disabled = Optiontype)
                with c29:
                    MedicalIntervention = form.multiselect("Previous Medical Interventions" , ["X-Ray MRI" , "Catscan" , "Injections" , "Others"] , disabled = Optiontype)
                with c30:
                    GoalsAfterTreat = form.text_input("What are the Goals to be Achieved by End of the therapy" , disabled = Optiontype)
                with c31:
                    MedicalInformation = form.multiselect("Medical Information" , ["Difficulty Swallowing", "Arthritis"
                            , "High Blood Pressure" , "Heart Trouble" , "Pacemaker" , "Epilepsy/Seizures" , "History of Drug Abuse"
                            , "Myofascial Pain" , "Cancer" , "Motion Sickness" , "Fever/Chills/Sweats" , "Unexplainable Weight Loss"
                            , "Blood Clots" , "Shortness of Breath" ,  "History of Smoking" , "Diabetes" , "Fibromyalgia"
                            , "Stroke" , "Osteoporous" , "Anemia" , "Bleeding Problem" , "HIV/Hepatitis" , "History of Alcohol Abuse",
                            "Depression/Anxiety" , "Pregnancy"] , disabled = Optiontype)
                with c32:
                    PrevSurger = form.text_input("Enter if any Previous Surgeries", disabled = Optiontype)
                with c33:
                    OtherInfo = form.text_input("Enter if any other information", disabled = Optiontype)
                with c34:
                    Medications = form.text_input("Enter if any medications are taken",disabled = Optiontype)
                with c35:
                    Allergies = form.text_input("Enter if any Allergies" , disabled = Optiontype)
                
                submit = form.form_submit_button("Click Here to add the Data!" , disabled = Optiontype)

                if submit == True:
                    NewMydata = myData.copy()
                    
                    NewMydata['DateOfAsses'].append(DateOfAsses.isoformat( ))
                    NewMydata['Complaint'].append(Complaint)
                    NewMydata['Injury'].append(Injury)
                    NewMydata['DateOfInjury'].append(DateOfInjury.isoformat( ))
                    NewMydata['DateOfInjuryforSurgery'].append(DateOfInjuryforSurgery.isoformat( ))

                    NewMydata['DecriptionOfSurgery'].append(DecriptionOfSurgery)
                    NewMydata['RecievedTherapy'].append(RecievedTherapyOptions.index(RecievedTherapy))
                    NewMydata['DateofTherapy'].append(DateofTherapy.isoformat( ))
                    NewMydata['CurrentCondition'].append(CurrentConditionOptions.index(CurrentCondition))
                    NewMydata['currentStatusSymptoms'].append(currentStatusSymptomsOptions.index(currentStatusSymptoms))
                
                    NewMydata['AtWorstPain'].append(AtWorstPain)
                    NewMydata['Surgical_History'].append(Surgical_History)
                    NewMydata['Referal_Doctor'].append(Referal_Doctor)
                    NewMydata['MakesConditionBetter'].append(MakesConditionBetter)
                    NewMydata['MakesConditionBetterWorse'].append(MakesConditionBetterWorse)
                    NewMydata['MedicalIntervention'].append(MedicalIntervention)
                    NewMydata['GoalsAfterTreat'].append(GoalsAfterTreat)
                    NewMydata['MedicalInformation'].append(MedicalInformation)
                    NewMydata['PrevSurger'].append(PrevSurger)
                    NewMydata['OtherInfo'].append(OtherInfo)
                    NewMydata['Medications'].append(Medications)
                    NewMydata['Allergies'].append(Allergies)



                    myquery = { "Patient_Id": track}
                    newvalues = { "$set": NewMydata}

                    ConnectData.update_one(myquery, newvalues)

                    st.success("Data Successfully Added")

    elif add_selectbox == 'Feedback':
        c1, c2 = st.columns(2)
        with c1:
            sel1 = st.selectbox("Search By", ("ID", "Phone No"))
        with c2:
            track = st.text_input("Enter the ID/Phone").upper()
        
        if sel1 != None and track != None:
            print("bad")
            if sel1 == "ID":
                Results = ConnectData.find_one({"Patient_Id" : track})
            else:
                Results = ConnectData.find_one({"contact_number" : track})
                
            if Results != None:
                NameId = Results['Patient_Name']
                st.write(f"Please fill the feed back form for {NameId}")
                form = st.form(key="feedback-form" , clear_on_submit=True)
                c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns(9)
                with c1:
                    form.subheader("Please do enter the patient Feedback here")
                with c2:
                    OverallRating = form.slider("On a scale of 1-10, how would you rate the overall quality of your treatment experience?" , min_value= 1, max_value=10)
                with c3:
                    Addressed = form.radio("Was the treatment effective in addressing your condition or concern?" , ["Yes" , "No"])
                with c4:
                    TreatmentExplaination = form.radio("Did the physiotherapist explain the treatment plan and goals clearly to you?" , ["Yes" , "No"])
                with c5:
                    Confortable = form.radio("Did you feel comfortable during the treatment?" , ["Yes" , "No"])
                with c6:
                    Punctual = form.radio("Was the physiotherapist punctual and respectful of your time?" , ["Yes", "No"])
                with c7:
                    Recommend = form.slider("How likely are you to recommend our clinic to a friend or family member?" , min_value = 1, max_value = 10)
                with c8:
                    Suggestions = form.text_input("Do you have any suggestions for how we could improve our services or your treatment experience?")
                with c9:
                    TreatmentExperience = form.text_input("Is there anything else you would like to share about your treatment experience?")


                submitFeed = form.form_submit_button("Click Here to submit the feedback form!")

                if submitFeed == True:
                    Results['Feedback'] = {
                        'OverallRating' : OverallRating,
                        "Addressed" : Addressed,
                        'TreatmentExplaination' : TreatmentExplaination,
                        "Confortable" : Confortable,
                        "Punctual" : Punctual,
                        "Recommend" : Recommend,
                        "Suggestions" : Suggestions,
                        "TreatmentExperience": TreatmentExperience
                    }

                    myquery = { "Patient_Id": track}
                    newvalues = { "$set": Results}

                    ConnectData.update_one(myquery, newvalues)

                    st.success("Data Successfully Added")





        

            
            

else:
    st.warning("Username/password Incorrect!")
   
