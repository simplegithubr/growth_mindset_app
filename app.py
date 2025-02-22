#streamlit 
import streamlit as st 
st.set_page_config(page_title = "Growth Mindset Project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")
st.header("🚀 Welcome To Your Growth Journey")
st.writte("This web app helps you understand and develop a growth mindset. "
    "Remember, learning is a journey, and every challenge is an opportunity to grow! ")
#quote section
st.header("Today's Growth Mindset Quote 💡")
st.write("Success is not final, failure is not fatal. It is the courage to continue that counts.")
st.header("whta's Your Challange Today?")
user_input = st.text_input("Describe a challange youre facing")
#condition
if user_input:
    st.success(f"you are facing : {user_input} . keep pushing toword your golls! 💪 ")
else:
        st.warning("Tell us about your challange to get started")
#Reflection Section
st.header("Reflecting on Your Learning")
reflection = st.text_area("write your reflection here ")
if reflection:
         st.success(f"great insight! your reflection : {reflection} ")
else:
     st.info("Reflecting on past experiences help you grow! share your thoughts.")


#achievement
st.header("Celebrate Your Win 🏆")
achievement = st.text_area("share somthing you have recently accomplished")

if achievement:
    st.success(f"Amazing! You achieved: {achievement} 🎉")
else:
    st.info("Big or Small , every achievement  counts! Share one now ")
#footer 
st.write("- - - ")
st.write("Keep beliving in yourself. Growth is a journey, not a destination! 🚀")
st.write("**⛔  Createt by Sagar sheikh")
