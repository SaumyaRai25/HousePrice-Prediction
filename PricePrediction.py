import numpy as np
from sklearn.linear_model import LinearRegressionimport numpy as np
from sklearn.linear_model import LinearRegression
X_train = np.array([[1000], [1500], [2000], [2500], [3000], [3500]])
y_train = np.array([200, 300, 400, 500, 600, 700])
y_train = np.array([200, 300, 400, 500, 600, 700])
model = LinearRegression()
model.fit(X_train, y_train)
X_test = np.array([[1750], [2300], [2800]])
y_pred = model.predict(X_test)
for i in range(len(X_test)):
    print("Predicted price for house with an area of", X_test[i][0], "sqft:", y_pred[i], "thousand dollars")S