import dotenv
from pathlib import Path

# read environment variables from .env file
config_dir = Path(__file__).parent.resolve() / "config"
config_env = dotenv.dotenv_values(dotenv_path=config_dir / "bot.env")

telegram_bot_token = config_env["TELEGRAM_BOT_TOKEN"]
openai_api_key = config_env["OPENAI_API_KEY"]
telegram_bot_name = config_env["TELEGRAM_BOT_NAME"]
question_limit_per_user = int(config_env["QUESTION_LIMIT_PER_USER"])