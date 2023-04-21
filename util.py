import pandas as pd
from joblib import load
import pickle
import numpy as np


def encode_features(query_df):
    """
        query_df: dataframe of the query
    """
    # select categorical columns
    categorical_cols = query_df.select_dtypes("object").columns

    ohe = load("model/ohe.joblib")

    # Transform your categorical features into one-hot encoded features
    oh_encoded = ohe.transform(query_df[categorical_cols])

    # Create a new dataframe with the one-hot encoded features
    onehot_encoded_df = pd.DataFrame(oh_encoded, columns=ohe.get_feature_names_out(categorical_cols))

    # concatenate the new and original dataframe
    df_encoded = pd.concat([query_df, onehot_encoded_df], axis=1)

    # remove the original categorical columns from the df
    df_encoded.drop(columns=categorical_cols, axis=1, inplace=True)

    return df_encoded


def suggest_program(query_data):

    # convert to dataframe
    query_df = pd.DataFrame(query_data, index=[0])

    # one hot encode
    query_df_encoded = encode_features(query_df)

    # load the saved model from a file
    with open('model/model.pkl', 'rb') as f:
        model = pickle.load(f)

    # use the model to make predictions on new data
    pred = model.predict(query_df_encoded)

    # load label encoder to get classes
    le = load("model/le.joblib")
    program = le.classes_[pred[0]]

    return program
#
#
# query_data = {
#     "gender": "Female",
#     "age": 21,
#     "grade_aggregate": 16,
#     "dream_job": "Museum Curator",
#     "fav_sub1": "Mathematics",
#     "fav_sub2": "Science",
#     "fav_sub3": "Mathematics",
#     "interest": "Technology",
#     "learning_style": "Logical",
# }
#
# suggested_program = suggest_program(query_data)
# print(suggested_program)