import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()


class EnvironmentEnum(Enum):
    TEST = "test"
    DEV = "dev"
    PROD = "prod"

ENVIRONMENT = EnvironmentEnum(os.getenv("ENVIRONMENT", "dev"))
