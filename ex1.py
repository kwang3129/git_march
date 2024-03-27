import fabric as fb

c = fb.Connection(host="quang@192.168.159.128", connect_kwargs={"password" : "quangbg123"})
result = c.run("whoami")
print(result.command)
print(result.connection.host)
print(result.stdout)

# result_sudo= c.sudo("cat /etc/shadow", password="quangbg123", hide="both")
# print(result_sudo.stdout)



def process_list(process, a):
    return process.run(f"ps aux | grep -i {a}").stdout.strip()

process_list(c,"python")


