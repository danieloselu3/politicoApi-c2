from app import polApp
from app.config import configs

polApp.config.from_object(configs['development'])


if __name__ == "__main__":
    polApp.run()
    