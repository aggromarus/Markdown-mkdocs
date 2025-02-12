import yaml
import os
from pathlib import Path

def define_env(env):
    """Функция для загрузки YAML-файлов из всех подпапок `data/` в макросы MkDocs"""

    base_data_dir = Path(env.conf['docs_dir']).parent / "data"
    env.variables['data'] = {}

    if base_data_dir.exists():
        for folder in base_data_dir.iterdir():
            if folder.is_dir():  # Проверяем, что это папка
                env.variables['data'][folder.stem] = {}

                for file in folder.glob("*.yml"):
                    with open(file, "r", encoding="utf-8") as f:
                        try:
                            key = file.stem  # Имя файла без .yml
                            env.variables['data'][folder.stem][key] = yaml.safe_load(f)
                        except yaml.YAMLError as e:
                            print(f"Ошибка загрузки {file}: {e}")

    env.variables['contract'] = env.variables['data'].get("Contract", {}).get("contract", {})
    env.variables['fuel'] = env.variables['data'].get("FuelCard", {}).get("card", {})
    env.variables['request'] = env.variables['data'].get("Requests", {}).get("request", {})