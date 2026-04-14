'''
PART 1: PRE-PROCESSING
- Tailor the code scaffolding below to load and process the data
- Write the functions below
    - Further info and hints are provided in the docstrings
    - These should return values when called by the main.py
'''

import pandas as pd

def load_data():
    '''
    Load data from CSV files
    
    Returns:
        model_pred_df (pd.DataFrame): DataFrame containing model predictions
        genres_df (pd.DataFrame): DataFrame containing genre information
    '''
    genres_df=pd.read_csv("data/genres.csv")
    model_pred_df = pd.read_csv("data/prediction_model_03.csv")
    return genres_df, model_pred_df

def process_data(model_pred_df, genres_df):
    '''
    Process data to get genre lists and count dictionaries
    
    Returns:
        genre_list (list): List of unique genres
        genre_true_counts (dict): Dictionary of true genre counts
        genre_tp_counts (dict): Dictionary of true positive genre counts
        genre_fp_counts (dict): Dictionary of false positive genre counts
    '''

    genre_list=list(genres_df["genre"])
    
    genre_true_counts={}
    genre_tp_counts = {}
    genre_fp_counts={}
    
    for genre in genre_list:
        genre_true_counts[genre]=0
        genre_tp_counts[genre]=0
        genre_fp_counts[genre]=0
    
    for movie_index in range(len(model_pred_df)):
        movie_genre= model_pred_df.iloc[movie_index]
        predicted_genre= movie_genre["predicted"]
        correct_movie_genre= movie_genre["correct?"]

        #actual genres column in the prediction model df holds a string that gives to a list of genres of a movie so to compare I will ned to cleaan it
        clean_actual_genre= movie_genre["actual genres"].replace("'", ""). replace("]","").replace("[", "").split(",")
        
        for genre in clean_actual_genre:
            if genre in genre_true_counts:
                genre_true_counts[genre]+=1
        if predicted_genre in genre_list:
            if correct_movie_genre == 1:
                genre_tp_counts[predicted_genre]+=1
            else:
                genre_fp_counts[predicted_genre]+=1
    return genre_list, genre_true_counts, genre_tp_counts, genre_fp_counts
        