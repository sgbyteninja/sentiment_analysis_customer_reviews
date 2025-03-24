"""
Sentiment Analysis Tool using Hugging Face's Transformers library.

This script allows users to analyze the sentiment of input text using a pre-trained sentiment 
analysis model. It prompts the user to enter their Hugging Face API key, then allows the user 
to input text for sentiment analysis in a loop. The sentiment result is displayed, and the loop 
continues until the user types 'exit'.

Functions:
    run_sentiment_analysis(text: str, api_key: str) -> dict:
        Analyzes the sentiment of the given text using a Hugging Face sentiment analysis model.
    
    main() -> None:
        Main function that runs the user interface and loops for sentiment analysis.
        
Usage:
    - Run the script and provide your Hugging Face API key when prompted.
    - Enter review text for sentiment analysis or type 'exit' to quit.
"""

from transformers import pipeline


def run_sentiment_analysis(text: str, api_key: str) -> dict:
    """
    Analyzes the sentiment of the given text using a Hugging Face sentiment analysis model.

    Args:
        text (str): The text input for sentiment analysis.
        api_key (str): The Hugging Face API key.

    Returns:
        dict: Sentiment analysis result containing sentiment and confidence.
    """
    classifier = pipeline(
        "sentiment-analysis", 
        model="sgbyteninja/sentiment_analysis_with_roBERTa", 
        token=api_key
    )

    try:
        result = classifier(text)
        return result
    except (ValueError, TypeError) as e:  # Catch more specific exceptions
        return {"Error": f"Invalid input: {str(e)}"}
    except Exception as e:
        return {"Error": f"An error occurred: {str(e)}"}


def main() -> None:
    """
    Main function that runs the user interface and loops for sentiment analysis.
    Prompts the user to enter reviews for sentiment analysis and exits upon 'exit'.
    """
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
