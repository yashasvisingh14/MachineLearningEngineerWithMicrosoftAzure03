# Capstone Project - Machine Learning with Microsoft Azure
## Table of Contents
* [Overview](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#brief-overview-of-the-project)
* [Set Up and Installation](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#project-set-up-and-installation)
* [Dataset](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#dataset)
  * [Overview]( https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#overview) 
  * [Task]( https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#task)
  * [Access]( https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#access)
* [Automated ML](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#automated-ml)
  * [Results]( https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#results)
  * [Best Parameters](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03#best-parameters)
  * [Improvement in Future]( https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#improvments-in-future)
* [Hyperparameter Tuning](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#hyperparameter-tuning)
  * [Results](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#results-1)
  * [Best Parameters](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#best-parameters-1)
  * [Improvements in Future]( https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#improvments-in-future-1)
* [Model Deployment](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#model-deployment)
* [Screen Recording](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/README.md#screen-recording) 
## Architectural Diagram
![AD (1)](https://user-images.githubusercontent.com/64837491/109812996-c2112c80-7c52-11eb-94fb-aaa3d530efb1.jpeg)
## Brief Overview of the Project
For this project, we have used a dataset external to the Azure ML ecosystem from Kaggle. It is supported by Azure ML's automl API. In this task, we will train our models on the dataset and deploy the best model. The binary classification model is trained using Logistic Regression algorithm. The [automl.ipynb](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/automl.ipynb) file trains the model using Automated ML and deploys the best model obtained as a webservice. On the other hand, the [hyperparameter_tuning.ipynb](https://github.com/yashasvisingh14/MachineLearningEngineerWithMicrosoftAzure03/blob/main/hyperparameter_tuning.ipynb) file trains the model and perform hyperparameter tuning using HyperDrive. The AutoML gives us the better accuracy for our model than HyperDrive. 

## Project Set Up and Installation
In order to set up this project in AzureML, we have to first create a workspace in the Machine Learning Studio with our Azure Subscription. When creating a new workspace, you can either automatically create services needed by the workspace or use existing services. To know more about the multiple ways to set up go through this [link](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace?tabs=python).

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
* experiment_timeout_minutes defines how long, in minutes, the experiment should continue to run, in our case its 60 minutes.
* label_column_name is the name of the label column. Here the target column is 'target' which specifies whether a person has heart disease (1) or not (0).
* Retrieved and saved the best automl model(MaxAbsScaler and LightGBM).

### Results
In this experiment, AutoML generated a best fitted model MaxAbsScaler and LightGBM algorithm and has shown an accuracy of 1.00. For some datasets, it is possible for several classifiers to achieve perfect scores. The screenshot of the Best Model Summary is being provided.
![ss4](https://user-images.githubusercontent.com/64837491/109666771-84020300-7b95-11eb-9388-5001b02dfde7.png)
![ss7](https://user-images.githubusercontent.com/64837491/109667701-6aad8680-7b96-11eb-861d-3f4ce1257de5.png)
Here, showing RunDetails Widget in Jupyter Notebook after the experiment is completed.
![ss3](https://user-images.githubusercontent.com/64837491/109667914-a5afba00-7b96-11eb-9cc1-2bfe7880ac08.png)
### Best Parameters
The best run generated the following values for parameters-
* learning_rate=0.1 - A tuning parameter in an optimization algorithm that determines the step size at each iteration.
* n_estimators=100 - The number of trees in the forest.
* n_jobs=1 - Number of CPU cores used when parallelizing over classes.
* random_state=None - Used when solver == ‘sag’, ‘saga’ or ‘liblinear’ to shuffle the data.
* verbose=-10 - Verbosity etc \
![imp4](https://user-images.githubusercontent.com/64837491/109859683-42e81c80-7c83-11eb-9dd6-aac2ebefb0ee.png)
### Improvments in Future
In this project, certain parameters and metrics were used as described above but to gain an improved accuracy we can experiment with them. For classfication experiment we used accuracy as our primary metric which can be replaced with AUC_weighted where AUC is Area under the Receiver Operating Characteristic Curve, the shape of the curve gives an intuition for relationship between TPR and FPR as a function of the classification threshold or decision boundary.For classification experiments, each of the line charts produced for automated ML models can be used to evaluate the model per-class or averaged over all classes. With regression or forecast models we can have different experiment timeout minutes sets and cross validation folds.

## Hyperparameter Tuning
In HyperDrive, we control the model training process by adjusting parameters and finding the configuration of hyperparameters results in the best performance. It uses a fixed machine learning algorithm that is provided.

* Created compute cluster using vm_size of "Standard_D2_V2" in provisioning configuration and max_nodes of 4.
* Specified a parameter sampler i.e RandomParameterSampling, since randomly selects both discrete and continuous hyperparameter values. The benefit of using Random Sampling is that it supports early termination of low peformance runs.
* The two hyperparameters tuned were C and max_iter where max_iter represents maximum number of iterations taken to converge and C is inverse of regularization strength where we create model which underfit or overfit the data according to the values of C. A larger C means less regularization and smaller C means better regularization. With choice(discrete hyperparameter) '--max_iter' takes one of the values (50, 100, 150, 200, 250) and with '--C' : uniform(0.0, 1.0)(continuous hyperparameter) returns a value uniformly distributed between low(0.0) and high(1.0). 
* Specified a policy early stopping policy i.e Bandit Policy, it helps to automatically terminate poorly performing runs based on slack factor.It improves computational efficiency. The benefit is that policy early terminates any runs where the primary metric is not within the specified slack factor with respect to best performing training run.
* The primary metric parameter determines the metric to be used during model training for optimization. In this case where classification scenario is used we provided accuracy as primary metric.
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
![hh4](https://user-images.githubusercontent.com/64837491/109699878-16ff6500-7bb7-11eb-8b65-062b8ceec609.png)
Here, we obtained visualization of different Run Numbers in terms of their Accuracy and other one shows hyperparameters used in our model with Accuracy.
![hh6](https://user-images.githubusercontent.com/64837491/109699789-018a3b00-7bb7-11eb-9fca-13c7547678f7.png)
Here, showing RunDetails Widget in Jupyter Notebook after the experiment is completed.
![hh1](https://user-images.githubusercontent.com/64837491/109699824-0b13a300-7bb7-11eb-9b2d-fb216e8ce459.png)
### Best Parameters
The best run generated the following values for hyperparameters-
* '--C', '0.056669921024075975' - Inverse of regularization strength
* '--max_iter', '150' - maximum number of iterations taken to converge \
![imp5](https://user-images.githubusercontent.com/64837491/109859686-44194980-7c83-11eb-99e0-aff5db93887d.png)
### Improvments in Future
In HyperDrive, we can run model with different parameter sampling methods like Grid sampling used to select discrete values over a search space, Bayesian sampling used to to select values based on how previous values improved the training performance. We can also explore early termination policy which automatically terminate poorly performing runs. Early termination improves computational efficiency. For Logistic Regression, we used C and max_iter as our best suited hyperparameters but it will change based on different algorithms like learning rate for training a neural network, C and sigma hyperparameters for support vector machines etc.


## Model Deployment
The steps to be followed for Deployment.
* Get the best fitted model, save it and display all the properties of the model like Id, Type and Status. 
Save the model using  joblib.dump(model,'outputs/model.joblib') where the Best AutoML model was saved in joblib format.
![ss18](https://user-images.githubusercontent.com/64837491/109674405-e90d2700-7b9c-11eb-9a9f-d137cd4ebb84.png)
* Register the model, create an inference config and deploy the model as a web service.
ACI Module contains functionality for deploying machine learning models as web service endpoints on Azure Container Instances. The recommended deployment pattern is to create a deployment configuration object with the deploy_configuration method and then use it with the deploy method of the Model class as shown below.
For Inference Configuration we used score.py and env.yml file. These files were downloaded as shown below. Since the files have been downloaded, define the inference_config by passing score.py and environment. After the files have been downloaded, we can define the inference_config by passing score.py and env.yml.
![ss19](https://user-images.githubusercontent.com/64837491/109676867-1e1a7900-7b9f-11eb-922f-3168b1cbc72c.png)
* Using enable_app_insights, we have enabled AppInsights logging for the Webservice.
![ss21](https://user-images.githubusercontent.com/64837491/109678475-a9e0d500-7ba0-11eb-935a-dc2163fc3fb1.png)
* Testing our deployed model by sending a request and see if the model gives a reponse in the desired format. The script endpoint.py containing the two sample data instances is used to interact with the endpoint with the help of scoring URI and the key of the deployment. We will obtain the result in form of {"result": [1, 0]} by running endpoint.py. \
![imp2](https://user-images.githubusercontent.com/64837491/109858586-ffd97980-7c81-11eb-9414-653175d569be.png)
![imp3](https://user-images.githubusercontent.com/64837491/109858592-010aa680-7c82-11eb-8e43-46d9ec1593f0.png)\
![ss20](https://user-images.githubusercontent.com/64837491/109678991-2d9ac180-7ba1-11eb-89e0-a5bf190efffb.png)
