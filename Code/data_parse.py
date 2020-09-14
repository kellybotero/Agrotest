# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:23:49 2020

@author: kelly
"""

import pandas as pd

def elementexist(array,element):
    for value in array:
        if value==element:
            return(True)
    return(False)        
                   
def parse_row_firts_condition(data,namecols,conditions):
    arrayrows=[]
    arrayindex=[]
    for index,row in data.iterrows() :
        for namecol in namecols:
            for condition in conditions:
                if row[namecol]==condition:
                    if elementexist(arrayindex,index)==False:
                        arrayrows.append(row)
                        arrayindex.append(index)
    return(arrayrows)                         
                   
def parse_row_second_condition(data,namecols,conditions):
    arrayrows=[]
    arrayindex=[]
    for index,row in data.iterrows() :
        for namecol in namecols:
            for condition in conditions:
                if row[namecol]>=condition:
                    if elementexist(arrayindex,index)==False:
                        arrayrows.append(row)
                        arrayindex.append(index)
    return(arrayrows)                         
                       
def parse_row_third_condition(data,namecols,conditions):
    arrayrows=[]
    arrayindex=[]
    for index,row in data.iterrows() :
        for namecol in namecols:
            for condition in conditions:
                if str(row[namecol]).find(condition)>-1:
                    if elementNCBI(row[namecol]):
                        if elementexist(arrayindex,index)==False:
                            arrayrows.append(row)
                            arrayindex.append(index)
    return(arrayrows)  

                   
def parseCol(data,suffix):  
    arrayCol=[]
    for col in data.columns:        
        if col.find(suffix)>-1:
           arrayCol.append(col)
    return(arrayCol)

def elementNCBI(element):
    for index,row in NCBI_file.iterrows():
        if element.find(row['refseq_nucleotide_accession'])>-1:
            if row['subclass']== 'CEPHALOSPORIN' or row['subclass']== 'CARBAPENEM':
                return(True)
    return(False) 

archivo1 = pd.read_csv("C:\\Users\\kelly\\Documents\\Agrosavia\\Prueba técnica\\Pruebba2\\exercise_2_ariba_amr_output.csv")
NCBI_file=pd.read_csv("C:\\Users\\kelly\\Documents\\Agrosavia\\Prueba técnica\\Pruebba2\\exercise_2_ncbi_acquired_genes_metadata.csv")


#Evaluation of firts condition

colsuffix='.assembled'

arrayAssembled=parseCol(archivo1,colsuffix)

rowconditions1=parse_row_firts_condition(archivo1,arrayAssembled,['yes','yes_nonunique'])


rowconditions1=pd.DataFrame(rowconditions1,columns=archivo1.columns)

#Evaluation second conditions

colsuffix1='.ctg_cov'
array_ctg_cov=parseCol(rowconditions1,colsuffix1)


rowconditions2=parse_row_second_condition(archivo1,array_ctg_cov,[10])
rowconditions2=pd.DataFrame(rowconditions2,columns=archivo1.columns)



#Evaluation third conditions
colsuffix1='.ref_seq'
array_ref_seq=parseCol(rowconditions2,colsuffix1)

rowconditions3=parse_row_third_condition(archivo1,array_ref_seq,['NG_'])

rowconditions3=pd.DataFrame(rowconditions3,columns=archivo1.columns)

print(rowconditions3)

#NCBI metada

