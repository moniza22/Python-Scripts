#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 23:10:28 2022

@author: monizanaseem
"""

import csv
import pandas as pd

data_row1=[0,1,0]
new_row=[0.4,0.5,0.6]


filepath= ''
input_variables=['Param: flagAddWorkers 0','Param: flagCons 0','Param: flagExpect 0']

size=len(input_variables)
print(size)

for variable in input_variables:
    
    with open(filepath,'r') as f:
        found=False    
        for line in f:
            if  variable in line:
                print("parameter exist in file.")
                print(line)
                
                found=True
        if not found:
            print("parameter doesnot exist")
  
with open('oldfile.csv', 'w') as f: 
    my_writer=csv.writer(f)
    my_writer.writerow(input_variables)
    my_writer.writerow(data_row1)
    my_writer.writerow(new_row)
    
 # reading the csv file for changes and creating new corresponding lsd file 
filepath_new=''
replacement_lines=[] 
input_lines=[]
import shutil
input_variables=['Param: flagAddWorkers 0','Param: flagCons 0','Param: flagExpect 0']    
df=pd.read_csv('oldfile.csv')
new_row=df.iloc[-1]
new_list=[]
for i in new_row:
     new_list.append(i)
print(new_list)

if new_list != data_row1:
    
         print('New values for parameters added')
         
         with open(filepath) as infile:
             with open(filepath_new, 'w+') as outfile:
             
             
                 shutil.copy(filepath,filepath_new)
                 f=outfile.readlines()
             
             
                 for k in range(0,len(input_variables)):
                 
                 
                     for line in f:
                     
                         if input_variables[k] in line:
                            
                            input_lines.append(line)
                            line = line.replace(line[-4:-1],' '+str(new_list[k]))
                            replacement_lines.append(line)

                 print(input_lines)
                 print(replacement_lines) 
                 
replacements = {input_lines[k]:replacement_lines[k] for k in range(0,len(input_variables))}   
with open(filepath) as infile, open(filepath_new, 'w') as outfile:
    
    for line in infile:
            for src, trg in replacements.items():
                
                line = line.replace(src, trg)
            outfile.write(line)              
                 
             