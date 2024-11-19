from dataclasses import dataclass


@dataclass
class RouteConfig:
    route_prefix: str
    destination_host: str
