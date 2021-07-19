# --------------

#1 we are creating a new register by combining data from two classes while making some modifications to the register.

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class=class_1+class_2
print(new_class)

#2 we might have missed a student whose name is Peter Warden. Let's add him in the new register. 

# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)

#3 It seems like there could also be a wrong entry in the list whose name is Carla Gentry. Let's remove her from the register.

# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)

#4  creating a dictionary for Geoffrey Hinton in each subject to generate his progress report. 

# Create the Dictionary
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
print(courses)

# Slice the dict and stores  the all subjects marks in variable
print(courses.values())

# Store the all the subject in one variable `Total`
total=65+70+80+70+60

# Print the total
print(total)

# Insert percentage formula
percentage=(total/500)*100

# Print the percentage
print(percentage)

#5  For the student who got the highest marks in this subject, the school has decided to award a scholarship.

# Let's check who performed best in mathematics from all the students who appeared for the test. 

# Create the Dictionary
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':65,'Peter Warden':75}

#student with the highest marks in Mathematics - 'topper'
topper = max(mathematics,key = mathematics.get)

print (topper)

#6 we know who is the 'Maths' topper in the class. 

#We have to print the name of the student on the certificate, but you will have to print his last name and then his first name. 

# Given string
topper='Andrew Ng'

# Create variable first_name 
first_name=topper.split()[0]

# Create variable Last_name and store last two element in the list
Last_name=topper.split()[1]

# Concatenate the string
full_name=Last_name+' '+first_name

# print the full_name
print(full_name)

# print the name in upper case
certificate_name=full_name.upper()

print(certificate_name)


