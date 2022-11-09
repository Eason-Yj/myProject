from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/user', methods=["GET"])
def hello_user():
    p = request.args
    return p


@app.route('/canghai/api/', methods=["GET", "POST"])
def export_dataset():
    if request.method == "POST":
        request_body = request.json
        print(request_body)

    result = {
        "success": True,
        "result": {
            "exportId": 125,
            "approvalId": "A7881CDEB8D34387"
        }
    }
    result_json = json.dumps(result)
    return result_json


@app.route('/canghai/api/exportStatus', methods=["GET", "POST"])
def export_status():
    if request.method == "POST":
        request_body = request.json
        print(request_body)
    result = {
        "success": True,
        "result": {
            "status": 2,
            "progress": 30,
            "finishTime": "2020-10-10 15:30:00"
        },
        "log_id": 319374481
    }
    result_json = json.dumps(result)
    return result_json


@app.route('/api/v1/dataset/1000')
def get_dataset():
    result = {
        "result": {
            "id": "1",
            "name": "gc_test_map-V1",
            "type": "TABLE",
            "sceneType": "",
            "description": "",
            "creatorId": "e77e9eb992c74211b51f87117460b586",
            "projectId": "proj-pzi6gb8a8j1pnvl6",
            "orgId": "org-1fqlgynptj0ya26v",
            "visibility": "Project",
            "storage": {
                "storageId": "v-q6nqtnigm4i41top",
                "storageName": "explorer",
                "storagePath": "/home/bml/storage/mnt/v-q6nqtnigm4i41top/_system_/dataset/ds-amtsdca0yqn49thh/parquet"
            },
            "count": 4,
            "createTime": "2022-09-27T14:03:57+08:00",
            "updateTime": "2022-09-27T14:08:13+08:00",
            "importStatus": 0,
            "importProgress": 100,
            "status": 0,
            "templateType": 20100
        },
        "status": 200,
        "success": True
    }
    result_json = json.dumps(result)
    return result_json


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
