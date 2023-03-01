# crbutils
A data science, machine and deep learning utility library





# Project structure
```
<root>
├── .github
│	└── workflows
│   	└── main.yml
├── data
├── dist
├── notebooks
├── src
│   └── crbutils (see Package structure)
├── tests
│	├── test_io.py
│	├── test_modeval.py
│	├── test_sample.py
│   └── test_version_match.py
├── main.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── requirements.txt
```

where
| Path | Name | Description |
| :-- | :-- | :-- |
| `.github\workflows` | `main.yml` | CI/CD workflow |
| TBD | TBD | TBD |






# Package structure
```
<root>
├── src
	└── crbutils
		├── io.py
		├── modeval.py
	   	└── sample.py
```

where
| Module | Function | Description |
| :-- | :-- | :-- |
| `io.py` |  | Utility functions supporting data IO |
| `io.py` | read_config_json | Read in a config file (JSON format) and return a dictionary object |
| `io.py` | replace_colname_spaces | Replace spaces in dataframe column names with underscores |
| `modeval.py` |  | Utility functions supporting model evaluation |
| `modeval.py` | performance_metrics | Get the high level performance metrics for a model on train, test and validation samples <br/>Regression: {R2, MAE, MSE, RMSE} <br/>Binary classifier: {Accuracy, Precision, Recall, F1 score, Classification report} <br/>Multi level classifier: {Accuracy, Classification report} |
| `modeval.py` | reg_scattr_plot | Get the actual v predicted scatter plot for train, test and validation dataset |
| `sample.py` |  | Utility functions supporting data sampling |
| `sample.py` | ttv_split (TBD) | Split a data frame into train, test and validation dataset's |
| `sample.py` | randomise | Randomise the order of a dataframe |






NB to minimise load to GDrive, then venv is stored locally at
`C:\Users\Christopher\venvs\crbutils`





# TODO



## Testing
Incorporate test functionality



## Core functionality
**Have a read through my Deliveroo job project and see what I can use from there**

### Sample module

* Get a sample function that takes train_test_split and returns train test AND validation
* Get jumble function - test that var stats still match

### IO module
* Read in a return a json config file

### EDA module
* missings
* distributions
* pandas report

### preprop module 
* clipping
* replace missing

### modeval module
* feat_imp
* lorenz_curve
* gains_curve
* conf_matrix
* Scatter plot
* perf_metrics returns perf metrics based on model
	* ~mae rms r2 etc. for continuous
	* F1 prec recall etc. for binary
	* Accuracy for binary 

