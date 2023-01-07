import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title('Mirage Smokes')

# image path
images_dir = 'images/mirage/'

def openImageAndDisplay(image, dir=images_dir, width=400):
  image = Image.open(images_dir + image)
  st.image(image, width=width)




st.markdown('##### Window')
col1, col2, col3 = st.columns(3)
with col1:
  image = Image.open(images_dir + 'window.jpg')
  st.image(image, width=400)

with col2:
  image = Image.open(images_dir + 'window-1-1.jpg')
  st.image(image, width=400)

with col3:
  image = Image.open(images_dir + 'window-1-2.jpg')
  st.image(image, width=400)

st.markdown("""<hr style="height:onee;background-color:#333;" /> """, unsafe_allow_html=True)




st.markdown('##### Stairs')
col1, col2 = st.columns(2)
with col1:
  image = openImageAndDisplay('stairs.jpg')

