from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Subha", page_icon=":tada:",layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_7X0d6AzODk.json")
img_contact_form = Image.open("images/a.jpg")

with st.container():
    st.header("Hi, I am Subhajeet Dey :wave:")
    st.title("A CS Student from Alipurduar")
    st.write("I am passionate about finding ways to use c and python to be more efficient")
    st.write("[Learn More>](https://github.com/rajib0777)")


with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("#####")
        st.write("-Hello and welcome to my website!")
        st.write("-I'm a final year CS student at Coochbehar College.")
        st.write("-I'm currently working on acquiring knowledge in JavaScript as well as improving my coding skills in C and Python...")
        

    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")

with st.container():
    st.write("-----")
    st.header("My Images")
    st.write("#####")
    image_column,text_column =st.columns((1,2))
    with image_column:
        st.image(img_contact_form)

    with text_column:
        st.subheader("hello")
        st.write("Here Am I")

        contact_form = """
        <form action="https://formsubmit.co/deysubhajeet22@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Write Your Message Here" required></textarea>
     <button type="submit">Send</button>
    </form>
        """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()














with st.container():
    st.write("------")
    st.header("About")
    st.write("#####")
    st.write("""I'm passionate about programming and love to learn new things, and this website is a place where I can share my experiences
              and insights with others who share the same interests.On this site, you'll find articles, tutorials, and resources related to 
              JavaScript, C, Python, and programming in general.I hope you find the content here useful and engaging, and I encourage you to
               share your thoughts and feedback with me through the comments section or by contacting me directly.""")
    st.header("Thank you for visiting, and happy coding!🙏")
    




with st.container():
    st.write("------")
    st.header("Get IN Touch With Me!!!")
    st.write("#####")
