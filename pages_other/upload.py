import streamlit as st
from itertools import cycle
from pymongo import MongoClient
from bson.binary import Binary
from PIL import Image
import io
import matplotlib.pyplot as plt
from PIL import Image


Data = MongoClient("mongodb+srv://chethanreddy1234:chethan1234@cluster0.yvbx0ko.mongodb.net/?retryWrites=true&w=majority")

images = Data['Images']['Images']



st.title("Cloud Image storage")
st.subheader("Upload your images here!!")

uploaded_file = st.file_uploader("Choose a file")
Caption = st.text_input("Enter the Caption for your image")

button = st.button("Add Image to cloud")

if uploaded_file is not None and button == True:
    im = Image.open(uploaded_file)

    image_bytes = io.BytesIO()
    im.save(image_bytes, format='JPEG')

    image = {

        'data': image_bytes.getvalue(),
        'caption' : Caption
    }

    image_id = images.insert_one(image).inserted_id



st.subheader("Your Previously Uploaded images")


image = images.find()




filteredImages = image # your images here

Count = images.count_documents({})
print(Count)


cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
for idx in range(Count):
    pil_img = Image.open(io.BytesIO(image[idx]['data']))
    next(cols).image(pil_img, width=300,  caption=image[idx]["caption"])