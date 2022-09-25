from dataclasses import dataclass
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap 

#READCSV
artists_df = pd.read_csv('moma.csv', low_memory=False)
uniquetitles_df = artists_df.drop_duplicates('Title')

#CALCULATING AREA
uniquetitles_df["area"] = uniquetitles_df["Height (cm)"] * uniquetitles_df["Width (cm)"]
sorted_df = uniquetitles_df.sort_values("area", ascending=False, ignore_index=True)
# print(sorted_df)

#SORTING AREAS BY THEIR VALUES - BIGGEST TO SMALLEST
top10 = sorted_df.head(50)
# print(top10)

#PLOTTING THE GRAPH BY GENDER
colors = ["#355070" if val == "Male" else "#b56576" for idx, val in sorted_df["Gender_x"].iteritems()]
cmap = ListedColormap(colors)
top10.plot(x="Title", y="area", kind="barh", figsize=(6, 6), fontsize=5, color=cmap.colors, legend=None)
# print(colors)
# top10.groupby(["area", "Gender_x"]).size().unstack(level=1)
# top10.groupby(["area", "Gender_x"]).size().unstack(level=1).plot(kind="barh") WORKED
# colors = plt.rcParams['Gender_x']
plt.xlabel("Total area (in cm sq)")
plt.ylabel("Title of artwork")
plt.title("Top 50 biggest artworks at MOMA (Colored by gender of the artist - Males are in blue, females are in pink)")
plt.xticks(rotation=30)
plt.show()

