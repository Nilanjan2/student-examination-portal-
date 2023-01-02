import csv
import re
import matplotlib.pyplot as plt
import numpy as np
def new_course(course_id,course_name,marks_obtained):
    course_list=[]
    course_file=open("Course Data.csv",'r')
    course_reader=csv.reader(course_file)
    for row in course_reader:
        course_list.append(row)
    course_file.close()
    student_list=[]
    student_file=open("Student Data.csv",'r')
    student_reader=csv.reader(student_file)
    for row in student_reader:
        student_list.append(row)
    student_file.close()
    length1=len(marks_obtained["Student Name"])
    length2=len(student_list)
    stdid_marks=""
    for i in range(length1-1):
        for j in range(length2):
            if((marks_obtained["Student Name"][i]==student_list[j][1])and(marks_obtained["Roll Number"][i]==student_list[j][2])):
                std_id=student_list[j][0]
        stdid_marks=stdid_marks+std_id+":"+marks_obtained["Marks"][i]+"-"
    for j in range(length2):
        if((marks_obtained["Student Name"][length1-1]==student_list[j][1])and(marks_obtained["Roll Number"][length1-1]==student_list[j][2])):
            std_id=student_list[j][0]
    stdid_marks=stdid_marks+std_id+":"+marks_obtained["Marks"][length1-1]
    course_list.append([course_id,course_name,stdid_marks])
    course_file=open("Course Data.csv",'w',newline='')
    csvwriter=csv.writer(course_file)
    csvwriter.writerows(course_list)
    course_file.close()
def view_course(course_id,course_name):
    course_list=[]
    course_file=open("Course Data.csv",'r')
    course_reader=csv.reader(course_file)
    for row in course_reader:
        course_list.append(row)
    course_file.close()
    student_list=[]
    student_file=open("Student Data.csv",'r')
    student_reader=csv.reader(student_file)
    for row in student_reader:
        student_list.append(row)
    student_file.close()
    length=len(course_list)
    k=0
    for i in range(length):
        if((course_list[i][0]==course_id)and(course_list[i][1]==course_name)):
            stdid_marks=course_list[i][2]
            k=1
    if(k==1):
        print("Class Roll Number\tStudent Name\t\t\tMarks obtained")
        stdid_marks_list=re.split(':|-',stdid_marks)
        length1=int(len(stdid_marks_list)/2)
        length2=int(len(student_list))
        for i in range(length1):
            for j in range(length2):
                if(stdid_marks_list[2*i]==student_list[j][0]):
                    print(student_list[j][2]+"\t\t\t"+student_list[j][1]+"\t\t\t"+stdid_marks_list[2*i+1])
    else:
        print("Course Name or Course ID is incorrect or Course does not exist!")
def histogram_course(course_id,course_name):
    course_list=[]
    course_file=open("Course Data.csv",'r')
    course_reader=csv.reader(course_file)
    for row in course_reader:
        course_list.append(row)
    course_file.close()
    length=len(course_list)
    k=0
    for i in range(length):
        if((course_list[i][0]==course_id)and(course_list[i][1]==course_name)):
            stdid_marks=course_list[i][2]
            k=1
            break
    if(k==1):
        stdid_marks_list=re.split(':|-',stdid_marks)
        length1=int(len(stdid_marks_list)/2)
        a=b=c=d=e=f=0
        for i in range(length1):
            marks=int(stdid_marks_list[2*i+1])
            if(marks>=90):
                a=a+1
            elif((marks<90)and(marks>=80)):
                b=b+1
            elif((marks<80)and(marks>=70)):
                c=c+1
            elif((marks<70)and(marks>=60)):
                d=d+1
            elif((marks<60)and(marks>=40)):
                e=e+1
            elif(marks<40):
                f=f+1
        plt.bar(['A','B','C','D','E','F'],[a,b,c,d,e,f],color='blue',width=1)
        plt.title(course_id+"\nFrequency vs Grades")
        plt.xlabel("Grades")
        plt.ylabel("Frequency")
        plt.show()
    else:
        print("Course Name or Course ID is incorrect or Course does not exist!")
