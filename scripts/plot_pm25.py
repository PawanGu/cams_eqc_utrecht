import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("../data/merged_pm25_utrecht.csv", parse_dates=["valid_time"])
df = df.set_index("valid_time")

bias = (df["cams_pm25_ug"] - df["obs_pm25"]).mean()
rmse = np.sqrt(((df["cams_pm25_ug"] - df["obs_pm25"])**2).mean())
corr = df["cams_pm25_ug"].corr(df["obs_pm25"])
print("Bias (ug/m3):", bias)
print("RMSE (ug/m3):", rmse)
print("Correlation:", corr)

# Time series
plt.figure(figsize=(12,5))
plt.plot(df.index, df["obs_pm25"], label="OpenAQ PM2.5", lw=2)
plt.plot(df.index, df["cams_pm25_ug"], label="CAMS PM2.5", lw=2)
plt.ylabel("PM2.5 (µg/m³)")
plt.title("PM2.5 — Utrecht (2016) — CAMS vs OpenAQ")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("../figs/timeseries_pm25_utrecht.png", dpi=300)
plt.close()

# Scatter
plt.figure(figsize=(6,6))
plt.scatter(df["obs_pm25"], df["cams_pm25_ug"], alpha=0.7)
plt.xlabel("Observed PM2.5 (µg/m³)")
plt.ylabel("CAMS PM2.5 (µg/m³)")
plt.title("CAMS vs Observation — PM2.5")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("../figs/scatter_pm25_utrecht.png", dpi=300)
plt.close()

print("Saved figures in figs/")
