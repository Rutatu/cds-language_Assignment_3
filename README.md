# cds-language_Assignment_3

***Class assignment for language analytics class at Aarhus University.***

***2021-03-01***

# Dictionary-based sentiment analysis 

## About the script
This assignment is Class Assignment 3. The task was to calculates the sentiment scores of over a million headlines taken from the Australian news source ABC (Start Date: 2003-02-19 ; End Date: 2020-12-31) using the spaCyTextBlob approach, create and save two plots of sentiment over time with a 1-week and a 1-month  rolling averages. In addition, this script creates one plot with 1-day, 1-week, 1-month and 1-year rolling averages together for a better comparison.


## Methods
The problem of the task relates to calculating sentiment scores for every headline in a datset and visualizing results. To calculate the sentiment polarity score (negative vs positive, -1.0 => +1.0) for every headline I used ```spacy```, a natural language processing library in Python along with ```Textblob```, which offers simple tools for sentiment analysis and text processing. ```Textblob``` library has a bag-of-words approach, meaning that it has a list of words such as “good”, “bad”, and “great” that have a sentiment score attached to them. It is also able to pick up modifiers (such as “not”) and intensifiers (such as “very”) that affect the sentiment score. Performance of the dictionary-based sentiment analysis depends heavily on the dictionary being used. Hence, to be able to interpret the results of this project better, read more about the dictionary in the homepage: https://textblob.readthedocs.io/en/dev/

For visualizations, I calculated 7, 30 and 365 days rolling averages to show the trends of changing headlines´ sentiment over time.


## Repository contents

| File | Description |
| --- | --- |
| data/ | Folder containing input data for the script |
| data/abcnews-date-text.rar | archived headlines dataset |
| output | Folder containing files produced by the scripts |
| output/weekly_sentiment.png | a plot displaying 7-days rolling average of sentiment scores |
| output/monthly_sentiment.png | a plot displaying 30-days rolling average of sentiment scores|
| output/combined_sentiment.png | a plot displaying 1, 7, 30  and 365-days rolling averages of sentiment scores |
| src | Folder containing the scripts |
| src/sentiment.py | Sentiment analysis script |
| LICENSE |  A software license defining what other users can and can't do with the source code |
| README.md | Description of the assignment and the instructions |
| create_sentiment_venv.bash | bash file for creating a virtual environmment |
| kill_sentiment_venv.bash | bash file for removing a virtual environment |
| requirements.txt | list of python packages required to run the script |


## Data

The dataset used (CSV single file) contains 1195191 news headlines sourced from the reputable Australian news source ABC (Australian Broadcasting Corporation). The headlines were published over a period of eighteen years: Start Date: 2003-02-19 ; End Date: 2020-12-31

The column structure of the CSV file is the following:
| Column | Description |
| --- | --- |
| publish_date | Date of publishing for the article in yyyyMMdd format |
| headline_text | Text of the headline in Ascii , English , lowercase |

Link to data: https://www.kaggle.com/therohk/million-headlines



## Intructions to run the code

Code was tested on an HP computer with Windows 10 operating system. It was executed on Jupyter worker02.


__Steps__

Set-up:
```
#1 Open terminal on worker02 or locally
#2 Navigate to the environment where you want to clone this repository
#3 Clone the repository
$ git clone https://github.com/Rutatu/cds-language_Assignment_3.git 

#4 Navigate to the newly cloned repo
$ cd cds-language_Assignment_3

#5 Create virtual environment with its dependencies and activate it
$ bash create_sentiment_venv.sh
$ source ./sentiment/bin/activate

#6 Unzip the CSV file in data folder
$ cd data
$ unzip abcnews-date-text.zip

``` 

Run the code:

```
#7 Navigate to the directory of the script
$ cd ../src

#8 Run the code 
$ python sentiment.py

#9 To remove the newly created virtual environment
$ bash kill_sentiment_venv.sh

 ```

I hope it worked!


## Results

The goal of sentiment analysis is to extract computationally the feeling that a text conveys. This task might seem highly subjective, but when there is a large amount of text that is beyond the capacity of human readers, automated sentiment analysis can be helpful. This project showed that dictionary-based approach can be used to get insight into changing emotional valence of the news headlines. Results are highly dependent on the choice of the dictionary, therefore, the dictionary must be chosen carefully.

The three output plots show the fluctuating general trend throughout 18 years with a few more specific shorter trends. Years 2013-2015 show the highest peaks of positive sentiment scores, which started to increase in year 2012 after a continuous main downward trend since 2003. The headlines sentiment scores started steadily decreasing again after 2016. Such observations reflect that Australian news source ABC News has been publishing both negative and positive news throughout the years. It indicated that ABC News´ headlines are not designed to convey only one kind of emotion - it is more realistic, portraying variety of life events with different emotional significance. To interpret such trends better, we would need to investigate the life events in Autralia in the corresponding years.


