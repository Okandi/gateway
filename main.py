from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.infra.config_parser_impl import ConfigParserImpl
from src.infra.routes_builder_impl import RoutesBuilderImpl
from src.services.custom_gateway_service import CustomGatewayService


app = FastAPI()

service = CustomGatewayService(ConfigParserImpl(), RoutesBuilderImpl(app))
service.build_custom_gateway()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run(app)
