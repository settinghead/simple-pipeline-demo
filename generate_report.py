from data_ingest import generate_fake_data
from tabulate import tabulate
from datetime import datetime

from skafossdk import *

ska = Skafos()

now = datetime.now()
report_time = now.strftime("%Y_%m_%d_%H_%M")

# generate the fake data
ska.log("Generating the data", labels = ['data_pipeline'])
df = generate_fake_data(rows = 10000)

# take a look at the data
ska.log("Take a look at the head of the data:", labels = ['data_pipeline'])
print(df.head())

# aggregate the data by user type and event type
ska.log("Running our aggregation by user and event type")
agg_df = df.groupby(['user_type', 'event_type']).count().reset_index()
agg_df.columns = ['user_type', 'event_type', 'count']

result_df = agg_df.pivot(index = 'user_type', columns = 'event_type').\
					reset_index()
result_df.columns = ['user_type', 'bounce_back', 'junk', 'open', 'un_opened']

ska.log("Calculating our metrics", labels = ['data_pipeline'])
result_df['total_sent'] = result_df[['bounce_back', 'junk', 'open', 'un_opened']].sum(axis =1)
result_df['open_rate'] = result_df['open'] / (result_df['open'] + result_df['un_opened'])
result_df['bounce_back_rate'] = result_df['bounce_back'] /result_df['total_sent']

result_df = result_df[['user_type', 'total_sent', 'open_rate', 'bounce_back_rate']]

ska.log("Aggregation job finished, take a look at the results below", labels = ['data_pipeline'])
print(result_df.head())