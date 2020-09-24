import re
# import xlsxwriter module 
import xlsxwriter 

workbook = xlsxwriter.Workbook("E:\\ResumeBuilding ML\\CV-all\\CVs Batch of 2017 IITDelhi\\Example.xlsx") 
worksheet = workbook.add_worksheet() 

# Start from the first cell. 
# Rows and columns are zero indexed. 


# iterating through content list 

	

import os
i=1
for filename in os.listdir("E:\\ResumeBuilding ML\\CV-all\\CVs Batch of 2017 IITDelhi"):
	if(filename[-4::]==".txt"):
		try:
			a=open("E:\\ResumeBuilding ML\\CV-all\\CVs Batch of 2017 IITDelhi\\"+str(filename))
			
			for line in a:
				x=re.findall('[0-9]\.[0-9][0-9][0-9]',line)
				
				if(len(x)):
					print(str(filename)[:-4])
					print(x)
					break
			if(len(x)!=0):
				worksheet.write(i,1,str(filename)[:-4])
				worksheet.write(i,2,x[0])

			i+=1
		except:
			try:
				a=open("E:\\ResumeBuilding ML\\CV-all\\CVs Batch of 2017 IITDelhi\\"+str(filename))
				
				for line in a:
					x=re.findall('[0-9]\.[0-9][0-9]',line)
					
					if(len(x)):
						print(str(filename)[:-4])
						print(x)
						break
				if(len(x)!=0):
					worksheet.write(i,1,str(filename)[:-4])
					worksheet.write(i,2,x[0])

				i+=1
			except:
				continue
workbook.close() 