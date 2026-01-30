import pandas as pd
import numpy as np

# Sample DataFrame for transformations
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'sales': [500, 200, 800, np.nan, 1000],
    'date_of_birth': ['1990-01-01', '1985-05-12', '2000-07-19', '1992-03-30', '1988-10-21'],
    'category': ['A', 'B', 'A', 'C', 'B']
}

df = pd.DataFrame(data)

# ---------------------------- 1. Data Cleansing - Handling Missing Values ----------------------------
# Filling missing sales with the mean value
df['sales'] = df['sales'].fillna(df['sales'].mean())

# ---------------------------- 2. Data Aggregation - Summarize Sales ----------------------------
# Grouping by category and calculating the total sales per category
sales_summary = df.groupby('category')['sales'].sum().reset_index()


# ---------------------------- 3. Data Filtering - Removing Rows Based on Condition ----------------------------
# Filtering out rows where sales are below 500
filtered_df = df[df['sales'] >= 500]

# ---------------------------- 4. Data Merging - Joining DataFrames ----------------------------
# Let's create another DataFrame to merge with our original one
additional_data = {
    'id': [1, 2, 3, 4, 5],
    'department': ['HR', 'Finance', 'Engineering', 'Marketing', 'IT']
}
df2 = pd.DataFrame(additional_data)

# Merging df with df2 on 'id'
merged_df = pd.merge(df, df2, on='id', how='left')


# ---------------------------- 5. Data Enrichment - Adding Calculated Columns ----------------------------
# Adding a calculated column for age (assuming date_of_birth is in YYYY-MM-DD format)
df['age'] = pd.to_datetime('today') - pd.to_datetime(df['date_of_birth'])
df['age'] = df['age'].dt.days // 365  # Convert age from days to years

# ---------------------------- 6. Data Transformation - Changing Data Types ----------------------------
# Converting 'sales' to a string type for some reason
df['sales_str'] = df['sales'].astype(str)

# ---------------------------- 8. Data Split - Splitting a Column ----------------------------
# Splitting the 'date_of_birth' into 'year', 'month', 'day'
df[['dob_year', 'dob_month', 'dob_day']] = df['date_of_birth'].str.split('-', expand=True)

# ---------------------------- 9. Data Sorting ----------------------------
# Sorting the DataFrame by sales in descending order
sorted_df = df.sort_values(by='sales', ascending=False)

# ---------------------------- 10. Data Validation - Checking for Duplicates ----------------------------
# Checking for duplicate rows based on 'name'
duplicates = df[df.duplicated(subset=['name'])]


# ---------------------------- 12. Data Concatenation - Concatenate Two Columns ----------------------------
# Concatenating 'name' and 'category' into a new column
df['name_category'] = df['name'] + ' (' + df['category'] + ')'

# ---------------------------- 13. Data Aggregation - Rolling Window Calculation ----------------------------
# Creating a rolling mean of 'sales' over a window of 3 entries
df['sales_rolling_mean'] = df['sales'].rolling(window=3).mean()

# ---------------------------- 14. Data Masking ----------------------------
# Masking 'name' column (display only the first letter of each name)
df['masked_name'] = df['name'].apply(lambda x: x[0] + '*' * (len(x) - 1))

# ---------------------------- 15. Data Pivot - Pivoting a Table ----------------------------
# Pivoting the dataset by 'category' and calculating the sum of 'sales'
pivoted_df = df.pivot_table(values='sales', index='category', aggfunc='sum')

# ---------------------------- 16. Data Reshaping - Unpivoting ----------------------------
# Unpivoting the 'sales' and 'age' columns into a long format
unpivoted_df = pd.melt(df, id_vars=['id', 'name'], value_vars=['sales', 'age'])

# Final DataFrame to see all transformations
final_df = df.copy()

# Save all transformations to CSV for visualization (optional)
df.to_csv('transformed_data.csv', index=False)

# Return all transformations to check results
{
    'original_data': df,
    'sales_summary': sales_summary,
    'filtered_df': filtered_df,
    'merged_df': merged_df,
    'final_df': final_df,
    'pivoted_df': pivoted_df,
    'unpivoted_df': unpivoted_df
}
