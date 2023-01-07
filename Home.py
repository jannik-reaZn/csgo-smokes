import streamlit as st
from PIL import Image

st.set_page_config(layout='wide')
st.title('CSGO Utilities')
st.markdown(
  'CSGO Nades is a website that collects nades for Counter-Strike Global Offensive. You can browse smokes, flashbangs, molotovs or he-grenades.  \n'
  'Important: All utilities are for **64-Tick** server!')

# key bindings
st.header('Jump Throw Bind')
st.markdown(
  'alias "+jumpthrow" "+jump;-attack";  \n'
  'alias "-jumpthrow" "-jump";  \n'
  'bind "<key>" "+jumpthrow"')

st.header('Run Throw Bind')
st.markdown(
  'alias "+forwardjumpthrow" "+forward; +jump;-attack;-attack2";  \n'
  'alias "-forwardjumpthrow" "-jump; -forward"  \n'
  'bind "<key>" "+forwardjumpthrow"')

st.header('Toogle Crosshairsize')
st.markdown(f'<p style="background-color:#cccccc; border-radius:2%;">bind "key" "toggle cl_crosshairsize 1000 <your cl_crosshairsize>"</p>', unsafe_allow_html=True)

