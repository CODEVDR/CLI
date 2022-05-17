from datetime import datetime, date


class data:
    def __init__(self, Name, Class, Cource, Time_period):
        self.Name = Name
        self.Class = Class
        self.Cource = Cource
        self.Time_period = Time_period

    def data(self):
        v = str(date.today())
        with open(f"data/StudDetails/Student {self.Name}.txt", "a") as data:
            store = data.write(
                f"Registration on Date {v}\nName Of Student Is : {self.Name}\nStudent Class : {self.Class}\nCource Opted By Student is : {self.Cource}\nFee Paying method : {self.Time_period}\n")
            data.close()


class fee:
    def __init__(self, name, amt, admn_no):
        self.amt = amt
        self.name = name
        self.admn_no = admn_no

    def feeStore(self):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        with open(f"data/feeData/feeData{self.admn_no}.txt", "a") as fee:
            store = fee.write(
                f"\nFee Paid On {date_time}\n\nName of Stundent is : {self.name}\nAmount Paid By Student is : {self.amt}\nAdmission Number of {self.name} is : {self.admn_no}")
            fee.close()
