import os
import pkgutil
from importlib import import_module

PROTOCOLS = list()

current_path = os.path.dirname(os.path.abspath(__file__))

for submodule in pkgutil.iter_modules([current_path]):
    if submodule.ispkg:
        module = import_module(name=f".{submodule.name}", package="driver.protocols")
        module_with_protocol = import_module(
            name=f".{submodule.name}.protocol", package="driver.protocols"
        )
        class_ = getattr(module_with_protocol, "Protocol")
        PROTOCOLS.append(
            {
                "uuid": module.UUID,
                "name": module.NAME,
                "description": module.DESCRIPTION,
                "class": class_,
            }
        )
