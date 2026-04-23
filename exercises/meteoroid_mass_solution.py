import pandas as pd
import numpy as np

# -----------------------------------
# Load CNEOS dataset
# -----------------------------------
df = pd.read_csv("../data/raw/cneos_fireball_sample.csv")

# -----------------------------------
# Unit conversions
# -----------------------------------
# impact energy: kilotons → Joules
df["E_J"] = df["impact_energy_kt"] * 4.184e12

# velocity: km/s → m/s
df["v_ms"] = df["velocity_km_s"] * 1000

# -----------------------------------
# Mass estimation
# m = 2E / v^2
# -----------------------------------
df["mass_kg"] = (2 * df["E_J"]) / (df["v_ms"] ** 2)

# -----------------------------------
# Results summary
# -----------------------------------
print("\n=== METEOROID MASS ESTIMATION ===")
print("Number of events:", len(df))
print("Mean mass (kg):", df["mass_kg"].mean())
print("Median mass (kg):", df["mass_kg"].median())
print("Max mass (kg):", df["mass_kg"].max())
print("Min mass (kg):", df["mass_kg"].min())

# -----------------------------------
# Save processed dataset
# -----------------------------------
df.to_csv("../data/processed/fireball_mass_estimates.csv", index=False)

print("\nProcessed dataset saved successfully.")