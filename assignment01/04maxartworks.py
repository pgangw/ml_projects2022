from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

#MAX ARTWORKS MADE BY ANY ARTIST
artists_df = pd.read_csv('moma.csv')
uniquetitles_df = artists_df.drop_duplicates('Title')
uniquetitles_df.drop(uniquetitles_df[uniquetitles_df['artist'] == 'Unidentified Artist'].index, inplace = True)
uniquetitles_df.drop(uniquetitles_df[uniquetitles_df['artist'] == 'Unidentified Designer'].index, inplace = True)

#THE ARTIST WHO CREATED THE MAXIMUM NUMBER OF ARTWORKS - MARC CHAGALL
print(uniquetitles_df['artist'].mode())

# #DIMENSIONS OF THE ARTWORKS CREATED BY THE ARTIST
maxartist_df = uniquetitles_df[uniquetitles_df['artist'] == 'Marc Chagall']
# print(maxartist_df.shape)

plt.scatter(maxartist_df['Width (cm)'], maxartist_df['Height (cm)'], c="#eaac8b")
plt.xlabel("Width (in cm)")
plt.ylabel("Height (in cm)")
plt.title("Dimensions of the artworks created by Marc Chagall")
plt.show()
