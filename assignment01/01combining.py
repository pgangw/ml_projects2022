import pandas as pd

#IMPORT CSVS TO MERGE
artists_df = pd.read_csv('artists.csv')
# print(artists_df.head())
artworks_df = pd.read_csv('artworks.csv')
# print(artworks_df.head())

#MERGE THE CSVS
moma_df=pd.merge(artists_df, artworks_df, on="artist", indicator="true", how='outer')
moma_df.to_csv("moma.csv", index=False, encoding='UTF8')


