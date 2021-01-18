#!/bin/python
#


#CSV: OLD Rule name, OLD VulID, OLD RulID, OLD_RulID_rule, NEW VulID, NEW RulID 
import csv
# from bs4 import beautifulsoup





csvmap  = input("Enter the CSV location")

old_check = input("Enter the old checklist location")
    
new_check = input ("Enter new checklist location")
    

# open(old_check) as oldf


    open(new_check) as newf
    
    
    #CSV input validation module
    #Checklist input validation module   

    
#read the first line and save the variables

    with open(csvmap) as csvfile:
        
        f = csv.reader(csvfile, delimiter=',')
        y = 0
        
        for row in f:
        
        
            oldRulName[y] = row[1]
            oldVulID[y] = row[2]
            oldRulID[y] = row[3]
            oldRulID_rule[y] = row[4]
            newVulID[y] = row[5]
            newRulID[y]  =row[6]
        
        
        
        #
        


        #find the rule
        
        
        
        
        

        
        #find rule
        
        #import status import comments        
        #<STATUS>NotAFinding</STATUS> <STATUS>OPEN</STATUS> <STATUS>NotReviewed</STATUS> <STATUS>NotApplicable</STATUS>
        #<COMMENTS>no IIS jk 10/27/20</COMMENTS>
        
        y++
        
        
        
 
 #set the flag associated with each 
	
	
	
	
	
	

