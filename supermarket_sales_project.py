# Analyze a year’s worth of supermarket sales to discover trends, top-selling products, and customer behavior.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('supermarket_sales.csv')
print(df.columns.tolist())

# clean the dataset using Pandas (handle missing values, dates, duplicates).

print(df.isnull().sum())

# df['Store ID'].fillna(df['Store ID'].mean(), inplace=True)
df['Store_Area'] = df['Store_Area'].fillna(df['Store_Area'].mean())
df['Items_Available'] = df['Items_Available'].fillna(df['Items_Available'].mean())
df['Daily_Customer_Count'] = df['Daily_Customer_Count'].fillna(df['Daily_Customer_Count'].mean())
df['Store_Sales'] = df['Store_Sales'].fillna(df['Store_Sales'].mean())

df.drop_duplicates(inplace=True)

# Data Exploration
print(df.describe())
corr = df['Store_Area'].corr(df['Store_Sales'])
corr2 = df['Daily_Customer_Count'].corr(df['Store_Sales'])
print("Correlation between Store Area and Sales:", corr)
print("Correlation between Daily_Customer_Count and Sales:", corr2)


df['sales_per_customer'] = df['Store_Sales'] / df['Daily_Customer_Count']
df['sales_per_area'] = df['Store_Sales'] / df['Store_Area']
df.columns = df.columns.str.strip().str.replace(' ', '_')
top_5_stores = df.sort_values('Store_Sales', ascending=False).head(5)
bottom_5_stores = df.sort_values('Store_Sales', ascending=True).head(5)

print("Top 5 stores:\n", top_5_stores[['Store_ID', 'Store_Sales']])
print("Bottom 5 stores:\n", bottom_5_stores[['Store_ID', 'Store_Sales']])

# area_corr = df['Store_Area'].corr(df['Store_Sales'])
#
# customer_corr = df['Daily_Customer_Count'].corr(df['Store_Sales'])
#
#
# print("Correlation between Store Area and Sales:", area_corr)
# print("Correlation between Customers and Sales:", customer_corr)


efficiant_store = df[df['sales_per_area'] > df['sales_per_area'].mean()]

underperforming_stores = df[df['sales_per_area'] < df['sales_per_area'].mean()]


print("Efficient stores:\n", efficiant_store[['Store_ID', 'Store_Area', 'sales_per_area']])
print("Underperforming stores:\n", underperforming_stores[['Store_ID', 'Store_Area', 'sales_per_area']])


high_customer_efficiency = df[df['sales_per_area'] > df['sales_per_area'].mean()]
print(high_customer_efficiency[['Store_ID', 'sales_per_area']])


print(df.info())

plt.bar(df['Store_ID'],df['Store_Sales'], color='red',edgecolor='black')
plt.title("compare sales stores")
plt.xlabel("Store ID")
plt.ylabel("Store Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.scatter(corr,corr2, color='skyblue', s=100)
plt.title("correlation between area & sales")
plt.xlabel("corr")
plt.ylabel("corr2")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


plt.scatter(df['Daily_Customer_Count'],df['Store_Sales'], color='skyblue', s=100)
plt.title("relationship between customers & sales")
plt.xlabel("sales per customer")
plt.ylabel("sales per area")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.hist(df['sales_per_customer'],bins=5, color='orange', edgecolor='black')
plt.show()

fig , axes = plt.subplots(2,2, figsize=(10,8))

axes[0,0].bar(df['Store_ID'],df['Store_Sales'], color='red',edgecolor='black')
axes[0, 0].set_title("Compare sales across stores")
axes[0, 0].legend()
axes[0,0].grid(True)

axes[0,1].scatter(corr,corr2, color='skyblue', s=100)
axes[0,1].set_title("correlation between area & sales")
axes[0,1].set_xlabel("corr")
axes[0,1].set_ylabel("corr2")
axes[0,1].grid(True)

axes[1,0].scatter(df['Daily_Customer_Count'],df['Store_Sales'], color='skyblue', s=100)
axes[1,0].set_title("relationship between customers & sales")
axes[1,0].set_xlabel("sales per area")
axes[1,0].set_ylabel("sales per store")
axes[1,0].grid(True)

axes[1,1].hist(df['sales_per_customer'],bins=5, color='orange', edgecolor='black')
axes[1,1].set_title("distribution of sales per customer")
axes[1,1].grid(True)

plt.tight_layout()
plt.show()

df.to_csv('store_performance_summary.csv', index=False)