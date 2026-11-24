# 1. A boolean filter checks each row against a condition and keeps
#    the rows where the condition is True.
#
# 2. df["revenue"] returns a Series, while df[["revenue"]] returns
#    a DataFrame with one column. The difference matters when an
#    operation expects a Series or a DataFrame.
#
# 3. I would choose pandas because I can save and rerun the same
#    analysis on updated data without repeating each step manually.

import pandas as pd

# Exercise 1: Load the data
df = pd.read_csv("data/retail_sales.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# Exercise 2: Filter by region
south = df[df["region"] == "South"]

print(len(south))
print(south.head())

# Exercise 3: Top 5 by revenue
top_five = df.sort_values("revenue", ascending=False).head(5)

print(top_five)

# Exercise 4: Two-condition filter
big_south = df[
    (df["region"] == "South") & (df["revenue"] > 1000)
]

print(len(big_south))
print(big_south.head())

# Exercise 5: A new column
df["per_unit"] = df["revenue"] / df["quantity"]

print(df.head())
print(df["per_unit"].mean())

# Exercise 6: Unique values
print(df["region"].unique())
print(df["region"].value_counts())

# Exercise 7: Select columns
selected = df[["region", "product", "revenue"]]

print(selected.shape)

# Exercise 8: Save the DataFrame
df.to_csv("data/explored.csv", index=False)