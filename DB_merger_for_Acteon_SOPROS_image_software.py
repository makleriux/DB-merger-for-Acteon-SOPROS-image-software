# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 02:11:06 2023

@author: makle
"""
import os

#Should be promt in the future or make IDE
#main DB
db1 = "c:/db/sdb"
db1data = db1+"/0-9999"

#secondary DB
db2 = "c:/db/db2"
db2data = db2+"/0-9999"

a = 0
b = 99
c = 0 #lasst entry in main DB

mainsize = len(os.listdir(db1data))
secondary_size = len(os.listdir(db2data))

dataset = [] #main DB how many sets are in DB 0-99, 100-199 etc

# get sub-folder names and store in list as datasets
for i in range(mainsize): 
    dataset.append(str(a)+"-"+str(b))
    a = a+100
    b = b+100

#get next entry in main DB to make
c = a-100 + len(os.listdir(db1data+"/"+dataset[-1]))

#rename elements to be ready be moved into new DB 
for i in range(secondary_size): # cycle for all folders in DB
    print(os.path.join(db2data+"/"+dataset[i]))
    os.chdir(os.path.join(db2data+"/"+dataset[i]))
    for x in os.listdir(os.path.join(db2data+"/"+dataset[i])):
        print("current name", x)
        os.rename(str(x),str(c))
        print("name changed to:", c)
        c=c+1
        


#how many items is in the last set of entries
#print("Last sub-folder has " + str(len(os.listdir(db1data+"/"+dataset[-1]))) + " entries")
