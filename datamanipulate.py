import pandas as pd

# Read the CSV file
df = pd.read_csv("Assignment.csv")

# FIX column spacing issues
df.columns = df.columns.str.strip()

# Calculate total games
df["Total Games"] = df["Sumer_Game"] + df["Winter_Games"]

# Calculate combined medal totals
df["Gold_Combined_Total"] = df["Gold"] + df["Gold.1"]
df["Silver_Combined_Total"] = df["Silver"] + df["Silver.1"]
df["Bronze_Combined_Total"] = df["Bronze"] + df["Bronze.1"]

# Calculate overall combined total
df["Combined_Total"] = (
    df["Gold_Combined_Total"] +
    df["Silver_Combined_Total"] +
    df["Bronze_Combined_Total"]
)

# Display the updated DataFrame
print(df)

# Save to new file
df.to_csv("Updated_Assignment.csv", index=False)

print("Data manipulation completed successfully.")