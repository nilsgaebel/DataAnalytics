import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data\\gdp.csv")
germany = data[data['Country Name'] == "Germany"]
us = data[data['Country Name'] == "United States"]
china = data[data['Country Name'] == "China"]

plt.plot(germany['Year'], germany['Value'], label="Germany")
plt.plot(us['Year'], us['Value'], label="USA")
plt.plot(china['Year'], china['Value'], label="China")
plt.title("GDP comparison")
plt.legend()
plt.show()
