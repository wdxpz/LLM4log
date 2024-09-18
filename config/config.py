from utils.arg_helper import get_config

config = None

def global_config():
    global config

    if config is None:
        config = get_config('/app/config/config.yaml')
    return config