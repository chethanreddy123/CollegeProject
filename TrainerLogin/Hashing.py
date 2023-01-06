import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["parker" , "henry"]
usernames = ["parke123" , "henry123"]
passwords = ["abc123" , "def123"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"

with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

    