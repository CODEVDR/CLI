import os  # Import Modules
import subprocess
from datetime import datetime  # [Date Time Module For Storing Current Date]


# Creating log file
v = datetime.now()
with open("data/log.txt", "a") as dt:
    date1 = dt.write(f"\nOpend on {v}")

# BAsic Headings And Comments
print("***Welcome to Shyam Computer Academy***")
print("U_U A CLI interface for storing student and fee details U_U")

print('Enter "s" to Open Student Details')
print('Enter "f" to Open Fee Details')
print('Enter "opensd" to Student Details')
print('Enter "openfd" to Fee Details')

s = input("Enter [s/f/openfd/opensd] : ")  # Taking s/f/openfd/opensd


if s in "sS":
    # For Storing Student Details
    print("Press F5 Key in Your Keyboard To Run StudentDetails.py")
    subprocess.call("StudentDetails.py", shell=True)
elif s in "fF":
    # For Storing Fee Details
    print("Press F5 Key in Your Keyboard To Run FeeStore.py")
    subprocess.call("FeeStore.py", shell=True)
elif s.lower() == "openfd":
    # For Fee Details
    print("Enter Correct [admission_no]!!!!")
    s = input("Enter : ")
    try:
        def openfile(filename):
            os.system(f"notepad.exe data/feeData/feeData{filename}.txt")
        openfile(s)
        print(f"feeData{s}.txt opened Sucessfully!!!!")
    except FileNotFoundError:
        print(
            f"feeData{s} Not in Database ...Please Enter Correct Admission Number")
elif s.lower() == "opensd":
    # For Student Details Details
    print("Enter Correct [Student_Name]!!!!")
    s = input("Enter Name of Student : ")
    s = s.capitalize()
    try:
        def openfile(filename):
            os.system(f"notepad.exe data/StudDetails/Student {filename}.txt")
        openfile(s)
        print(f"Student {s}.txt opened Sucessfully!!!!")
    except FileNotFoundError:
        print(
            f"feeData{s} Not in Database ...Please Enter Correct Admission Number")
else:
    print("Please Enter A Valid Syntax!!!!")
