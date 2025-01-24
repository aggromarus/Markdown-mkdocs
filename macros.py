import os
import yaml

def define_env(env):
    # Базовая папка, где хранятся данные
    base_dir = "data"

    # Проходим по всем поддиректориям
    for service_name in os.listdir(base_dir):
        service_path = os.path.join(base_dir, service_name)

        # Проверяем, что это директория
        if os.path.isdir(service_path):
            variables_path = os.path.join(service_path, "variables.yml")
            
            # Загружаем YAML-файл с переменными
            if os.path.exists(variables_path):
                with open(variables_path, "r", encoding="utf-8") as f:
                    env.variables[service_name] = yaml.safe_load(f)
