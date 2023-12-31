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

from core import get_firebase_client, get_supabase_client
from core.exceptions import EmptyResultsWarning


class PostgresConnectionManager:
    @staticmethod
    def connect_to_prefix(uri):
        return get_supabase_client(uri)

    @staticmethod
    def convert_dict(items):
        if not items:
            raise EmptyResultsWarning(items)

        vector = []

        for i in items:
            vector.append(dict(i))

        return vector


class FirebaseConnectionManager:
    @staticmethod
    def connect_to_prefix(service_account_key):
        return get_firebase_client(service_account_key)
