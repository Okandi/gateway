from pathlib import Path
import sys

from src.domain.exceptions.config_file_exceptions import ConfigFileNotFound
from src.domain.interfaces.config_parser_interface import ConfigParser
from src.domain.interfaces.routes_builder_interface import RoutesBuilder


class CustomGatewayService:

    def __init__(self, config_parser: ConfigParser, routes_builder: RoutesBuilder) -> None:
        self.__config_parser = config_parser
        self.__routes_builder = routes_builder

    def build_custom_gateway(self) -> None:
        config_file_path = self.__find_config_file()
        config_list = self.__config_parser.get_config_from_file(config_file_path)
        self.__routes_builder.build_routes(config_list)

    def __find_config_file(self) -> Path:
        try:
            return Path(sys.argv[1])
        except IndexError as e:
            raise ConfigFileNotFound("Config file path was not provided") from e
