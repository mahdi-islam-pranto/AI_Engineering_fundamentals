import pandas as pd

# Step 1: Create the data as a list of dictionaries
data = [
    {"Name": "John", "Age": 25, "Email": "john@example.com", "Salary": 50000},
    {"Name": None, "Age": 29, "Email": "missing", "Salary": 55000},
    {"Name": "Linda", "Age": None, "Email": "linda@example.com", "Salary": None},
    {"Name": "Mike", "Age": 22, "Email": "mike@example.com", "Salary": 48000}
]

# Step 2: Create a DataFrame from the data
df = pd.DataFrame(data)
print(df)

# Step 3: Save to CSV
df.to_csv("people_data.csv", index=False)
print(" CSV saved as 'people_data.csv'")

# Step 4: Load from CSV
df = pd.read_csv("people_data.csv")
# print(df)

# print sum of missing values
print(df.isnull().sum())

# Step 5: Handle missing values
df["Name"].fillna("Unknown", inplace=True) # replace missing values with "Unknown"
df["Age"].fillna(df["Age"].mean(), inplace=True) # replace missing values with mean
df["Salary"].fillna(0, inplace=True) # replace missing values with 0
df["Email"].replace("missing", "unknown@example.com", inplace=True) # replace "missing" with "unknown@example.com"

# remove duplicates
df.drop_duplicates(inplace=True)

# Step 6: Save to CSV
df.to_csv("cleaned_people_data.csv", index=False)
print("Cleaned CSV saved as 'cleaned_people_data.csv'")
