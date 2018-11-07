import pandas as pd
import numpy as np

def generate_fake_data(rows):
	'''
	Input: Takes an integer representing the # of rows you want for your data frame
	Output: Returns a fake data set of "events" and user types with a time column
	'''

	try:
		_rows = int(rows)
	except:
		print("Please provide an integer")
		return pd.DataFrame(None)

	event_types = ['open', 'bounce_back', 'junk', 'un_opened']
	events = [np.random.choice(event_types, p = [0.6, 0.05, 0.02, 0.33]) for i in range(_rows)]

	# create fake time range, 10,000 events, events coming in each minute
	time_stamp = pd.date_range("11/15/2018", periods = _rows, freq="Min")

	# create random user type distribution over the events
	user_types = ['a', 'b', 'c']
	user_type = [np.random.choice(user_types, p = [0.6, 0.3, 0.1]) for i in range(_rows)]

	# create the dataframe
	event_df = pd.DataFrame({'time_stamp' : time_stamp, 'event_type' : events, 'user_type': user_type})

	return event_df

