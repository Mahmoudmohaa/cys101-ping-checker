
import os
import subprocess
import platform


op_sys = "-n" if platform.system() == "Windows" else "-c"
ttl_str = "TTL=" if platform.system() == "Windows" else "ttl="

with open("ip_list.txt" ,"r") as file :
    ip_list = file.readlines()

ip_list = [ip.strip() for ip in ip_list]

def ping_ips(ip):
    try:
        output = subprocess.run(
            ["ping",op_sys ,"1" ,ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if ttl_str in output.stdout:
            print(f"{ip} Is Reachable ✔️")
        else :
            print(f"{ip} Is NOT Reachable❌")
    except Exception as e :
        print(f"Error {e}")

for ip in ip_list:
    ping_ips(ip)

