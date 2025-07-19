import os
import subprocess
import platform

# Detect the correct flag for the ping command based on the operating system
# Windows uses '-n', Linux/macOS use '-c'
op_sys = "-n" if platform.system() == "Windows" else "-c"

# Set the expected TTL string that indicates a successful ping response
ttl_str = "TTL=" if platform.system() == "Windows" else "ttl="

# Read the list of IP addresses from a file named 'ip_list.txt'
# Each IP should be on a separate line
with open("ip_list.txt", "r") as file:
    ip_list = file.readlines()

# Clean up each IP (remove newline characters and extra spaces)
ip_list = [ip.strip() for ip in ip_list]

def ping_ips(ip):
    """
    Ping a single IP address and check if it's reachable.
    It works for both Windows and Unix-like systems.
    If the response contains a TTL value, it's considered reachable.
    """
    try:
        # Run the ping command using subprocess
        output = subprocess.run(
            ["ping", op_sys, "1", ip],  # "1" means send one packet
            stdout=subprocess.PIPE,     # Capture the output
            stderr=subprocess.PIPE,
            text=True                   # Return output as string
        )

        # Check if the expected TTL string is in the ping output
        if ttl_str in output.stdout:
            print(f"{ip} Is Reachable ✔️")
        else:
            print(f"{ip} Is NOT Reachable ❌")

    except Exception as e:
        # Print any unexpected errors that occur during pinging
        print(f"Error: {e}")

# Loop through all IPs and test each one
for ip in ip_list:
    ping_ips(ip)
