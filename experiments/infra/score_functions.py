from sklearn.metrics import mean_squared_error


def test1(a, b):
    return 1


def test_minus(a, b):
    return a - b


def mse(a, b):
    return mean_squared_error(a, b)
