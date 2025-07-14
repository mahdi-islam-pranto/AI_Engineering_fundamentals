import numpy as np
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

# Difference between Ridge & Lasso Regression: 
# Ridge regression and Lasso regression are both techniques used for linear regression analysis to prevent overfitting.
# Ridge regression takes all the features into account for making predictions.
# Lasso regression takes a subset of features, not all of them into account for making predictions.
# Ridge regression adds "squared magnitude" of coefficient as penalty term to the loss function.
# Lasso regression adds "absolute value of magnitude" of coefficient as penalty term to the loss function.


# dataset
X = np.array([[2.4 ], [5.5], [4.1], [7.3], [3.2]])
y = np.array([55, 80, 70, 90, 65])

# initialize Ridge model
ridge = Ridge()

ridge.fit(X, y)

y_pred = ridge.predict(X)

print(y_pred)

y_pred_with_new_value = ridge.predict([[8.2]])

print(y_pred_with_new_value)

# initialize Lasso model
lasso = Lasso()

lasso.fit(X, y)

y_pred = lasso.predict(X)

print(y_pred)

y_pred_with_new_value = lasso.predict([[8.2]])

print(y_pred_with_new_value)
