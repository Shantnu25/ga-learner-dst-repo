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

0 	Rooms 	- Number of rooms

1 	Type 	Property type

2 	Price 	Price in dollars (Target Variable)

3 	Method 	Property status

4 	SellerG 	Real Estate Agent

5 	Distance 	Distance from CBD

6 	Postcode 	Code of the area

7 	Bathroom 	Number of Bathrooms

8 	Car 	Number of carspots

9 	Landsize 	Land Size

10 	BuildingArea 	Building Size

11 	YearBuilt 	The year in which home was built

12 	CouncilArea 	Governing council for the area

13 	Longitude 	The angular distance of a place east or west

14 	Regionname 	General Region (West, North West, North, North...

15 	PropertyCount 	PropertyCount|Number of properties that exist ...

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
