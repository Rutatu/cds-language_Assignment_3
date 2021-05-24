# cds-language_Assignment_3

***Class assignment for language analytics class at Aarhus University.***

***2021-***

# Dictionary-based sentiment analysis 

## About the script
This assignment is Class Assignment 3. The task was to calculates the sentiment scores of over a million headlines taken from the Australian news source ABC (Start Date: 2003-02-19 ; End Date: 2020-12-31) using the spaCyTextBlob approach, create and save two plots of sentiment over time with a 1-week and a 1-month  rolling averages. In addition, this script creates one plot with 1-day, 1-week, 1-month and 1-year rolling averages together for a better comparison.


## Methods
The problem of the task relates to calculating sentiment scores for every headline in a datset and visualizing results. To calculate the sentiment score for every headline I used ```spacy```, a natural language processing library in Python along with ```Textblob```, which offers simple tools for sentiment analysis and text processing. ```Textblob``` library has a bag-of-words approach, meaning that it has a list of words such as “good”, “bad”, and “great” that have a sentiment score attached to them. It is also able to pick up modifiers (such as “not”) and intensifiers (such as “very”) that affect the sentiment score. Performance of the dictionary-based sentiment analysis depends heavily on the dictionary being used. Hence, to be able to interpret the results of this project better, read more about the dictionary in the homepage: https://textblob.readthedocs.io/en/dev/

For visualizations, I calculated 7, 30 and 365 days rolling averages to show the trends of changing headlines´ sentiment over time.


## Repository contents

| File | Description |
| --- | --- |
| output | Folder containing files produced by the scripts |
| output/ | |
| output/ ||
| output/ | |
| src | Folder containing the scripts |
| src/sentiment.py | Sentiment analysis script |
| README.md | Description of the assignment and the instructions |
| create_classification_venv.bash | bash file for creating a virtual environmment |
| kill_classification_venv.bash | bash file for removing a virtual environment |
| requirements.txt | list of python packages required to run the script |


## Data


## Intructions to run the codes

Both codes were tested on an HP computer with Windows 10 operating system. They were executed on Jupyter worker02.

__Code parameters__


| Parameter | Description |                                              
| --- | --- |                                                                    
| train_size (trs) | The size of the training data as a percentage. Default = 0.8 (80%) |                                       
| test_size (tes) | The size of the testing data as a percentage. Default = 0.2 (20%) | 
| name (n) | Name of the classification report to be saved as .csv file. Default = logReg_report |                                       



__Steps__

Set-up:
```
#1 Open terminal on worker02 or locally
#2 Navigate to the environment where you want to clone this repository
#3 Clone the repository
$ git clone https://github.com/Rutatu/cds-visual_Assignment_4.git 

#4 Navigate to the newly cloned repo
$ cd cds-visual_Assignment_4

#5 Create virtual environment with its dependencies and activate it
$ bash create_classification_venv.sh
$ source ./classification/bin/activate

``` 

Run the code:

```
#6 Navigate to the directory of the script
$ cd src

#7 Run each code with default parameters
$ python Logistic_Regression.py
$ python Neural_Network.py

#8 Run each code with self-chosen parameters
$ python Logistic_Regression.py -trs 0.9 -tes 0.1 -n lr_cm
$ python Neural_Network.py -trs 0.7 -tes 0.3 -hl1 30 -hl2 15 -hl3 5 -ep 500 -n classification_report

#9 Run the NN script only with hidden_layer_1:
$ python Neural_Network.py -hl1 30 -hl2 0

#10 To remove the newly created virtual environment
$ bash kill_classification_venv.sh

#11 To find out possible optional arguments for both scripts
$ python Logistic_Regression.py --help
$ python Neural_Network.py --help


 ```

I hope it worked!


## Results
