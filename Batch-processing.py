#Instead of sending one API call per tweet, you can send a batch of tweets in a single request. OpenAI models can process larger inputs, so you can classify sentiments for multiple tweets at once.
#This approach is effective:  
#1. Fewer API Calls: You reduce the number of API calls to just one for the entire batch.
#2. Lower Costs: Sending multiple tweets in a single request reduces overhead from repeated instructions.
#3. Faster Execution: Minimizes the latency introduced by multiple requests.

import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def analyze_sentiments_batch(tweets):
    messages = [
        {"role": "system", "content": "You are a sentiment analysis assistant."},
        {"role": "user", "content": "Classify the sentiment for each of the following tweets as Positive, Negative, or Neutral: " +
                                     "\n".join([tweet for tweet in tweets])}
    ]
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0
        )
        sentiments = response.choices[0].message.content
        return sentiments
    except Exception as e:
        return [f"Error: {str(e)}"] * len(tweets)

tweets = [
    "I love the new features in the latest update!",
    "This product is the worst thing I've ever purchased.",
    "I feel so-so about the customer support. It could be better.",
    "Absolutely thrilled with the service. Great job!",
    "The delivery was late, and I’m not happy about it.",
]

sentiments = analyze_sentiments_batch(tweets)
print(sentiments)
