from celery_app import app


@app.task
def test_task():
    print('✨ Hello from Celery test task!!!')