import wandb
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer

from src.crbutils import modeval

'''
As we are building model build utility functions a good starting
point would be to build a model long hand and then bit by bit 
replace the long hand code with calls to the utility functions
'''




def download_data():
    '''Import dummy training data from wandb, import to a dataframe
    and write to a .csv file in the data directory.

    Inputs: None
    Returns: None
    '''
    run = wandb.init(project = "nyc_airbnb", job_type="pull_data")
    local_path = wandb.use_artifact("clean_sample.csv:latest").file()
    run.finish()
    df = pd.read_csv(local_path)
    df.to_csv("./data/dev_data_nyc_airbnb.csv", index = False)



def read_data():
    '''Import data from the data directory

    Inputs: None
    Returns: df. Pandas dataframe
    '''
    return pd.read_csv("./data/dev_data_nyc_airbnb.csv")


# Get dev data
df = read_data()

# Extract features and labels
y = df['price']
X = df[['minimum_nights','number_of_reviews','availability_365','reviews_per_month']]

# Fill missings with mean
my_imputer = SimpleImputer(strategy="mean")
X = my_imputer.fit_transform(X)

# Initialise the model (Random forest)
rf_model = RandomForestRegressor()

# Train the model
rf_model.fit(X,y)

# Score the training data
y_pred = rf_model.predict(X)

print(type(y))
print(type(y_pred))
print(y[:5])
print(y_pred[:5])