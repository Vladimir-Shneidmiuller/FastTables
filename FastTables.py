import subprocess

# Clear all iptables rules
subprocess.run(["iptables", "-F"])

# Close all incoming connections
subprocess.run(["iptables", "-P", "INPUT", "DROP"])

# Allow outgoing connections
subprocess.run(["iptables", "-P", "OUTPUT", "ACCEPT"])

# Allow connections on localhost
subprocess.run(["iptables", "-A", "INPUT", "-i", "lo", "-j", "ACCEPT"])

# Allow connections on the ports required for the server to work. 

subprocess.run(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", "22", "-j", "ACCEPT"])  # SSH
subprocess.run(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", "80", "-j", "ACCEPT"])  # HTTP
subprocess.run(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", "443", "-j", "ACCEPT"])  # HTTPS
# You can add other ports if necessary
# subprocess.run(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", "Your port here", "-j", "ACCEPT"])

# Close all other connections
subprocess.run(["iptables", "-A", "INPUT", "-j", "DROP"])

# Save iptables rules
subprocess.run(["iptables-save"])

