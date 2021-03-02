# Capstone Project - Machine Learning with Microsoft Azure
## Brief Overview of the Project
For this project, we have used a dataset external to the Azure ML ecosystem from Kaggle. It is supported by Azure ML's automl API. In this task, we will train our models on the dataset and deploy the best model. The binary classification model is trained using Logistic Regression algorithm. The [automl.ipynb](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/automl.ipynb) file trains the model using Automated ML and deploys the best model obtained as a webservice. On the other hand, the [hyperparameter_tuning.ipynb](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/hyperparameter_tuning.ipynb) file trains the model and perform hyperparameter tuning using HyperDrive. The AutoML gives us the better accuracy for our model than HyperDrive. 

## Project Set Up and Installation
In order to set up this project in AzureML, we have to first create a workspace in the Machine Learning Studio with our Azure Subscription. When creating a new workspace, you can either automatically create services needed by the workspace or use existing services. To know more about the multiple ways to set up go through this link.

## Dataset
### Overview
For this project, the dataset chosen is the [Heart Disease UCI](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/heart.csv) csv file from Kaggle. The database contains 14 attributes containing integer and float values. The "target" field refers to the presence of heart disease in the patient (0 or 1). 

### Task
The task here to classify the presence of heart disease in a person and thus a binary classification algorithm is required. All the features is being used for training the model and the column "target" is considered as the target column representing 0 for no trace of heart disease and 1 for presence of heart disease.

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
AutoML creates a number of pipelines in parallel that try different algorithms and parameters for us. It gives us the best model which "fits" our data. It trains and tunes the model using the target metric specified. AutoML implements ML solutions without extensive programming knowledge. It saves time and resources. \
In this project, AutoML was configured using an instance of the AutoMLConfig object. The following parameters were set:

* Task helps us determine the kind of machine learning problem we need to solve. It can be classification, regression, and forecasting.
* The primary metric parameter determines the metric to be used during model training for optimization. In this case where classification scenario is used we provided accuracy as primary metric.
* training_data is the training data to be used within the experiment. Here train_data is a TabularDataset loaded from a CSV file.
* experiment_timeout_minutes defines how long, in minutes, the experiment should continue to run, in our case its 30 minutes.
* n_cross_validations parameter sets number of cross validations to perform, based on the same number of folds.
* label_column_name is the name of the label column. Here the target column is 'target' which specifies whether a person has heart disease (1) or not (0).
* Retrieved and saved the best automl model.

### Results
In this experiment, AutoML generated a model which uses the MaxAbsScaler and LightGBM algorithm and has shown an accuracy of 1.00. For some datasets, it is possible for several classifiers to achieve perfect scores. The screenshot of the Best Model Summary is being provided.
![ss4](https://user-images.githubusercontent.com/64837491/109666771-84020300-7b95-11eb-9388-5001b02dfde7.png)
![ss7](https://user-images.githubusercontent.com/64837491/109667701-6aad8680-7b96-11eb-861d-3f4ce1257de5.png)
Here, showing RunDetails Widget in Jupyter Notebook after the experiment is completed.
![ss3](https://user-images.githubusercontent.com/64837491/109667914-a5afba00-7b96-11eb-9cc1-2bfe7880ac08.png)

In this project, certain parameters and metrics were used as described above but to gain an improved accuracy we can experiment with them. For classfication experiment we used accuracy as our primary metric which can be replaced with AUC_weighted where AUC is Area under the Receiver Operating Characteristic Curve, the shape of the curve gives an intuition for relationship between TPR and FPR as a function of the classification threshold or decision boundary.For classification experiments, each of the line charts produced for automated ML models can be used to evaluate the model per-class or averaged over all classes. With regression or forecast models we can have different experiment timeout minutes sets and cross validation folds.

## Hyperparameter Tuning
In HyperDrive, we control the model training process by adjusting parameters and finding the configuration of hyperparameters results in the best performance. It uses a fixed machine learning algorithm that is provided.

* Created compute cluster using vm_size of "Standard_D2_V2" in provisioning configuration and max_nodes of 4.
* Specified a parameter sampler i.e RandomParameterSampling, since randomly selects both discrete and continuous hyperparameter values. The benefit of using Random Sampling is that it supports early termination of low peformance runs.
* Specified a policy early stopping policy i.e Bandit Policy, it helps to automatically terminate poorly performing runs based on slack factor.It improves computational efficiency. The benefit is that policy early terminates any runs where the primary metric is not within the specified slack factor with respect to best performing training run.
* Created a SKLearn estimator for use with train.py. est = SKLearn(source_directory = "./", compute_target=cpu_cluster, vm_size='STANDARD_D2_V2', entry_script="train.py")
* Created a HyperDriveConfig using the estimator, hyperparameter sampler, and policy with max_total_runs=20 and max_concurrent_runs=4.Used get_best_run_by_primary_metric() method of the run to select best hyperparameters. \
*hyperdrive_run_config = HyperDriveConfig(
    estimator=estimator, 
    hyperparameter_sampling=ps, 
    policy=early_termination_policy, 
    primary_metric_name='Accuracy', 
    primary_metric_goal=PrimaryMetricGoal.MAXIMIZE,
    max_total_runs=20,
    max_concurrent_runs=4)*
 ![ss16](https://user-images.githubusercontent.com/64837491/109670390-15bf3f80-7b99-11eb-8a39-36aa96f544d9.png)

### Results
In this experiment, HyperDrive trained the model with an accuracy of 0.85714 which is quite less than AutoML. The screenshot of the Model Summary is being provided.
![ss14](https://user-images.githubusercontent.com/64837491/109671284-f248c480-7b99-11eb-8f78-a561fce5057d.png)
![ss15](https://user-images.githubusercontent.com/64837491/109671396-0987b200-7b9a-11eb-92d6-db8557c7c2bf.png)
In HyperDrive, we can run model with different parameter sampling methods like Grid sampling used to select discrete values over a search space, Bayesian sampling used to to select values based on how previous values improved the training performance. We can also explore early termination policy which automatically terminate poorly performing runs. Early termination improves computational efficiency.\
Here, showing RunDetails Widget in Jupyter Notebook after the experiment is completed.
![ss17](https://user-images.githubusercontent.com/64837491/109672490-1a84f300-7b9b-11eb-9c69-d6c5a6290c1f.png)

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.
Below steps are to be followed for model deployment.

* Get the best fitted model, save it and display all the properties of the model like Id, Type and Status. 
Save the model using joblib.dump(fitted_model, filename="outputs/automl-model.pkl") where the Best AutoML model was saved in pickle format.
![ss18](https://user-images.githubusercontent.com/64837491/109674405-e90d2700-7b9c-11eb-9a9f-d137cd4ebb84.png)
* Register the model, create an inference config and deploy the model as a web service.
ACI Module contains functionality for deploying machine learning models as web service endpoints on Azure Container Instances. The recommended deployment pattern is to create a deployment configuration object with the deploy_configuration method and then use it with the deploy method of the Model class as shown below.
For Inference Configuration we used score.py and env.yml file. These files were downloaded as shown below. Since the files have been downloaded, define the inference_config by passing score.py and environment. After the files have been downloaded, we can define the inference_config by passing score.py and env.yml.
![ss19](https://user-images.githubusercontent.com/64837491/109676867-1e1a7900-7b9f-11eb-922f-3168b1cbc72c.png)
* Using enable_app_insights, we have enabled AppInsights logging for the Webservice.


* Testing our deployed model by sending a request and see if the model gives a reponse in the desired format. We will obtain the result in form of {"result": [1, 0]} by running endpoint.py.


## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response
