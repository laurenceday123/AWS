# Objectives
- Exploring and Preparing the Data used for building the recommendation system on Sagemaker Notebook Instance
- Building and Training the Recommendation System using  MXNET
- Deploying and Evaluating the Model

## Tools
### Amazon SageMaker
"Amazon SageMaker is a fully managed machine learning service. With SageMaker, data scientists and developers can quickly and easily build and train machine learning models, and then directly deploy them into a production-ready hosted environment. It provides an integrated Jupyter authoring notebook instance for easy access to your data sources for exploration and analysis, so you don't have to manage servers. It also provides common machine learning algorithms that are optimized to run efficiently against extremely large data in a distributed environment. With native support for bring-your-own-algorithms and frameworks, SageMaker offers flexible distributed training options that adjust to your specific workflows. Deploy a model into a secure and scalable environment by launching it with a few clicks from SageMaker Studio or the SageMaker console. "

### Apache MXNet
Open source Deep Learning framework. Includes 8 Language bindings, meaning you can develop in python and export readily to Java, C++, R, Perl, Scala etc. Support for distributed training enables GPU and multi host trianing with near linear scaling efficiency.  
#### Gluon Datasets and Dataloader
API for data loading and handling. Define Dataset and DataLoader instances.
- Dataset includes out of the box handling of image data, for instance
- DataLoader is used to create mini-batches of Dataset samples, for parallelisation to speed up training as well as increased training stability that is inherent in minibatch gradient descent
#### Estimator
Amazon SageMaker has built in support for MXNet making training a simple task. 
Example code for an MXNet estimator using data from an S3 bucket:
```python
mxnet_estimator = MXNet('train.py',
                        instance_type='ml.p2.xlarge',
                        instance_count=1,
                        framework_version='1.6.0',
                        py_version='py3',
                        hyperparameters={'batch-size': 100,
                                         'epochs': 10,
                                         'learning-rate': 0.1})
mxnet_estimator.fit('s3://my_bucket/my_training_data/')
```
#### Gluon Fit API
Provides an easy training interface for Apache MXNet, enabling trianing in a minimum amount of code. Training loops do not need to be defined explicitly, you only need to specify the network architecture, loss function and training data
