- Source : https://www.youtube.com/watch?v=7eh4d6sabA0&t=744s&ab_channel=ProgrammingwithMosh
- Get data set from popular website. https://www.kaggle.com/
    - search for 'vidio game sale' and download the first data setw which as 16K records and put it in project folder

# Jupiter note book
- Allows to code in web browser. it runs on port 8888
- OPEN EXISTING SOURCE CODE:
    + you can simply select the file with .ipynb to open the source code and you can edit.
- CREATE A MODEL FROM THE SOURCE CODE:
    + you can use the 'Joblib' class or any other similar one to create a model from the source code.
    + you can see the example in the 'music_recommondation' project folder.
- LOAD A EXSISING MODEL:
    + You can simply load trained model and use it without the source code of it.
    + In the example 'load_existing_model' folder you can find how this works.
- in Jupyter notebook on each cell (block where you write code) if it's green on the side it means this is 
    selected for edit and if you press ESC it will turn into blue. now you can use some key board commands to do some works like below.
    - to insert new block below. in blue color (commnad mode) press 'B' or for above press 'A'
    - to delete a block press 'D' twice
- every time you run code it will only execute code in current block. this will save lot of time in big proejct. 
    but if you want to run all block. go to 'cell' menu and clik 'run all' or 'run above' or 'run below'
- to see all available attibures available for an object. press 'tab' after <objectname>. eg. df.
-  to get help for function arguments and it's usage. click on the function name and press shift+tab.
- if you want to run a block multiple times. you can go into command mode and ctl+enter for every time.
- for comment ctl+/ for uncomment use the same.


# Machine Learning Major Hirarchial Structure:

- Artificial Inteligence

    - Supervised Learning
        * It uses labled input and output data
        * learn mapping btw input and output based on labeled example as we already know the expected o/p
        * Predict or classicy based on known examples
        * Labeles aer required for training
        * This model is evaluated by it's accuracy, precision, etc.
        * This is commonly used thatn unsupervised learing. This model is more accurate and efficient.
        * Working with larger data set is complex but gives more accurate result and trust worthy.

            - Classification
                - Decision Tree
                - Random Forest
            - Regression
                - Linear Regression
                - Logistic Regression

    - Unsupervised Learning
        * It doesn't require labled data
        * It discovers patterns and structures in data without labels
        * discovers inherent structure, grouping or relationships
        * This model is evaluated specific to technique used. Eg, Clustering quality
        * This models can be relatively simpler due to un use of labeled data
        * This can be used for data with no lables and can be used to find hidden patterns and structures.
        * This can be used with larger volume and variety of data.

            - Clustering
            - Associating
            - Dimensionality Reduction

    - Semi Supervised Learning
        * Training data set can be both labeled or un labeled data. For eg. data set with partially labeled.

# NUERAL NETWORK
- INTRODUCTION:
- A singl nueron is called Perceptron. it takes

# DATA PRE PROCESSING MAJOR STEPS:
- Data Collection: Gather the relevant data from various sources, such as databases, files, APIs, or web scraping. Ensure that the collected data is representative of the problem you are trying to solve and includes the necessary features or attributes.

- Data Cleaning: This step focuses on identifying and handling missing values, noisy data, or outliers. Common techniques include imputing missing values, removing or correcting outliers, and handling inconsistencies in the data.

- Data Exploration and Visualization: Perform exploratory data analysis (EDA) to gain insights into the data. Explore the statistical summaries, visualize the distributions, and plot relationships between variables. This step helps identify patterns, correlations, or anomalies in the data and guides subsequent preprocessing steps. For eg, you can visualise table of data in bigquery using BI tools like looker, google studio python libraties, etc.

- Feature Selection: Selecting the subset of relevant features that are most informative for the machine learning task. This can involve removing irrelevant or redundant features to reduce dimensionality and improve model performance.

- Dimensionality Reduction: Apply dimensionality reduction techniques, such as Principal Component Analysis (PCA) or feature selection algorithms, to further reduce the number of features while preserving the most important information. This step helps alleviate the curse of dimensionality and can improve the efficiency and performance of machine learning models.

- Feature Encoding: Converting categorical or text features into numerical representations that can be understood by machine learning models. This can include techniques such as one-hot encoding, label encoding, or embedding for textual data.

- Feature Scaling: Ensuring that the numerical features are on similar scales to prevent some features from dominating others. Techniques like standardization (mean=0, variance=1) or normalization to a specific range (e.g., 0 to 1) can be applied.

- Handling Imbalanced Data: Addressing class imbalance issues when the distribution of target classes is skewed. Techniques like oversampling the minority class, undersampling the majority class, or using synthetic data generation methods can help balance the class distribution.

- Handling Missing Data: Decide on an appropriate strategy for handling missing data, such as imputing missing values, removing rows or columns with missing data, or treating missing values as a separate category. The approach depends on the extent and nature of the missing data.

- Data Splitting: Dividing the dataset into training, validation, and testing sets. The training set is used to train the model, the validation set is used for tuning hyperparameters, and the testing set is used for evaluating the final model's performance.

- Data Transformation: Applying mathematical transformations to the data to make it more suitable for the machine learning algorithms. This can involve techniques like log transformation, power transformation, or scaling to meet the assumptions of the models.

- Handling Time-Series Data: If dealing with time-series data, additional preprocessing steps may be required, such as resampling, lagging, or rolling window operations to capture temporal patterns.

- You can also add some additional colums if you needed like unique id for each row.


# SCIKIT LEARN:
- Primarily focused on traditional machine learning algorithms and tasks, such as classification, regression, and clustering.
- Well-suited for small to medium-sized datasets and traditional feature engineering. Because, it loads entire dataset
    into momory that may lead to memory error. Also, as dataset grows the computational efficiency will be degraded.
- Integrates well with other scientific computing libraries in Python, such as NumPy and SciPy.
- Supports model evaluation, hyperparameter tuning, and feature preprocessing.

# TENSOR FLOW:
- Primarily focused on deep learning and neural network-based algorithms.
- Well-suited for large-scale datasets and complex deep learning architectures.
- Provides seamless integration with other deep learning frameworks and libraries, such as Keras and PyTorch.
- Provides extensive capabilities for model training, inference, and deployment in production environments.



# BIG QUERY IN GCP:
- helps to store and analyse structure and unstrucred data including images

# Machine learning process
- steps
    - import data
    - clean the data
    - feature engineering
    - split data into Training / Teast sets
    - create model
    - train the model
    - make predictions
    - evaluate and improve


## ----------- DEPLOYMENT ------------------ ##

# ML Model Production Deployment Options
- REST Api
    - Write a flask application with rest api and some front-end.
    - put that in a docker
    - deploy to GCP, cloud run, app engine, EC2, K8s  etc.
- Deploy on edge (eg, Arudium, RasberryPi)
