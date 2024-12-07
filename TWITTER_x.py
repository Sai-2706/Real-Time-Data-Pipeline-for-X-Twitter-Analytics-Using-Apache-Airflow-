import tweepy
import pandas as pd

def run_twitter_etl():
    # Replace with your actual credentials
    bearer_token = "Your 'X'(twitter) bearer token"
    
    # Initialize Tweepy Client
    client = tweepy.Client(bearer_token=bearer_token)
    
    # Define the username and maximum tweets to fetch
    username = "narendramodi"
    max_results = 50  # Adjust as needed, max is 100 per request in v2
    
    # Fetch user information to get user ID
    user = client.get_user(username=username)
    user_id = user.data.id
    
    # Fetch tweets from the user's timeline
    tweets = client.get_users_tweets(
        id=user_id,
        max_results=max_results,
        tweet_fields=["created_at", "public_metrics", "text"]
    )
    
    # Process the tweets
    tweet_list = []
    for tweet in tweets.data:
        refined_tweet = {
            "user": username,
            "text": tweet.text,
            "favorite_count": tweet.public_metrics["like_count"],
            "retweet_count": tweet.public_metrics["retweet_count"],
            "created_at": tweet.created_at
        }
        tweet_list.append(refined_tweet)
    
    # Create a DataFrame and save to CSV
    df = pd.DataFrame(tweet_list)
    df.to_csv('Modi_tweets.csv', index=False)
    print("Tweets have been saved to 'Modi_tweets.csv'.")

# Run the ETL function
if __name__ == "__main__":
    run_twitter_etl()
