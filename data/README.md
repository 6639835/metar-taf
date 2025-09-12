# Data Directory

This directory contains the collected METAR data organized by timestamp.

## Directory Structure

```
data/
├── YYYY/           # Year (e.g., 2025)
│   ├── MM/         # Month (e.g., 09)
│   │   ├── DD/     # Day (e.g., 12)
│   │   │   ├── HH-MM/    # Hour-Minute (e.g., 14-30)
│   │   │   │   ├── metars_YYYYMMDD_HHMM UTC.xml
│   │   │   │   └── download_info.txt
│   │   │   └── ...
│   │   └── ...
│   └── ...
└── README.md       # This file
```

## File Naming Convention

- **METAR XML files**: `metars_YYYYMMDD_HHMM UTC.xml`
  - Example: `metars_20250912_1430 UTC.xml`
- **Metadata files**: `download_info.txt`
  - Contains download timestamp, source URL, file size, etc.

## Data Source

All data is downloaded from: https://aviationweather.gov/data/cache/metars.cache.xml.gz

The data is updated every minute and contains current METAR reports from airports worldwide.
