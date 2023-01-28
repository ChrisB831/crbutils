'''
Utililty functions for model evaluation

Author: Christopher Bonham
Date: 27 January 2023
'''
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, classification_report


def performance_metrics(
        model_type="reg",
        y_train=None, y_train_p=None,
        y_valid=None, y_valid_p=None,
        y_test=None, y_test_p=None):
    '''Get the high level performance metrics for a model

    input:
        model_type: Str (default = "reg"). Type of model {reg, binary_class, "multi_class"}
        y_train: Pandas series or numpy array (default = None). Traing data labels
        y_train_p: Pandas series or numpy array (default = None). Training data predictions
        y_valid: Pandas series or numpy array (default = None). Validation data label
        y_valid_p: Pandas series or numpy array (default = None). Validation data predictions
        y_test: Pandas series or numpy array (default = None). Validation data labels
        y_test_p: Pandas series or numpy array (default = None). Training data predictions

        In the case of a regressor the iterables represent probabilities
        In the case of a classifier (binary or multileve) the iterables represent class memberships

    output:
        None
    '''
    print("Headline performance metrics")

    if model_type == "reg":
        print("Model R2")
        if y_train is not None and y_train_p is not None:
            print(f"\tTrain:\t\t{r2_score(y_train, y_train_p):.4f}")
        if y_valid is not None and y_valid_p is not None:
            print(f"\tValidation:\t{r2_score(y_valid, y_valid_p):.4f}")
        if y_test is not None and y_test_p is not None:
            print(f"\tTest:\t\t{r2_score(y_test, y_test_p):.4f}")

        print("MAE")
        if y_train is not None and y_train_p is not None:
            print(f"\tTrain:\t\t{mean_absolute_error(y_train, y_train_p):.4f}")
        if y_valid is not None and y_valid_p is not None:
            print(f"\tValidation:\t{mean_absolute_error(y_valid, y_valid_p):.4f}")
        if y_test is not None and y_test_p is not None:
            print(f"\tTest:\t\t{mean_absolute_error(y_test, y_test_p):.4f}")

        print("MSE")
        if y_train is not None and y_train_p is not None:
            print(f"\tTrain:\t\t{mean_squared_error(y_train, y_train_p):.4f}")
        if y_valid is not None and y_valid_p is not None:
            print(f"\tValidation:\t{mean_squared_error(y_valid, y_valid_p):.4f}")
        if y_test is not None and y_test_p is not None:
            print(f"\tTest:\t\t{mean_squared_error(y_test, y_test_p):.4f}")

        print("RMSE")
        if y_train is not None and y_train_p is not None:
            print(f"\tTrain:\t\t{np.sqrt(mean_squared_error(y_train, y_train_p)):.4f}")
        if y_valid is not None and y_valid_p is not None:
            print(f"\tValidation:\t{np.sqrt(mean_squared_error(y_valid, y_valid_p)):.4f}")
        if y_test is not None and y_test_p is not None:
            print(f"\tTest:\t\t{np.sqrt(mean_squared_error(y_test, y_test_p)):.4f}")

    if model_type == "binary_class":
        print("Accuracy")
        if y_train is not None and y_train_p is not None:
            print(f"\tTrain:\t\t{accuracy_score(y_train, y_train_p):.4f}")
        if y_valid is not None and y_valid_p is not None:
            print(f"\tValidation:\t{accuracy_score(y_valid, y_valid_p):.4f}")
        if y_test is not None and y_test_p is not None:
            print(f"\tTest:\t\t{accuracy_score(y_test, y_test_p):.4f}")

        print("Precision")
        if y_train is not None and y_train_p is not None:
            print(f"\tTrain:\t\t{precision_score(y_train, y_train_p):.4f}")
        if y_valid is not None and y_valid_p is not None:
            print(f"\tValidation:\t{precision_score(y_valid, y_valid_p):.4f}")
        if y_test is not None and y_test_p is not None:
            print(f"\tTest:\t\t{precision_score(y_test, y_test_p):.4f}")

        print("Recall")
        if y_train is not None and y_train_p is not None:
            print(f"\tTrain:\t\t{recall_score(y_train, y_train_p):.4f}")
        if y_valid is not None and y_valid_p is not None:
            print(f"\tValidation:\t{recall_score(y_valid, y_valid_p):.4f}")
        if y_test is not None and y_test_p is not None:
            print(f"\tTest:\t\t{recall_score(y_test, y_test_p):.4f}")

        print("F1 score")
        if y_train is not None and y_train_p is not None:
            print(f"\tTrain:\t\t{f1_score(y_train, y_train_p):.4f}")
        if y_valid is not None and y_valid_p is not None:
            print(f"\tValidation:\t{f1_score(y_valid, y_valid_p):.4f}")
        if y_test is not None and y_test_p is not None:
            print(f"\tTest:\t\t{f1_score(y_test, y_test_p):.4f}")

        print("\n\nClassification report")
        if y_train is not None and y_train_p is not None:
            print("\nTrain")
            print(classification_report(y_train, y_train_p, digits=4))
        if y_valid is not None and y_valid_p is not None:
            print("\nValid")
            print(classification_report(y_valid, y_valid_p, digits=4))
        if y_test is not None and y_test_p is not None:
            print("\nTest")
            print(classification_report(y_test, y_test_p, digits=4))

    if model_type == "multi_class":
        print("Accuracy")
        if y_train is not None and y_train_p is not None:
            print(f"\tTrain:\t\t{accuracy_score(y_train, y_train_p):.4f}")
        if y_valid is not None and y_valid_p is not None:
            print(f"\tValidation:\t{accuracy_score(y_valid, y_valid_p):.4f}")
        if y_test is not None and y_test_p is not None:
            print(f"\tTest:\t\t{accuracy_score(y_test, y_test_p):.4f}")

        print("\n\nClassification report")
        if y_train is not None and y_train_p is not None:
            print("\nTrain")
            print(classification_report(y_train, y_train_p, digits=4))
        if y_valid is not None and y_valid_p is not None:
            print("\nValid")
            print(classification_report(y_valid, y_valid_p, digits=4))
        if y_test is not None and y_test_p is not None:
            print("\nTest")
            print(classification_report(y_test, y_test_p, digits=4))

