import subprocess 
import requests  # type: ignore
import time 
import sys 
import logging

IMAGE = "ramram27/devops-test:latest"
PRIVIOS_IMAGE = "ramram27/devops-test:previous"
CONTAINER = "devops-test"
PORT = "8080"
HELTH_URL = "http://localhost:4000/health"

MAX_RETRIES = 5
SLEEP_TIME = 3


def run(cmd):
    logging.info(f"Running command: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        logging.error(f"Command failed with error: {result.stderr}")
    else:
        logging.info(f"Command output: {result.stdout}")

    return result


def pull_image():
    print("Pulling your latest docker image..")
    run("docker pull {IMAGE}")

def stop_container():
    print("stopping your running container..")
    run(f"docker stop {CONTAINER} || true")
    run(f"docker rm {CONTAINER} || true")

def start_container():
    print("start your new container..")
    run(f"docker run -d --name {CONTAINER} -p 4000:{PORT} {IMAGE}")

def check_health():
    print("checking health of your application..")
    for i in range(MAX_RETRIES):
        try:
            res = requests.get(HELTH_URL)

            if res.status_code == 200:
                print("Deployment successful and application")
                logging.info("Application is healthy and running.")
                return True
            else:
                logging.warning(f"Health check failed with status code: {res.status_code}",i+1)
            
        except Exception as e:
            logging.info(f"Health check attempt {i+1} failed with error: {e}")
            time.sleep(SLEEP_TIME)

    print("Deployment failed, application is not healthy after multiple attempts.")
    logging.error("Application failed health checks after multiple attempts.")
    return False

def rollback():
    print("Rolling back to previous version..")
    logging.info("Rolling back to previous version of the application.")

    run(f"docker pull {PRIVIOS_IMAGE}")
    stop_container()

    run(f"docker run -d --name {CONTAINER} -p 4000:{PORT} {PRIVIOS_IMAGE}")

def check_container():
     res = run(f"docker ps")

     if CONTAINER in res.stdout:
         logging.info("Container is running.")
         return True
     else:
          logging.error("Container is not running.")
          return False
     

def main():
    logging.info("Starting deployment process...")
    pull_image()
    stop_container()
    start_container()

    time.sleep(5)  # Wait for the container to start before checking health

    if not check_container():
            print("Container failed to start. Rolling back...")
            sys.exit(1)

    if not check_health():
        logging.error("Deployment failed due to health check failure.")
        rollback()
        sys.exit(1)


if __name__ == "__main__":
    main()
