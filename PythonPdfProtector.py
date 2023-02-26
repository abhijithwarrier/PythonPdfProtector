# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI APPLICATION TO PROTECT PDF FILE USING USER-INPUT PASSWORD.
#
# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping,
# and transforming the pages of PDF files. It can also add custom data, viewing options, and
# passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.
#
# The module can be installed using the command - pip install pypdf

# Importing necessary packages
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from pypdf import PdfReader, PdfWriter

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    pdfFileLabel = Label(root, text="PDF FILE NAME : ", bg="darkseagreen4")
    pdfFileLabel.grid(row=1, column=1, padx=5, pady=10)

    root.openPDFEntry = Entry(root, width=35, textvariable=filePath)
    root.openPDFEntry.grid(row=1, column=2, padx=10, pady=10)

    root.openPDFButton = Button(root, width=10, text="BROWSE", command=pdfBrowse)
    root.openPDFButton.grid(row=1, column=3, padx=10, pady=10)

    passwordLabel = Label(root, text="PDF PASSWORD : ", bg="darkseagreen4")
    passwordLabel.grid(row=2, column=1, padx=5, pady=10)

    root.passwordEntry = Entry(root, width=35, textvariable=pdfPassword)
    root.passwordEntry.grid(row=2, column=2, padx=10, pady=10)

    root.captureBTN = Button(root, text="PROTECT", command=Protect, bg="LIGHTBLUE", font=('Comic Sans MS',15), width=20)
    root.captureBTN.grid(row=3, column=2, padx=10, pady=10)

# Defining pdfBrowse() to browse and select the PDF files to be encrypted
def pdfBrowse():
    # Presenting user with a pop-up for directory selection. initialdir argument is optional
    # Retrieving the user-input destination directory and storing it in destinationDirectory
    # Setting the initialdir argument is optional. SET IT TO YOUR DIRECTORY PATH
    openDirectory = filedialog.askopenfilename(initialdir="YOUR DIRECTORY PATH")
    # Displaying the directory in the directory textbox
    filePath.set(openDirectory)

# Defining Protect() to protect PDF file using the user-input password
def Protect():
    # Fetching and storing the user-input password for the pdf file
    pdf_password = pdfPassword.get()
    # Fetching and storing the name of the input pdf along with the path
    input_file_path_name = filePath.get()
    # Create PdfFileReader, PdfWriter Objects
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(input_file_path_name)
    # Storing the destination path and name for protected file
    file_path = os.path.dirname(os.path.abspath(input_file_path_name))
    file_name = os.path.basename(input_file_path_name.split(".")[0])
    # Looping through each pages of the pdf and adding them to PDF Writer object
    for page in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page])
    # Encrypting the pdf using the encrypt() function of pdf_writer
    pdf_writer.encrypt(user_password=pdf_password, owner_pwd=None, use_128bit=True)
    # Create new PDF file and saving the pages
    with open(file_path + "/" + file_name + "-protected.pdf", "wb") as pdf_file:
        pdf_writer.write(pdf_file)
    messagebox.showinfo('SUCCESS!', 'PDF FILE HAS BEEN PROTECTED')

# Creating object of tk class
root = tk.Tk()
# Setting the title, window size, background color
# and disabling the resizing property
root.title("PDF-PROTECTOR")
root.geometry("600x150")
root.resizable(False, False)
root.configure(background = "darkseagreen4")
# Creating tkinter variables
filePath = StringVar()
pdfPassword = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
