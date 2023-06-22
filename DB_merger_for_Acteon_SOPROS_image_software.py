# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 02:11:06 2023

@author: Simas Simanavicius
simas@simsim.lt

not implemented:
calculate total indexes in both DB and create sets in DB nr.1
change path for os.rename to move new indexes into DB nr.1
GUI with TKinter???
"""
import os

#Should be promt in the future or make IDE

#main DB path
db1 = "c:/db/sdb"
db1data = db1+"/0-9999"

#secondary DB path
db2 = "c:/db/db2"
db2data = db2+"/0-9999"

a = 0
b = 99
c = 0 #lasst entry in main DB

def db_size (path):
    size = len(os.listdir(a))
    return size

def db_dataset_calc (size):
    temp_set = []
    a = 0
    b = 99
    for i in range(a):
        temp_set.append(str(a)+"-"+str(b))
        a = a+100        
        b = b+100
    return temp_set

#rename it!!
mainsize = db_size(db1data)
secondary_size = db_size(db2data)

dataset = db_dataset_calc(mainsize) #main DB how many sets are in DB 0-99, 100-199 etc
dataset_merged = db_dataset_calc(mainsize+secondary_size)
# POP to remove existin folders

#get next entry in main DB to make
c = a-100 + len(os.listdir(db1data+"/"+dataset[-1]))

#rename elements to be ready be moved into new DB 
for i in range(secondary_size): # cycle for all folders in DB
    print(os.path.join(db2data+"/"+dataset[i]))
    os.chdir(os.path.join(db2data+"/"+dataset[i]))
    for x in os.listdir(os.path.join(db2data+"/"+dataset[i])):
        print("current name", x)
        # if str(c)[0] == dataset[i[1]]:
            #change str(c) to path of Db.1+dataset[i]+str(c)
        #else
            #os.mkdir()
        os.rename(str(x),str(c))
        print("name changed to:", c)
        c=c+1
        


#how many items is in the last set of entries
#print("Last sub-folder has " + str(len(os.listdir(db1data+"/"+dataset[-1]))) + " entries")
