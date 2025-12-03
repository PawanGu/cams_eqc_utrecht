import requests
import pandas as pd

API_KEY = "your private keys"

headers = {"X-API-Key": API_KEY}

lat, lon = 52.0907, 5.1214

resp = requests.get(
    "https://api.openaq.org/v3/locations",
    params={
        "coordinates": f"{lat},{lon}",
        "radius": 25000,
        "parameters_id[]": [2],
        "limit": 100,
    },
    headers=headers,
)
resp.raise_for_status()
locations = resp.json()["results"]

sensor_id = None
for loc in locations:
    for s in loc["sensors"]:
        if s.get("parameter", {}).get("id") == 2:
            sensor_id = s["id"]
            break
    if sensor_id:
        break

print("Using sensor:", sensor_id)

resp2 = requests.get(
    f"https://api.openaq.org/v3/sensors/{sensor_id}/days",
    params={"limit": 60},
    headers=headers,
)
resp2.raise_for_status()
meas = resp2.json()["results"]
df = pd.DataFrame(meas)

def extract_utc(period):
    return period["datetimeFrom"]["utc"]

df["date"] = pd.to_datetime(df["period"].apply(extract_utc))
df["obs_pm25"] = df["value"]
df = df[["date", "obs_pm25"]].sort_values("date")

df.to_csv("../data/openaq_utrecht_pm25.csv", index=False)
print("Saved data/openaq_utrecht_pm25.csv")
