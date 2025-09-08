import os
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Annotated
from loguru import logger
class AppBaseSetting(BaseSettings):
        """Application setting - base calss"""

        model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
        env_nested_delimiter="__",
    )
        
class DBSetting(AppBaseSetting):
    """Database settings"""
    db_url: Annotated[str, Field(description="Database connection URL")]

class LangChainSetting(AppBaseSetting):
    """Lang Chain Setting
        LC__<name variable> in file .env
        model_config = SettingsConfigDict(env_prefix="LC")
    """

    langchain_tracing_v2: Annotated[bool, Field(
        default=False, description="Lang chai traicing")]
    langsmith_api_key: Annotated[SecretStr, Field(description="API KEY LANGSMITH")]



class LLMSetting(AppBaseSetting):
    """Model_setting SettingsConfigDict(env_prefix='LLM')"""
    openai_model: Annotated[str, Field(description="Name model OpenAI")]
    openai_api_key: Annotated[SecretStr, Field(description="API key OpenAI")]
    temperature: Annotated[float, Field(default=0.1, description="Temperature")]
    tavily_api_key: Annotated[SecretStr, Field(description="API KEY TAVILY")]


class AppSetting(AppBaseSetting):
    """Application settings"""
    app_name: Annotated[str, Field(
        default="Multi Agent System", description="Application name")]
    app_version: Annotated[str, Field(description="")]
    app_description: Annotated[str, Field(description="")]
    app_suport_email: Annotated[str, Field(description="")]
    llm: Annotated[LLMSetting, Field(description="App settings to LLM")]
    db_work: Annotated[DBSetting, Field(
        description="App settings to work database")]
    lc: Annotated[LangChainSetting, Field(description="Lang Chain Setting")]

if __name__ == "__main__":
    setting = AppSetting()
    logger.info(f"app name: {setting.app_name}")
    logger.info(f"db url: {setting.db_work.db_url}")