import streamlit as st
from Views import FeedView, AddPostView
from Services import GetFeed, AddPost
AddPostView(AddPost)
st.write("___")
FeedView(GetFeed)