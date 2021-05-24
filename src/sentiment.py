#!/usr/bin/env python



''' ---------------- About the script ----------------

Assignment 3: Sentiment Analysis

This script calculates sentiment scores of over a million headlines taken from the Australian news source ABC (Start Date: 2003-02-19 ; End Date: 2020-12-31) using the spaCyTextBlob approach, creates and saves two plots of sentiment over time with a 1-week and a 1-month  rolling averages. Also, it creates one plot with 1-day, 1-week, 1-month and 1-year rolling averages together for a better comparison.


Example:    
    $ python sentiment.py
        
  

'''






"""---------------- Importing libraries ----------------
"""

# importing libraries
import spacy
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
sys.path.append(os.path.join(".."))

from spacytextblob.spacytextblob import SpacyTextBlob

# initialising spacy
nlp = spacy.load("en_core_web_sm")

# initialising spaCyTextBlob and adding it as a new component to spaCy nlp pipeline.
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)


"""---------------- Main script ----------------
"""


def main():
     
    
    
    """------ Reading data and preparation ------
    """


    # Defining path to the csv file
    in_file = os.path.join("..", "data", "abcnews-date-text", "abcnews-date-text.csv")

    # Reading the csv file and saving into a variable
    abc_news = pd.read_csv(in_file)
    
    # Presenting a sample of 10 headlines to the user
    print(f"\n[INFO] This is an overview of the dataset:\n")
    print(abc_news.sample(10))
    
    
    # Geting a list of every publish date, which I will loop through later 
    dates = sorted(abc_news["publish_date"].unique())

    # Creating an empty list for total sentiment score for each day
    total_scores = []

    # Create ouput folder, if it doesn´t exist already, for saving the plots and other output 
    if not os.path.exists("../output"):
        os.makedirs("../output")
    
        
    """------ The loop calculating sentiment scores ------
    """
    
    print(f"\n[INFO] Calculating sentiment scores\n")
    
    # Looping through each day
    for day in dates:
    
        # Creating a variable to store a total sentiment score for all the headlines per day 
        polarity_score_total = 0
    
    
        # Getting a list of every headline in the day that the code is looping through
        headlines = abc_news[abc_news["publish_date"]==day]
    
        # Looping through each headline in a day
        for headline in nlp.pipe(headlines["headline_text"], batch_size=1000):
        
            # Calculating sentiment score for that headline
            headline_polarity = headline._.sentiment.polarity
        
            # Adding the above calculated headline score to the total score. In the end this will result in a total sentiment score from all the headlines per one day
            polarity_score_total = headline_polarity + polarity_score_total
     
        # Appending the total score to an empty list
        total_scores.append(polarity_score_total)
        
        
  
    

    """------ Calculating and ploting rolling averages ------
    """    
    
    # Calculating 7 day rolling average
    smoothed_sentiment_weeks = pd.Series(total_scores).rolling(7).mean()

    # Calculating 30 day rolling average
    smoothed_sentiment_months = pd.Series(total_scores).rolling(30).mean()

    # Calculating 365 day rolling average
    smoothed_sentiment_years = pd.Series(total_scores).rolling(365).mean()
    

    """------ Weekly rolling average ------
    """
    
    # Creating a figure no. 1
    fig = plt.figure(figsize = (12,6)) 
    # Creating a grid for readability
    plt.grid()
    # Plotting average sentiment for 7 days rolling
    plt.plot(smoothed_sentiment_weeks)
    # Creating a title
    plt.title("ABC Headline sentiment scores -  weekly average", fontsize= 22)
    # Creating x and y labels
    plt.xlabel("Year since 2003", fontsize= 15)
    plt.ylabel("Sentiment score", fontsize= 15)
    # Creating a legend
    plt.legend(labels = ["Weekly rolling average"],
                loc='upper right', fontsize= 10)
    
    # Setting x ticks to be in weeks rather than default days for a better data interpretation
    plt.xticks(np.arange(0, len(total_scores)+1,365), range(0,18))
    # Defining full filepath to save the plot 
    outfile = os.path.join("..", "output", "weekly_sentiment.png")
    # Saving the figure
    plt.savefig(outfile)
    
    # Printing that plot has been saved
    print(f"\n[INFO] weekly_sentiment plot is saved in directory {outfile}")
    
    
    """------ Monthly rolling average ------
    """  
    
    # Creating a figure no.2
    fig = plt.figure(figsize = (12,6)) 
    # Creating a grid for readability
    plt.grid()
    # Plotting average sentiment for 30 days rolling
    plt.plot(smoothed_sentiment_months)
    # Creating a title
    plt.title("ABC Headline sentiment scores -  monthly average", fontsize= 22)
    # Creating x and y labels
    plt.xlabel("Year since 2003", fontsize= 15)
    plt.ylabel("Sentiment score", fontsize= 15)
    # Creating a legend
    plt.legend(labels = ["Monthly rolling average"],
                loc='upper right', fontsize= 10)
    
    # Setting x ticks to be in months rather than default days for a better data interpretation
    plt.xticks(np.arange(0, len(total_scores)+1,365), range(0,18))
    
    # Defining full filepath to save the plot 
    outfile2 = os.path.join("..", "output", "monthly_sentiment.png")
    # Saving the figure
    plt.savefig(outfile2)
    
    # Printing that plot has been saved
    print(f"\n[INFO] monthly_sentiment plot is saved in directory {outfile2}")
    
    
    """------ Combined rolling averages ------
    """  
    
    # Creating a figure no. 3
    fig = plt.figure(figsize = (12,6)) 
    # Creating a grid for readability
    plt.grid()
    # Plotting sentiment for every day
    plt.plot(total_scores)
    # Plotting average sentiment for 7 days rolling
    plt.plot(smoothed_sentiment_weeks)
    # Plotting average sentiment for 30 days rolling
    plt.plot(smoothed_sentiment_months)
    # Plotting average sentiment for 365 days rolling
    plt.plot(smoothed_sentiment_years)
    # Creating a title
    plt.title("ABC Headline sentiment scores since 2003",fontsize= 22)
    # Creating x and y labels
    plt.xlabel("Year since 2003", fontsize= 15)
    plt.ylabel("Sentiment score", fontsize= 15)
    # Creating a legend
    plt.legend(labels = ["Daily sentiment", "Weekly rolling average", "Monthly rolling average", "Yearly rolling average"],
               loc='upper right',
                fontsize= 10)

    # Setting x ticks to be in years rather than default days for a better data interpretation
    plt.xticks(np.arange(0, len(total_scores)+1,365), range(0,18))

    # Defining full filepath to save the plot 
    outfile3 = os.path.join("..", "output", "combined_sentiment.png")
    # Saving the figure
    plt.savefig(outfile3)
            
    # Printing that plot has been saved
    print(f"\n[INFO] combined_sentiment plot is saved in directory {outfile3}")
    
    # Final message to the user
    print(f"\n[INFO] Sentiment analysis script was executed successfully. Have a nice day!")
    
    
    

    
# Define behaviour when called from command line
if __name__=="__main__":
    main()

    
    
    
    
    
    