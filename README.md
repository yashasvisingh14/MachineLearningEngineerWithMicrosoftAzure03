# Capstone Project - Machine Learning with Microsoft Azure
## Brief Overview of the Project
For this project, we have used a dataset external to the Azure ML ecosystem from Kaggle. It is supported by Azure ML's automl API. In this task, we will train our models on the dataset and deploy the best model. The binary classification model is trained using Logistic Regression algorithm. The automl.ipynb file trains the model using Automated ML and deploys the best model obtained as a webservice. On the other hand, the hyperparameter_tuning.ipynb file trains the model and perform hyperparameter tuning using HyperDrive. AutoML gives us the better accuracy than HyperDrive. 

## Project Set Up and Installation
In order to set up this project in AzureML, we have to first create a workspace in the Machine Learning Studio with our Azure Subscription. When creating a new workspace, you can either automatically create services needed by the workspace or use existing services. To know more about the multiple ways to set up go through this link.

## Dataset
### Overview
For this project, the dataset chosen is the [Heart Disease UCI](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/heart.csv) csv file from Kaggle. The database contains 14 attributes containing integer and float values. The "target" field refers to the presence of heart disease in the patient (0 or 1). \

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.
The task here to classify the presence of heart disease in a person and thus a binary classification algorithm is required. All the features is being used for training the model and the column 'target' is considered as the target column representing 0 for no trace of heart disease and 1 for presence of heart disease.

Attribute Information -
* age
* sex
* chest pain type (4 values)
* resting blood pressure
* serum cholestoral in mg/dl
* fasting blood sugar > 120 mg/dl
* resting electrocardiographic results (values 0,1,2)
* maximum heart rate achieved
* exercise induced angina
* oldpeak = ST depression induced by exercise relative to rest
* the slope of the peak exercise ST segment
* number of major vessels (0-3) colored by flourosopy
* thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
* target
There were no null or missing values present in the dataset.

### Access
For accessing the data in our workspace, we have uploaded the csv file in our Github repository. Using Raw tab we can obtain the raw URL of the file. This URL can be directly accessed using TabularDatasetFactory module. \
Dataset - https://raw.githubusercontent.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/main/heart.csv

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
