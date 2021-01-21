#!/usr/bin python	


 # CSV: OLD Rule name, OLD VulID, OLD RulID, OLD_RulID_rule, NEW VulID, NEW RulID 
import csv
import xml.etree.ElementTree as ET




csvmap  = input("Enter the CSV location")

old_check = input("Enter the old checklist location")
    
new_check = input ("Enter new checklist location")
    

#with open(old_check) as oldf:
#import old XML data
oldtree = ET.parse(old_check)
rootOldTree = oldtree.getroot()

#with open(new_check) as newf:
newtree = ET.parse(new_check)
rootNewTree = newtree.getroot()
       
with open(csvmap) as csvfile:
 f = csv.reader(csvfile, delimiter=',')
 oldRulName=[]
 oldVulID=[]
 oldRulID=[]
 oldRulID_rule=[]
 newVulID=[]
 newRulID=[]
 y=0

 for row in f:
        
        
  oldRulName.append(row[0])
  oldVulID.append(row[1])
  oldRulID.append(row[2])
  oldRulID_rule.append(row[3])
  newVulID.append(row[4])
  newRulID.append(row[5])        	 
  #print(oldVulID[y])
  #y +=1





 
for child in rootOldTree.iter():
 for vulID in oldVulID:
  if child.text == vulID:
  #is there a way to call the array position of this match?
  #save array position
  #find the next status
  #capture the next status
  #capture the comments
   
 

 
 # for oldVul in oldVulID:
 
 # print(rootOldTree.tag)

 # for stig in rootOldTree.find('VULN'):
 # print(stig.attrib)
 # if attribute_Data == oldrul:
 # print(oldVul)
        
          
        
        

        
    # find rule
        
    # import status import comments        
    # <STATUS>NotAFinding</STATUS> <STATUS>OPEN</STATUS> <STATUS>NotReviewed</STATUS> <STATUS>NotApplicable</STATUS>
    # <COMMENTS>no IIS jk 10/27/20</COMMENTS>
     
        
    
    #may need to strip some data
    # print(oldRulName)   
    #    with open(old_check) as oldreader

    #  with open(new_check) as newreader
    
    #  for indID in oldVulID
     
       #search for old tags
        
       #        #captureold data
       #        oStatus = 
       #        oComments = fin
        
        #write to new data
        
    
        


            
 
# set the flag associated with each 
	
	
	
	

