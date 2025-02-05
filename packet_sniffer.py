from scapy.all import sniff, IP, TCP, UDP
import csv
from datetime import datetime

# Define a list to store packet information
packets = []

# Define a callback function to process captured packets
def packet_callback(packet):
    if IP in packet:
        # Extract the details of interest
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"

        # Store packet details as a tuple
        packets.append((timestamp, src_ip, dst_ip, protocol))

        # Print packet details for immediate feedback
        print(f"{timestamp} | {src_ip} -> {dst_ip} | {protocol}")

# Start sniffing packets on the network (adjust the interface as needed)
print("Starting packet capture...")
sniff(prn=packet_callback, iface="Ethernet 2",  timeout=120)
print("Packet capture complete.")

# Save captured packet data to a CSV file
with open('packets.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Timestamp', 'Source IP', 'Destination IP', 'Protocol'])
    writer.writerows(packets)

print("Captured packet data saved to packets.csv")
