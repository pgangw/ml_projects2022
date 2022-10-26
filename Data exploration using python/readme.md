# Assignment 1: Exploring the MOMA dataset

This is a class assignment completed for the module 'Machine Learning'. The dataset for the assigment were provided from the link - https://github.com/Amirosimani/Machine_Learning_Pratt/blob/master/assignments/assignment_01.md

## Files uploaded

- 01combining.py combines the two datasets
- 02ageoftheartists.py explores how long the artists lived for and which gender category they belonged to
- 03oldestyoungest.py explores the number of artists who lived for under 5 years or over 100 years
- 04maxartworks.py finds the artist who has made maximum number of paintings and visualizes the dimanesions of the same
- 05material.py finds the materials most popularly used in the lenghtiest artworks
- 06area.py finds the artworks with the biggest areas and also finds the gender of the artists

The two csv files uploaded, were generated using queries:
- moma.csv is the file created by combining the initially given datasets
- maxheight.csv is the file that was generated in 05material.py

## Walkthrough of the exploration

The python files are described as follows:

### STEP 1: Merging the two datasets

The file 01combining.py combines the two datasets on awrtists and artworks, to ensure all the data is captured in one csv file. 
![1 - Artist Age](https://user-images.githubusercontent.com/102167360/192128424-7097f2a4-91d5-4ad9-9476-8dc2a191e532.png)

### STEP 2: How old did the artists live for and what is the gender of the artists?

ageoftheartists.py explores the age and gender of all the artists. Majortiy of the artists fall in the age group of 75 - 85 years. Further, works of more male artists (roughly 10,000) than female (roughly 2,100) have been listed on MOMA.
![2 - gender](https://user-images.githubusercontent.com/102167360/192128426-6e705cc9-7875-4f75-92f0-fc1e6ec7d05d.png)

### STEP 3: What are the highest and lowest ages of the artists? How many artists lived for under 5 years and over 100 years?

03oldestyoungest.py finds that roughly 7 artists listed on MOMA have lived for under 5 years. Whereas around 50 artists have been documented to have lived for over 100 years. This data highlights age anomalies in the dataset. 
![3 - min and max age](https://user-images.githubusercontent.com/102167360/192128429-5e31516c-1a6d-4981-aba4-b1c988245c1a.png)

Further investigation of the dataset shows that roughly 200 artworks might have incorrect age details of the artists.
![3b](https://user-images.githubusercontent.com/102167360/192128434-d4a55786-176f-45f8-a239-fc2f6c25381a.png)

### STEP 4: Who created the most number of artworks and what are the dimensions of the same?

04maxartworks.py finds that Marc Chagall has the most number of artworks listed on MOMA. His longest artworks measures roughly 100cm and widest 69cm. His smallest artwork measures approximately 5x5cm.
![4 - dimensions of the artworks](https://user-images.githubusercontent.com/102167360/192128442-f1c1a94f-1e75-4f11-968a-56ab7a254871.png)

### STEP 5: Which materials have been used in the longest artworks?

05material.py calculates a list of top 100 lenghtiest artworks and uses wordclouds to find the most popular materials used in them. The visual shows that paper, steel, ink, polyester, metal, aluminium and wood are some of the most popular materials used.  
![5 - wordcloud of materials](https://user-images.githubusercontent.com/102167360/192128447-7fcd86e8-9597-4c3f-a0df-523bdaab76bc.png)

### STEP 6: Which are the biggest artworks and who created them - men or women?

05material.py discovers the top 50 biggest artworks. It can be noted that the biggest artwork "Bus" was created by a female (almost 3,50,000 cm sq). A good mix of men and women have created some of the biggest artworks at MOMA. 
![6 - biggest artworks](https://user-images.githubusercontent.com/102167360/192128593-b94f523b-dfe4-424f-8a56-d47a9c53c90e.png)
