# Shopee - Price Match Guarantee: Match products with descriptions and images


## Machine learning project
[![CI](https://github.com/nogibjj/Shopee-Price-Match-Guarantee/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Shopee-Price-Match-Guarantee/actions/workflows/main.yml)

#### Duke University (MIDS) - Spring 2023

#### Team Members: [Suzy Anil](https://github.com/sanil72900), [Isha Singh](https://github.com/IshaSingh01), [Alisa Tian](https://github.com/alisa0705), [Dingkun Yang](https://github.com/Yer1k)

----

## Project Overview
A competitive feature amongst retail platforms is product matching which allows companies to offer products at rates competitive to other retailers selling similar products. There are many methods that combine deep learning and traditional machine learning methods to analyze image and text information to calculate similarity between products, however there is little research comparing the effectiveness of integrating multimodal data (product images and descriptions) under this domain (Łukasik et al., 2021). Here, we compare the performance of both unimodal and multimodal models. We trained separate models for text (SBERT and DistilBERT) and images (ResNet50 and MobileNet); the DistilBERT and ResNet50 models outperform the other two in terms of  F1 score and accuracy. The multimodal model used joint embeddings from DistilBERT and MobileNet to predict product labels, which outperformed both unimodal implementations. The integration of product images and titles offer the most useful information to find product matches on a particular platform. 

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



