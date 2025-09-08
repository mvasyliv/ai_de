from src.setting import app_setting

def test_app_setting():
    assert app_setting.app_name == "Multi Agent"
    assert app_setting.app_version == "0.0.1"
    assert app_setting.app_description == "MULTI AGENT SYSTEM WITH SUPERVISER"
    assert app_setting.app_suport_email == "support@gmail.com"
    assert app_setting.llm.openai_model == "gpt-4o"
    assert app_setting.llm.temperature == 0.1
    assert app_setting.llm.openai_api_key is not None
    assert app_setting.llm.tavily_api_key is not None
if __name__ == "__main__":
    test_app_setting()