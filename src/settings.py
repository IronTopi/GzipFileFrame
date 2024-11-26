from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    zip_file_path: str = "tmp/random_data.txt.gz"
    data_size: int = 1073741824  # 1 GB in bytes

    class Config:
        env_file = ".env"


settings = Settings()
