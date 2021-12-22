from locust import HttpUser, TaskSet, task
from gevent._semaphore import Semaphore

class WebsiteTasks(TaskSet):
    def on_start(self):
        #self.client.post("oauth/pass", { "username": "13723492985", "password": "65a0ec385ca6a0c1e20d1f8270c28303","client": "web" })
        #self.client.get("/login?key=00d91e8e0cca2b76f515926a36db68f5&phone=13594347817&passwd=123456")
        Url = "oauth/pass"
        Data = {'username': "13723492985", 'password': "65a0ec385ca6a0c1e20d1f8270c28303", 'client': "web"}
        Headers = {'Content_type': "application/json"}
        with self.client.post(Url, Data, Headers) as rep:
            print(rep.json())
        try:
            rep.json()['code'] == 200
            print('登录成功！')
        except Exception as err:
            print('登录失败！')
    # @task(2)
    def config(self):
        self.client.get("web/config/table/900001")

    # @task(1)
    def companyBaseInfo(self):
        self.client.get("web/company/companyBaseInfo")

    def search(self):
        self.client.get("web/msgPush/search")

    def transport(self):
        self.client.get("web/company/search/transport")

    def todo(self):
        self.client.get("web/home/biz/todo")

    tasks = {config: 2, companyBaseInfo: 1, search: 2, transport: 3, todo: 2}  # 与装饰器效果一致

class WebsiteUser(HttpUser):
    # https://blog.csdn.net/c__chao/article/details/78573737
    # task_set = WebsiteTasks  # Usage of User.task_set is deprecated since version 1.0. Set the tasks attribute instead (tasks = [WebsiteTasks])
    tasks = [WebsiteTasks]
    host = "https://uat.pxxtech.com/"
    min_wait = 1000
    max_wait = 5000