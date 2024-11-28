import pandas as pd
from matplotlib import pyplot as plt

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# ex1
average_salary = df3.groupby('Department')['Salary'].mean()
print(average_salary)

# ex2
# most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
# print(most_experienced)

# ex3
# min_salary = df3['Salary'].min()
# df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100
# print(df3)

# ex4
# department_counts = df3['Department'].value_counts()
#
# department_counts.plot(kind='bar', figsize=(8, 6), color='skyblue')
# plt.title('Distribution of Employees Across Departments')
# plt.xlabel('Department')
# plt.ylabel('Number of Employees')
# plt.grid(axis='y')
# plt.show()

