import csv
import re 
'''def csv_create():
    with open('studentfile.csv','w') as studentfile:
        studentfileWriter=csv.writer(studentfile)
        studentfileWriter.writerow(["name","age","contactno","email"])
        studentfile.close()'''
def check_mail(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):  
        return 1    
    else:  
        return 0
def check(stu_list):
     f=1
     if(len(stu_list)!=4):
        print("enter all details correctly")
     if not stu_list[0].isalpha():
        print("Please enter a valid name.")
        f=0
     if not stu_list[1].isnumeric():
        print("enter age correctly")
        f=0
     if len(stu_list[2])!=10:
        print("enter phone number correctly")
        f=0
     if(check_mail(stu_list[3])!=1):
        print("Invalid Email")
        f=0
     if(f==1):
        return 1
     else:
        print("enter valid details")
        return 0
def add_details():
    string=input("enter name,age,contact_no,email_id")
    stu_list=string.split(" ")
    if(check(stu_list)!=1):
        pass
   # print(stu_list)
    else:
        with open('studentfile.csv','a') as studentfile:
            studentfileWriter=csv.writer(studentfile)
            studentfileWriter.writerow([stu_list[0],stu_list[1],stu_list[2],stu_list[3]])
            studentfile.close()
def viewdetails():
    f=open("studentfile.csv","r",encoding="utf8")
    displaylist=f.read()
    print(displaylist)
    f.close()
def main():
    #csv_create()
    print("*****Welcome to student administration System*****")
    condition="yes"
    while(condition=="yes"):
        print("1.Add details to csv file")
        print("2.View the details")
        n=int(input("enter ur option:"))
        if(n==1):
            add_details()
        elif(n==2):
            viewdetails()
        condition=input("type 'yes' if you want to enter details or view")
        if(condition!="yes"):
            print("THANK YOU")
            
main()    
