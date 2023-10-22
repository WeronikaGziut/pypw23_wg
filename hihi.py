import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [25, 30, 30, 40, 45],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# }
#
# df = pd.DataFrame(data)
# df.to_excel("exampl.xlsx")
# print(df)
df = pd.read_csv("users.csv")
print(df[["ID", "Name"]])
