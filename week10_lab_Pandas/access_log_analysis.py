# this program reads the access log file and creates a dataframe from it
# Author: Stephen Kerr

# import pandas as pd
import pandas as pd

# import re
import re

# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# add column names to the dataframe
column_name = ('ip',
'dash1',
'userId',
'time',
'url',
'status code',
'size of response',
'referer',
'user agent',
'dunno'
)


# read the access log file and create a dataframe from it
df = pd.read_csv('access.log.demo', sep=' ', header=None, names=column_name)



# drop the columns that contain just dashes
df.drop(columns=['dash1', 'userId'], inplace =True)

# print(df.head(3))

# reformat the time column to a more readable format
df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())

print(df.head(3))

# change the time column to a datetime object and format it to a more readable format
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

#print(df.dtypes)

# get the events that happened between 2 times
start_time = '2024-02-22 18:00:00'
end_time = '2024-02-22 23:59:59'
mask = (df['time'] > start_time) & (df['time'] <= end_time)
times_df = df.loc[mask]
#print(times_df)

#print(df['time'].max())

# Set the time column as the index
df.set_index('time', inplace=True)

# mean download every 30 minutes 
download_samples = df['size of response'].resample(rule='30Min').mean()

download_samples.plot(title='Mean download every 30 minutes', figsize=(10, 5), color='blue')
plt.xlabel('Time')
plt.ylabel('Mean download size')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig('mean_download.png')
plt.show()


