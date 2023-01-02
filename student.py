import csv
import re
import matplotlib.pyplot as plt
import numpy as np
def new_student(student_id,name,class_roll_no,batch_id):
    student_list=[]
    student_file=open("Student Data.csv",'r')
    student_reader=csv.reader(student_file)
    for row in student_reader:
        student_list.append(row)
    student_file.close()
    l=[student_id,name,class_roll_no,batch_id]
    student_list.append(l)
    student_file=open("Student Data.csv",'w',newline='')
    csvwriter=csv.writer(student_file)
    csvwriter.writerows(student_list)
    student_file.close()
    print("New Student added!")
def update_student(student_id,name,class_roll_no,batch_id):
    student_list=[]
    student_file=open("Student Data.csv",'r')
    student_reader=csv.reader(student_file)
    for row in student_reader:
        student_list.append(row)
    student_file.close()
    length=len(student_list)
    k=0
    for i in range(length):
        if(student_list[i][0]==student_id):
            student_list[i]=[student_id,name,class_roll_no,batch_id]
            student_file=open("Student Data.csv",'w',newline='')
            csvwriter=csv.writer(student_file)
            csvwriter.writerows(student_list)
            student_file.close()
            k=1
            print("Student details updated!")
    if(k==0):
        print("Student Not Found!")
def remove_student(student_id,name,class_roll_no,batch_id):
    student_list=[]
    student_file=open("Student Data.csv",'r')
    student_reader=csv.reader(student_file)
    for row in student_reader:
        student_list.append(row)
    student_file.close()
    n=len(student_list)
    k=0
    for i in range(n):
        if(student_list[i][0]==student_id):
            student_list.remove([student_id,name,class_roll_no,batch_id])
            k=1
            print("Student removed!")
            break
    if(k==0):
        print("Student Not Found!")
    else:
        student_file=open("Student Data.csv",'w',newline='')
        csvwriter=csv.writer(student_file)
        csvwriter.writerows(student_list)
        student_file.close()
def result_student(student_id,name,class_roll_no,batch_id):
    student_list=[]
    student_file=open("Student Data.csv",'r')
    student_reader=csv.reader(student_file)
    for row in student_reader:
        student_list.append(row)
    student_file.close()
    n=len(student_list)
    k=0
    for i in range(n):
        if(student_list[i][0]==student_id):
            k=1
            batch_id=student_list[i][3]
            name=student_list[i][1]
            class_roll_no=student_list[i][2]
            break
    if(k==1):
        batch_list=[]
        batch_file=open("Batch Data.csv",'r')
        batch_reader=csv.reader(batch_file)
        for row in batch_reader:
            batch_list.append(row)
        batch_file.close()
        length1=len(batch_list)
        course_list=[]
        course_file=open("Course Data.csv",'r')
        course_reader=csv.reader(course_file)
        for row in course_reader:
            course_list.append(row)
        course_file.close()
        result_file=open(student_id+'_result.txt','w')
        totmarks=0
        for i in range(length1):
            if(batch_list[i][0]==batch_id):
                result_file.write("Student ID: "+student_id+"\tName: "+name+"\tClass Roll Number: "+class_roll_no+"\tBatch name: "+batch_list[i][1]+"\n")
                result_file.write("COURSE ID\tCOURSE NAME\t\t\tGRADES\n\n") 
                crse_liststr=batch_list[i][3]
                crse_list=re.split(':',crse_liststr)
                length2=len(crse_list)
                length3=len(course_list)
                for j in range(length2):
                    for m in range(length3):
                        if(crse_list[j]==course_list[m][0]):
                            stdid_marksstr=course_list[m][2]
                            stdid_markslist=re.split(':|-',stdid_marksstr)
                            length4=len(stdid_markslist)
                            marks=0
                            for n in range(length4):
                                if(stdid_markslist[n]==student_id):
                                    marks=int(stdid_markslist[n+1])
                                    break
                            if(marks>=90):
                                grade='A'
                            elif((marks>=80)and(marks<90)):
                                grade='B'
                            elif((marks>=70)and(marks<80)):
                                grade='C'
                            elif((marks>=60)and(marks<70)):
                                grade='D'
                            elif((marks>=40)and(marks<60)):
                                grade='E'
                            elif(marks<40):
                                grade='F'
                            result_file.write(course_list[m][0]+"\t\t"+course_list[m][1]+"\t\t\t"+grade+"\n")
                            totmarks=totmarks+marks
                result_file.write("\n")
                percentage=totmarks/length2
                result_file.write("PERCENTAGE: "+str(percentage)+"%\n")
                if(percentage>40):
                    result_file.write("PASS STATUS: PASSED")
                else:
                    result_file.write("PASS STATUS: FAILED")
        result_file.close()
        print("Result generated with the name: ",(student_id+'_result.txt'))
    else:
        print("Incorrect details!")
