import os
import typer
import subprocess
from rich.console import Console
from rich.table import Table


console = Console(emoji=False)
app = typer.Typer()

@app.callback(
    invoke_without_command=True,
    help="""Check unnecessary directories in attic."""
)
def ls():

    env = os.environ.copy()
    e = subprocess.Popen('$SHELL -c -i alias', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
    output, error = e.communicate()

    aliases = Table(title=f"Aliases")
    aliases.add_column("Alias", style="green")
    aliases.add_column("Definition", style="cyan")

    for cmd in output.decode().split('\n'):
        cmd = cmd.strip()
        if cmd:
            alias, alias_cmd = cmd.split('=', 1)
            aliases.add_row(alias, alias_cmd.strip("'"))

    console.print(aliases)