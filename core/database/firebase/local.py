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

from .base import AbstractFirebaseClient


class LocalFirebaseClient(AbstractFirebaseClient):
    def initialize_firebase(self):
        print("Initializing local Firebase client")
        # Mock  logic

    def execute(self, path, action="get", data=None):
        if not path:
            raise ValueError("Path is required for Firebase operations")

        print(f"Executing {action} on path: {path}")

        if action == "get":
            return "Mocked data"
        elif action == "set":
            if data is None:
                raise ValueError("Data is required for 'set' action")
            self.mock_database[path] = data
            return "Data set successfully in mock database"
        elif action == "update":
            if data is None:
                raise ValueError("Data is required for 'update' action")
            self.mock_database[path] = {**self.mock_database.get(path, {}), **data}
            return "Data updated successfully in mock database"
        else:
            raise ValueError(f"Unsupported action: {action}")
