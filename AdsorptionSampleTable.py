import pandas as pd
import numpy as np

# ---------- Read & clean ----------
df = pd.read_excel("ammoniatest4.xlsx", engine="openpyxl")  # <-- key change
df.columns = df.columns.str.strip()          # trim stray spaces

df = df.rename(columns={
    "Sample": "ID",
    "Time":   "Time(biochar char)"
})

# Make sure the two critical columns are present
required_cols = {
    "ID", "run time", "influent mg/m^3", "effluent mg/m^3",
    "Flow Rate", "mass(g)", "Biochar Temp", "Time(biochar char)",
    "Feed", "Room Temp", "Relative Humidity"
}
missing = required_cols.difference(df.columns)
if missing:
    raise ValueError(f"Missing columns in CSV: {missing}")

# ---------- Sort & process ----------
df = df.sort_values(by=["ID", "run time"])

results = []
for sample_id, g in df.groupby("ID"):

    time = g["run time"].to_numpy()                 # min
    Cin  = g["influent mg/m^3"].to_numpy()          # mg/m³
    Cout = g["effluent mg/m^3"].to_numpy()

    Q    = g["Flow Rate"].iloc[0]                   # L/s
    m    = g["mass(g)"].iloc[0]                     # g adsorbent

    # optional: convert L → m³ (1 L = 1e-3 m³) right here:
    adsorbed_mass = Q * 1e-3 * np.trapz(Cin - Cout, x=time)

    q = adsorbed_mass / m                           # mg adsorbed per g

    results.append({
        "ID": sample_id,
        "Adsorption Capacity (mg/g)": q,
        "Pyrolysis Temp (C)":        g["Biochar Temp"].iloc[0],
        "Pyrolysis Time (min)":      g["Time(biochar char)"].iloc[0],
        "Feedstock":                 g["Feed"].iloc[0],
        "Room Temp (C)":             g["Room Temp"].iloc[0],
        "Relative Humidity (%)":     g["Relative Humidity"].iloc[0]
    })

results_df = pd.DataFrame(results)
display(results_df)
