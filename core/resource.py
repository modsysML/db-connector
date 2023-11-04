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

from core.const import QUERY_CONTEXT
from core.manager import (
    FirebaseConnectionManager,
    PostgresConnectionManager,
    ProviderConnectionManager,
)


class Firebase:
    _manager = FirebaseConnectionManager()

    _firebase_curs = None


class Postgres:
    # Specific sql queries
    _context = QUERY_CONTEXT

    # Database utility class
    _manager = PostgresConnectionManager()

    # curosr instance
    psql_curs = None


class General(
    Firebase,
    Postgres,
):
    # Current LLM to be used
    model = None

    # Class instance connection manager to AI providers
    _api_manager = ProviderConnectionManager()
