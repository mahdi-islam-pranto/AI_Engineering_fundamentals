import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

# Sample dataset
# X represents the features (independent variables): Students hours of study
X = np.array([[2.4 ], [5.5], [4.1], [7.3], [3.2]])
# y represents the target variable (dependent variable): Students marks
y = np.array([55, 80, 70, 90, 65])


# Create a linear regression model
model = LinearRegression()

# Train the model on the dataset (X/y: train the model on student hours of study against their marks)
# Fit the model to the data
model.fit(X,y)

# all predicted data on X
y_pred = model.predict(X)
print(y_pred)

# Predict the marks for a new student who studies for 8 hours
new_student_pred_mark = model.predict([[8.0]])
print("Predicted marks for a new student who studies for 8 hours:", new_student_pred_mark)

# compare real data with predicted data using graph
plt.scatter(X, y, color='blue', label='Actual Marks')
plt.plot(X, y_pred, color='red', label='Predicted Marks')
plt.xlabel('Hours of Study')
plt.ylabel('Marks')
plt.title('Linear Regression: Hours of Study vs. Marks')
plt.legend()
plt.show()