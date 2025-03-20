from transformers import pipeline

def run_sentiment_analysis(text, api_key):
    # Loading the sentiment analysis pipeline
    classifier = pipeline("sentiment-analysis", model="sgbyteninja/sentiment_analysis_with_roBERTa", token=api_key)
    
    try:
        result = classifier(text)
        return result
    except Exception as e:
        return f"Error: {e}"

def main():
    # Prompting the user to enter their Hugging Face API key
    api_key = input("Replace with YOUR_API_KEY")
    
    if not api_key:
        print("Error: No API key provided.")
        return
    
    # Example texts for the sentiment analysis
    text = "This sentiment analysis tool is just awesome!"
    print(f"Analysis for the text: '{text}'")
    result = run_sentiment_analysis(text, api_key)
    print(f"Result: {result}")

    # Analyze some more reviews
    texts = [
        "I hate waiting in long lines. But the food is worth it",
        "Everyone should have these shoes!",
        "The furniture in this restaurant is beyond ugly."
    ]
    
    print("\nAdditional Analyses:")
    for t in texts:
        print(f"\nText: {t}")
        result = run_sentiment_analysis(t, api_key)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
