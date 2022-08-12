#!/usr/bin/env python
# coding: utf-8

# In[2]:


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# In[3]:


# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


# In[4]:


#Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded".
#Test your function with the data stored in damages.


# In[27]:


# new list of updated damages in which data are converted into float type

updated_damages= []
def updated_damage():
    for amount in damages:
        prefix = ''
        
        if amount == "Damages not recorded":
            updated_damages.append(amount)
        else:
            for letter in amount:
                prefix += letter
                
                if letter == "M":
                    prefix = float(prefix.replace("M", ""))
                    updated_damages.append(prefix*float(conversion["M"]))
                
                elif letter == "B":
                    prefix = float(prefix.replace("B", ""))
                    updated_damages.append(prefix*float(conversion["B"]))
                    
    return updated_damages

print (updated_damage())


# In[6]:


# create a new dictionary in which names of hurricane are the keys and the rest of parameters are values

hurricane_biography = {}

def hurricane_names():
    
    for item in range(len(names)):
        hurricane_parameters = []
        hurricane_parameters.append(months[item])
        hurricane_parameters.append(years[item])
        hurricane_parameters.append(areas_affected[item])
        hurricane_parameters.append(damages[item])
        hurricane_parameters.append(deaths[item])
        
        hurricane_biography[names[item]] = hurricane_parameters
    
    return hurricane_biography     

print(hurricane_names())


# In[7]:


# create a new dictionary in which years of hurricane are the keys and the rest of lists are values

hurricane_biography = {}

def hurricane_years():
    for item in range(len(years)):
        hurricane_parameters = []
        hurricane_parameters.append(names[item])
        hurricane_parameters.append(months[item])
        hurricane_parameters.append(areas_affected[item])
        hurricane_parameters.append(damages[item])
        hurricane_parameters.append(deaths[item])
        
        hurricane_biography[years[item]] = hurricane_parameters
    
    return hurricane_biography     

print(hurricane_years())


# In[8]:


# count the number of times that each area suffered from hurricanes

hurricane_biography = dict()

for item in range(len(names)):
    for area in areas_affected[item]:
        if area not in hurricane_biography:
            hurricane_biography[area] = 1
        else: 
            hurricane_biography[area] += 1
print (hurricane_biography)        


# In[26]:


# find the area which get the most of hurricanes and the number of times

max_area = ''
max_area_count = 0

for area in hurricane_biography:
    if hurricane_biography[area] > max_area_count:
        max_area = area
        max_area_count = hurricane_biography[area]
print(max_area, max_area_count)       


# In[10]:


# find the hurricane cause the most of deaths and its number

hurricane_deaths = {}
max_death = 0
max_death_name = 'Cuba I'

for item in range(len(names)):
    hurricane_parameters = 0
    hurricane_parameters += (deaths[item])
    hurricane_deaths[names[item]] = hurricane_parameters
    
for name in hurricane_deaths:
    if hurricane_deaths[name] > max_death:
        max_death_name = name
        max_death = hurricane_deaths[name]
        
print(max_death_name, max_death)


# In[11]:


hurricane_deaths


# In[12]:


# rating the hurricanes according to the number of deaths

death_rating = {}
key_rating = [0, 1, 2, 3, 4, 5]
rating_zero = []
rating_one = []
rating_two = []
rating_three = []
rating_four = []
rating_five = []

for i in range(len(names)):
    if deaths[i]==0:
        rating_zero.append(names(i))
        death_rating[key_rating[0]]
    elif deaths[i]>0 and deaths[i]<100:
        rating_one.append(names[i])
    elif deaths[i]>100 and deaths[i]<500:
        rating_two.append(names[i])
    elif deaths[i]>500 and deaths[i]<1000:
        rating_three.append(names[i])
    elif deaths[i]>1000 and deaths[i]<10000:
        rating_four.append(names[i])
    elif deaths[i]>10000:
        rating_five.append(names[i])
            
death_rating[key_rating[0]]=rating_zero
death_rating[key_rating[1]]=rating_one
death_rating[key_rating[2]]=rating_two
death_rating[key_rating[3]]=rating_three
death_rating[key_rating[4]]=rating_four
death_rating[key_rating[5]]=rating_five

death_rating
           
            
                                           


# In[13]:


# find the hurricane cause the most damages and its damages

# first of all, the values must be converted into float instead string values

updated_damages= []

for amount in damages:
    prefix = ''
    
    if amount == "Damages not recorded":
        updated_damages.append(amount)
    else:
        for letter in amount:
            prefix += letter
            if letter == "M":
                prefix = float(prefix.replace("M", ""))
                updated_damages.append(prefix*float(conversion["M"]))
                
            elif letter == "B":
                prefix = float(prefix.replace("B", ""))
                updated_damages.append(prefix*float(conversion["B"]))
                    
print(updated_damages)




# In[23]:


max_damage_hurricane = ''
max_damage = 0
not_recorded = ['Damages not recorded']

for i in range(len(names)):
    if updated_damages[i] not in not_recorded:
        if updated_damages[i] > max_damage:
            max_damage = updated_damages[i]
            max_damage_hurricane = names[i]
print(max_damage_hurricane, max_damage)
            
            
            


# In[25]:


# rating the hurricanes according to its damages

damage_rating = {}
key_rating = [0, 1, 2, 3, 4, 5]
rating_zero = []
rating_one = []
rating_two = []
rating_three = []
rating_four = []
rating_five = []

for i in range(len(names)):
    if updated_damages[i] not in not_recorded:
        if updated_damages[i]==0:
            rating_zero.append(names(i))
        elif updated_damages[i]>0 and updated_damages[i]<100000000:
            rating_one.append(names[i])
        elif updated_damages[i]>100000000 and updated_damages[i]<1000000000:
            rating_two.append(names[i])
        elif updated_damages[i]>1000000000 and updated_damages[i]<10000000000:
            rating_three.append(names[i])
        elif updated_damages[i]>10000000000 and updated_damages[i]<50000000000:
            rating_four.append(names[i])
        elif updated_damages[i]>50000000000:
            rating_five.append(names[i])

damage_rating[key_rating[0]]=rating_zero
damage_rating[key_rating[1]]=rating_one
damage_rating[key_rating[2]]=rating_two
damage_rating[key_rating[3]]=rating_three
damage_rating[key_rating[4]]=rating_four
damage_rating[key_rating[5]]=rating_five

damage_rating
           


# In[ ]:




