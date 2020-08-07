import subprocess as sp

ip = "192.168.0."

knownHosts = []

for i in range(1,255):
    status, result = sp.getstatusoutput("ping -c 1 -o -W 100 " + ip + str(i))
    print('.', end ="", flush=True)
    if (status == 0):
        knownHosts.append(i)

print(knownHosts)
