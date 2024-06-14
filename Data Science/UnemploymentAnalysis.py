import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('Unemployment in India.xlsx')
df['Date'] = pd.to_datetime(df['Date'],format='%d-%m-%Y')

grouped = df.groupby(['Region', 'Area'])
aggregated=grouped.sum(numeric_only=True).reset_index()

plt.subplot(2,2,1)
aggregated['Estimated Unemployment Rate (%)'].hist(bins=5, figsize=(20,15))
plt.grid(False)
plt.title('Histogram of Estimated Unemployment Rate (%)')
plt.xlabel('Estimated Unemployment Rate (%)')
plt.ylabel('Frequency')


plt.subplot(2,2,2)
# bar plot for Region vs Estimated Unemployment Rate

plt.bar(aggregated['Region'],aggregated['Estimated Unemployment Rate (%)'])
plt.title('Region vs Estimated Unemployment Rate (%)')  
plt.xlabel('Region')
plt.xticks(rotation=75)
plt.ylabel('Estimated Unemployment Rate (%)')


plt.subplot(2,2,3)
#bar plot for Area vs Estimated Unemployment Rate

colors = ['red','blue']
plt.bar(aggregated['Area'],aggregated['Estimated Unemployment Rate (%)'],color=colors)
plt.title('Area vs Estimated Unemployment Rate (%)')  
plt.xlabel('Area')
plt.xticks(rotation=90)
plt.ylabel('Estimated Unemployment Rate (%)')



plt.subplot(2,2,4)

min_=aggregated[aggregated['Estimated Unemployment Rate (%)']==aggregated['Estimated Unemployment Rate (%)'].min()]
max_=aggregated[aggregated['Estimated Unemployment Rate (%)']==aggregated['Estimated Unemployment Rate (%)'].max()]
plt.title("Min and Max Estimated Unemployment Rate (%)")  
plt.xlabel('Region & Area')
plt.ylabel('Unemployment Rate (%)')
plt.bar(min_['Region']+" "+min_['Area'],min_['Estimated Unemployment Rate (%)'],color='green')
plt.bar(max_['Region']+" "+max_['Area'],max_['Estimated Unemployment Rate (%)'],color='red')
plt.tight_layout()
plt.show()