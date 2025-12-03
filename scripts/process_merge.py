import pandas as pd
import xarray as xr

# Observations
df_obs = pd.read_csv("../data/openaq_utrecht_pm25.csv", parse_dates=["date"])
df_obs = df_obs.set_index("date").resample("1D").mean()

# CAMS
ds = xr.open_dataset("../data/cams_pm25_utrecht.nc")
cams_ts = ds["pm2p5"].mean(dim=["latitude", "longitude"]).to_series()
cams_df = cams_ts.to_frame(name="cams_pm25").resample("1D").mean()

# Make indices tz-naive
df_obs.index  = df_obs.index.tz_localize(None)
cams_df.index = cams_df.index.tz_localize(None)

df = cams_df.join(df_obs, how="inner")
df["cams_pm25_ug"] = df["cams_pm25"] * 1e9

df.to_csv("../data/merged_pm25_utrecht.csv")
print("Saved data/merged_pm25_utrecht.csv")
