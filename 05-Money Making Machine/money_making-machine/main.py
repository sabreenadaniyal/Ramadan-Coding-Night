import streamlit as st   # UI purpose k liye use krte hain
import random            # random number generate krwane k liye  btw specific things
import time              # time se jitni bhi functionalily hai wo provide krta hai(current time etc)
import requests          # help krta APIs ko call krne main(important)

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)   # specific method hai jis ka name hai randint(specific integer generate krta hai)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting Your Money...")
    time.sleep(3)                   # time delay krwane hmain hmari madad krta hai
    amount =  generate_money()            
    st.success(f"You made ${amount}!")

def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustles"]
        else:
            return ("Freelancing")
        
    except:
        return ("Something went Wrong!")
    
st.subheader("Side Hustle Ideas")
if st.button("Generate Hustles"):
    idea = fetch_side_hustle()
    st.success(idea)


def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["quotes"]
        else:
            return ("Money is the root of all evil!!")
    except:
        return ("Something went Wrong!")
    
st.subheader("Money-making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quotes()
    st.info(quote)