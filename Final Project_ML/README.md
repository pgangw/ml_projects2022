# **Final Project: Predicting visitor purchases & discovering the UX features relevant to purchases on the Google Merchandise website using Machine Learning**

## About the project

It is known that data science can be used to discover user behavior and needs. Investigating Google Analytics (GA) data such as pageviews, bounces, device category, etc. can be used to enhance the UX of a website. This project explores how UX designers and researchers today can leverage from the capabilities of ML to enhance experiences for users, by studying user behavior on the Google Merchandise website. 

This project is created as part of a classroom assignment at Pratt Institute, NYC in December 2022.

## Research questions

The project will answer the following research questions:
1. Will a new visitor to the Google Merchandise website make a revenue-generating transaction in the ecommerce store? 
2. Which features of the website/user experience are relevant in contributing to making purchases?

## Data source

Visitor-wise data for 6 months (1 August 2016 through 31 January 2017) is collected from Google Merchandise’s GA data using BigQuery on the Google Console. Columns in the dataset are shortlisted on the basis of their hopthesized connection with the UX of a website.

## Files uploaded in the folder(s) above

- **Code - Jupter Notebook:** This folder has the comprehensive notebook with all the code used for the project
- **Data source - SQL code:** This folder has the code used to extract GA analytics data usign BigQuery on Google console
- **Output files:** This folder has all the files exported from the code notebook. All files except d3final.csv have been uploaded here. The file d3final is not uploaded because it is a huge file with 2382169 rows. The final file used for the code has 4,90,996 rows and 12 columns. The file, d4check.csv gives a glimpse of the file used.
- **Project proposal:** This folder has the project proposal in pdf format.

## Steps 

Overview of the steps followed in the notebook:

1. Step 1: Understanding the dataset
2. Step 2: Data exploration using visuals
3. Step 3: Data filtering and preparation
4. Step 4: Building the Neural Network model
5. Step 5: Building the Random Forest model
6. Step 6: Building the Logistic Regression model
7. Step 7: Logistic Regression Grid Search
8. Step 8: Logistic Regression Confusion Matrix and PR curve
9. Step 9: Logistic Regression Feature Importance Calculation
10. Conclusion
11. Testing the random forest model performance on a balanced train set 

## Key findings

- The models help identify an important feature for making transactions - mobile device. This insight can be used to make informed UXR decisions - help shape questions in surveys or inetrviews for example.
- The nature of the dataset - which is heavily skewed towards no transaction, has a negative impact on the model. This can be seen from the last step in the notebook, where the project tries to run the same random forest model using a balanced dataset and performs well. However, this balanced dataset model does not perform well on the original test set.

## Further scope

Additional classification techniques like using ROC AUC as the accuracy metric in the neural network model, using autoencoder as the model architecture or preliminary data structuring techniques (oversampling the minority class, or undersampling the majority class) can be used to find the best model and get better model accuracy.
