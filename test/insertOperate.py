from locust import HttpUser, SequentialTaskSet, task
import json

#如何做好参数化，让数据更真实？
class WebsiteTasks(SequentialTaskSet):
    @task(1)
    def login(self):
        with self.client.post("oauth/pass", { "username": "13723492985", "password": "65a0ec385ca6a0c1e20d1f8270c28303","client": "web" }) as response:
            data = json.loads(response.text)
            token = data.get('data').get('accessToken')
            self.token = token
    @task(50)
    def insert_Operate(self):
         Url = '/web/request/operate'
         data = {"paymentType": "20", "estimateArriveTime": "2021-04-20T11:41:53", "cargoRequestList": [
             {"cargoRequestNo": "X7693466880003968", "cargoPointList": [
                 {"pointType": 10, "pointAddress": "广东省深圳市南山区南山街道学府路大新时代大厦", "pointLongitude": "113.911818",
                  "pointLatitude": "22.528034", "pointCode": "440305", "pointSort": 0, "contacts": "王测试",
                  "contactsPhone": "15112545693"},
                 {"pointType": 20, "pointAddress": "北京市东城区东华门街道公安部中华人民共和国公安部", "pointLongitude": "116.405779",
                  "pointLatitude": "39.90621", "pointCode": "110101", "pointSort": 1, "contacts": "赵测试",
                  "contactsPhone": "15112545694"}], "cargoGoodsList": [
                 {"tempId": "2b0rc8smxdi", "priceMode": "0", "goodsItemGrossWeight": 1000000,
                  "descriptionOfGoods": "石头",
                  "cargoTypeClassificationCode": "0200", "goodsItemCube": 20000000, "totalNumberOfPackages": 5,
                  "unitPrice": 200000, "accountReceivable": 1000000}]}], "receipt": {"mailBack": 0, "uploadPhoto": 0},
                 "pointList": [{"contacts": "苦测试", "contactsPhone": "15112545691", "sendTime": "2021-04-20T11:44:06",
                                "arriveTime": "2021-04-20T11:41:53", "pointAddress": "广东省深圳市南山区南山街道学府路大新时代大厦",
                                "pointCode": "440305", "pointLatitude": "22.528034", "pointLongitude": "113.911818",
                                "pointSort": 0, "operationType": 1, "pointType": 10},
                               {"contacts": "禹测试", "contactsPhone": "15112515693",
                                "pointAddress": "北京市东城区东华门街道公安部中华人民共和国公安部", "pointCode": "110101",
                                "pointLatitude": "39.90621", "pointLongitude": "116.405779", "pointSort": 1,
                                "operationType": 2, "pointType": 20}],
                 "pointOperationList": [{"cargoRequestNo": "X7693466880003968", "pointSort": 0, "operationType": 1},
                                        {"cargoRequestNo": "X7693466880003968", "pointSort": 1, "operationType": 2}],
                 "costCent": 100000,
                 "attachList": [{"attachCatalog": "20", "attachGroup": "30", "attachKey": "1003998"}], "assignList": [
                 {"assignType": 1, "platformUndertakeDuty": 0, "driverPhone": "18200003333", "driverName": "陈浩",
                  "driverId": "102112000024", "carrierDriverId": "2358258", "vehicleId": "183",
                  "carrierVehicleId": "6358202", "vehicleNumber": "浙B7F925", "vehiclePlateColorCode": "2"}],
                 "operateType": 1}
         headers = {"content-type": 'application/json; charset=utf-8', "authorization": self.token}
         with self.client.post(Url, data=data, headers=headers) as response:
             print(response.json())


class WebsiteUser(HttpUser):
    # task_set = WebsiteTasks  # Usage of User.task_set is deprecated since version 1.0. Set the tasks attribute instead (tasks = [WebsiteTasks])
    tasks = [WebsiteTasks]
    host = "https://uat.pxxtech.com"
    min_wait = 1000
    max_wait = 5000