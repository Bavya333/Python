from datetime import datetime

class Employee:  
    
    def __init__(self,name,salary,DOJ):  
        self.__name = name  
        self.__salary = salary
        self.__DOJ = DOJ
    
    def payRaise(self,amount):  
        self.__salary +=amount

    def toString(self):
        print("Name: ",self.__name)
        print("DOJ: ",self.__DOJ.strftime("%d/%m/%Y"))
        print("Salary: ",self.__salary)
        
    def payBonus(self,percentage=1,minSalary=30000,maxSalary=75000):
        if(self.__salary>=minSalary and self.__salary<=maxSalary):
            self.__salary += (1/100)*self.__salary
    
i=1;
while(i>0):
    print("1.Create Employee Date \n 2.Raise Salary \n 3.Pay Bonus \n 4.Display Data \n 0.Exit\n")
    i = int(input())
    if(i==1):
        print("Enter Name:")
        name = input()
        print("Enter Day of Joining:")
        day = int(input())
        print("Enter Month of Joining:")
        month = int(input())
        print("Enter Year of Joining:")
        yr = int(input())
        print("Enter Salary:")
        salary= int(input())
        emp = Employee(name,salary,datetime(yr,month,day))
    elif(i==2): 
        print("Enter upraisal amount:")
        amnt= int(input())
        emp.payRaise(amnt)
    elif(i==3):
        j=1;
        print("1.Pay Bonus \n 2.Pay Bonus with % \n 3.Pay Bonus with % & Min,Max Salary \n 0.Exit\n")
        j = int(input())
        if(j==1):
            emp.payBonus()
        elif(j==2):        
            print("Enter Percentage of Bonus:")
            percent= int(input())
            emp.payBonus(percent)
        elif(j==3):
            print("Enter Percentage of Bonus:")
            percent= int(input())
            print("Enter Min Salary:")
            min = int(input())
            print("Enter Max Salary:")
            max = int(input())
            emp.payBonus(percent, min, max)
        else:
            break;
    elif(i==4):
        emp.toString()
    else:
        break;
