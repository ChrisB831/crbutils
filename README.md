# crbutils
A DS utility function library


ref folder with reference data and models for Testing and dev for three model examples
* Continuous
* Binary classifier
* Multilevel classifier

 Folders
 * Raw data
 * Processed data
 * Models 
        
   

NB to minimise load to GDrive, then venv is stored locally at
`C:\Users\Christopher\venvs\crbutils`

# TODO

## CI / CD
* CI func
  * Flake8
  * And pytest
  * Add GHithub actions
* CD func
  * Increment build number
  * Hydra config file
  * Create built distribution and copy to library



## Testing
Incorporate test functionality



## Core functionality
**Have a read through my Deliveroo job project and see what I can use from there**

### Sample module
* Get a sample function that takes train_test_split and returns train test AND validation

### IO module
* Read in a rreturn a json config file

### EDA module
* missings
* distributions
* pandas report

### preprop module 
* clipping
* replace missing

## modeval module
* feat_imp
* lorenz_curve
* gains_curve
* conf_matrix
* Scatter plot
* perf_metrics returns perf metrics based on model
	* ~mae rms r2 etc. for continuous
	* F1 prec recall etc. for binary
	* Accuracy for binary 
