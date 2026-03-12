import pandas as pd
from matplotlib import pyplot as plt

# -------------------------------
# Load and filter population data
# -------------------------------
df_pop = pd.read_csv('/Users/shailahriddick/Documents/Labs/populations.csv')
print("Population DataFrame shape:", df_pop.shape)
print(df_pop.head(3))

# Filter for 2024 population
df_pop_2024 = df_pop[['country_code', 'country_name', '2024']]
df_pop_2024.columns = ['country_code', 'country_name', 'Population_2024']
df_pop_2024 = df_pop_2024[df_pop_2024['Population_2024'] >= 2_000_000]
print("Filtered Population DataFrame shape:", df_pop_2024.shape)
print(df_pop_2024.head(3))

# ---------------------------------------------
# Load and filter greenhouse gas emissions data
# ---------------------------------------------
df_ghg = pd.read_csv('/Users/shailahriddick/Documents/Labs/GHG_2025.csv')
print("GHG DataFrame shape:", df_ghg.shape)
print(df_ghg.head(3))

# Filter for 2024 emissions
df_ghg_2024 = df_ghg[['country_code', 'country_name', '2024']]
df_ghg_2024.columns = ['country_code', 'country_name', 'GHG_2024']
print("Filtered GHG DataFrame shape:", df_ghg_2024.shape)
print(df_ghg_2024.head(3))

# ----------------------
# Merge and calculate GHG per capita
# ----------------------
df_merged = pd.merge(df_pop_2024, df_ghg_2024, on='country_code')
print("Merged DataFrame shape:", df_merged.shape)
print(df_merged.head(3))

# Calculate per capita emissions (convert MtCO2e to tCO2e)
df_merged['GHG_per_capita'] = (df_merged['GHG_2024'] * 1_000_000) / df_merged['Population_2024']
print("DataFrame with GHG per capita:")
print(df_merged[['country_name_x', 'Population_2024', 'GHG_2024', 'GHG_per_capita']].head(3))

# --------------------
# Plot: GHG vs Population
# --------------------
plt.figure(figsize=(12, 8))
plt.scatter(df_merged['Population_2024'], df_merged['GHG_2024'])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Population (log scale)')
plt.ylabel('GHG Emissions (MtCO2e)')
plt.title('GHG Emissions vs Population (2024)')
plt.grid(True)
plt.savefig('ghg_vs_population.png')
plt.close()

# -------------------------------
# Plot: GHG per capita vs Population
# -------------------------------
plt.figure(figsize=(12, 8))
plt.scatter(df_merged['Population_2024'], df_merged['GHG_per_capita'])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Population (log scale)')
plt.ylabel('GHG Emissions Per Capita (tCO2e)')
plt.title('GHG Emissions Per Capita vs Population (2024)')
plt.grid(True)
plt.savefig('ghg_vs_population_per_capita.png')
plt.close()

# -------------------------------------
# Bar chart: Top 10 countries by GHG
# -------------------------------------
top_10_ghg = df_merged.nlargest(10, 'GHG_2024')
plt.figure(figsize=(12, 8))
plt.bar(top_10_ghg['country_name_x'], top_10_ghg['GHG_2024'])
plt.xticks(rotation=45, ha='right')
plt.xlabel('Country')
plt.ylabel('GHG Emissions (MtCO2e)')
plt.title('Top 10 Countries by GHG Emissions (2024)')
plt.tight_layout()
plt.savefig('top_10_ghg_emissions.png')
plt.close()

# --------------------------------------------------
# Bar chart: Top 10 countries by GHG per capita
# --------------------------------------------------
top_10_ghg_per_capita = df_merged.nlargest(10, 'GHG_per_capita')
plt.figure(figsize=(12, 8))
plt.bar(top_10_ghg_per_capita['country_name_x'], top_10_ghg_per_capita['GHG_per_capita'])
plt.xticks(rotation=45, ha='right')
plt.xlabel('Country')
plt.ylabel('GHG Emissions per capita (tCO2e)')
plt.title('Top 10 Countries by GHG Emissions Per Capita (2024)')
plt.tight_layout()
plt.savefig('top_10_ghg_per_capita.png')
plt.close()
