from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    zip_file_path: str = "tmp/random_data.txt.gz"
    data_size: int = 2048

    class Config:
        env_file = ".env"


settings = Settings()
