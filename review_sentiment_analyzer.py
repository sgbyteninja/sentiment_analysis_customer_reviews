from transformers import pipeline

def run_sentiment_analysis(text, api_key):
    # Load the sentiment analysis pipeline
    classifier = pipeline("sentiment-analysis", model="sgbyteninja/sentiment_analysis_with_roBERTa", token=api_key)
    
    try:
        result = classifier(text)
        return result
    except Exception as e:
        return f"Error: {e}"

def main():
    # Prompt the user to enter their Hugging Face API key
    api_key = input("Enter your Hugging Face API key: ")

    if not api_key:
        print("Error: No API key provided.")
        return
    
    print("\nWelcome to the Sentiment Analysis Tool!")
    print("You can type your review below, and I will analyze the sentiment.")

    # Loop to allow the user to analyze multiple reviews
    while True:
        # User enters a review
        text = input("\nEnter review text (or type 'exit' to quit): ")

        # Exit condition
        if text.lower() == "exit":
            print("Goodbye!")
            break

        # Run sentiment analysis on the entered review
        result = run_sentiment_analysis(text, api_key)

        # Display the result
        print(f"Sentiment Analysis Result: {result}")

if __name__ == "__main__":
    main()