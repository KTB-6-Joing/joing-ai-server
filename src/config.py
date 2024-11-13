import boto3
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # comment it when you test it in local
    # OPENAI_API_KEY: str
    # model_config = SettingsConfigDict(env_file="../.env")

    # Parameter Store Settings
    class Settings(BaseSettings):
    OPENAI_API_KEY: str = None
    AWS_REGION: str = "ap-northeast-2"
    PARAMETER_NAME: str = "/joing/ai/openai-key"  # Parameter Store의 파라미터 이름

    def __init__(self):
        super().__init__()
        if not self.OPENAI_API_KEY:
            self.OPENAI_API_KEY = self.get_parameter_from_aws()

    def get_parameter_from_aws(self) -> str:
        try:
            ssm = boto3.client('ssm', region_name=self.AWS_REGION)
            response = ssm.get_parameter(
                Name=self.PARAMETER_NAME,
                WithDecryption=True
            )
            return response['Parameter']['Value']
        except Exception as e:
            raise Exception(f"Failed to get OPENAI_API_KEY from AWS Parameter Store: {str(e)}")


settings = Settings()
