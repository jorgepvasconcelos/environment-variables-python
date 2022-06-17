import os
from pprint import pprint

from pydantic import BaseModel

__os_env_values = dict(os.environ)


class EnvModel(BaseModel):
    PROCESSOR_ARCHITECTURE: str
    OS: str


ENV = EnvModel(**__os_env_values)
print(ENV.OS)
