import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Hourly, Daily
# pip install meteostat



# Set time period
start = datetime(2022, 1, 1)
end = datetime(2022, 12, 31)

# 中央公园的坐标
tpr = Point(40.78325, -73.96565)

# Get daily data for 2018
dataHourly = Hourly(tpr, start, end)
dataHourly = dataHourly.fetch()
dataHourly.reset_index(inplace=True)

dataHourly = pd.DataFrame(dataHourly)

dataHourly.to_csv('weather_hourly_2022.csv', index=False)

dataDaily = Daily(tpr, start, end)
dataDaily = dataDaily.fetch()
dataDaily.reset_index(inplace=True)

dataDaily = pd.DataFrame(dataDaily)

dataDaily.to_csv('weather_daily_2022.csv', index=False)

#https://dev.meteostat.net/python/hourly.html#data-structure 对照datastructure看