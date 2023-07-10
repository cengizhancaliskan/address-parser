import typer
from address_parser import AddressParser
import pandas as pd
import regex as re

app = typer.Typer()

address_parser = AddressParser()


@app.command()
def addressline(address: str):
    res = address_parser.parse(address)
    print(res)


if __name__ == "__main__":
    app()
