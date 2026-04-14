import subprocess
import requests # pyright: ignore[reportMissingModuleSource]
import time
import sys

IMAGE = "ramram27/devops-test:latest"
CONTAINER = "devops-test"

def run(cmd):
    return subprocess.run(cmd, shell=True)

print("Pull latest image")
run(f"docker pull {IMAGE}")

print("Stop old container")
run(f"docker rm -f {CONTAINER}")

print("Run new container")
run(
    f"docker run -d -p 4000:8080 --name {CONTAINER} {IMAGE}"
)

print("Waiting for app...")
time.sleep(5)

try:
    r = requests.get("http://localhost:4000/health")
    if r.status_code == 200:
        print("Deployment successful")
    else:
        print("Health check failed")
        sys.exit(1)
except:
    print("App not responding")
    sys.exit(1)