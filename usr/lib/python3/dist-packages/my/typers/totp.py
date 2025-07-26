import os
import typer
import pyotp
import datetime
from rich.console import Console
from typing_extensions import Annotated


TOTP_FILE = os.path.expanduser('~/.ssh/tfa.txt')

console = Console(emoji=False)
app = typer.Typer()

@app.callback(
    invoke_without_command=True,
    help="""Print an actual TOTP code based on the entries in ~/.ssh/tfa.txt"""
)
def ls(host: Annotated[str, typer.Argument()] = ''):

    totp_key = ''

    try:
        with open(TOTP_FILE, 'r') as f:
            for line in f:
                server, key = line.strip().split(':')

                if server == host:
                    totp_key = key
                    break

    except Exception as e:
        typer.secho(f"Error: {str(e)}. Be sure to check your ~/.ssh/tfa.txt. "
                      f"It should contain lines like keyname:secret "
                      f"for each TOTP you want to use.", fg=typer.colors.RED)

    if totp_key:
        try:
            totp = pyotp.TOTP(totp_key)
            code = totp.now()
            time_remaining = round(
                totp.interval - datetime.datetime.now().timestamp() % totp.interval)
            console.print(f"{code} (expires in {time_remaining}s)")
        except Exception as e:
            typer.secho(f"Error generating a TOTP: {str(e)}. "
                          f"Are you sure to use a valid secret for {host}?", fg=typer.colors.RED)
    else:
        typer.secho(f"Host {host} not found", fg=(215,135,0))
