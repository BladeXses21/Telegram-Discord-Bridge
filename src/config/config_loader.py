from dotenv import load_dotenv


class ConfigLoader:
    def __init__(self, config_path = ".env"):
        load_dotenv(dotenv_path=config_path)

    def get_config(self, key, default = None):
        import os

        value = os.getenv(key, default)
        if not value:
            raise ValueError(f"Configuration {key} not found.")
        return value
