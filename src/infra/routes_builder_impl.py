from typing import Callable, Coroutine

from fastapi import FastAPI, Request, Response
from httpx import AsyncClient, Timeout

from src.domain.interfaces.routes_builder_interface import RoutesBuilder
from src.domain.model.route_config import RouteConfig


class RoutesBuilderImpl(RoutesBuilder):

    def __init__(self, app: FastAPI) -> None:
        self.__app = app

    def build_routes(self, route_config_list: list[RouteConfig]) -> None:
        for route_config in route_config_list:
            print(f"Redirecting route '{route_config.route_prefix}' to host '{route_config.destination_host}'")
            self.__build_route_from_config(route_config)

    def __build_route_from_config(self, config: RouteConfig) -> None:
        endpoint = self.__build_endpoint(config)
        self.__app.add_api_route(
            config.route_prefix.replace("*", "{full_path:path}"),
            endpoint,
            methods=["GET", "PUT", "POST", "DELETE", "PATCH", "HEAD", "OPTIONS"]
        )

    def __build_endpoint(self, config: RouteConfig) -> Callable[[Request], Coroutine[None, None, Response]]:
        async def endpoint(request: Request, full_path: str) -> Response:
            print(f"Sending a {request.method} to {config.destination_host+full_path}")
            async with AsyncClient(timeout=Timeout(10., read=None)) as client:
                res = await client.request(
                    request.method,
                    config.destination_host+full_path+self.__get_query_params(request),
                    data=await request.body(),
                    headers=self.__fix_headers(request),
                )
                return Response(res.content, res.status_code, res.headers)
        return endpoint

    @staticmethod
    def __get_query_params(request: Request) -> str:
        return "?" + str(request.query_params) if str(request.query_params) != "" else ""

    @staticmethod
    def __fix_headers(request: Request) -> dict:
        headers = dict(request.headers)
        for header in ["Host", "Content-Length"]:
            headers.pop(header, None)
            headers.pop(header.lower(), None)
        return headers
