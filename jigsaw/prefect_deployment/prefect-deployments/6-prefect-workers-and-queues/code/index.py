import requests
from prefect import flow, task
from prefect.deployments.deployments import Deployment
from prefect.server.schemas.schedules import IntervalSchedule


@task
def find_receipts(name):
    url = "https://data.texas.gov/resource/naix-2893.json"
    response = requests.get(url, params = {'taxpayer_name': name})
    return response.json()[:1]

@flow
def get_restaurants(url: str):
    receipts = find_receipts(url)
    return receipts

# add the lines above to the top of the index.py file

# if __name__ == "__main__":
#     get_restaurants.serve(
#         name="get-restaurants-deployment",
#         schedule=IntervalSchedule(interval=120),
#         parameters={'url': "HONDURAS MAYA CAFE & BAR LLC"}
#         )
if __name__ == "__main__":
    schedule = IntervalSchedule(interval=10)
    parameters={'url': "HONDURAS MAYA CAFE & BAR LLC"}
    deployment = Deployment.build_from_flow(
        name="honduras_maya",
        flow=get_restaurants,
        version=1,
        schedule=schedule,
        is_schedule_active=True,
        work_queue_name="default",
        parameters=parameters,
        entrypoint="./index.py:get_restaurants",
    )
    deployment.apply(upload=True)

