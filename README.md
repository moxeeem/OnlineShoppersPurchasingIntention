# 🛍️ Online Shoppers Purchasing Intention
![img.png](https://github.com/moxeeem/OnlineShoppersPurchasingIntention/blob/main/img.png)

## Project Description
In this project, we use machine learning models to analyze e-commerce data in order to determine the probability of a website visitor making a purchase.

The purpose of the project is to conduct exploratory data analysis, build one or more models to solve the task, interpret model forecasts, create an interactive dashboard and wrap it in a docker container.

## Table of Contents

- [Project Description](#project-description)
- [Files](#files)
- [Dataset](#dataset)
- [ML Model](#ml-model)
- [Deployment](#deployment)
- [How to Install and Run the Project](#how-to-install-and-run-the-project)
- [How to Use the Project](#how-to-use-the-project)
- [Include Credits](#include-credits)
- [License](#license)

## Files
- [EDA.ipynb](https://github.com/moxeeem/OnlineShoppersPurchasingIntention/blob/main/EDA.ipynb) : Jupyter Notebook with Exploratory Data Analysis
- [pipeline.ipynb](https://github.com/moxeeem/OnlineShoppersPurchasingIntention/blob/main/pipeline.ipynb) : Jupyter Notebook with ML pipeline
- [dashboard.html](https://github.com/moxeeem/OnlineShoppersPurchasingIntention/blob/main/dashboard.html) : HTML ExplainerDashboard
- [Dockerfile](https://github.com/moxeeem/OnlineShoppersPurchasingIntention/blob/main/Dockerfile) : File for creating a Docker Container with ExplainerDashboard 
- [app.py](https://github.com/moxeeem/OnlineShoppersPurchasingIntention/blob/main/app/app.py) : File that generates the dashboard
- [dashboard.py](https://github.com/moxeeem/OnlineShoppersPurchasingIntention/blob/main/app/dashboard.py) : File that launches the dashboard

## Dataset
We obtained the dataset for our analysis from the [UC Irvine Machine Learning Repository](https://archive-beta.ics.uci.edu/), which provides the original dataset at this [link](https://archive-beta.ics.uci.edu/ml/datasets/online+shoppers+purchasing+intention+dataset).
The dataset consists of rows that represent visit "sessions" of users on an e-commerce website, with each row containing a feature vector of corresponding data. To ensure uniqueness of users over a 1-year period, the dataset was specifically structured so that each session belongs to a unique user. The total number of sessions in the dataset is 12,330.


**Target Variable**
- `Revenue` (categorical, bool) : whether the user has made a purchase

**All features**

| Feature                   | Description                                                                                                | Type             |
|---------------------------|------------------------------------------------------------------------------------------------------------|------------------|
| `Revenue`                 | TARGET LABEL: whether the visitor made a purchase (True) or not (False)                                    | Categorical, boolean   |
| `Administrative`          | the number of pages of this type (administarive) that the user visited                                     | Numerical, int   |
| `Administrative_Duration` | the amount of time spent in this category (administarive) of pages                                         | Numerical, float |
| `Informational`           | the number of pages of this type (informational) that the user visited                                     | Numerical, int   |
| `Informational_Duration`  | the amount of time spent in this category (informational) of pages                                         | Numerical, float |
| `ProductRelated`          | the number of pages of this type (product related) that the user visited                                   | Numerical, int   |
| `ProductRelated_Duration` | the amount of time spent in this category (product related) of pages                                       | Numerical, float |
| `BounceRates`             | the percentage of visitors who enter the website through that page and exit without triggering any additional tasks (characteristic of Google Analytics)                  | Numerical, float |
| `ExitRates`               | the percentage of pageviews on the website that end at that specific page (characteristic of Google Analytics)                    | Numerical, float  |
| `PageValues`              | the average value of the page averaged over the value of the target page and/or the completion of an eCommerce (characteristic of Google Analytics)                    | Numerical, float |
| `SpecialDay`              | the closeness of the visiting site to a specific special day (e.g. Mother's Day)                           | Numerical, float |
| `Month`                   | the month of the year of the visiting site                                                                 | Categorical, object |
| `OperatingSystems`        | user's operating system                                                                                    | Categorical, int |
| `Browser`                 | user's browser                                                                                             | Categorical, int |
| `Region`                  | user's region                                                                                              | Categorical, int |
| `TrafficType`             | the type of traffic the brought the visitor to the website                                                 | Categorical, int |
| `VisitorType`             | visitor type (Returning_Visitor or New_Visitor or Other)                                                   | Categorical, object |
| `Weekend`                 | is the visit day a weekend                                                                                 | Categorical, boolean |

## Analysis
In this project, we perform primary data analysis and research before starting modeling and prediction. We use EDA to identify the main characteristics of our data and test the assumptions on which we will build our model.

During EDA, we analyze the distribution of data, identify outliers, duplicates, missing values, and plot graphs to visually assess the relationships between different variables. We also analyze the values of various correlations and the results of Pearson's chi-squared test.

## ML Model
In this project, we have built several models that solve the problem.

We settled on the NB model with hyperparameters selected by GridSearchCV. f1-score was chosen as the target metric. Also, the variables were encoded using ONE and standardized using StandardScaler.

## Deployment
In this project, we built an interactive dashboard and wrapped it in a docker container.

Using Docker, we created a Dockerfile that contains all the necessary instructions to build a container with our dashboard.

## How to Install and Run the Project
Please note that you need to have Docker on your computer to perform the above steps. If you do not have it, please install Docker before starting the process.

To start the dashboard, follow these steps:

1. Open a terminal on your computer.

2. Download the image from Docker Hub by running the command:
```
$ docker pull moxeeeem/explainerdashboard
```
This will download the dashboard image to your computer.

3. Pull up the container from the downloaded image by running the command:
```
$ docker run moxeeeem/explainerdashboard
```
This will create and start the dashboard container.

4. A link will appear in the terminal. Copy this link and paste it into the address bar of your web browser.

After clicking the link, you will see the dashboard open in your web browser. You can now view and use the dashboard to analyze the data.


## How to Use the Project
This dashboard allows you to investigate SWAP values, permutation importances, interaction effect, partial dependence plots, all kinds of performance plots, 
and even individual decision trees inside a random forest.

## Include Credits

### Author
- Maxim Ivanov - [GitHub](https://github.com/moxeeem), [Telegram](https://t.me/fwznn_ql1d_8)

This project was completed as part of the ["Разведочный анализ данных и основы разработки"](https://stepik.org/course/177213) course offered by [AI Education](https://stepik.org/users/628121134).

## License
This project is licensed under the MIT license. For more information, see the [LICENSE](/LICENSE) file.
