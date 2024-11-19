from abc import ABC, abstractmethod

from src.domain.model.route_config import RouteConfig


class RoutesBuilder(ABC):

    @abstractmethod
    def build_routes(route_config_list: list[RouteConfig]) -> None:
        pass
