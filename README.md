# Sentiment Analysis on Yelp Reviews

# Sentiment Analysis on Yelp Reviews

This repository contains a sentiment analysis project using the RoBERTa model to classify Yelp reviews into three sentiment categories: Positive (1), Neutral (0), and Negative (2). The dataset used is the Yelp Reviews dataset, and the model is trained using Hugging Face's transformers library.

## Dataset

The dataset used is the Yelp Reviews dataset, available on Kaggle. To download it, you can use the following method to load it:

1. First, ensure you have the Kaggle API credentials set up and available in your environment.
2. Then, run the following code to download the dataset:

```python
import kaggle

# Specify the dataset name
dataset_name = "omkarsabnis/yelp-reviews-dataset"

# Download the dataset
kaggle.api.dataset_download_files(dataset_name, path='./', unzip=True)