# celery_config.py
broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'
SCHEDULER_TASK_NAME = 'scheduler_task'
MERGE_FILES_NAME = 'merge_files'

task_routes = {
    SCHEDULER_TASK_NAME: {
        'queue': 'scheduler'
    },
    MERGE_FILES_NAME: {
        'queue': 'worker'
    },
}
