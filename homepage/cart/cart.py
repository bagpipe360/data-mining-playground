


def draw_cart():
    # Import the necessary modules and libraries
    import numpy as np
    from sklearn.tree import DecisionTreeRegressor
    import matplotlib.pyplot as plt

    # Return scatter, two line charts
    graphing_json = {"scatter_plots": {"data": []}, "line_chart_1": [], "line_chart_2": []}
    # Create a random dataset
    rng = np.random.RandomState(1)
    X = np.sort(5 * rng.rand(80, 1), axis=0)
    y = np.sin(X).ravel()
    y[::5] += 3 * (0.5 - rng.rand(16))

    # Fit regression model
    regr_1 = DecisionTreeRegressor(max_depth=2)
    regr_2 = DecisionTreeRegressor(max_depth=5)
    regr_1.fit(X, y)
    regr_2.fit(X, y)

    # Predict
    X_test = list(np.arange(0.0, 5.0, 0.01)[:, np.newaxis])
    y_1 = list(regr_1.predict(X_test))
    y_2 = list(regr_2.predict(X_test))

    for i in range(len(X) - 1):
        graphing_json["scatter_plots"]["data"].append([X[i][0], y[i]])
    for i in range(len(X_test) - 1):
        graphing_json["line_chart_1"].append([X_test[i][0], y_1[i]])
        graphing_json["line_chart_2"].append([X_test[i][0], y_2[i]])

    return graphing_json

