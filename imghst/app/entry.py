
from .configuration.configuration import Configuration
from .app import app

import uvicorn


def entry():
    uvicorn.run(app, port=Configuration.port_number_to_run_on)