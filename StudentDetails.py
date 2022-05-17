import main  # [Importing main.py]
import subprocess  # A Module For Opening Different Files
print("Student Details Store")  # Heading

# Main Call
n = int(input("Enter How Many Students : "))
for i in range(1, n+1):
    name = input("Enter Student Name : \n")  # Name Store
    Class = input("Enter Student class : \n")  # Class Store
    sub = input("Enter Subject Opted By Student : \n")  # Subject Store
    # Fee Method Store
    fee = input("Fee Paying [Monthly/Quaterly/Yearly] : \n")
    # For Capitalizing All Details
    name = name.capitalize()
    sub = sub.capitalize()
    fee = fee.capitalize()
    # Class data in main.py
    v = main.data(name, Class, sub, fee)  # Class Data Accessing Here
    v.data()  # Function in data class :- To store details Of Student in Database

subprocess.call("run.py", shell=True)  # For Calling run.py
