import streamlit as st
from PIL import Image

# page settings
st.set_page_config(page_title='CS:GO Utilities', layout="wide")
st.title('Mirage Nades')

# path setting
images_dir = 'images/mirage/'
videos_dir = 'videos/mirage/'

def openImageAndDisplay(image, dir=images_dir, width=350):
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
  st.markdown("""<hr style="height:1px;background-color:#333;" /> """, unsafe_allow_html=True)

# switch between utilities
utility = st.radio('Utility', ('Smoke', 'Molotov', 'HE-Grenade', 'Flash'))

###############################################################################
if utility == 'Smoke':
  st.markdown('##### Stairs')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('stairs.jpg')
    with col2:
      openVideoAndDisplay('stairs.mp4')
  displayHorizontalLine()
  ###########################################################################
  st.markdown('##### Jungle')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('jungle.jpg')
    with col2:
      openVideoAndDisplay('jungle.mp4')
  displayHorizontalLine()
  ###########################################################################
  st.markdown('##### Slope')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('slope.jpg')
    with col2:
      openVideoAndDisplay('slope.mp4')
  displayHorizontalLine()
  ###########################################################################
  st.markdown('##### Connector Oneway')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('connector-oneway.jpg')
    with col2:
      openVideoAndDisplay('connector-oneway.mp4')
    displayHorizontalLine()
    ###########################################################################
    st.markdown('##### Deep Apps')
    col1, col2, col3, col4 = st.columns(4)
    with st.container():
      with col1:
        openImageAndDisplay('apps-deep.jpg')
      with col2:
        openVideoAndDisplay('apps-from-side.mp4')
      with col3:
        openVideoAndDisplay('apps-from-truck.mp4')
    displayHorizontalLine()
    ###########################################################################
    st.markdown('##### Arch Left')
    col1, col2, col3, col4 = st.columns(4)
    with st.container():
      with col1:
        openImageAndDisplay('arch-left.jpg')
      with col2:
        openVideoAndDisplay('arch-left.mp4')
    displayHorizontalLine()
    ###########################################################################
    st.markdown('##### Arch Right')
    col1, col2, col3, col4 = st.columns(4)
    with st.container():
      with col1:
        openImageAndDisplay('arch-right.jpg')
      with col2:
        openVideoAndDisplay('arch-right.mp4')
      with col3:
        openVideoAndDisplay('arch-right-jumpthrow.mp4')

###############################################################################
if utility == 'Molotov':
  st.markdown('##### Sandwitch')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('sandwitch.jpg')
    with col2:
      openVideoAndDisplay('sandwitch.mp4')

###############################################################################
if utility == 'HE-Grenade':
  st.write('To come')

###############################################################################
if utility == 'Flash':
  st.write('To come')

