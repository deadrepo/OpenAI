import os
import time
import tweepy
import openai

# Twitter API Credentials (ALL REQUIRED)
TWITTER_API_KEY = ''  # Consumer Key
TWITTER_API_KEY_SECRET = ''  # Consumer Secret
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
TWITTER_BEARER_TOKEN = ''

# OpenAI API Credentials
OPENAI_API_KEY = ''  # Replace this with your OpenAI API Key


class CardanoFunFactBot:
    def __init__(self):
        # Twitter Authentication
        self.auth = tweepy.OAuthHandler(
            TWITTER_API_KEY,
            TWITTER_API_KEY_SECRET
        )
        self.auth.set_access_token(
            TWITTER_ACCESS_TOKEN,
            TWITTER_ACCESS_TOKEN_SECRET
        )

        # Initialize Twitter API clients
        self.twitter_client = tweepy.Client(
            consumer_key=TWITTER_API_KEY,
            consumer_secret=TWITTER_API_KEY_SECRET,
            access_token=TWITTER_ACCESS_TOKEN,
            access_token_secret=TWITTER_ACCESS_TOKEN_SECRET,
            bearer_token=TWITTER_BEARER_TOKEN
        )

        # Set OpenAI API Key
        openai.api_key = OPENAI_API_KEY

    def generate_cardano_fact_tweet(self):
        """Generate a fun fact tweet about Cardano using OpenAI's GPT-3.5-Turbo"""
        try:
            # Call GPT-3.5-Turbo using the new OpenAI library format
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use GPT-3.5-Turbo
                messages=[
                    {"role": "system",
                     "content": "You are an expert on Cardano blockchain. Generate short, fun, and engaging facts about Cardano under 280 characters."},
                    {"role": "user",
                     "content": "Share a fun fact about Cardano blockchain in less than 280 characters."}
                ],
                max_tokens=70,  # Keeps the response concise
                temperature=0.7  # Creativity level
            )

            # Extracting the text output properly for OpenAI >=1.0.0
            tweet_text = response.choices[0].message.content.strip()
            print(f"Generated Cardano Fact: {tweet_text}")
            return tweet_text

        except Exception as e:
            print(f"Error generating tweet: {e}")
            return "Cardano combines peer-reviewed research and sustainability. A leader in blockchain innovation! 🌍 #CardanoFunFact"

    def post_tweet(self):
        """Post a randomly generated Cardano fun fact tweet"""
        try:
            # Generate the fun fact tweet
            tweet_text = self.generate_cardano_fact_tweet()

            # Post tweet
            response = self.twitter_client.create_tweet(text=tweet_text)
            print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")

        except Exception as e:
            print(f"Error posting tweet: {e}")

    def start_bot(self):
        """Start the bot to tweet Cardano fun facts every 30 minutes"""
        print("Cardano Fun Fact Bot Started!")
        while True:
            # Post a tweet
            self.post_tweet()

            # Wait for 30 minutes before the next tweet
            time.sleep(1800)


# Initialize and run the bot
if __name__ == "__main__":
    bot = CardanoFunFactBot()
    bot.start_bot()
