# Objectives
- Build a machine learning-based spam detector API
- Deploy the machine learning application into AWS virtual servers.
## Tools
### Flask
Python web microframework providing minimal structure to form a system from available components. You only use what you need. In this case, we are creating a basic API which enables the client to interact with a Machine Learning model to detect spam. 
### AWS
#### EC2 
Elastic Compute Cloud EC2 is secure, resizable cloud compute servers for running applications on AWS infrastructure
#### Elastic Beanstalk
Service for deployment and scaling of services (in e.g. Python) on servers (Apache, Nginx etc).
Elastic Beanstalk handles:
- Capacity provisioning
- Load Balancing
- Auto scaling
- App Health Monitoring
Elastic Beanstalk is 'Impossible to outgrow', scaling up and down automatically based upon app specific needs.
![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/cgYsx4TSSVaGLMeE0vlW5g_6a34335537e94515bc0c45d9f931a480_aeb-architecture2.png?expiry=1606694400000&hmac=zRrZhYkGDA7XTudCelq3MhIKVrX-v-fqrxCUw_pocQk)

# Step 1: Create and test Flask API with trained model
- A basic spam detection model is created, using a TFIDF vectorizer and logistic regression on the document vectors. 

![Flask App](https://i.imgur.com/9Ds3Uu5.png)

- Postman is used to query the API with input data by making a GET request to the API

![Postman](https://i.imgur.com/sWEqqOS.png)

# Step 2: Configure Elastic Beanstalk
- Elastic beanstalk contains a plethora of options, including scalability, load balancing, capacity, security and more. Creating this was a very simple process
![ElasticBeanstalkScale](https://imgur.com/ec6fe442-a581-457a-8614-c43aa8610333)
![ElasticBeanstalkOptions](https://i.imgur.com/z9003Ch.png)
