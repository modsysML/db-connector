# Copyright: (c) 2022, Adrian Brown <adrbrownx@gmail.com>
# Copyright: (c) 2023, ModsysML Project
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from .base import AbstractFirebaseClient


class FirebaseClient(AbstractFirebaseClient):
    @staticmethod
    def __init__(self, database_url, credentials_path):
        self.database_url = database_url
        self.credentials_path = credentials_path
        self.initialize_firebase()

    def initialize_firebase(self):
        cred = credentials.Certificate(self.credentials_path)
        firebase_admin.initialize_app(cred, {"databaseURL": self.database_url})

    def execute(self, path, action="get", data=None):
        if not path:
            raise ValueError("Path is required for Firebase operations")

        ref = db.reference(path)

        try:
            if action == "get":
                return ref.get()
            elif action == "set":
                if data is None:
                    raise ValueError("Data is required for 'set' action")
                ref.set(json.loads(data))
                return "Data set successfully"
            elif action == "update":
                if data is None:
                    raise ValueError("Data is required for 'update' action")
                ref.update(json.loads(data))
                return "Data updated successfully"
            else:
                raise ValueError(f"Unsupported action: {action}")
        except Exception as e:
            # will add logic for this exception as I commit changes
            raise e
