# Development docker containers

Contains all the development playgrounds, represented as docker containers.

- Celery Demo Project

Celery exploration with task schedulers / workers

Starting beat scheduler
`celery beat -A celery_demo -l INFO`

Starting worker
`celery worker -A celery_demo -l INFO`

If you want to run a task, open `ipython` import that task, and manually execute it, with a loop, but don't forget to add a delay.
