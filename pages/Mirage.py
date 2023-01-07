import streamlit as st
from PIL import Image

# page settings
st.set_page_config(page_title='CS:GO Utilities', layout="wide")
st.title('Mirage Smokes')

# path setting
images_dir = 'images/mirage/'
videos_dir = 'videos/mirage/'

def openImageAndDisplay(image, dir=images_dir, width=300):
  """  Opens an image and displays it in the streamlit app. """
  image = Image.open(images_dir + image)
  st.image(image, width=width)

def openVideoAndDisplay(video, dir=videos_dir):
  """ Opens a video and displays it in the streamlit app. """
  video_file = open(videos_dir + video, 'rb')
  video_bytes = video_file.read()
  st.video(video_bytes)

def displayHorizontalLine():
  """ Displays a horizontal line in the streamlit app. """
  st.markdown("""<hr style="height:onee;background-color:#333;" /> """, unsafe_allow_html=True)

###############################################################################
st.markdown('##### Window')
col1, col2, col3 = st.columns(3)
with st.container():
  with col1:
    openImageAndDisplay('window.jpg')
  with col2:
    openImageAndDisplay('window-1-1.jpg')
  with col3:
   openImageAndDisplay('window-1-2.jpg')

displayHorizontalLine()
###############################################################################
st.markdown('##### Stairs')
col1, col2, col3, col4 = st.columns(4)
with st.container():
  with col1:
    openVideoAndDisplay('stairs.mp4')
  with col2:
    openVideoAndDisplay('stairs.mp4')
  with col3:
    openVideoAndDisplay('stairs.mp4')
  with col4:
    openVideoAndDisplay('stairs.mp4')
