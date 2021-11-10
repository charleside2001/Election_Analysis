print("Hello World!")
#counties = ["Arapahoe","Denver","Jefferson"]
#counties.append("El Paso")
#counties.insert(2, "El Paso")
#counties.remove("El Paso")
#counties.pop(3)
#print(counties)
#counties[2] = "El Paso"
#print(counties)
#my_tuple = tuple()
#print(my_tuple)
#counties_tuple = ("Arapahoe","Denver","Jefferson")
#print(counties_tuple)
#print(len(counties_tuple))
#print(counties_tuple[:-1])

#Dictionaries
my_dictionary = {}
my_dictionary = dict()
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print(counties_dict['Arapahoe'])

#Voting exercise
#voting_data = []
#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#voting_data.append({"county":"Denver", "registered_voters": 463353})
#voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#print(voting_data)

#List
#n = [2, 4, 6, 8]
#res = 1
#for x in n[1:3]:
#  res *= x
#rint(res)
#algorithm that calculates the percentage of votes a candidate receives in an election - muted
# How many votes did you get?
#my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
#total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")
# Conditional Statements
#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
#    print(counties[1])
# If-Else Statements
#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
#    print("Turn on the AC.")
#else:
#    print("Open the windows.")
# Nested Loop - If-Else Statements
#What is the score?

# Determine the grade.
#score = int(input("What is your test score? "))
#if score >= 90:
#   print('Your grade is an A.')
#else:
 #   if score >= 80:
 #       print('Your grade is a B.')
 #   else:
  #      if score >= 70:
 #           print('Your grade is a C.')
 #       else:
  #          if score >= 60:
  #              print('Your grade is a D.')
 #           else:
  #              print('Your grade is an F.')

# What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
#if score >= 90:
#    print('Your grade is an A.')
#elif score >= 80:
 #   print('Your grade is a B.')
#elif score >= 70:
 #   print('Your grade is a C.')
#elif score >= 60:
 #   print('Your grade is a D.')
#else:
 #   print('Your grade is an F.')

# Membership Operators - in and not in
#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
 #   print("El Paso is in the list of counties.")
#else:
 #   print("El Paso is not the list of counties.")

# Logical Operators
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

    
# 3.2.10 Repetition Statements to retrieve data to complete the audit
    # This type of repetition structure is called a loop
    #While Loop
x = 0
while x <= 5:
    print(x)
    x = x + 1

    #For Loops
for county in counties:
    print(county)

    numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

# Iterate Through a Dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    # Get the Keys of a Dictionary
for county in counties_dict:
    print(county)

#  use the keys() method to iterate over a dictionary
for county in counties_dict.keys():
    print(county)

# Get the Values of a Dictionary
for voters in counties_dict.values():
    print(voters)

# using the format dictionary_name[key]
for county in counties_dict:
    print(counties_dict[county])

# Using Get
for county in counties_dict:
    print(counties_dict.get(county))
    
# Get the Key-Value Pairs of a Dictionary    
for county, voters in counties_dict.items():
    print(county, voters)
    
# Iterate Through a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
    
    
# Get the Values from a List of Dictionaries

    