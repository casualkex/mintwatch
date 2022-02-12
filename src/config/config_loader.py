import toml

from config.models import Config, Service
from telegram import Bot


def load_config():
    base_config_name = "BASE"
    config_file_path = "./config.toml"

    toml_obj = toml.load(config_file_path)
    config = Config(**toml_obj.get(base_config_name))
    config.bot = Bot(token=config.token, chat_id=config.chat_id)

    services = [service for service in toml_obj if service != base_config_name]
    for service in services:
        config.service_configs.append(Service(**toml_obj.get(service)))

    return config
