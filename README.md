# Shopee - Price Match Guarantee: Match products with descriptions and images


## Machine learning project
[![CI](https://github.com/nogibjj/Shopee-Price-Match-Guarantee/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Shopee-Price-Match-Guarantee/actions/workflows/main.yml)

#### Duke University (MIDS) - Spring 2023

#### Team Members: [Suzy Anil](https://github.com/sanil72900), [Isha Singh](https://github.com/IshaSingh01), [Alisa Tian](https://github.com/alisa0705), [Dingkun Yang](https://github.com/Yer1k)

----

## Project Overview
A competitive feature amongst retail platforms is product matching which allows companies to offer products at rates competitive to other retailers selling similar products. There are many methods that combine deep learning and traditional machine learning methods to analyze image and text information to calculate similarity between products, however there is little research comparing the effectiveness of integrating multimodal data (product images and descriptions) under this domain (Łukasik et al., 2021). Here, we compare the performance of both unimodal and multimodal models. We trained separate models for text (SBERT and DistilBERT) and images (ResNet50 and MobileNet); the DistilBERT and ResNet50 models outperform the other two in terms of  F1 score and accuracy. The multimodal model used joint embeddings from DistilBERT and MobileNet to predict product labels, which outperformed both unimodal implementations. The integration of product images and titles offer the most useful information to find product matches on a particular platform. 

## Presentation

**Click on the image to watch the presentation**

[![image](https://user-images.githubusercontent.com/81750079/233124833-7b0fcfab-86bf-4579-a364-d508ebd4a798.png)](https://youtu.be/FvDNHgyIBxA)

## Data
Shopee is the leading e-commerce platform in Southeast Asia and Taiwan; their platform contains products from vendors all over the world, predominantly in Singapore and Indonesia. In 2021, the company launched a Kaggle competition aimed at improving product matching algorithms to optimize their customers’ online shopping experience (Dane et al., 2021).

[Link to Data](https://www.kaggle.com/c/shopee-product-matching/data)

## Methods
We used the following methods to train our models:
- [SBERT](https://www.sbert.net/)
- [DistilBERT](https://huggingface.co/transformers/model_doc/distilbert.html)
- [ResNet50](https://keras.io/api/applications/resnet/)
- [MobileNet](https://keras.io/api/applications/mobilenet/)
- Joint Embeddings of DistilBERT and MobileNet

<img src="https://user-images.githubusercontent.com/81750079/233115703-5d9269f0-c75e-4f19-86df-1d42a974fdaa.png"  width="30%" height="40%">


## Results
The following table shows the performance of the models trained on the Shopee dataset. The DistilBERT and ResNet50 models outperform the other two in terms of  F1 score and accuracy. The multimodal model used joint embeddings from DistilBERT and MobileNet* to predict product labels , which outperformed both unimodal implementations. The integration of product images and titles offer the most useful information to find product matches on a particular platform.

Note: Due to computational restritions, we substitued ResNet50 to MobileNet for the multimodal model.

Performance on Test Set
Model Type| Model | F1 Score | Accuracy |
| --- | --- | --- | --- |
| Text | SBERT | 0.43 | 0.45 |
| Text | DistilBERT | 0.48 | 0.45 |
| Image | ResNet50 | 0.45 | 0.48 |
| Image | MobileNet | 0.38 | 0.40 |
| Text & Image | Multimodal | 0.50 | 0.53 |


## Reproducibility
To reproduce our results, please follow the steps below:
1. Clone the repository
1. Install the requirements in `requirements.txt` using `pip install -r requirements.txt`
1. If you cannot access data in `00_source_data` in this repo, download the data from the [Shopee Kaggle competition](https://www.kaggle.com/c/shopee-product-matching/data)
1. Under `10_code`, run `01_train_test_split.ipynb` to split the data into train, validation and test sets
1. Under `10_code`, run `02_Bert_Model.ipynb` to train and use the embeddings from SBERT and DistilBERT
1. Under `10_code`, run `03_ResNet50_Embeddings.ipynb` to train and use the embeddings from ResNet50
1. Under `10_code`, run `04_MobileNet_Embeddings.ipynb` to train and use the embeddings from MobileNet
1. Under `10_code`, run `05_Multimodal_Model_Embeddings.ipynb` to train and use the embeddings from DistilBERT and MobileNet
