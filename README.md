# Tweet Sentiment Analysis using OpenAI

This project demonstrates how to perform sentiment analysis on a list of tweets using OpenAI's GPT-based models, such as `gpt-3.5-turbo` or `gpt-4`. The script classifies each tweet's sentiment as **Positive**, **Negative**, or **Neutral**.

---

## Prerequisites

Before running the script, ensure you have the following:

1. **OpenAI API Key**: Sign up at [OpenAI](https://platform.openai.com/) to obtain your API key.
2. **Google Colab or Python Environment**: This script is optimized for Google Colab but can also run in any Python environment.
3. **Python Libraries**: Install the required `openai` library.

---

## Setup Instructions

1. **Install Dependencies**:
   Open your terminal or Google Colab and install the latest version of the `openai` library:
   ```bash
   pip install openai
   ```

2. **Verify Installation**:
   Ensure the `openai` library version is `>=1.0.0` by running:
   ```python
   import openai
   print(openai.__version__)
   ```

3. **Set API Key**:
   Replace `your_openai_api_key` in the script with your actual API key:
   ```python
   openai.api_key = "your_openai_api_key"
   ```

4. **Run the Script**:
   Copy and paste the provided Python script into your Colab or Python environment and execute it.

---

## Script Overview

### Input:
- A predefined list of tweets:
  ```python
  tweets = [
      "I love the new features in the latest update!",
      "This product is the worst thing I've ever purchased.",
      "I feel so-so about the customer support. It could be better.",
      "Absolutely thrilled with the service. Great job!",
      "The delivery was late, and I’m not happy about it.",
  ]
  ```

### Output:
- Sentiment classification for each tweet as `Positive`, `Negative`, or `Neutral`.

### Key Function:
- **`analyze_sentiment(tweet)`**:
  - Sends the tweet to OpenAI's `ChatCompletion` API for sentiment analysis.
  - Processes and returns the sentiment response.

---

## Example Output

```
Tweet: I love the new features in the latest update!
Sentiment: Positive

Tweet: This product is the worst thing I've ever purchased.
Sentiment: Negative

Tweet: I feel so-so about the customer support. It could be better.
Sentiment: Neutral

Tweet: Absolutely thrilled with the service. Great job!
Sentiment: Positive

Tweet: The delivery was late, and I’m not happy about it.
Sentiment: Negative
```

---

## Troubleshooting

1. **OpenAI API Errors**:
   - Ensure your API key is valid.
   - Check for network issues.

2. **Library Version Issues**:
   - If you encounter errors related to `openai.Completion`, ensure you’re using `ChatCompletion` and have updated the library.

3. **Colab Caching Issues**:
   - Restart the Colab runtime: `Runtime > Restart runtime`.

---

## Additional Notes

- This script uses the `gpt-3.5-turbo` model. You can upgrade to `gpt-4` for potentially better accuracy.
- Adjust the `temperature` parameter in the `ChatCompletion.create` function to control the randomness of responses.
- For larger datasets, consider batching requests to stay within OpenAI's rate limits.



