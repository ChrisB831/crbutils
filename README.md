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
        

** Have a read through tmy Deliveroo job project and see what I can use from there **

Package library
* eda
  * missings
  * distributions
  * pandas report
* preprop (general preprocessing)
  * clipping
  * replace missing
* utils (general functionality)
* modeval
  * feat_imp
  * lorenz_curve
  * gains_curve
  * conf_matrix
  * Scatter plot
  * perf_metrics returns perf metrics based on model
    * ~mae rms r2 etc. for continuous
    * F1 prec recall etc. for binary
    * Accuracy for binary 
