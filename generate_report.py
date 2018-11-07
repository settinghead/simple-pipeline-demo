from data_ingest import generate_fake_data
from tabulate import tabulate
from datetime import datetime

now = datetime.now()
report_time = now.strftime("%Y_%m_%d_%H_%M")

# generate the fake data
df = generate_fake_data(rows = 10000)

# take a look at the data
print(df.head())

# aggregate the data by user type and event type
agg_df = df.groupby(['user_type', 'event_type']).count().reset_index()
agg_df.columns = ['user_type', 'event_type', 'count']

result_df = agg_df.pivot(index = 'user_type', columns = 'event_type').\
					reset_index()
result_df.columns = ['user_type', 'bounce_back', 'junk', 'open', 'un_opened']


result_df['total_sent'] = result_df[['bounce_back', 'junk', 'open', 'un_opened']].sum(axis =1)
result_df['open_rate'] = result_df['open'] / (result_df['open'] + result_df['un_opened'])
result_df['bounce_back_rate'] = result_df['bounce_back'] /result_df['total_sent']

result_df = result_df[['user_type', 'total_sent', 'open_rate', 'bounce_back_rate']]

# output the csv
result_df.to_csv("./reports/user_event_report_" + report_time + ".csv", index = None)

# send the csv to a slack channel in 'nice' format
# would require slack set up
#tidy_df = "```" + tabulate(df.head(), tablefmt="grid") + "```"
#sc.api_call('chat.postMessage',
#			channel = "boss",
#			text = tidy_df)
