import pandas as pd
import matplotlib.pyplot as plt

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# ex1
total_revenue = df4['Total_Price'].sum()
print(total_revenue)

# ex2
# most_ordered_product = df4['Product'].value_counts().idxmax()
# print(most_ordered_product)

# ex3
# average_quantity = df4['Quantity'].mean()
# print(average_quantity)

# ex4
# product_sales = df4.groupby('Product')['Total_Price'].sum()
#
# product_sales.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), startangle=90, cmap='viridis')
# plt.title('Distribution of Sales Across Products')
# plt.ylabel('')
# plt.show()
