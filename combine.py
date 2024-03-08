import pandas as pd

# Replace 'file1.csv' and 'file2.csv' with the actual filenames of your CSV files
file1_path = 'ott_churn_dataset.csv'
file2_path = 'ott_churn_dataset2.csv'
file3_path = 'ott_churn_dataset3.csv'
file4_path = 'ott_churn_dataset4.csv'
file5_path = 'ott_churn_dataset5.csv'

# Read CSV files into pandas DataFrames
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)
df3 = pd.read_csv(file2_path)
df4 = pd.read_csv(file2_path)
df5 = pd.read_csv(file2_path)

# Combine the two DataFrames
combined_df = pd.concat([df1, df2,df3,df4,df5], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined_file.csv', index=False)

