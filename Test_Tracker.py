#!/usr/bin/env python
# coding: utf-8

# # Test Tracker

# In[1]:


#importing modules/packages 
import csv


# In[2]:


#saves current user input to corresponding csv file.
def write_to_file(file_name, data):
    contents = []
    with open(file_name, "a+") as file:
        writer = csv.writer(file)
        writer.writerow([data])


# In[3]:


#formating the csv file beacuse its not inputing a intger as input :(
def format_data(file_name):
    container = []
    with open(file_name, "r") as file:   
        data = csv.reader(file)
        for row in data:
            try:
                num = int(row[0])
                container.append(num)
            except:
                pass
    return container


# In[9]:


# looks at highest, lowest, current and last result and compares them
def anlayse_data(file_name):
    results = format_data(file_name)
    print("This is all your results to date: ")
    print(results)

    current = results[-1]   
    print("This is your score now: ", current)
    last = results[-2]
    print("This is your previous score: ", last)
    highest = max(results)
    print("This is your highest score: ", highest)
    lowest = min(results)
    print("This is your lowest score: ", lowest)
    
    print("Let's guage your performance?")
    if current > last:
        print("Your improving,keep it up")
    elif current < last:
        print("You will need to do better next time")
    elif current == last:
        print("your score stayed the same, are revising enough")


# In[10]:


#makes sure they enter an integer
def reminders():
    print("Remember entry is a integer out of 100!")


# In[11]:


#this is where the magic happens

print("1. Maths")
print("2. Science")
print("3. English")
print("E. Exit")
subject = input("input your subject first: ")

if subject == "1":
        reminders()
        Maths = input("please enter your test result")
        print("Math Results")
        write_to_file("MathResults.csv", Maths)
        format_data("MathResults.csv")
        anlayse_data("MathResults.csv")
         #print(Maths)
elif subject == "2":
        reminders()
        Science = input("please enter your test result")
        print("Science Results")
        write_to_file("ScienceResults.csv", Science)
        format_data("ScienceResults.csv")
        anlayse_data("ScienceResults.csv")
        #print(Science)
elif subject == "3":
        reminders()
        English = input("please enter your test result")
        print("English Results")
        write_to_file("EnglishResults.csv", English)
        format_data("EnglishResults.csv")
        anlayse_data("EnglishResults.csv")
        #print(English)
elif subject == "e" or Subject == "E":
        print("program ended")
        quit()
#print(result)
#print(type(result))


# In[ ]:




