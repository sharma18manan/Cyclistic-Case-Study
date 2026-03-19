import pandas as pd

df = pd.read_csv("cyclistic_cleaned_data.csv")

print(df['member_casual'].value_counts())

print(df.groupby('member_casual')['ride_length_minutes'].mean())

print(df.groupby(['member_casual','day_of_week'])['ride_id'].count())

df['started_at'] = pd.to_datetime(df['started_at'])
df['month'] = df['started_at'].dt.month_name()

print(df.groupby(['member_casual','month'])['ride_id'].count())

print(df.groupby(['member_casual','rideable_type'])['ride_id'].count())

ride_count = df.groupby('member_casual')['ride_id'].count().reset_index()
ride_count.to_csv("ride_count_summary.csv", index=False)

avg_duration = df.groupby('member_casual')['ride_length_minutes'].mean().reset_index()
avg_duration.to_csv("avg_duration_summary.csv", index=False)

weekly_usage = df.groupby(['member_casual','day_of_week'])['ride_id'].count().reset_index()
weekly_usage.rename(columns={'ride_id': 'ride_count'}, inplace=True)
weekly_usage.to_csv("weekly_usage_summary.csv", index=False)

monthly_usage = df.groupby(['member_casual','month'])['ride_id'].count().reset_index()
monthly_usage.rename(columns={'ride_id': 'ride_count'}, inplace=True)
monthly_usage.to_csv("monthly_usage_summary.csv", index=False)

ride_type_usage = df.groupby(['member_casual','rideable_type'])['ride_id'].count().reset_index()
ride_type_usage.rename(columns={'ride_id': 'ride_count'}, inplace=True)
ride_type_usage.to_csv("ride_type_summary.csv", index=False)

