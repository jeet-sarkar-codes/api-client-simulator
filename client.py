import requests
import time

BASE_URL = "http://127.0.0.1:5000"

def get_status():
    try:
        res = requests.get(f"{BASE_URL}/status")
        print("Status:", res.json())
    except Exception as e:
        print("Status check failed:", e)

def run_diagnostics():
    try:
        res = requests.get(f"{BASE_URL}/run-diagnostics")
        print("Diagnostics:", res.json())
    except Exception as e:
        print("Diagnostics failed:", e)

if __name__ == "__main__":
    get_status()
    time.sleep(1)
    run_diagnostics()