import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

# Sample tweets
tweets = [
    "I love the new features in the latest update!",
    "This product is the worst thing I've ever purchased.",
    "I feel so-so about the customer support. It could be better.",
    "Absolutely thrilled with the service. Great job!",
    "The delivery was late, and I’m not happy about it."
]

# Function to analyze sentiment
def analyze_sentiment(tweet):
    messages = [
        {"role": "system", "content": "You are a sentiment analysis assistant."},
        {"role": "user", "content": f"Classify the sentiment of this tweet: '{tweet}'. Respond with 'Positive', 'Negative', or 'Neutral'."}
    ]
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  
            messages=messages,
            temperature=0  # Low temperature for deterministic results
        )
        sentiment = response.choices[0].message.content.strip()
        return sentiment
    except Exception as e:
        return f"Error: {str(e)}"

# Analyze and display sentiment for each tweet
for tweet in tweets:
    sentiment = analyze_sentiment(tweet)
    print(f"Tweet: {tweet}\nSentiment: {sentiment}\n")
