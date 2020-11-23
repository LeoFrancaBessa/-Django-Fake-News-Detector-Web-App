# Diabates Predictor Web App :brazil: 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technologies Used](#technologies-used)
  * [Technical Aspect](#technical-aspect)
  * [Machine Learning Model](#machine-learning-model)
  * [Data Collection](#data-collection)
  * [Team](#team)
  * [Credits](#credits)

## Demo
Link: [https://fake-news-detector-lfb.herokuapp.com/](https://fake-news-detector-lfb.herokuapp.com/)

[![](https://i.imgur.com/XuU4Ki1.png)]https://fake-news-detector-lfb.herokuapp.com/)

## Overview
This is a classifation app build in the Django Framework. The program receives a raw text (a news text) as a input, then the text is cleaned and fed to the model, in wich predicts if the text
is a true or fake news.

## Motivation
In this period of political chaos around the world, many news portals took advantage of the polarization to publish fake news to attract more people. 
The problem is because large parts of the people do not know how to distinguish true or false news, and end up disseminating it, causing false accusation, 
reputation murder, and other things. The purpose of this application is to offer a platform on which people can check whether their news is true or false, 
with the help of artificial intelligence.

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png" width=200>](https://scikit-learn.org/stable/) [<img target="_blank" src="https://cdn.iconscout.com/icon/free/png-512/django-2-282855.png" width=170>](https://www.djangoproject.com/) [<img target="_blank" src="https://cdn.iconscout.com/icon/free/png-512/heroku-5-569467.png" width=200>](https://dashboard.heroku.com/apps) 


## Technical Aspect
This project is divided into two parts:
1. Training a machine learning model using Sk-learn.
2. Building and hosting a Django web app on Heroku.


## Machine Learning Model
In this classification problem, many classification techniques were used, and although simple, logistic regression was chosen. For two reasons: the classification metrics were equivalent to other more robust techniques, 
and mainly due to its speed of execution. For more information about the code and the techniques used, check out the Jupyter notebook in the "Machine Learning Model Folder".


## Data Collection
The dataset used was the Fake and real news dataset, available on [Kaggle](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)


## Team
[![Leonardo França Bessa](https://avatars2.githubusercontent.com/u/22757584?s=460&u=34b2e3fde44b13d47ce00e372cf66db078a8e300&v=4)](https://www.linkedin.com/in/leonardo-fran%C3%A7a-2246641a3/) |
-|
[Leonardo França Bessa](https://www.linkedin.com/in/leonardo-fran%C3%A7a-2246641a3/) |)

## Credits
- [Creating a Machine Learning Based Web Application Using Django](https://towardsdatascience.com/creating-a-machine-learning-based-web-application-using-django-5444e0053a09): Withouth this amazing tutorial on how to build a app using Django, I wouldn't be able to develop this.
