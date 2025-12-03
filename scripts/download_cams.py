import cdsapi
import pandas as pd

df = pd.read_csv("../data/openaq_utrecht_pm25.csv", parse_dates=["date"])
date_from = df["date"].min().date().isoformat()
date_to   = df["date"].max().date().isoformat()

print("CAMS period:", date_from, "to", date_to)

c = cdsapi.Client()

bbox = [52.20, 4.95, 51.95, 5.35]

c.retrieve(
    "cams-global-reanalysis-eac4",
    {
        "date": f"{date_from}/{date_to}",
        "format": "netcdf",
        "variable": ["particulate_matter_2.5um"],
        "model_level": "60",
        "area": bbox,
        "time": [
            "00:00","03:00","06:00","09:00",
            "12:00","15:00","18:00","21:00",
        ],
    },
    "../data/cams_pm25_utrecht.nc",
)

print("Saved data/cams_pm25_utrecht.nc")
