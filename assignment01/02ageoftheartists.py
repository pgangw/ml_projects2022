import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#READCSV
artists_df = pd.read_csv('moma.csv')

#REPLACE 0 BIRTH YEAR, DEATH YEAR & GENDER WITH NAN
artists_df["EndDate_x"] = artists_df["EndDate_x"].replace(0, np.nan)
artists_df["BeginDate_x"] = artists_df["BeginDate_x"].replace(0, np.nan)
artists_df["Gender_x"] = artists_df["Gender_x"].replace("female", "Female")
artists_df["Gender_x"] = artists_df["Gender_x"].replace("male", "Male")
artists_df["Gender_x"] = artists_df["Gender_x"].replace("Non-Binary", np.nan)
artists_df["Gender_x"] = artists_df["Gender_x"].replace("Non-binary", np.nan)

# CHECKING THE MIN AND MAX YEARS TO IDENTIFY 0s
# print(artists_df["BeginDate_x"].min())

#CALCULATING THEIR AGE
artists_df["age"] = artists_df["EndDate_x"] - artists_df["BeginDate_x"]

#FOUND THAT THE MAX AGE OF AN ARTIST IS 130
#print(artists_df[artists_df["age"] == artists_df["age"].max()])

uniqueArtists = artists_df.drop_duplicates('ConstituentID_x')
# print(uniqueArtists.head())

#PLOTTING THE BAR GRAPHS

# ##Plotting the age group and number of artists in the age group
# bins = [10,15,20,25,30,35,40,45,50,60,70,80,90,100,110,120,130] 
# plt.hist(uniqueArtists["age"], bins, histtype='bar',rwidth=0.9, color='#6d597a') 
# plt.xlabel('Age')
# plt.ylabel('Number of Artists')
# plt.title('Artist Age')
# plt.show()

##Plotting the total number of artists by gender
uniqueArtists.groupby('Gender_x')['artist'].nunique().plot(kind='bar', color="#eaac8b")
plt.title('Number of males and females')
plt.xlabel('Gender')
plt.ylabel('Number of Artists')
plt.show()