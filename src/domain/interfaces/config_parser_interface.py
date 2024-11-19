from abc import ABC, abstractmethod
from pathlib import Path

from src.domain.model.route_config import RouteConfig


class ConfigParser(ABC):

    @abstractmethod
    def get_config_from_file(file_path: Path) -> list[RouteConfig]:
        pass
