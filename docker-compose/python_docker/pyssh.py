import paramiko

# Define SSH parameters
hostname = "192.168.1.2"
username = "shreya"
password = "12wq"

# Create SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the server
ssh_client.connect(hostname, username=username, password=password)

# Execute a command
stdin, stdout, stderr = ssh_client.exec_command("ls -l")

# Print the output
for line in stdout:
    print(line.strip())

# Close the connection
ssh_client.close()