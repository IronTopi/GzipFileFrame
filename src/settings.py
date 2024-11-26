from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    zip_file_path: str = "tmp/random_data.txt.gz"
    data_size: int = 524288000  # 5 MB in bytes
    use_random_data: bool = False
    header: str = "This is a header for the file."

    class Config:
        env_file = ".env"


settings = Settings()
