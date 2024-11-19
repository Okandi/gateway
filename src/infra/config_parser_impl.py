from pathlib import Path
import json

from src.domain.exceptions.config_file_exceptions import ConfigFileNotFound
from src.domain.exceptions.config_file_exceptions import InvalidConfigFormat
from src.domain.interfaces.config_parser_interface import ConfigParser
from src.domain.model.route_config import RouteConfig


class ConfigParserImpl(ConfigParser):

    def get_config_from_file(self, file_path: Path) -> list[RouteConfig]:
        try:
            with open(file_path) as file:
                content = json.load(file)
            return self.__parse_configs(content)
        except (json.decoder.JSONDecodeError, KeyError) as e:
            raise InvalidConfigFormat(f"Couldn't retrieve configurations from file at {file_path}") from e
        except FileNotFoundError as e:
            raise ConfigFileNotFound(f"Couldn't find file at path {file_path.absolute()}") from e

    @staticmethod
    def __parse_configs(json_configs: list[dict[str, str]]) -> list[RouteConfig]:
        configs = []
        for config in json_configs:
            configs.append(RouteConfig(config["route_prefix"], config["destination_host"]))
        return configs
