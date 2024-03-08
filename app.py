import random
from faker import Faker
import pandas as pd

# Set up Faker and seed for reproducibility
fake = Faker()
random.seed(42)

# Number of records
num_records = 200

# Define the platforms
platforms = ['Netflix', 'Prime Video', 'Hotstar', 'Zee5']

# Generate fake data
data = []
for _ in range(num_records):
    username = fake.user_name()

    # Generate watch time based on specified ranges
    netflix_watch_time = random.randint(0,50)
    prime_video_watch_time = random.randint(0, 60)
    hotstar_watch_time = random.randint(0, 80)
    zee5_watch_time = random.randint(0, 20)
    data.append([username, netflix_watch_time, prime_video_watch_time, hotstar_watch_time, zee5_watch_time])

# Create a DataFrame
columns = ['Username', 'Netflix_Watch_Time', 'PrimeVideo_Watch_Time', 'Hotstar_Watch_Time', 'Zee5_Watch_Time']
df = pd.DataFrame(data, columns=columns)

# Save the dataset to a new CSV file
df.to_csv('ott_churn_dataset5.csv', index=False)
