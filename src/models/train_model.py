# train_model.py
import pathlib
import sys
import yaml
import joblib

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_model(train_features, target, n_estimators, max_depth, seed):
    # Train your machine learning model
    model = RandomForestClassifier()
    model.fit(train_features, target)
    return model

def save_model(model, output_path):
    # Save the trained model to the specified output path
    joblib.dump(model, output_path + '/model.joblib')

def main():

    curr_dir = pathlib.Path(__file__)
    home_dir = curr_dir.parent.parent.parent
    params_file = home_dir.as_posix() + '/params.yaml'
    params = yaml.safe_load(open(params_file))["train_model"]

    input_file = sys.argv[1]
    data_path = home_dir.as_posix() + input_file
    output_path = home_dir.as_posix() + '/data/models'
    
    train_features = pd.read_csv(data_path + '/train.csv')
    X = train_features.iloc[:, 1:30]
    y = train_features.iloc[:, 30:31]

    trained_model = train_model(X, y, params['n_estimators'], params['max_dpeth'], params['seed'])
    save_model(trained_model, output_path)

    

if __name__ == "__main__":
    main()
