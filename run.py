import pandas as pd

# Reading from "input.xlsx"
df = pd.read_excel(r'input.xlsx')
# print(df)

# Adding new column
df['Client Name'] = ['John', 'Jane', 'Mike', 'Alex', 'Stacey', 'Stan']
# print(df)

# Writing to new / already existing file "output.xlsx"
df.to_excel(r'output.xlsx')
print("Completed.")