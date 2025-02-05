=> CYBER SECURITY PROJECT <=

PROJECT TOPIC : NETWORK TRAFFIC ANALYSIS TOOL
PROJECT REQUIREMENTS : 
        - Implement packet sniffing techniques to capture network traffic.
        - Use data visualization to display network traffic patterns.

>Overview :
        This Network Traffic Analysis Tool is a Python-based tool for capturing, analyzing, and visualizing network traffic patterns. 
        It captures packets on the specified network interface, saves them to a CSV file named 'packets.csv'.
        It also provides analytical insights, such as protocol distribution and packet count over time.
        This tool is useful for identifying traffic patterns, detecting potential security threats, and optimizing network performance.

>Features :
        - Packet Capture : Captures network packets on a specified interface.
        - Traffic Analysis : Extracts information such as source/destination IP addresses, protocols, and timestamps.
        - Data Visualization : Displays traffic patterns with visualizations for better insight into network activity.

>Requirements :
        - Python : version 3.13 was used for making this project
        - Text/Code Editor (Optional) : For getting a better perspective of your code
        - Python Libraries : scapy, pandas, matplotlib, seaborn

>Usage :
        1. Packet Sniffing : 
                To capture network packets and save them to a CSV file, run packet_sniffer.py
                Make sure to update the network interface in the script (e.g., eth0, wlan0).
        2. Analyzing Packet Data :
                To analyze captured packets and view visualizations, run analyze_packets.py:

>File Structure :
        The main files in this project include:
                - packet_sniffer.py: Captures network packets and saves data to a CSV file.
                - analyze_packets.py: Loads and analyzes captured packet data, displaying visualizations of traffic patterns.