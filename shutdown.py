from tkinter import *
import os

# Function to restart the system immediately
def Restart():
    os.system("shutdown /r /t 1")

# Function to restart the system after 20 seconds
def RestartWithTime():
    os.system("shutdown /r /t 20")

# Function to log out the current user
def LogOut():
    os.system("shutdown /l")  # Corrected flag from -1 to /l

# Function to shut down the system immediately
def ShutDown():
    os.system("shutdown /s /t 1")

# GUI setup
st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="blue")

# Restart button
rst_btn = Button(st, text="Restart", font=("Times New Roman", 15), relief=RAISED, cursor="plus", command=Restart)
rst_btn.place(x=190, y=60, height=40, width=120)

# Timed restart button
rst_time_btn = Button(st, text="Restart in 20s", font=("Times New Roman", 15), relief=RAISED, cursor="plus", command=RestartWithTime)
rst_time_btn.place(x=190, y=135, height=40, width=120)

# Log out button
log_out_btn = Button(st, text="Log Out", font=("Times New Roman", 15), relief=RAISED, cursor="plus", command=LogOut)
log_out_btn.place(x=190, y=220, height=40, width=120)

# Shut down button
shut_dowm_btn = Button(st, text="Shut Down", font=("Times New Roman", 15), relief=RAISED, cursor="plus", command=ShutDown)
shut_dowm_btn.place(x=190, y=300, height=40, width=120)

st.mainloop()
