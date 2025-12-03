# CAMS–OpenAQ PM2.5 Evaluation — Utrecht (2016)

Small demo project comparing **CAMS EAC4 PM2.5** with **OpenAQ** observations
from Utrecht (Kardinaal de Jongweg). The workflow mimics elements of the
CAMS Evaluation & Quality Control (EQC) activities carried out at KNMI.

## Workflow

1. Download daily PM2.5 from OpenAQ for a Utrecht station.
2. Download CAMS EAC4 PM2.5 for the same period and a small Utrecht area.
3. Spatially average CAMS data and resample to daily means.
4. Convert CAMS units (kg/m³ → µg/m³).
5. Merge model and observations and compute:
   - Bias
   - RMSE
   - Pearson correlation
6. Plot a time series and scatter diagram.

Key result for 2016-01-29 to 2016-02-27:
- **Bias:** +1.7 µg/m³  
- **RMSE:** 7.4 µg/m³  
- **Correlation:** 0.30  

These values and the plots are consistent with typical CAMS vs urban PM2.5
behaviour: CAMS is smoother and tends to overestimate in some winter episodes.

## Structure

- `notebooks/01_cams_openaq_pm25_utrecht.ipynb` — main analysis
- `scripts/` — optional script version (download, process, plot)
- `data/` — input/output data (NetCDF and CSV; not tracked in git)
- `figs/` — generated figures

This repo was prepared in the context of an application for a postdoctoral
position in atmospheric composition at **KNMI**.

cams_eqc_utrecht/
│
├── README.md
├── environment.yml
│
├── scripts/
│   ├── download_openaq.py
│   ├── download_cams.py
│   ├── process_merge.py
│   └── plot_pm25.py
│
├── data/   
└── figs/   
