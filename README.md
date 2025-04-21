# my-digital-life-dashboard

Project Architecture:

Data Collection (Integration Layer)

Use Airbyte OSS or Meltano to fetch:
Google Takeout (Search/YouTube history)
Spotify listening history (API)
Strava or Fitbit data (if applicable)
Email metadata (Gmail API)
Local CSVs (screen time, purchases, etc.)

Storage

Store raw data in S3 (Free Tier) or MinIO if local.
Archive CSV/JSON exports here.

Staging Layer

Transform and clean the data with Python/Pandas.
Store processed datasets in DuckDB or SQLite.

Dashboard Layer

Use Streamlit to:
Show trends (daily/weekly usage, sleep, steps)
Word clouds (emails, searches)
Time-of-day heatmaps
Top artists/songs (Spotify)