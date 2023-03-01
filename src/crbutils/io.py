'''
Utililty functions for data IO

Author: Christopher Bonham
Date: 1st March 2023
'''
import json


def replace_colname_spaces(df):
    '''Replace spaces in dataframe column names with underscores

    Inputs:
        df: Pandas datafranme
            Dataframe to clean

    Outputs:
        Pandas datafranme
            Randomised dataframe
    '''
    df.columns = [x.replace(' ', '_') for x in df.columns]
    return df


def read_config_json(pth, display=False):
    '''Read in a config file (JSON format) and return a dictionary object
    Inputs:
        pth (string)
            Path to config file
        display (boolean default = False)
            Display contents of config JSON to scree
    Outputs:
        dict
            Contents of config file
    '''
    with open(pth, 'r') as fp:
        config = json.load(fp)

    if display:
        print(json.dumps(config, indent=3))

    return config
