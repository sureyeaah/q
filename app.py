import json
import logging
import os
from uuid import uuid4

import numpy as np
import redis
from celery import Celery
from flask import Flask, jsonify, request
from flask_cors import CORS

from tasks import TEST_DATA_PATH, scheduler_task

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

log = logging.getLogger(__name__)
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})
celery_client = Celery("tasks", broker='redis://localhost:6379/0')

# generate N files with total array_size numbers in output_dir
# Return: file_names and directory
def generate_random_files(total_files, array_size, output_dir):
  pass

# Generate random numbers and schedule a task to average them
@app.route('/calculateAverage', methods=['POST'])
def calculate_average():
  pass


r = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/task-metrics/<prefix>', methods=['GET'])
def get_task_metrics(prefix):
  tasks_json = r.lrange(prefix, 0, -1)
  tasks = [json.loads(task.decode('utf-8')) for task in tasks_json]
  return jsonify(tasks)

# Metrics to help us understand how the system is performing
@app.route('/metrics', methods=['GET'])
def metrics():
  pass


@app.route('/get-prefixes', methods=['GET'])
def get_prefixes():
  prefixes = [
      file for file in os.listdir(TEST_DATA_PATH)
      if os.path.isdir(os.path.join(TEST_DATA_PATH, file))
  ]
  return jsonify(prefixes)
