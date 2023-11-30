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

from django.utils.module_loading import import_string

from core.const import FIREBASE_CLIENT_CLASS, SUPABASE_CLIENT_CLASS
from core.database.firebase.base import AbstractFirebaseClient
from core.database.supabase.base import AbstractSupabaseClient


def get_supabase_client(connection_string) -> AbstractSupabaseClient:
    client = import_string(SUPABASE_CLIENT_CLASS)
    return client(connection_string)


def get_firebase_client(service_account_key) -> AbstractFirebaseClient:
    client = import_string(FIREBASE_CLIENT_CLASS)
    return client(service_account_key)
