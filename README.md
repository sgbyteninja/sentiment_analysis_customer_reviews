# Sentiment Analysis on Yelp Reviews

This project aims to perform sentiment analysis on Yelp reviews using a fine-tuned RoBERTa model. The goal is to classify Yelp reviews into three sentiment categories: Positive (1), Neutral (0), and Negative (2). The dataset used for this project is the Yelp Reviews dataset, which can be accessed on Kaggle.

## Dataset

The dataset used for this analysis is the Yelp Reviews dataset. It contains a collection of customer reviews from Yelp, including both the review text and a star rating. For the purpose of this project, the star ratings are converted into sentiment labels as follows:
- **1**: Positive sentiment (4 or 5 stars)
- **0**: Neutral sentiment (3 stars)
- **2**: Negative sentiment (1 or 2 stars)

## Data Preprocessing

The dataset is preprocessed by cleaning unnecessary columns and converting the star ratings into sentiment labels. The reviews are then tokenized using the RoBERTa tokenizer, which is prepared for the model training process.

## Model Training

A pre-trained RoBERTa model is fine-tuned on the Yelp dataset. The training process is configured with the following settings:
- 5 epochs of training
- A batch size of 8
- Early stopping based on evaluation loss

The model training and Evaluation was conducted in [Google Colab](https://colab.research.google.com/drive/1f448qyenngeujyvWKleprM5Mt_fbRfO2?usp=sharing), where the full training notebook is available for review and reproduction.

## Model Evaluation

After training, the model is evaluated using the following metrics:
- Accuracy
- Precision
- Recall
- F1-score

These metrics are used to assess the model's performance in classifying sentiment in the Yelp reviews.

## Saved Model

The model has been fine-tuned on a sentiment analysis task and is hosted on Hugging Face's Model Hub. You can easily load the model and use it for predictions through the Hugging Face API.

Model Name: `sgbyteninja/sentiment_analysis_with_roBERTa`

To interact with the model, you'll need a Hugging Face API key. Follow these steps to access the model using the `transformers` library:

## Usage

To use the model, you can either access it directly via the Hugging Face API or run a local inference script.

1. Install Dependencies
2. run the python script review_sentiment_analyzer.py
3. Enter you Hugging Face API Key
5. Test the Model with Review Texts

## Conclusion

This project demonstrates how to perform sentiment analysis on Yelp reviews using RoBERTa. By fine-tuning the pre-trained model, we can effectively classify customer reviews into sentiment categories, which can be useful for further analysis or integration into a production system.
