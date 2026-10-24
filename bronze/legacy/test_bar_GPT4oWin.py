# https://www.mckinsey.com/~/media/mckinsey/industries/public%20and%20social%20sector/our%20insights/covid%2019s%20effect%20on%20minority%20owned%20small%20businesses%20in%20the%20united%20states/covid-19s-effect-on-minority-owned-small-businesses-in-the-us-final.pdf

#%%
# ChatGPT 4o ~ 거의 유사한 그래프 생성
# 다음 그래프를 생성하는 코드를 작성해주세요.
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Non-Hispanic white', 'Non-Hispanic Asian', 'Hispanic', 'Non-Hispanic Black']
healthy = [37, 29, 22, 17]
stable = [36, 40, 29, 26]
at_risk = [22, 23, 31, 37]
distressed = [5, 8, 18, 20]

# Bar chart configuration
barWidth = 0.5
r1 = np.arange(len(categories))

# Create stacked bars
plt.bar(r1, healthy, color='#9ad2e4', edgecolor='white', width=barWidth, label='Healthy')
plt.bar(r1, stable, bottom=healthy, color='#4fa3d2', edgecolor='white', width=barWidth, label='Stable')
plt.bar(r1, at_risk, bottom=np.array(healthy) + np.array(stable), color='#1a609d', edgecolor='white', width=barWidth, label='At risk')
plt.bar(r1, distressed, bottom=np.array(healthy) + np.array(stable) + np.array(at_risk), color='#092f4b', edgecolor='white', width=barWidth, label='Distressed')

# Add labels and title
plt.xlabel('Type of ownership', fontweight='bold')
plt.ylabel('% of companies', fontweight='bold')
plt.title('Financial-health spectrum by type of ownership')

# Add x-axis categories
plt.xticks(r1, categories)

# Add legend
plt.legend()

# Show the chart
plt.show()


#%%
# Gemini ~ 축적한 바 그래프 실패
# 다음 그래프를 생성하는 코드를 작성해주세요.

import pandas as pd
import matplotlib.pyplot as plt

# 데이터 준비
data = {'Category': ['Healthy', 'Stable', 'At risk', 'Distressed'],
        'Non-Hispanic White': [37, 36, 22, 5],
        'Non-Hispanic Asian': [29, 40, 23, 8],
        'Hispanic': [22, 29, 31, 18],
        'Non-Hispanic Black': [17, 26, 37, 20]}

df = pd.DataFrame(data)

# 그래프 생성
df.plot(x='Category', kind='bar', figsize=(10, 6))
plt.title('Financial-health spectrum by type of ownership')
plt.xlabel('Financial Health')
plt.ylabel('Percentage of Companies')
plt.legend(title='Ownership Type')
plt.show()

"""
코드 설명
plot(): DataFrame에 포함된 데이터를 시각화하는 Pandas의 메소드입니다.
kind='bar': 막대 그래프를 생성하도록 지정합니다.
figsize: 그래프의 크기를 조절합니다.
xlabel, ylabel: x축과 y축의 레이블을 설정합니다.
legend(): 범례를 추가합니다.
추가 기능

색상 지정: 각 막대의 색상을 직접 지정하여 시각적인 차이를 더욱 분명하게 할 수 있습니다.
그래프 스타일 변경: Matplotlib의 다양한 스타일 옵션을 사용하여 그래프의 외형을 변경할 수 있습니다.
데이터 레이블 추가: 각 막대 위에 데이터 값을 표시하여 더욱 상세한 정보를 제공할 수 있습니다.
축 조정: x축 또는 y축의 범위를 조절하여 특정 부분을 강조할 수 있습니다.
"""

# %%
