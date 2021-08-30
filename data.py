import csv
import re
import serial
import threading
import streamlit as st
from PIL import Image
import serial
import time


def authenticate(u,p):
    with open("user_detail.txt", "r") as f:
        file = csv.reader(f)
        for i in file:
            if u == i[0] and p == i[1]:
                return True


def valdate_check(u):
    with open("user_detail.txt", "r") as f:
        file = csv.reader(f)
        for i in file:
            if u == i[0]:
                return True


def set_interval(f, t):
    e = threading.Event()
    while not e.wait(t):
        f()


def arduino_data():
    arduino = serial.Serial('COM3', 9600)
    arduino.close()
    arduino.open()
    while True:
        data = arduino.readline()
        data = data.split()
        print("sesor1",data[0].decode())
        print("sensor2",data[1].decode())
        if int(data[0]) <= 15 and int(data[1]) <= 15:
            st.write("Slot are full")
            break
        elif int(data[0]) > 16 and int(data[1]) <= 15:
            st.write("Slot 1 is open")
            break
        elif int(data[0]) <= 15 and int(data[1]) > 16:
            st.write("Slot 2 is open")
            break
        else:
            st.write("SLots are open")
            break


# img1 = Image.open('C:/Users/Sachet/Desktop/ultrsonic/img1.jpg')
# st.image(img1, use_column_width=True)
st.header("Car Charging Station")
# sidebar components
x = st.sidebar.radio("Select", ('login','signup'))
if x == 'login':
    r = re.compile(r'[a-zA-Z]{5,15}') # allows only to enter aplhabets # (r'[a-zA-Z1-9]{5-15}) allowes alphabets and numbers
    st.sidebar.header("Login")
    user = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password(>=8 character)", type='password')
    if st.sidebar.button("Login"):
        if user == "" and password == "":
            st.sidebar.error("Empty Fields")
        elif user != "" and password == "":
            st.sidebar.error("Enter a password")
        elif user == "" and password != "":
            st.sidebar.error("Enter Username")
        elif len(password) < 8:
            st.sidebar.error("Password is too short")
        elif not r.match(user):
            st.sidebar.error("Please Enter a proper Username")
        else:
            x = authenticate(user,password)
            if x:
                st.sidebar.success("Welcome " + user)
                set_interval(arduino_data, 7)
            else:
                st.sidebar.error("User not Registered")

elif x == 'signup':
    st.sidebar.header('Sign-Up')
    u = st.sidebar.text_input('Userrname')
    p = st.sidebar.text_input('Password(>=8 characters)')

    if st.sidebar.button('Register'):
        if u == "" and p == "":
            st.sidebar.error("Empty Fields")
        elif u != "" and p == "":
            st.sidebar.error("Enter a password")
        elif u == "" and p != "":
            st.sidebar.error("Enter Username")
        elif len(p) < 8:
            st.sidebar.error("Password is too short")
        elif u != '' and p != '':
            if valdate_check(u):
               st.error("Username exist")
            else:
                try:
                    f = open("user_detail.txt", "a+")
                    f.write(u+","+p)
                    f.write("\n")
                    f.close()
                    st.sidebar.success("Registered")
                except Exception:
                    st.sidebar.error("User Not registered")

        else:
            st.sidebar.error()
