#%%
# GPT4o
import matplotlib.pyplot as plt
import numpy as np

# Data for the graph, based on the image provided
years = np.arange(2019, 2024)
share_of_hours = {
    "Spain": [5, 10, 15, 30, 45],
    "Germany": [2, 5, 7, 20, 40],
    "France": [1, 3, 5, 15, 35],
    "Belgium": [0, 2, 5, 10, 25],
    "The Netherlands": [0, 0, 2, 5, 15],
    "Italy": [0, 0, 1, 5, 10]
}

# Colors corresponding to the legend in the image
colors = {
    "Spain": "navy",
    "Germany": "deepskyblue",
    "France": "blue",
    "Belgium": "teal",
    "The Netherlands": "purple",
    "Italy": "dodgerblue"
}

# Plotting the data
plt.figure(figsize=(10, 6))
for country, values in share_of_hours.items():
    plt.plot(years, values, label=country, color=colors[country], linestyle='-' if country != 'Italy' else '--')

# Adding labels and title
plt.title('Day-ahead electricity prices are falling below the costs of gas and CO₂.')
plt.xlabel('Years')
plt.ylabel('Share of hours with electricity prices below gas and CO₂, %')
plt.legend(title='Countries')

# Show plot
plt.grid(True)
plt.show()

#%%
# Gemini
import matplotlib.pyplot as plt
import pandas as pd

# 가상 데이터 생성 (실제 데이터로 대체해야 함)
data = {'Year': [2019, 2020, 2021, 2022, 2023],
        'Spain': [45, 48, 42, 38, 50],
        'Germany': [40, 42, 39, 36, 45],
        'France': [38, 40, 37, 34, 42],
        'Belgium': [42, 44, 41, 38, 43],
        'The Netherlands': [41, 43, 40, 37, 42],
        'Italy': [35, 37, 34, 31, 38]}
df = pd.DataFrame(data)

# 그래프 생성
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Spain'], label='Spain')
plt.plot(df['Year'], df['Germany'], label='Germany')
plt.plot(df['Year'], df['France'], label='France')
plt.plot(df['Year'], df['Belgium'], label='Belgium')
plt.plot(df['Year'], df['The Netherlands'], label='The Netherlands')
plt.plot(df['Year'], df['Italy'], label='Italy', linestyle='--')

# 그래프 설정
plt.title('Day-ahead electricity prices are falling below the costs of gas and CO2')
plt.xlabel('Year')
plt.ylabel('Share of hours with electricity prices below gas and CO2, %')
plt.ylim(0, 50)
plt.legend()
plt.grid(True)

# 이미지 저장
# plt.savefig('electricity_prices.png')
plt.show()
# %%
