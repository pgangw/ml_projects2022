import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# nltk.download('stopwords')
from nltk.corpus import stopwords

stop = stopwords.words('english')

artists_df = pd.read_csv("moma.csv")
uniquetitles_df = artists_df.drop_duplicates('Title')

#SORTING THE DATAFRAME BY HEIGHT
uniquetitles_df = uniquetitles_df.sort_values("Height (cm)", ascending=False, ignore_index=True)

#SAVING THE FILE
uniquetitles_df.to_csv("maxheight.csv")

#VISUALIZING THE WORDCLOUD OF THE MATERIALS
text = ""
print(uniquetitles_df.loc[0:100,:])
for idx, row in uniquetitles_df.loc[0:100,:].iterrows():
    text = text + row["Medium"]
wordcloud = WordCloud(background_color="black", colormap='Blues').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()