from locust import HttpUser, SequentialTaskSet, task
import json

#如何做好参数化，让数据更真实？
class WebsiteTasks(SequentialTaskSet):
    @task(1)
    def login(self):
        with self.client.post("/oauth/pass", { "username": "13723492985", "password": "65a0ec385ca6a0c1e20d1f8270c28303","client": "web" }) as response:
            d = json.loads(response.text)
            token = d.get('data').get('accessToken')
            self.token = token

    @task(50)
    def address_Search(self):
        headers = {"content-type": 'application/json; charset=utf-8', "authorization":self.token}
        Url = '/web/request/operate'
        with self.client.get(Url,headers=headers) as response:
             print(response.json())

class WebsiteUser(HttpUser):
    # task_set = WebsiteTasks  # Usage of User.task_set is deprecated since version 1.0. Set the tasks attribute instead (tasks = [WebsiteTasks])
    tasks = [WebsiteTasks]
    host = "https://uat.pxxtech.com"
    min_wait = 1000
    max_wait = 5000