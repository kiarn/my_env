# my

Simple tool to display my personal configuration (ssh config, ssh keys, aliases ...) in a pretty way. This tool is based on [typer](https://github.com/fastapi/typer).

## Some examples

  * `my aliases` will give a table with all my personal aliases,
  * `my aliases FILTER` will give a table with all my personal aliases containing the string `FILTER`,
  * `my ssh` will output a table containing the content of `~.ssh/config` (Hosts, User, IdentityFile, Port, ...), one line per host,
  * `my ssh FILTER` will filter the above table with the hosts containing `FILTER`,
  * `my ssh_keys` lists recursively my SSH keys under `~/.ssh` and gives for each key the type and the length.


