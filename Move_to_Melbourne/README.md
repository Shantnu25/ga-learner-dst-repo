# Move to Melbourne

Melbourne housing data's each observation is a different house attribute with various features,
like the number of properties that exist in the suburb, land size, building size,
governing council for the area, real estate agent, price of the house, etc.

The dataset has details of 6830 house entries with 16 features.

You need to predict the Price.

# Problem Statement

To predict the final price of each home in Melbourne.

# Feature Description

Feature  - 	Description

Rooms 	- Number of rooms

Type 	Property type

Price 	Price in dollars (Target Variable)

Method 	Property status

SellerG 	Real Estate Agent

Distance 	Distance from CBD

Postcode 	Code of the area

Bathroom 	Number of Bathrooms

Car 	Number of carspots

Landsize 	Land Size

BuildingArea 	Building Size

YearBuilt 	The year in which home was built

CouncilArea 	Governing council for the area

Longitude 	The angular distance of a place east or west

Regionname 	General Region (West, North West, North, North...

PropertyCount 	PropertyCount|Number of properties that exist ...

# Evaluation metrics

For this particular dataset, we are using r2 score as the evaluation metric. 

r2_score (coefficient of determination) regression score function.

Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse).
A constant model that always predicts the expected value of y, disregarding the input features, would get a score of 0.0.

# Outcomes

In this project, I applied the following concepts:

    Linear Regression
    Polynomial Regressor
    Lasso Regressor
    Ridge Regressor
    R^2 Evaluation Metrics
