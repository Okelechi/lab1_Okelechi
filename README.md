# lab1_Okelechi
My individual coding lab
# Twitter Data Analysis Project

## Overview
This project is a data analysis tool built in Python that processes a messy Twitter dataset. It cleans raw data, identifies the most viral tweet, sorts tweets by engagement, and allows keyword-based searching. It also includes a Bash script that analyzes user activity from the command line.

The project was built to practice core programming concepts such as loops, conditionals, functions, file handling, and algorithm design without using built-in sorting or max functions.


## Project Structure

- "data-detective.py" → Main Python program (all four quests)
- "feed-analyzer.sh" → Bash script for user activity analysis
- "twitter_dataset.csv" → Dataset used for testing
- "README.md" → Project documentation


## Features

### Quest 1: Data Cleaning
- Removes tweets with missing or empty text
- Replaces missing Likes and Retweets with 0
- Tracks number of fixed and removed rows

### Quest 2: Viral Tweet Detection
- Finds the tweet with the highest number of likes
- Displays username, likes, and tweet text
- Does not use built-in max() function

### Quest 3: Custom Sorting
- Sorts tweets by number of likes in descending order
- Uses Bubble Sort algorithm
- Displays Top 10 most liked tweets

### Quest 4: Keyword Search
- Searches tweets based on user input keyword
- Matches are case-insensitive
- Displays all matching tweets and count


## How to Run

### Run Python Program
Make sure Python is installed, then run:

   ### Run Python Program
Make sure Python is installed, then run:

```bash
python data-detective.py