import os
import sys
import subprocess

jar = "OfficeDriveClient.jar"
odPath = os.path.join(os.environ.get("LOCALAPPDATA",""), "OfficeDrive")
localJarPath = os.path.join(odPath, jar)
pidFile = os.path.join(odPath, "pidfile")

updateUrl = "https://websockettest.officedrive.net/plugin/OfficeDriveClient.jar"

if len(sys.argv) > 1:
	updateUrl = sys.argv[1]

try:
    pid = open(pidFile, "r").read()
except (IOError):
    sys.stdout.write("error reading pidfile %s\n" %pidFile)
   # sys.exit(-1)

if pid:
    sys.stdout.write("trying to terminate process: %s\n" %pid)
    try:
        ret = os.kill(int(pid),9)
    except:
        ret = -127
        pass
    
    if ret == 0:
        sys.stdout.write("process id: %s was terminated\n" %pid)
    else:
        sys.stdout.write("could not terminate process: %s\n" %pid)
        try:
            ret = os.kill(int(pid),15)
        except:
            ret = -128
            pass
    #if not ret:
    #sys.exit(-1)

cmd = subprocess.Popen(["curl.exe", "-k", "-o", localJarPath, updateUrl] , stdout=subprocess.PIPE)

cmd.wait()
out = cmd.stdout.readlines()

for l in out:
    sys.stdout.write(l)

if cmd.returncode:
	sys.stdout.write("exitcode: %d - fail!\n" %cmd.exitcode)
# 	sys.exit(-1)
else:
    sys.stdout.write("updat of %s completed.\n"  %localJarPath)
	
# sys.exit(0)

    
