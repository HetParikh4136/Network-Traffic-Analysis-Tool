import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load captured packet data into a DataFrame
df = pd.read_csv('packets.csv')

# Count the number of packets by protocol
protocol_counts = df['Protocol'].value_counts()
print("\nProtocol counts:")
print(protocol_counts)

# Visualize protocol distribution
sns.barplot(x=protocol_counts.index, y=protocol_counts.values)
plt.title('Packet Count by Protocol')
plt.xlabel('Protocol')
plt.ylabel('Count')
plt.show()

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Set 'Timestamp' as the DataFrame index
df.set_index('Timestamp', inplace=True)

# Resample data by 10-second intervals and count packets in each interval
time_interval = '10S'  # Set to 10 seconds
packet_counts = df.resample(time_interval).size()

# Plot the packet count over time intervals
plt.figure(figsize=(10, 6))
packet_counts.plot(kind='line', marker='o', color='b')
plt.title(f'Packet Count Over Time (Interval: {time_interval})')
plt.xlabel('Time')
plt.ylabel('Number of Packets')
plt.grid(True)
plt.show()