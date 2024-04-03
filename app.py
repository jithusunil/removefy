import streamlit as st
from rembg import remove 
from PIL import Image
def removebg(img):
    input = Image.open(img)
    return remove(input)


def main():
    st.title("BACKGROUND REMOVER WEBSITE")
    uploaded_file = st.file_uploader("Choose the image..",type=["jpg","jpeg","png"])

    if uploaded_file is not None:
        st.image(uploaded_file,caption="uploaded...")
        st.write("processing...")
        result=removebg(uploaded_file)
        st.image(result,caption="Result")

if __name__ == '__main__':
    main()