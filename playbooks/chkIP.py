# 1. Read Credentials from CSV file
# 2. Login to multiple device one by one
# 3. Execute command
# 4. Save the output in a txt file
# pyinstaller info_collector.py --onefile

import paramiko

p = paramiko.SSHClient()
cred = open("cred.csv","r")
for i in cred.readlines():
    try:
        line=i.strip()
        ls =line.split(",")
        print(ls)
        p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        p.connect("%s"%ls[0],port =22, username = "%s"%ls[1], password="%s"%ls[2])
        stdin, stdout, stderr = p.exec_command("uname -r")
        opt = stdout.readlines()
        opt ="".join(opt)
        print(opt)
        temp=open("%s.txt"%ls[0],"w")
        temp.write(opt)
        temp.close()
    except Exception as error:
        print(error)

cred.close()
