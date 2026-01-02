from pathlib import Path

import yaml

from app.models.prompt import AIAgentPrompt


def load_prompt_messages(prompt_files_path: str, version: str) -> AIAgentPrompt:
    """
    Loads system an human prompt stored in a yaml file.

    :param prompt_files_path: path to the prompt folder holding the yaml files
    :param version: version number of the prompt
    :return: loaded system and human prompt from the file
    """
    path = Path(f"{prompt_files_path}/{version}.yaml")

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return AIAgentPrompt(
        system=data["system"]
    )