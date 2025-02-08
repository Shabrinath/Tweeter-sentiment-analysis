#Data file is available as CSV file/google sheet

import pandas as pd
import openai

# Google Sheets ID (Replace with your actual Sheet ID)
sheet_id = "1i4K9YiB-k_lfCYGyINcyo38EhGdK4OTqenobqQn6tKg"

# Construct the CSV URL
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"

# Read the CSV file
df = pd.read_csv(csv_url)

# Display the first 5 rows
#print(df.head())

openai.api_key = "<replace with your token>"

# Function to get sentiment
def analyze_sentiment(review):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a sentiment analysis assistant."},
        {"role": "user", "content": f"Classify the sentiment of this tweet: '{review}'. Respond with 'Positive', 'Negative', or 'Neutral'."}
    ]
      
    )
    
    # Extract message content correctly
    return response.choices[0].message.content  

# Apply sentiment analysis to each review
df["sentiment"] = df["customer-review"].apply(analyze_sentiment)

print(df[["customer-review", "sentiment"]].head())
