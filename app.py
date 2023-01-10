import streamlit as st
import sys
from streamlit import cli as stcli

click = st.button("Click me Here!")

if click  == True:
   if __name__ == '__main__':
      sys.argv = ["streamlit", "run", "APP_NAME.py"]
      sys.exit(stcli.main())