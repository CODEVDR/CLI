import main  # Importing Main to access fee class
import subprocess

print("Fee Store")  # Heading

n = int(input("Enter Number Of Students : "))
for i in range(1, n+1):
    name = input("Enter Name Of Student : \n")  # Name Store
    amount = float(input("Enter Fee Amount : \n"))  # Amount Store
    admission_no = int(input("Enter Admission Number : \n"))  # Admn_no Store
    f = main.fee(name, amount, admission_no)  # fee class in main.py
    f.feeStore()  # A Function in main.py to store fee details in feeData File

subprocess.call("run.py", shell=True)  # For Cllaing run.py
