import streamlit as st
from PIL import Image

# page settings
st.set_page_config(page_title='CS:GO Utilities', layout="wide")
st.title('Mirage Nades')

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
  st.markdown("""<hr style="height:1px;background-color:#333;" /> """, unsafe_allow_html=True)

# switch between utilities
utility = st.radio('Utility', ('Smoke', 'Molotov', 'HE-Grenade', 'Flash'))

###############################################################################
if utility == 'Smoke':
  st.markdown('##### Stairs')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/stairs.jpg')
    with col2:
      openVideoAndDisplay('/smokes/stairs.mp4')
  displayHorizontalLine()

  st.markdown('##### Jungle')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/jungle.jpg')
    with col2:
      openVideoAndDisplay('/smokes/jungle.mp4')
  displayHorizontalLine()

  st.markdown('##### Jungle Deep')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/jungle-deep.jpg')
    with col2:
      openVideoAndDisplay('/smokes/jungle-deep-from-tetris.mp4')
  displayHorizontalLine()


  st.markdown('##### CT-Spawn')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/ct-spawn.jpg')
    with col2:
      openVideoAndDisplay('/smokes/ct-spawn.mp4')
    with col3:
      openVideoAndDisplay('/smokes/ct-spawn-from-tetris.mp4')
    with col4:
      openVideoAndDisplay('/smokes/ct-spawn-from-top-mid.mp4')
  displayHorizontalLine()


  st.markdown('##### Slope')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/slope.jpg')
    with col2:
      openVideoAndDisplay('/smokes/slope.mp4')
  displayHorizontalLine()

  st.markdown('##### Connector top')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/connector-top.jpg')
    with col2:
      openVideoAndDisplay('/smokes/connector-top-from-tetris.mp4')
    with col3:
      openVideoAndDisplay('/smokes/connector-top-from-top-mid.mp4')
    with col4:
      openVideoAndDisplay('/smokes/connector-top-from-side-alley-2.mp4')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
      openVideoAndDisplay('/smokes/connector-top-from-side-alley-1.mp4')
    with col2:
      openVideoAndDisplay('/smokes/connector-top-from-ct-spawn.mp4')
    displayHorizontalLine()

  st.markdown('##### Connector Top Oneway')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/connector-oneway.jpg')
    with col2:
      openVideoAndDisplay('/smokes/connector-oneway.mp4')
    displayHorizontalLine()

  st.markdown('##### Connector Bottom')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/connector-bottom.jpg')
    with col2:
      openVideoAndDisplay('/smokes/connector-bottom-from-short.mp4')
  displayHorizontalLine()
 
  st.markdown('##### Apps')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/apps.jpg')
    with col2:
      openVideoAndDisplay('/smokes/apps-from-trash.mp4')
  displayHorizontalLine()


  st.markdown('##### Deep Apps')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/apps-deep.jpg')
    with col2:
      openVideoAndDisplay('/smokes/apps-from-side.mp4')
    with col3:
      openVideoAndDisplay('/smokes/apps-from-truck.mp4')
  displayHorizontalLine()

  st.markdown('##### Arch Left')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/arch-left.jpg')
    with col2:
      openVideoAndDisplay('/smokes/arch-left.mp4')
  displayHorizontalLine()

  st.markdown('##### Arch Right')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/arch-right.jpg')
    with col2:
      openVideoAndDisplay('/smokes/arch-right.mp4')
    with col3:
      openVideoAndDisplay('/smokes/arch-right-jumpthrow.mp4')

  st.markdown('##### Short')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/short.jpg')
    with col2:
      openVideoAndDisplay('/smokes/short.mp4')

  st.markdown('##### Window')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/smokes/window.jpg')
    with col2:
      openVideoAndDisplay('/smokes/window-from-top-mid.mp4')
    with col3:
      openVideoAndDisplay('/smokes/window-from-spawn-1.mp4')
    with col4:
      openVideoAndDisplay('/smokes/window-from-spawn-2.mp4')

  st.markdown('##### Mid Top')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col2:
      openVideoAndDisplay('/smokes/mid-top.mp4')


###############################################################################
if utility == 'Molotov':
  st.markdown('##### Sandwitch')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/molotovs/sandwitch.jpg')
    with col2:
      openVideoAndDisplay('/molotovs/sandwitch.mp4')

  st.markdown('##### Triple')
  col1, col2, col3, col4 = st.columns(4)
  with st.container():
    with col1:
      openImageAndDisplay('/molotovs/triple.jpg')
    with col2:
      openVideoAndDisplay('/molotovs/triple-from-tetris.mp4')

###############################################################################
if utility == 'HE-Grenade':
  st.write('To come')

###############################################################################
if utility == 'Flash':
  st.write('To come')

