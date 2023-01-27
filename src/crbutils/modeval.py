
'''
Utililty functions for model evaluation

Author: Christopher Bonham
Date: 27 January 2023
'''


def perf_mets(model_type = "reg"):
    '''Get the performance metrics for a model
    input:
        model_type: Str (default = "reg"). Type of model {reg, binary_class, "multi_class"}
    output:
        None
    '''

    if model_type == "reg":
        print("Regression model")

    if model_type == "binary_class":
        print("Binary classifier model")

    if model_type == "multi_class":
        print("Multyi level classifier model")