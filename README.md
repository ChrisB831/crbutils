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



### Sort out the CD component
How do I copy a file from the github actions vm to my local machine??  
https://andrewpwheeler.com/2022/05/10/building-wheel-files-in-github-actions/  
https://www.dynamsoft.com/codepool/cpython-barcode-qr-wheel-build-publish.html  
https://pythonprogramming.org/automatically-building-python-package-using-github-actions/  
https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/  
https://www.seanh.cc/2022/05/21/publishing-python-packages-from-github-actions/  

SSH connection between github and local machine
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection?platform=windows

https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#runners
"A runner is a server that runs your workflows when they're triggered. Each runner can run a single job at a time. 
GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners to run your workflows; each workflow run executes in 
a fresh, newly-provisioned virtual machine. GitHub also offers larger runners, which are available in larger 
configurations."

