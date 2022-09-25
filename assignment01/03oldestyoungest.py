import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#READCSV
artists_df = pd.read_csv('moma.csv')

#YOUNGEST & OLDEST ARTISTS DETAILS - Artists above 100 and below 5
artists_df["EndDate_x"] = artists_df["EndDate_x"].replace(0, np.nan)
artists_df["BeginDate_x"] = artists_df["BeginDate_x"].replace(0, np.nan)

artists_df["age"] = artists_df["EndDate_x"] - artists_df["BeginDate_x"]
print(artists_df[artists_df["age"] == artists_df["age"].max()])
print(artists_df[artists_df["age"] == artists_df["age"].min()])

#VISUALIZING HOW MANY MIN AND MAX AGE ARTISTS ARE LISTED
uniqueArtists = artists_df.drop_duplicates('ConstituentID_x')
minmaxage_df = uniqueArtists[(uniqueArtists["age"]>=100) | (uniqueArtists["age"]<=5)] 
print(minmaxage_df)

plt.hist(minmaxage_df["age"], histtype='bar',rwidth=0.9, color="#355070") 
plt.xlabel('Age')
plt.ylabel('Number of Artists')
plt.title('Age of the Artists')
plt.show()

#VISUALIZING HOW MANY ARTWORKS DID MIN AND MAX AGE ARTISTS MAKE
minmaxage_df = artists_df[(artists_df["age"]>=100) | (artists_df["age"]<=5)] 

plt.hist(minmaxage_df["age"], histtype='bar',rwidth=0.9, color="#e56b6f") 
plt.xlabel('Age (in years)')
plt.ylabel('Number of Artworks')
plt.title('Number of artworks where artist age may be incorrect')
plt.show()