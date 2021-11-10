# Haroon Malik
# Parse Eric File

inputFile=open("c://temp//comments.csv") # Subedi you can change the path for the inputfile based on your machine
outputFile=open("c://temp//comments_file.txt", "a") # Subedi you can change the path for the onputfile based on your machine
Clean_File=[] # List that will contain all the comments
for line in inputFile:
    line1=line.strip()
    line1=line1.split(';') # Splitting the line based on ; as delimiter
    #print(line1)
    Clean_File.append(line1[4]) # i looked in to the Eric file and found that Comments are in the 4th Column
#print(len(Clean_File)) # Debug statement to ensure that the length of the items in list are same as that of the lines in file. [Disabled]

for item in Clean_File:  # Iterating through the list
    outputFile.write("%s\n" % item) Coverting the line into string add adding 'newline' as escape sequence to the line. Also wrinting it to a file
inputFile.close() 
outputFile.close()
  
    
    
