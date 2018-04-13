# data-question-2
### Metro Nashville Open Data Cleanup &amp; Analysis

#### Steps in this Data Problem include

1. Determine and implement a strategy to reduce the 900+ violation types listed
in the spreadsheet "Codes' List of Violations 15 aug 2017.xlsx" to just 20 or so main categories.

2. Tidy the Property Standards Violations dataset available at
https://data.nashville.gov/Business-Development-Housing/Property-Standards-Violations/479w-kw2x so that you have a single observation in each row and a single variable (measurement) in each column (https://en.wikipedia.org/wiki/Tidy_data). This will
allow you to test the efficacy of your coding strategy from step 1.

3. Perform Exploratory Data Analysis on the Property Standards Violations data
to showcase the insight your work has enabled.

## Setup

Create a `.env.secret` file in the top level directory. Fill in the redacted
values for your system:

```
JUPYTER_APP_TOKEN=REDACTED

POSTGRES_PASSWORD=REDACTED
POSTGRES_USER=REDACTED
POSTGRES_HOSTNAME=REDACTED

SOCRATA_APP_TOKEN=REDACTED
SOCRATA_SECRET_TOKEN=REDACTED
```

## Run The Analysis Notebook

To start a local docker-compose (docker must be installed) environment to run
the analysis, simply run:

```
make
```

- Builds the postgres, pgadmin, and jupyter server docker containers with all
  dependencies and volume mounts included.
- Creates a `violations` database and seeds the `property_standards_violations`
  and `violation_codes` tables from their respective csv files in the data directory.
- Starts a notebook browser window using the appropriate login token.
