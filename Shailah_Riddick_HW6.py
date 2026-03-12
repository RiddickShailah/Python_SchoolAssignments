import pandas as pd
import matplotlib.pyplot as plt

# --------------------------
# Task 1: Read CSV into DataFrame and print shape
# --------------------------
df = pd.read_csv('/Users/shailahriddick/Documents/Labs/car_info.csv')

# Print original columns to help map dynamically
print("Original columns in CSV:", df.columns.tolist())

# Normalize column names: strip spaces, lowercase, replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# --------------------------
# Map expected columns dynamically
# --------------------------
# Function to find the correct column by keyword
def find_column(cols, keyword_list):
    for kw in keyword_list:
        for col in cols:
            if kw in col:
                return col
    return None

cols = df.columns

car_col = find_column(cols, ['car', 'name'])
origin_col = find_column(cols, ['origin', 'country'])
cyl_col = find_column(cols, ['cylinder'])
mpg_col = find_column(cols, ['mpg'])
weight_col = find_column(cols, ['weight'])
disp_col = find_column(cols, ['displacement'])
hp_col = find_column(cols, ['horsepower', 'hp'])

# Convert horsepower to numeric if exists
if hp_col:
    df[hp_col] = pd.to_numeric(df[hp_col], errors='coerce')

print("Shape of the dataframe:", df.shape)
print(f"Mapped columns: car={car_col}, origin={origin_col}, cylinders={cyl_col}, mpg={mpg_col}, weight={weight_col}, displacement={disp_col}, horsepower={hp_col}")

# --------------------------
# Task 2: Japanese cars with V6 engines
# --------------------------
japanese_v6 = df[(df[origin_col].str.lower() == 'japan') & (df[cyl_col] == 6)][car_col].tolist()
print("Japanese v6 cars:", japanese_v6)

# --------------------------
# Task 3: Cars with missing horsepower
# --------------------------
missing_hp = df[df[hp_col].isnull()][car_col].tolist()
print("Cars with missing horsepower data:", missing_hp)

# --------------------------
# Task 4: Number of cars with mpg >= 20
# --------------------------
num_mpg_20 = df[df[mpg_col] >= 20].shape[0]
print("Number of cars having mpg >= 20:", num_mpg_20)

# --------------------------
# Task 5: Car with highest mpg
# --------------------------
max_mpg_car = df[df[mpg_col] == df[mpg_col].max()][car_col].tolist()
print("Most fuel-efficient car:", max_mpg_car)

# --------------------------
# Task 6: Max, min, average weight
# --------------------------
max_weight = df[weight_col].max()
min_weight = df[weight_col].min()
avg_weight = df[weight_col].mean()
print(f"minimum weight: {min_weight}, maximum weight: {max_weight}, average weight: {avg_weight:.2f}")

# --------------------------
# Task 7: Drop rows with missing values
# --------------------------
df_clean = df.dropna()
print("Shape after removing the missing values:", df_clean.shape)

# --------------------------
# Task 8: Pie chart for origin
# --------------------------
country_counts = df_clean[origin_col].str.lower().value_counts()
plt.figure(figsize=(6,6))
plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Cars Manufactured in Different Countries')
plt.show()
plt.close()  # Close the pie chart figure so subplots appear next

# --------------------------
# Task 9: Two vertically stacked subplots
# --------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,10))

# Scatter plot: mpg vs weight
ax1.scatter(df_clean[weight_col], df_clean[mpg_col], color='blue', label='MPG vs Weight')
ax1.set_xlabel('Weight')
ax1.set_ylabel('MPG')
ax1.set_title('MPG vs Weight Scatter Plot')
ax1.legend()

# Line plot: mpg vs displacement
ax2.plot(df_clean[disp_col], df_clean[mpg_col], color='green', marker='o', label='MPG vs Displacement')
ax2.set_xlabel('Displacement')
ax2.set_ylabel('MPG')
ax2.set_title('MPG vs Displacement Line Plot')
ax2.legend()

plt.tight_layout()
plt.show()
plt.close()  # Optional: close subplots after displaying
