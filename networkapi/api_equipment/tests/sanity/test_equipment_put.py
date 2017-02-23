# -*- coding: utf-8 -*-
import json
import logging

from django.core.management import call_command
from django.test.client import Client

from networkapi.test.test_case import NetworkApiTestCase

log = logging.getLogger(__name__)


def setup():
    call_command(
        'loaddata',
        'networkapi/system/fixtures/initial_variables.json',
        'networkapi/usuario/fixtures/initial_usuario.json',
        'networkapi/grupo/fixtures/initial_ugrupo.json',
        'networkapi/usuario/fixtures/initial_usuariogrupo.json',
        'networkapi/grupo/fixtures/initial_permissions.json',
        'networkapi/grupo/fixtures/initial_permissoes_administrativas.json',
        'networkapi/api_equipment/fixtures/initial_pre_equipment.json',
        verbosity=0
    )


class EquipmentPutTestCase(NetworkApiTestCase):

    fixtures = [
        'networkapi/api_equipment/fixtures/initial_base.json',
    ]

    json_path = 'api_equipment/tests/sanity/json/put/%s'

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_put_one_equipment_success(self):
        """Test of success to put of one equipment."""

        name_file = self.json_path % 'put_one_equipment.json'

        # Does put request
        response = self.client.put(
            '/api/v3/equipment/1/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        # Does get request
        response = self.client.get(
            '/api/v3/equipment/1/',
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        self.compare_json(name_file, response.data)

    def test_put_one_equipment_add_groups(self):
        """Test of success to put of one equipment adding one group."""

        name_file = self.json_path % 'put_one_equipment_add_groups.json'

        # Does put request
        response = self.client.put(
            '/api/v3/equipment/1/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        # Does get request
        response = self.client.get(
            '/api/v3/equipment/1/?include=groups',
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        self.compare_json(name_file, response.data)

    def test_put_one_equipment_update_groups(self):
        """Test of success to put of one equipment update group."""

        name_file = self.json_path % 'put_one_equipment_update_groups.json'

        # Does put request
        response = self.client.put(
            '/api/v3/equipment/1/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        # Does get request
        response = self.client.get(
            '/api/v3/equipment/1/?include=groups',
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        self.compare_json(name_file, response.data)

    def test_put_one_equipment_new_groups(self):
        """Test of success to put of one equipment with new group."""

        name_file = self.json_path % 'put_one_equipment_new_groups.json'

        # Does put request
        response = self.client.put(
            '/api/v3/equipment/1/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        # Does get request
        response = self.client.get(
            '/api/v3/equipment/1/?include=groups',
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        self.compare_json(name_file, response.data)

    def test_put_one_equipment_add_environments(self):
        """Test of success to put of one equipment adding one environment."""

        name_file = self.json_path % 'put_one_equipment_add_environments.json'

        # Does put request
        response = self.client.put(
            '/api/v3/equipment/1/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        # Does get request
        response = self.client.get(
            '/api/v3/equipment/1/?include=environments',
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        self.compare_json(name_file, response.data)

    def test_put_one_equipment_update_environments(self):
        """Test of success to put of one equipment update environment."""

        name_file = self.json_path % 'put_one_equipment_update_environments.json'

        # Does put request
        response = self.client.put(
            '/api/v3/equipment/1/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        # Does get request
        response = self.client.get(
            '/api/v3/equipment/1/?include=environments',
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        self.compare_json(name_file, response.data)

    def test_put_one_equipment_new_environments(self):
        """Test of success to put of one equipment with new environment."""

        name_file = self.json_path % 'put_one_equipment_new_environments.json'

        # Does put request
        response = self.client.put(
            '/api/v3/equipment/1/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        # Does get request
        response = self.client.get(
            '/api/v3/equipment/1/?include=environments',
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        self.compare_json(name_file, response.data)


class EquipmentputErrorTestCase(NetworkApiTestCase):

    fixtures = [
        'networkapi/api_equipment/fixtures/initial_base.json',
    ]

    json_path = 'api_equipment/tests/sanity/json/put/%s'

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_put_duplicated_equipment(self):
        """Test of error to put of one equipment with name already existent."""

        name_file = self.json_path % 'put_one_duplicated_equipment.json'

        # Does put request
        response = self.client.put(
            '/api/v3/equipment/1/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(400, response.status_code)

        self.compare_values(
            'There is another equipment with same name VM-SANITY-TEST-02',
            response.data['detail'])

    def test_put_equipment_invalid_env(self):
        """Test of error to put of one equipment with environment non existent.
        """

        name_file = self.json_path % 'put_one_equipment_invalid_env.json'

        # Does put request
        response = self.client.put(
            '/api/v3/equipment/1/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(400, response.status_code)

        self.compare_values(
            'There is no environment with id = 10.',
            response.data['detail'])

    def test_put_equipment_invalid_group(self):
        """Test of error to put of one equipment with group non existent.
        """

        name_file = self.json_path % 'put_one_equipment_invalid_group.json'

        # Does put request
        response = self.client.put(
            '/api/v3/equipment/1/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(400, response.status_code)

        self.compare_values(
            'There is no group with a pk = 10.',
            response.data['detail'])
