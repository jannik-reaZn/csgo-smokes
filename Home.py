import streamlit as st
from PIL import Image

# page settings
st.set_page_config(page_title='CS:GO Utilities', layout='wide')
st.title('CSGO Utilities')

# main text
st.markdown(
  'CSGO Nades is a website that collects nades for Counter-Strike Global Offensive. You can browse smokes, flashbangs, molotovs or he-grenades. All utilities are for **64-Tick** servers.')

# jump throw bind
st.header('Jump Throw Bind')
st.text(
  'alias "+jumpthrow" "+jump;-attack";  \n'
  'alias "-jumpthrow" "-jump";  \n'
  'bind "<key>" "+jumpthrow"')

# run throw bind
st.header('Run Throw Bind')
st.text(
  'alias "+forwardjumpthrow" "+forward; +jump;-attack;-attack2";  \n'
  'alias "-forwardjumpthrow" "-jump; -forward"  \n'
  'bind "<key>" "+forwardjumpthrow"')

# toggle crosshair bind
st.header('Toogle Crosshairsize')
st.text('bind "<key>" "toggle cl_crosshairsize 1000 <your cl_crosshairsize>')

