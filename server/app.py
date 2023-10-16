import os
import google.generativeai as palm
import customtkinter

palm.configure(api_key=os.getenv('PALM_API_KEY'))

# building a base GUI

customtkinter.set_appearance_mode("Light")
root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("test")










