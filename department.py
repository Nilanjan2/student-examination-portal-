import csv
import re
import matplotlib.pyplot as plt
import numpy as np
def new_department(department_id,department_name,department_batchlist):
    department_list=[]
    department_file=open("Department Data.csv",'r')
    department_reader=csv.reader(department_file)
    for row in department_reader:
        department_list.append(row)
    department_file.close()
    length=len(department_batchlist)
    department_batchstr=""
    if(length!=0):
        for i in range(length-1):
            department_batchstr=department_batchstr+department_batchlist[i]+":"
        department_batchstr=department_batchstr+department_batchlist[length-1]
    department_list.append([department_id,department_name,department_batchstr])
    department_file=open("Department Data.csv",'w',newline='')
    csvwriter=csv.writer(department_file)
    csvwriter.writerows(department_list)
    department_file.close()
def viewbatch_department(department_id):
    department_list=[]
    department_file=open("Department Data.csv",'r')
    department_reader=csv.reader(department_file)
    for row in department_reader:
        department_list.append(row)
    department_file.close()
    length=len(department_list)
    k=0
    for i in range(length):
        if(department_id==department_list[i][0]):
            department_batchstr=department_list[i][2]
            k=1
    if(k==1):
        department_batchlist=re.split(':',department_batchstr)
        batch_list=[]
        batch_file=open("Batch Data.csv",'r')
        batch_reader=csv.reader(batch_file)
        for row in batch_reader:
            batch_list.append(row)
        batch_file.close()
        length1=len(department_batchlist)
        length2=len(batch_list)
        print("Batch ID\tBatch Name")
        for i in range(length1):
            for j in range(length2):
                if(department_batchlist[i]==batch_list[j][0]):
                    print(batch_list[j][0]+"\t\t"+batch_list[j][1])
    else:
        print("Department ID is incorrect or the Department does not exist!")
def avgperformance_department(department_id):
    department_list=[]
    department_file=open("Department Data.csv",'r')
    department_reader=csv.reader(department_file)
    for row in department_reader:
        department_list.append(row)
    department_file.close()
    length=len(department_list)
    k=0
    for i in range(length):
        if(department_id==department_list[i][0]):
            department_batchstr=department_list[i][2]
            k=1
    if(k==1):
        department_batchlist=re.split(':',department_batchstr)
        batch_list=[]
        batch_file=open("Batch Data.csv",'r')
        batch_reader=csv.reader(batch_file)
        for row in batch_reader:
            batch_list.append(row)
        batch_file.close()
        length1=len(department_batchlist)
        length2=len(batch_list)
        print("Batch ID\tBatch Name\t\tBatch average performance")
        for i in range(length1):
            for j in range(length2):
                if(department_batchlist[i]==batch_list[j][0]):
                    batch_coursestr=batch_list[j][3]
                    batch_courselist=re.split(':',batch_coursestr)
                    course_list=[]
                    course_file=open("Course Data.csv",'r')
                    course_reader=csv.reader(course_file)
                    for row in course_reader:
                        course_list.append(row)
                    course_file.close()
                    length3=len(batch_courselist)
                    length4=len(course_list)
                    totbatchmarks=0
                    for m in range(length3):
                        for n in range(length4):
                            if(batch_courselist[m]==course_list[n][0]):
                                totmarks=0
                                stdid_marksstr=course_list[n][2]
                                stdid_markslist=re.split(':|-',stdid_marksstr)
                                length5=len(stdid_markslist)
                                h=0
                                avgcoursemarks=0
                                for o in range(int(length5/2)):
                                    if(str(batch_list[j][0])==str(stdid_markslist[2*o][0:5])):
                                        totmarks=totmarks+int(stdid_markslist[2*o+1])
                                        h=h+1
                                if(h!=0):
                                    avgcoursemarks=totmarks/h
                                totbatchmarks=totbatchmarks+avgcoursemarks
                    avgbatchmarks=totbatchmarks/length3
                    print(batch_list[j][0]+"\t\t"+batch_list[j][1]+"\t\t"+str(avgbatchmarks))
    else:
        print("Department ID is incorrect or the Department does not exist!")
def lineplot_department(department_id):
    department_list=[]
    department_file=open("Department Data.csv",'r')
    department_reader=csv.reader(department_file)
    for row in department_reader:
        department_list.append(row)
    department_file.close()
    length=len(department_list)
    k=0
    for i in range(length):
        if(department_id==department_list[i][0]):
            department_batchstr=department_list[i][2]
            k=1
    if(k==1):
        bach=[]
        avgperf=[]
        department_batchlist=re.split(':',department_batchstr)
        batch_list=[]
        batch_file=open("Batch Data.csv",'r')
        batch_reader=csv.reader(batch_file)
        for row in batch_reader:
            batch_list.append(row)
        batch_file.close()
        length1=len(department_batchlist)
        length2=len(batch_list)
        for i in range(length1):
            for j in range(length2):
                if(department_batchlist[i]==batch_list[j][0]):
                    batch_coursestr=batch_list[j][3]
                    batch_courselist=re.split(':',batch_coursestr)
                    course_list=[]
                    course_file=open("Course Data.csv",'r')
                    course_reader=csv.reader(course_file)
                    for row in course_reader:
                        course_list.append(row)
                    course_file.close()
                    length3=len(batch_courselist)
                    length4=len(course_list)
                    totbatchmarks=0
                    for m in range(length3):
                        for n in range(length4):
                            if(batch_courselist[m]==course_list[n][0]):
                                totmarks=0
                                stdid_marksstr=course_list[n][2]
                                stdid_markslist=re.split(':|-',stdid_marksstr)
                                length5=len(stdid_markslist)
                                h=0
                                avgcoursemarks=0
                                for o in range(int(length5/2)):
                                    if(str(batch_list[j][0])==str(stdid_markslist[2*o][0:5])):
                                        totmarks=totmarks+int(stdid_markslist[2*o+1])
                                        h=h+1
                                if(h!=0):
                                    avgcoursemarks=totmarks/h
                                totbatchmarks=totbatchmarks+avgcoursemarks
                    avgbatchmarks=totbatchmarks/length3
                    bach.append(batch_list[j][1])
                    avgperf.append(avgbatchmarks)
        plt.plot(np.array(bach),np.array(avgperf))
        plt.xlabel("Batch")
        plt.ylabel("Average Performance")
        plt.show()
    else:
        print("Department ID is incorrect or the Department does not exist!")
