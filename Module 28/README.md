# Vacation Monthly Booking Capacity Predictor

This project delves into Austin's short-term listings using airdna to predict a listings ability to meet 50% montly booking rates. This project will detail the wrangling, eda, preprocessing, training and model metrics performed on the dataset to achieve our objective. Further enhancements can be made to this model to improve upon model accuracy, and details can be found at the 'Reccomendation' section of the 'modeling' Jupyter notebook.


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── assets
    |───|data
    |       |── listing_images <- Image directory used in object detection portion of data preprocessing
    |       |── modified <- Directory where modified listing data through the wrangling and preprocessing were stored
    |       |── orig <- Directory for the original listing data used for this project
    |   |model <- Model files saved from the experiments
    |
    ├── notebooks          <- Jupyter notebooks,
    │   ├── Final_Capstone_Vaction_Rentals.ipynb
    │
    ├── reports             <- Generated analysis as PDF
    │   ├── Final Capstone Project.pdf                    
    │
    └── metrics                <- Folder housing model metrics used in this project.
        └── model_metrics.csv
