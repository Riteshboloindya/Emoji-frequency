import requests
import json

# URL = "http://127.0.0.1:8000/Student_api"

def get_data(id =None):
    # globals URL
    print("id",id)
    URL="http://127.0.0.1:8000/Student_api?id="+str(id)
    # data = {}
    # if id is not None:
    #     data={"id":id}
    # json_data =json.dumps(data)

    # r =requests.get(url=URL, data= json_data)
    r =requests.get(url=URL)

    data=r.json()
    print(data)
get_data(2)