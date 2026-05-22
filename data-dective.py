import csv
import sys
import os

def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
            
    return raw_tweets

def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    Check for missing text, and replace empty likes/retweets with 0.
    Return a clean list of tweets.
    """
    clean_tweets = []
    fixed_rows = 0
    removed_rows = 0

    for tweet in tweets:

        # Check if text is missing
        if tweet["Text"].strip() == "":
            removed_rows = removed_rows + 1
            continue

        # Fix missing likes
        if tweet["Likes"].strip() == "":
            tweet["Likes"] = "0"
            fixed_rows = fixed_rows + 1

        # Fix missing retweets
        if tweet["Retweets"].strip() == "":
            tweet["Retweets"] = "0"
            fixed_rows = fixed_rows + 1

        clean_tweets.append(tweet)

    print(f"Fixed {fixed_rows} bad rows, and removed {removed_rows} bad rows.\n")

    return clean_tweets

def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    Do not use the max() function.
    """
    viral_tweet = tweets[0]

    for tweet in tweets:

        current_likes = int(tweet["Likes"])
        highest_likes = int(viral_tweet["Likes"])

        if current_likes > highest_likes:
            viral_tweet = tweet

    print("MOST VIRAL TWEET")
    print(f"Username: {viral_tweet['Username']}")
    print(f"Likes: {viral_tweet['Likes']}")
    print(f"Text: {viral_tweet['Text']}\n")


def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Bubble Sort or Selection Sort to sort the list 
    by 'Likes' in descending order. NO .sort() allowed!
    """
    n = len(tweets)

    for i in range(n):

        for j in range(0, n - i - 1):

            likes1 = int(tweets[j]["Likes"])
            likes2 = int(tweets[j + 1]["Likes"])

            if likes1 < likes2:
                tweets[j], tweets[j + 1] = tweets[j + 1], tweets[j]

    return tweets

def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    matching_tweets = []

    for tweet in tweets:

        if keyword.lower() in tweet["Text"].lower():
            matching_tweets.append(tweet)

    print(f"\nFound {len(matching_tweets)} matching tweets.\n")

    for tweet in matching_tweets:
        print(f"Username: {tweet['Username']}")
        print(f"Likes: {tweet['Likes']}")
        print(f"Text: {tweet['Text']}")
        print()


if __name__ == "__main__":
    # Load the messy data
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")


                
    # Call your functions here to complete the quests!
    # Example: clean_dataset = clean_data(dataset)
    
    # Quest 1
    clean_dataset = clean_data(dataset)

    # Quest 2
    find_viral_tweet(clean_dataset)

    # Quest 3
    sorted_tweets = custom_sort_by_likes(clean_dataset)

    print("TOP 10 MOST LIKED TWEETS")

    top_10 = sorted_tweets[:10]

    for tweet in top_10:
        print(f"{tweet['Username']} | Likes: {tweet['Likes']}")
        print(f"Text: {tweet['Text']}")
        print()

    # Quest 4
    keyword = input("Enter keyword to search: ")

    search_tweets(clean_dataset, keyword)
    