# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 02:11:06 2023

@author: Simas Simanavicius
Simas@simsim.lt
"""
import os

#left
db1 = "c:/db/sdb"
db1data = db1+"/0-9999"
#right
db2 = "c:/db/db2"
db2data = db2+"/0-9999"
#output
db3 = "c:/db/db1"
db3data = db3+"/0-9999"

a = 0
b = 99
c = 0 #lasst entry in main DB

mainsize = len(os.listdir(db1data))
secondary_size = len(os.listdir(db2data))

dataset = [] #main DB 
dataset2 = [] #secondary DB

# get sub-folder names and store in list    
for i in range(mainsize): 
    dataset.append(str(a)+"-"+str(b))
    a = a+100
    b = b+100

#get last entry in main DB
c = a-100 + len(os.listdir(db1data+"/"+dataset[-1]))

for i in range(secondary_size): # cycle for all folders in DB
    for x in os.listdir(os.path.join(db2data+"/"+dataset[i])):
        print(x)
        if x < str(c):
            print("need to change name")


#how many items is in the last set of entries
print("Last sub-folder has " + str(len(os.listdir(db1data+"/"+dataset[-1]))) + " entries")
#print("Last sub-folder has " + str(len(os.listdir(db2data+"/"+dataset2[-1]))) + " entries")

# List all files in a directory using os.listdir
"""
for a in os.listdir(db1data):
    if os.path.isdir(os.path.join(db1data, a)):
        print(a)
        print(len(os.listdir(db1data))) #how many entries in dir
        
        for i in os.listdir(db1data+"/"+a):
            if os.path.isdir(os.path.join(db1data+"/"+a)):
                print(len(os.listdir(db1data+"/"+a))) #how many entries in sub-dir
"""
print("last entry in db is: " + str(c))
print(dataset)
print(dataset2)

