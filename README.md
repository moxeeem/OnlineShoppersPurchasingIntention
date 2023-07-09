# 🛍️ Online Shoppers Purchasing Intention
[![readme.jpg](https://anopic.ag/WvbX82bzV78Bf6eN2rSZr9hhPvu3mD85D4YeV5PB.jpg)](https://anopic.ag/WvbX82bzV78Bf6eN2rSZr9hhPvu3mD85D4YeV5PB.jpg)

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
Coming soon

## Dataset
We obtained the dataset for our analysis from the [UC Irvine Machine Learning Repository](https://archive-beta.ics.uci.edu/), which provides the original dataset at this [link](https://archive-beta.ics.uci.edu/ml/datasets/online+shoppers+purchasing+intention+dataset).
The dataset consists of rows that represent visit "sessions" of users on an e-commerce website, with each row containing a feature vector of corresponding data. To ensure uniqueness of users over a 1-year period, the dataset was specifically structured so that each session belongs to a unique user. The total number of sessions in the dataset is 12,330.


**Target Variable**
- `Revenue` (categorical, bool) : whether the user has made a purchase

**All features**

| Feature                   | Description                                                                                                | Type             |
|---------------------------|------------------------------------------------------------------------------------------------------------|------------------|
| `Revenue`                 | TARGET LABEL: Whether the visitor made a purchase (True) or not (False)                                    | Boolean          |
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
Coming soon

## ML Model
Coming soon

## Deployment
Coming soon

## How to Install and Run the Project
Coming soon

## How to Use the Project
Coming soon

## Include Credits

### Author
- Maxim Ivanov - [GitHub](https://github.com/moxeeem)

This project was completed as part of the ["Разведочный анализ данных и основы разработки"](https://stepik.org/course/177213) course offered by [AI Education](https://stepik.org/users/628121134).

## License
Coming soon
