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

## Model Evaluation

After training, the model is evaluated using the following metrics:
- Accuracy
- Precision
- Recall
- F1-score

These metrics are used to assess the model's performance in classifying sentiment in the Yelp reviews.

## Saved Model

The trained model and tokenizer are saved for future use. They are available for download via the following link:

[Trained RoBERTa Model and Tokenizer on Google Drive](https://drive.google.com/drive/folders/1bYO7UKGbv5ej6a-sNTuY_fRCkhFyaTaM?usp=sharing)

## Conclusion

This project demonstrates how to perform sentiment analysis on Yelp reviews using RoBERTa. By fine-tuning the pre-trained model, we can effectively classify customer reviews into sentiment categories, which can be useful for further analysis or integration into a production system.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
