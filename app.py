import threading
import time
import uvicorn
from backend.main import app as fastapi_app
import streamlit as st
import requests
import subprocess

def run_fastapi():
    uvicorn.run(fastapi_app, host="127.0.0.1", port=8000)

def run_streamlit():
    subprocess.Popen(["streamlit", "run", "frontend/main.py"])

if __name__ == "__main__":
    fastapi_thread = threading.Thread(target=run_fastapi)
    fastapi_thread.start()
    time.sleep(2)
    run_streamlit()
