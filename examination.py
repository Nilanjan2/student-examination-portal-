import csv
import re
import matplotlib.pyplot as plt
import numpy as np
def exam(crse_name,std_list):
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
    length1=len(std_list)
    length2=len(course_list)
    length3=len(student_list)
    e=0
    for i in range(length2):
        if (crse_name==course_list[i][1]):
            stdid_marksstr=course_list[i][2]
            stdid_markslist=re.split(':|-',stdid_marksstr)
            length4=len(stdid_markslist)
            for j in range(length1):
                for m in range(length3):
                    if((std_list[j][0]==student_list[m][2])and(std_list[j][1]==student_list[m][1])):
                        k=0
                        for n in range(length4):
                            if (stdid_markslist[n]==student_list[m][0]):
                                stdid_markslist[n+1]=std_list[j][2]
                                k=1
                        if(k==0):
                            stdid_markslist.append(student_list[m][0])
                            stdid_markslist.append(std_list[j][2])
            stdid_marksstr=''
            length6=len(stdid_markslist)
            for h in range(int(length6/2)-1):
                stdid_marksstr=stdid_marksstr+stdid_markslist[2*h]+':'+stdid_markslist[2*h+1]+'-'
            stdid_marksstr=stdid_marksstr+stdid_markslist[length6-2]+':'+stdid_markslist[length6-1]
            course_list[i][2]=stdid_marksstr
            course_file=open("Course Data.csv",'w',newline='')
            csvwriter=csv.writer(course_file)
            csvwriter.writerows(course_list)
            course_file.close()
            e=1
    if(e==0):
        print("Course does not exist!")
def view_exam(year):
    batch_list=[]
    batch_file=open("Batch Data.csv",'r')
    batch_reader=csv.reader(batch_file)
    for row in batch_reader:
        batch_list.append(row)
    batch_file.close()
    length=len(batch_list)
    print("Student ID\tClass Roll Number\tStudent Name\tPercentage Obtained")
    for i in range(length):
        if(batch_list[i][0][3:5]==year[2:4]):
            std_liststr=batch_list[i][4]
            crse_liststr=batch_list[i][3]
            std_list=re.split(':',std_liststr)
            student_list=[]
            student_file=open("Student Data.csv",'r')
            student_reader=csv.reader(student_file)
            for row in student_reader:
                student_list.append(row)
            student_file.close()
            crse_list=re.split(':',crse_liststr)
            course_list=[]
            course_file=open("Course Data.csv",'r')
            course_reader=csv.reader(course_file)
            for row in course_reader:
                course_list.append(row)
            course_file.close()
            length1=len(std_list)
            length2=len(student_list)
            length3=len(crse_list)
            length4=len(course_list)
            for j in range(length1):
                for m in range(length2):
                    if(std_list[j]==student_list[m][0]):
                        totmarks=0
                        for p in range(length3):
                            for n in range(length4):
                                if(crse_list[p]==course_list[n][0]):
                                    stdid_marks_list=re.split(":|-",course_list[n][2])
                                    length5=len(stdid_marks_list)
                                    for o in range(length5):
                                        if(student_list[m][0]==stdid_marks_list[o]):
                                            totmarks=totmarks+int(stdid_marks_list[o+1])
                        percentage=totmarks/length3
                        print(student_list[m][0]+"\t\t"+student_list[m][2]+"\t\t\t"+student_list[m][1]+"\t\t"+str(percentage))
def scatterplot_exam(year):
    batch_list=[]
    batch_file=open("Batch Data.csv",'r')
    batch_reader=csv.reader(batch_file)
    for row in batch_reader:
        batch_list.append(row)
    batch_file.close()
    length=len(batch_list)
    colors=np.array(["red","salmon","pink","violet","blue","yellow","turquoiseblue","silver","sgiteal","slategray3","brown","rosybrown","purple4","limegreen","banana","tomato3","thistle1","mint","mediumslateblue","aqua"])
    for i in range(length):
        if(batch_list[i][0][3:5]==year[2:4]):
            std_liststr=batch_list[i][4]
            crse_liststr=batch_list[i][3]
            std_list=re.split(':',std_liststr)
            student_list=[]
            student_file=open("Student Data.csv",'r')
            student_reader=csv.reader(student_file)
            for row in student_reader:
                student_list.append(row)
            student_file.close()
            crse_list=re.split(':',crse_liststr)
            course_list=[]
            course_file=open("Course Data.csv",'r')
            course_reader=csv.reader(course_file)
            for row in course_reader:
                course_list.append(row)
            course_file.close()
            length1=len(std_list)
            length2=len(student_list)
            length3=len(crse_list)
            length4=len(course_list)
            bach=[]
            mrks=[]
            for j in range(length3):
                bach.append([])
                mrks.append([])
            for j in range(length1):
                for p in range(length2):
                    if(std_list[j]==student_list[p][0]):
                        for m in range(length3):
                            for n in range(length4):
                                if(crse_list[m]==course_list[n][0]):
                                    stdid_marks_list=re.split(":|-",course_list[n][2])
                                    length5=len(stdid_marks_list)
                                    for o in range(length5):
                                        if(student_list[p][0]==stdid_marks_list[o]):
                                            bach[m].append(batch_list[i][0])
                                            mrks[m].append(int(stdid_marks_list[o+1]))
            for i in range(length3):
                x=np.array(mrks[i])
                y=np.array(bach[i])
                plt.scatter(x,y,c=colors[i])
    plt.xlabel("Marks")
    plt.ylabel("Batch")
    plt.show()
