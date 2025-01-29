import json
import logging
import os
import time
from typing import List
from uuid import uuid4

import numpy as np
import redis
from celery import Celery

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

log = logging.getLogger(__name__)

from celery.signals import task_postrun, task_prerun

import celery_config
from celery_config import MERGE_FILES_NAME, SCHEDULER_TASK_NAME

celery = Celery(__name__)
celery.config_from_object(celery_config)

TEST_DATA_PATH = "test_data"

r = redis.Redis(host='localhost', port=6379, db=0)

# Called by app to schedule average job
@celery.task(bind=True, name=SCHEDULER_TASK_NAME, queue="scheduler")
def scheduler_task(self, files: List[str], task_id: str, prefix: str):
  pass
