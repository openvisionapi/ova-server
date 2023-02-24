#!/usr/bin/env python3

from pathlib import Path

import click
import requests

from api.config.api.config import config

model_base_url = "https://huggingface.co/openvisionapi/{model}/resolve/main/{file_name}"


@click.group()
def cli():
    pass


@cli.command()
@click.option("--model", required=True, help="Model name", type=click.Choice(["yolov4"]))
@click.option(
    "--framework",
    required=True,
    help="Deep learning framework",
    type=click.Choice(["tensorflow", "tensorflow_lite"]),
)
@click.option(
    "--hardware",
    required=True,
    help="Dardware accelerator",
    type=click.Choice(["cpu", "gpu", "edgetpu"]),
)
def download(model, framework, hardware):
    Path(f"{config.MODELS_FOLDER}/{framework}/{hardware}/{model}").mkdir(
        parents=True, exist_ok=True
    )
    if framework == "tensorflow":
        file_name = f"{model}.h5"

    elif framework == "tensorflow_lite":
        if hardware == "edgetpu":
            file_name = f"{model}-edgtpu.tflite"
        else:
            file_name = f"{model}.tflite"

    model_url = model_base_url.format(model=model, file_name=file_name)

    if Path(f"{config.MODELS_FOLDER}/{framework}/{hardware}/{model}/{file_name}").exists():
        click.echo(f"The model {model} exists already. Skipping download")
    else:
        try:
            click.echo(f"Download the model: {model}")
            response = requests.get(url=model_url)
            response.raise_for_status()
            with open(
                f"{config.MODELS_FOLDER}/{framework}/{hardware}/{model}/{file_name}", "wb"
            ) as f:
                f.write(response.content)
        except Exception as e:
            raise SystemExit(e)

    if Path(f"{config.MODELS_FOLDER}/{framework}/{hardware}/{model}/labels.txt").exists():
        click.echo("The label.txt file exists already. Skipping download")
    else:
        try:
            click.echo("Download labels file")
            url = model_base_url.format(model=model, file_name="labels.txt")
            response = requests.get(url=url)
            response.raise_for_status()
            with open(
                f"{config.MODELS_FOLDER}/{framework}/{hardware}/{model}/labels.txt", "wb"
            ) as f:
                f.write(response.content)
        except Exception as e:
            raise SystemExit(e)


if __name__ == "__main__":
    cli()
