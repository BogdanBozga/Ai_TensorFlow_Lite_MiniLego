import paramiko
import os

# # Define the remote host and username
# remote_host = "bogdan@192.168.22.118"
#
# # Define the local and remote directories
local_dir = "/home/bbozga/PycharmProjects/AiGUI"
remote_dir = "/home/bogdan/Desktop/AI/tflite1/results/test1.jpg"

filename = 'test1.jpg'
# # Prompt for password
# password = "bogdan"
#
# # Create an SSH client
# client = paramiko.SSHClient()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.22.118',username='bogdan',password='bogdan')
#

ftp_client = ssh_client.open_sftp()
ftp_client.get(remote_dir+filename, local_dir)
ftp_client.close()









# # Automatically add the server's host key
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # Connect to the server
# client.connect(remote_host, password=password)
#
# # Create an SFTP client
# sftp = client.open_sftp()
#
#
# # Construct the local and remote file paths
# local_path = os.path.join(local_dir, filename)
# remote_path = os.path.join(remote_dir, filename)
#
# # Download the file
# sftp.get(remote_path, local_path)
#
# # Close the SFTP client
# sftp.close()
#
# # Close the SSH client
# client.close()

print("Success: Images transferred")
