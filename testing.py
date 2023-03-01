import streamlit as st
import datetime

from pymongo.mongo_client import MongoClient

Data = MongoClient("mongodb://localhost:27017/")
ConnectData = Data['Test']['Test']

d = datetime.datetime.now()



data = st.date_input("Enter the Date" , datetime.datetime.now())

l = ConnectData.find_one({'date' :d})

diaply = st.date_input("Display date is",l)