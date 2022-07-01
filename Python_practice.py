#print("Hello World")
#one = 1.5 + 2 *3
#two = 2.8 // 5-3
#three = (5+2)*3
#print(one)
#print(two)
#print(three)
#counties = ["Arapahoe",'Denver','Jefferson']
#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
   #print(counties[1])
#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
    #print("El Paso is not the list of counties.")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
 #   print(county)
#for county in counties_dict.keys():
 #   print(county)
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
 #   f"You received {candidate_votes} number of votes. "
  #  f"The total number of votes in the election was {total_votes}. "
   # f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)
# Import the datetime class from the datetime module.
import datetime as dt 
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)