import pandas as pd
from matplotlib import pyplot as plt

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# ex1
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print(total_sales)

# ex2
# df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
# highest_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
# print(highest_sales_date)

# ex3
# percentage_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
# print(percentage_change)

# ex4
# import matplotlib.pyplot as plt
# df2.set_index('Date')[['Product_A', 'Product_B', 'Product_C']].plot(figsize=(10, 6))
# plt.title('Sales Trends for Each Product Over Time')
# plt.xlabel('Date')
# plt.ylabel('Sales')
# plt.legend(title='Product')
# plt.grid()
# plt.show()
