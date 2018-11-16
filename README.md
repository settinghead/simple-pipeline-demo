# Data Pipeline Example
This is a repository that serves as an example for a simple job you might have to run on a daily/hourly/weekly basis. It generates a mock data set, supposed to be representing some email events that are coming in and some user types associated with each of those emails.

We run a simple job to aggregate this data and from there it can either be written to file, stored in a database, send a message to a Slack channel, etc.

## Components
The components of this repo are:
- `data_ingest.py` - a script that generates a mock data set
- `generate_report.py` - a script runs a simple aggregation over the mock data
- `requirements.txt` - a text file indicating the jobs dependencies
- `metis.config.yml` - a file that tells Skafos how to run the jobs
