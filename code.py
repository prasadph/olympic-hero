# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'}, inplace= True)
print(data.head())


# --------------
data['Better_Event'] = np.where(data.Total_Summer > data.Total_Winter, "Summer", "Winter")
data['Better_Event'] = np.where(data.Total_Summer == data.Total_Winter, "Both", data.Better_Event)
better_event = data.Better_Event.value_counts()

better_event = np.argmax(better_event)



# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries = top_countries.iloc[:-1]
def top_ten(top_countries, column):
    country_list = []
    country_list = top_countries.nlargest(10,column)["Country_Name"]
    return list(country_list)

top_10_summer = top_ten(top_countries, "Total_Summer")
top_10_winter = top_ten(top_countries, "Total_Winter")
top_10 = top_ten(top_countries, "Total_Medals")
# top_10
common =set(top_10_summer) & set(top_10_winter) & set(top_10)
common = list(common)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3 , ncols = 1, figsize=(20,10))

ax_1.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
ax_1.set_xlabel('Total Summer')

ax_2.bar(summer_df['Country_Name'],summer_df['Total_Winter'])
ax_2.set_xlabel('Total Winter')

ax_3.bar(summer_df['Country_Name'],summer_df['Total_Medals'])
ax_3.set_xlabel('Total Medals')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
# summer_df[['Golden_Ratio', 'Gold_Summer', 'Total_Summer']]
# summer_df['Gold_Summer']/summer_df['Total_Summer']
z = summer_df.nlargest(n=1,columns=['Golden_Ratio'])
summer_max_ratio = z['Golden_Ratio'].iloc[0]

summer_country_gold = z['Country_Name'].iloc[0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
y = winter_df.nlargest(n=1,columns=['Golden_Ratio'])
winter_max_ratio = y['Golden_Ratio'].iloc[0]
winter_country_gold = y['Country_Name'].iloc[0]

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

x = top_df.nlargest(1,columns=['Golden_Ratio'])
top_max_ratio = x['Golden_Ratio'].iloc[0]
top_country_gold = x['Country_Name'].iloc[0]



# --------------
#Code starts here
data_1 = data.iloc[:-1].copy()
# data_1['Total_Points'] = data_1['Gold_Total']
data_1['Total_Points'] = data_1['Gold_Total']* 3 + data_1['Silver_Total'] *2 + data_1['Bronze_Total']

most_points = data_1['Total_Points'].max()
m = data_1['Total_Points'].idxmax()
best_country = data_1.loc[m,'Country_Name']


# --------------
#Code starts here
best = data[data.Country_Name == best_country]
# best.reset_index(inplace=True, drop=True)
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xticks(rotation=45)
plt.xlabel("United States")
plt.ylabel("Medals Tally")



