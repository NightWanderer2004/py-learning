from ftplib import FTP

ftp_host = "demo.wftpserver.com"
ftp_user = "demo"
ftp_password = "demo"

ftp = FTP()

ftp.connect(ftp_host)

ftp.login(user=ftp_user, passwd=ftp_password)

print(ftp.getwelcome())

file_list = ftp.nlst()
print(f"List of files: {file_list}")

ftp.quit()
