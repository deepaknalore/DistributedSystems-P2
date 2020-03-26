import subprocess
import time
from datetime import datetime

pingCount = 1
count = 0
#ipList = ['www.google.com']
ipList = ["c220g1-030811.wisc.cloudlab.us", "ms0619.utah.cloudlab.us", "clnode216.clemson.cloudlab.us"]

startTime = time.time()
numberofMinutes = 10

def WritePingStats():
    t = datetime.utcnow()
    for ip in ipList:
        p = subprocess.Popen(["ping", "-c " + str(pingCount),ip], stdout = subprocess.PIPE)
        out = str(p.communicate()[0])
        timeUnit = out.split()[-1][:2]
        averageLatency = str(out.split()[-2]).split('/')[1]
        maxLatency = str(out.split()[-2]).split('/')[2]
        stdDev = str(out.split()[-2]).split('/')[3]
        print(str(maxLatency) + str(timeUnit))
        print(str(averageLatency) + str(timeUnit))
        print(stdDev)
        with open(str(ip) + ".csv", "a") as fd:
            fd.write(str(t) + "," + averageLatency + "," + maxLatency + "," + stdDev + "\n")


while time.time() < (startTime + (60 * numberofMinutes)):
    WritePingStats()


