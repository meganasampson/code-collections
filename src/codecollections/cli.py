import typer
import os
from pathlib import Path

app = typer.Typer()

@app.command()
def showdir():
    print(os.getcwd())

@app.command()
def repeat(repeat: str):
    print(f"repeating: {repeat}")

@app.command()
def getpath(mypath: Path):
    print(mypath)

if __name__ == "__main__":
    app()