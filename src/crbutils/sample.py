'''
Utililty functions for sampling

Author: Christopher Bonham
Date: 1st March 2023
'''


def ttv_split():
    '''Split dataframe into train test and validation

    Inputs:
        df: Pandas datafranme
            Dataframe to randomise

    Outputs:
        Pandas datafranme
            Randomised dataframe
    '''
    ...


def randomise(df):
    '''Randomise the order of a dataframe

    Inputs:
        df: Pandas datafranme
            Dataframe to randomise

    Outputs:
        Pandas datafranme
            Randomised dataframe
    '''
    return df.sample(frac=1.0).reset_index(drop=True)
