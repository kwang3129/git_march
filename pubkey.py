from fabric import Connection


# with open(r"C:\Users\PC\Desktop\python\paramiko\id_rsa","r") as f:
#     a = f.read()
# print(a)
try:
    ubuntu = Connection(host="192.168.159.128", user="root", connect_kwargs={"key_filename":[r"C:\Users\PC\Desktop\python\paramiko\id_rsa"]})
    result = ubuntu.run("cat /etc/shadow")
    result
except Exception as e:
    print(e)