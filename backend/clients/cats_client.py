from backend.clients.base.request import APIRequest
from utils.config_parser import ConfigParserIni


class CatsClient:
    def __init__(self):
        super().__init__()
        config_reader = ConfigParserIni("backend_props.ini")
        self.base_url = config_reader.config_section_dict("AUT")["host"]

        if self.base_url is None:
            raise Exception("Environment variable must be set 'BASE_URI'")

        self.request = APIRequest()

    def get_random_facts(self):
        return self.base_url + "facts/random"

    def get_fact_by_id(self, id):
        return self.base_url + "facts/" + id
