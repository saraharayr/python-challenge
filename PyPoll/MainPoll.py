# import dependencies
import csv , os 

#create path to file
election_data = "/Users/saraharayratti/Desktop/python-challenge/PyPoll/Resources/election_data.csv"

#Variables
voter_number = []
candidates = []

#Open file as csv
with open(election_data ,newline= '') as csvfile:
   
   electioncsv = csv.reader(csvfile, delimiter = ',')
   print(electioncsv)   
   for column in electioncsv:
       voter_number.append(column[0])
       candidates.append(column[2])
       
      
   #Vote numbers
   Total_Votes = (len(voter_number))
   print(f"Total Votes: {Total_Votes}")
   
   #Total number of candidates
   Khan = int(candidates.count("Khan"))
   Correy = int(candidates.count("Correy"))
   Li = int(candidates.count("Li"))
   O_Tooley = int(candidates.count("O'Tooley"))
  
   #Vote percentage per candidate
   Correy_percentage = (Correy/Total_Votes) * 100
   Khan_percentage = (Khan/Total_Votes) * 100
   O_Tooley_percentage = (O_Tooley/Total_Votes) * 100
   Li_percentage = (Li/Total_Votes) * 100

   
   #Print each candidate's name
   print(f"Correy: {Correy_percentage}% ({Correy})")
   print(f"Khan: {Khan_percentage}% ({Khan})")
   print(f"Li: {Li_percentage}% ({Li})")
   print(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley})")
   
   #Candidate with most votes
   if Khan > Correy > Li > O_Tooley:
       Winner = "Khan"
   elif Correy > Khan > Li > O_Tooley:
       Winner = "Correy"
   elif Li > Khan > Correy > O_Tooley:
       Winner = "Li"
   elif O_Tooley > Khan > Correy > Li:
       Winner = "O'Tooley"
   print(f"Winner: {Winner}")
   
   #Create a path to a txt file and export it
   
   analysispolltxt = "/Users/saraharayratti/Desktop/python-challenge/PyPoll/Analysis/electionanalysis.txt"
   
   with open(analysispolltxt, "w") as txt_file:
       
       txt_file.write(f"Total Votes: {Total_Votes}")
       txt_file.write(f"Khan: {Khan_percentage}% ({Khan})")
       txt_file.write(f"Correy: {Correy_percentage}% ({Correy})")
       txt_file.write(f"Li: {Li_percentage}% ({Li})")
       txt_file.write(f"O'Tooley: {O_Tooley_percentage}% ({Correy})")
       txt_file.write(f"Winner: {Winner}")
       txt_file.close()
    




