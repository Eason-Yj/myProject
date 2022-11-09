#!/usr/bin/env python
# -*- coding=utf8 -*-
################################################################
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#
################################################################
"""
Dataset Client
"""
import hashlib
import json
import threading
import time
import uuid
import datetime
import requests
import logging

logger = logging

DatasetHttpConfig = {"CreateDatasetUri": "/api/v4/dataset",
                     "GetDatasetUri": "/api/v4/dataset/{}",
                     "InferDatasetSchemaUri": "/api/v4/dataset/{}/schema",
                     "UploadDatasetUri": "/api/v4/dataset/{}?action=upload",
                     "CreateDatasetRetryTimes": 1,
                     "InferDatasetRetryTimes": 1,
                     "UploadDatasetRetryTimes": 1,
                     "ExportDatasetUri": "/canghai/api",
                     "ExportStatusUri": "/canghai/api/exportStatus",
                     "GetDatasetV1Uri": "/api/v1/dataset/{}"
                     }
"""Global HEADER KEY"""
X_BCE_REQUEST_ID_KEY = "X-Bce-Request-ID"
X_BCE_REQUEST_ACCESS_ADDRESS_KEY = "X-Bce-Request-Access-Address"
ACCESS_KEY = "Access-Key"
TOKEN_KEY = "Token"
SIGN_TIME_KEY = "Sign-Time"
SECRET_KEY = "Secret-Key"


class DatasetClient(object):
    """
    发送到数据集的client
    """
    org_id = None
    project_id = None
    sk = "sk"
    ak = "ak"
    tracking_url = "http://127.0.0.1:8080"
    is_mock = None

    mocked_create_dataset_detail = None
    mocked_get_dataset_detail = None
    mocked_infer_dataset_schema = None
    mocked_upload_dataset_response = None

    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(DatasetClient, "_instance"):
            with DatasetClient._instance_lock:
                if not hasattr(DatasetClient, "_instance"):
                    DatasetClient._instance = object.__new__(cls)
        return DatasetClient._instance

    @classmethod
    def set_bml_auth_headers(cls, request_body=None):
        """
        set parameter in config for Authentication
        """
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        request_id = uuid.uuid4()
        header_params = {SIGN_TIME_KEY: now,
                         X_BCE_REQUEST_ID_KEY: str(request_id),
                         X_BCE_REQUEST_ACCESS_ADDRESS_KEY: "",
                         ACCESS_KEY: cls.ak,
                         SECRET_KEY: cls.sk}
        if request_body:
            token_str = json.dumps(request_body) + cls.sk + header_params[X_BCE_REQUEST_ID_KEY] + \
                        header_params[SIGN_TIME_KEY]
        else:
            token_str = "" + cls.sk + header_params[X_BCE_REQUEST_ID_KEY] + header_params[
                SIGN_TIME_KEY]
        encode_token = hashlib.sha256(token_str.encode('utf-8')).hexdigest()
        header_params[TOKEN_KEY] = encode_token
        return header_params

    @classmethod
    def export_dataset(cls, dataset_id, volume_id, project_id, storage_path):
        """
        智能数据数据集导出
        """
        if cls.is_mock is True:
            return cls.mocked_get_dataset_detail
        if cls.tracking_url is not None:
            request_url = cls.tracking_url + DatasetHttpConfig["ExportDatasetUri"]
            export_dataset_param = {
                "method": "bml/exportDataset",
                "sourceDatasetId": int(dataset_id),
                "exportType": 1,
                "exportFormat": 102,
                "destination": 2,
                "volumeId": volume_id,
                "storagePath": storage_path,
                "projectId": project_id,
                "isPublishPublic": False,
                "isPublishToBml": True
            }
            headers = cls.set_bml_auth_headers(export_dataset_param)
            logger.info("get_dataset...request_url:{}".format(request_url))
            logger.info("get_dataset...headers:{}".format(headers))
            response = requests.post(request_url, json=export_dataset_param, headers=headers)
            if response.status_code == 200:
                content = json.loads(response.text)
                return content
            else:
                logger.error("get_dataset error:{}".format(response.text))
                raise ValueError("get_dataset err")
        else:
            raise ValueError("dataset tracking client is not initialized")

    @classmethod
    def export_status(cls, exp_id):
        """
        获取某个数据集导出任务的状态
        """
        if cls.is_mock is True:
            return cls.mocked_get_dataset_detail
        if cls.tracking_url is not None:
            request_url = cls.tracking_url + DatasetHttpConfig["ExportStatusUri"]
            export_dataset_param = {
                "id": int(exp_id),
                "method": "dataset/exportStatus"
            }
            headers = cls.set_bml_auth_headers(export_dataset_param)
            logger.info("get_dataset...request_url:{}".format(request_url))
            logger.info("get_dataset...headers:{}".format(headers))
            response = requests.post(request_url, json=export_dataset_param, headers=headers)
            content = json.loads(response.text)
            if response.status_code == 200:
                return content
            else:
                logger.error("get_dataset error:{}".format(response.text))
                raise ValueError("get_dataset err")
        else:
            raise ValueError("dataset tracking client is not initialized")

    @classmethod
    def get_easydata_dataset(cls, bmlDatasetId):
        """
        通过 bml DatasetId 获取 easyData DatasetId
        """
        if cls.is_mock is True:
            return cls.mocked_get_dataset_detail
        if cls.tracking_url is not None:
            request_url = cls.tracking_url + DatasetHttpConfig["GetDatasetV1Uri"].format(bmlDatasetId)
            headers = cls.set_bml_auth_headers()
            logger.info("get_dataset...request_url:{}".format(request_url))
            logger.info("get_dataset...headers:{}".format(headers))
            response = requests.get(request_url, headers=headers)
            if response.status_code == 200:
                content = json.loads(response.text)
                return content
            else:
                logger.error("get_dataset error:{}".format(response.text))
                raise ValueError("get_dataset err")
        else:
            raise ValueError("dataset tracking client is not initialized")


if __name__ == '__main__':
    # DatasetClient.export_status(1000)
    DatasetClient.get_easydata_dataset(bmlDatasetId="1000")
    # DatasetClient.export_dataset(dataset_id=1000, volume_id="volume_id",
    #                              project_id="project_id", storage_path="storage_path")
