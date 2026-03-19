import pandas as pd
import os

folder_path = r"C:\Users\dell\Desktop\Cyclistic case study\Raw data"

files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

df_list = []

for file in files:
    data = pd.read_csv(os.path.join(folder_path, file))
    df_list.append(data)

combined_df = pd.concat(df_list, ignore_index=True)

# Convert date columns
combined_df['started_at'] = pd.to_datetime(combined_df['started_at'])
combined_df['ended_at'] = pd.to_datetime(combined_df['ended_at'])

# Create ride_length
combined_df['ride_length'] = combined_df['ended_at'] - combined_df['started_at']

# Remove negative durations
combined_df = combined_df[combined_df['ride_length'] > pd.Timedelta(seconds=0)]

# Create day_of_week
combined_df['day_of_week'] = combined_df['started_at'].dt.day_name()

# Remove missing important data
combined_df = combined_df.dropna(subset=['ride_id','started_at','ended_at','member_casual'])

# Remove duplicate rides
combined_df = combined_df.drop_duplicates(subset=['ride_id'])

# Convert duration to minutes
combined_df['ride_length_minutes'] = combined_df['ride_length'].dt.total_seconds() / 60

# Remove unrealistic durations
combined_df = combined_df[
    (combined_df['ride_length_minutes'] >= 1) &
    (combined_df['ride_length_minutes'] <= 1440)
]

# Save cleaned dataset
combined_df.to_csv("cyclistic_cleaned_data.csv", index=False)
