# line: y = bx + a
    # xbar = average x value
    # ybar = average y value
    # a = y - bx
    # b = (Sample variance)/(Sample Covariance)
    # Sample variance = (sum from 1 to sample size) of (xi - xbar)(yi - ybar)
    # Sample covariance = (sum from 1 to sample size) of (xi - xbar)^2

def calculate_trendline(xData, yData):
    xbar = 0
    ybar = 0
    ahat = 1
    bhat = 1
    sampleVariance = 0
    sampleCovariance = 0

    n = len(xData)

    for i in range(n):
        xbar += xData[i]
        ybar += yData[i]

    xbar = xbar / n
    ybar = ybar / n

    for i in range(n):
        sampleVariance += (xData[i] - xbar)*(yData[i] - ybar)
        sampleCovariance += (xData[i] - xbar)**2

    bhat = sampleVariance / sampleCovariance
    ahat = ybar - (bhat * xbar)

    return [ahat, bhat]