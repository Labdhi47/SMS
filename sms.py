import os

file_name = input("Enter your file name as a text file format : ")

if not os.path.exists(file_name):
    with open(file_name, 'w') as f:
        f.write("")
    print(f"File '{file_name}' created successfully!")
else:
    print(f"File '{file_name}' already exists!")


while(True):
    print("\n1.Add Record")
    print("2.Display All Record")
    print("3.Search Student Record")
    print("4.Delete Student Record")
    print("5.Update Student Record")
    print("6.Exit")
    
    n=int(input("\nEnter your choice = "))
    match n:
        case 1:
            print("\nEnter Student Detail")
            name=input("Enter Name = ")
            Enroll_no=input("Enter Enrollment No = ")
            Semester=input("Enter Semester = ")
            Branch=input("Enter Branch = ")
            CPI=input("Enter CPI = ")
            with open(file_name,"a") as fp:
                fp.write(name+"\t\t"+Enroll_no+"\t\t"+Semester+"\t\t"+Branch+"\t\t"+CPI+"\n")
        
        case 2: 
            print("📃 List of Present Records 📃")
            print("Name - Enroll_No - Semester - Branch - CPI")
            with open(file_name,"r") as fp:
                while(True):
                    d=fp.readline()
                    l=len(d)
                    if(l==0):
                        break
                    print(d.strip())
        
        case 3:
            print("1.Search by Name ??")
            print("2.Search by Enroll_NO ??")
            print("3.Search by Semester ??")
            print("4.Search by Branch ??")                        
            print("5.Search by CPI ??")
            m=int(input("Enter your choice:"))
            match m:
                case 1:
                    search=input("Enter Student Name:")
                    with open(file_name,"r") as fp:
                        flag=0
                        while (True):
                            t=fp.readline()
                            l=len(t)
                            if(l==0):
                                break
                            g=t.split("\t")
                            if(g[0]==search):
                                print("Name is ",g[0])
                                print("Enrollment NO is ",g[1])
                                print("Semester is ",g[2])
                                print("Branch is ",g[3])
                                print("CPI is ",g[4])
                                flag=1
                                break 
                        if(flag==0):
                                print("Record Not Found")
                    
                case 2:
                    search=input("Enter Student Enrollment No:")
                    print("\tName\t\tEnrollment No\t\tSemester\t\tBranch\t\tCPI\n")
                    with open(file_name,"r") as fp:
                        flag=0
                        while (True):
                            t=fp.readline()
                            l=len(t)
                            if(l==0):
                                break
                            g=t.split("\t")
                            if(g[1]==search):
                                print("\t"+g[0] + "\t\t" + g[1] + "\t\t" + g[2] + "\t\t" + g[3] + "\t\t" + g[4] + "\n")
                                # print("\tName is " + g[0])
                                # print("Enrollment NO is ",g[1])
                                # print("Semester is ",g[2])
                                # print("Branch is ",g[3])
                                # print("CPI is ",g[4])
                                flag=1
                                break 
                            if(flag==0):
                                print("Record Not Found")
                                
                case 3:
                    search=input("Enter Student Semester:")
                    with open(file_name,"r") as fp:
                        flag=0
                        while (True):
                            t=fp.readline()
                            l=len(t)
                            if(l==0):
                                break
                            g=t.split("\t")
                            if(g[2]==search):
                                print("Name is ",g[0])
                                print("Enrollment NO is ",g[1])
                                print("Semester is ",g[2])
                                print("Branch is ",g[3])
                                print("CPI is ",g[4])
                                flag=1
                                break 
                            if(flag==0):
                                print("Record Not Found")
                                
                                
                case 4:
                    search=input("Enter Student Branch:")
                    with open(file_name,"r") as fp:
                        flag=0
                        while (True):
                            t=fp.readline()
                            l=len(t)
                            if(l==0):
                                break
                            g=t.split("\t")
                            if(g[3]==search):
                                print("Name is ",g[0])
                                print("Enrollment NO is ",g[1])
                                print("Semester is ",g[2])
                                print("Branch is ",g[3])
                                print("CPI is ",g[4])
                                flag=1 
                            if(flag==0):
                                print("Record Not Found")
                                
                case 5:
                    search=input("Enter Student CPI:")
                    with open(file_name,"r") as fp:
                        flag=0
                        while (True):
                            t=fp.readline()
                            l=len(t)
                            if(l==0):
                                break
                            g=t.split("\t")
                            if(g[4]==search):
                                print("Name is ",g[0])
                                print("Enrollment NO is ",g[1])
                                print("Semester is ",g[2])
                                print("Branch is ",g[3])
                                print("CPI is ",g[4])
                                flag=1
                                break 
                            if(flag==0):
                                print("Record Not Found")
                
                case 6:
                    ("Not found")

        case 4:
            search=input("Enter Student Name:")
            f=open(file_name,"r")
            tt=open("temp.txt","w")
            h=0
            flag=0
            while(True):
                t=f.readline()
                l=len(t)
                if(l==0):
                    break
                g=t.split('\t')
                if(g[0]!=search):
                    tt.write(t)
                if(g[0]==search):
                    h=1
            f.close()
            tt.close()
            if(h==1):
                print("Record Deleted Successfully")
                os.remove(file_name)
                os.rename("temp.txt",file_name)
            elif(h==0):
                print("Record Not Found !! Deletion unsuccessful")
             
        case 5:
            h=0
            search=input("Enter Student Name:")
            with open(file_name,"r") as f:
                with open("temp.txt","w") as tt:
                    flag=0 
                    while(True):
                        t=f.readline()
                        l=len(t)
                        if(l==0):
                            break
                        g=t.split('\t')
                        if(g[0]==search):
                            print("Current Detial is\n",t)
                            print("-------------------------")
                            newenroll_no=input("Want to change enroll_no? Enter new detail of Press enter to continue")
                            newbranch=input("Want to change branch? Enter new detail of Press enter to continue")
                            newsemester=input("Want to change semester? Enter new detail of Press enter to continue")
                            newcpi=input("Want to change cpi? Enter new detail of Press enter to continue")
                            if(len(newenroll_no)==0):
                                newenroll_no=g[1]
                            if(len(newbranch)==0):
                                newbranch=g[2]
                            if(len(newsemester)==0):
                                newsemester=g[3]
                            if(len(newcpi)==0):
                                newcpi=g[4] 
                            tt.write(g[0]+"-"+newenroll_no+"-"+newbranch+"-"+newsemester+"-"+newcpi+"\n")
                            h=1
                        else:
                            tt.write(t)
                    if(h==1):
                        print("Record Updated Successfully")
                        os.remove(file_name)
                        os.rename("temp.txt",file_name)
                    elif(h==0):
                            print("No such Record Exist: For Updation Process")
                                        
        case 6:
            exit()                                                  
                                        

                
            