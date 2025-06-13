# Ammonia Adsorption on Acid-Activated Biochar
_Toward a low-cost, farm-scale alternative to wet scrubbers_

## Project Aim
Agricultural activities emit large quantities of gaseous ammonia (NH₃), a precursor to fine-particulate matter that harms respiratory health and the climate. This project evaluates **acid-activated biochars** produced from rice straw (R) and cherry wood chips (WC) as sustainable, on-farm adsorbents for NH₃ capture. We combine laboratory breakthrough experiments with open, reproducible data analysis in Python to quantify removal performance and identify the feedstock / pyrolysis settings that maximize adsorption capacity. :contentReference[oaicite:0]{index=0}

## Experimental Snapshot
| Step | Details (key parameters) |
|------|--------------------------|
| **Feedstocks** | Rice straw (R) & cherry wood chips (WC) |
| **Pyrolysis** | 400 – 600 °C for 15, 30, 60 min in a muffle furnace |
| **Chemical activation** | Overnight soak in 30 % H₃PO₄ (3 mL g⁻¹), 100 °C dry → acid-activated “A” samples |
| **Column tests** | 0.5 g packed bed, 2.5 L min⁻¹ air carrying 25 – 35 ppm NH₃ |
| **Sensors & logging** | Electrochemical NH₃ sensor (0.01 ppm res.), 1 min interval |
| **Breakthrough criterion** | Effluent ≈ influent or plateau >15 min |

## Key Findings
* Acid activation boosted NH₃ capacity roughly **3- to 5-fold** compared with non-activated chars.
* Best performer: **WC-500-30-A** ≈ 0.31 mg NH₃ g⁻¹ at breakthrough (duplicate-trial mean).
* Adsorption capacity rises with **lower pH (< 3)** and, to a lesser extent, higher pyrolysis temperature up to ~500 °C.
* Rice-straw chars showed higher yields but slightly lower capacities than wood-chip chars under identical conditions.
These trends indicate acid-activated biochar is a viable, greener substitute for wet scrubbers and small-bed activated-carbon systems in livestock facilities. :contentReference[oaicite:2]{index=2}

## Repository Layout

### How the Code Connects
`AdsorptionMaster_test4.ipynb` walks through the entire analytics pipeline:

1. **Data clean-up** – trims header whitespace, standardizes IDs and time stamps.
2. **Feature engineering** – computes the **effluent / influent ratio** and tags breakthrough.
3. **Curve plotting** – generates per-sample breakthrough curves and correlation heat maps.
4. **Capacity calculation** – numerically integrates (C_in – C_out)·Q dt and normalizes by biochar mass.
5. **Sensitivity exploration** – rapid regression fits (Polynomial, OLS) to test links between pH, pyrolysis settings, room RH/Temp, and capacity.

Running the notebook reproduces every figure cited in the manuscript draft.

## Quick Start
```bash
# 1) Clone and enter the repo
git clone https://github.com/your-handle/biochar-nh3-adsorption.git
cd biochar-nh3-adsorption

# 2) Create environment (conda or venv)
conda env create -f environment.yml     # or: pip install -r requirements.txt
conda activate biochar

# 3) Launch Jupyter
jupyter lab AdsorptionMaster_test4.ipynb
```
