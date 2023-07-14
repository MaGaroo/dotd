# dotd
Merge files in whatever.d directory into whatever file

## Setup
Downlaod [dotd.py](https://raw.githubusercontent.com/MaGaroo/dotd/main/dotd.py) into a directory in your `PATH` (e.g. `/usr/bin`)

```bash
sudo wget https://raw.githubusercontent.com/MaGaroo/dotd/main/dotd.py -O /usr/bin/dotd
sudo chmod +x /usr/bin/dotd
```

## Usage

```
dotd /path/to/file
```

### Basic Usage
If you have a directory `/path/to/directory` and want to
merge its files into a single file at `/path/to/file`, run
the following:

```
dotd -d /path/to/directory /path/to/file
```

Note: If you don't provide the directory's path, it will
use the default value as the `/path/to/file` with a `.d`
suffix. For example, if the file is `/etc/hosts`, it will
look for the directory at `/etc/hosts.d`.

### Recursive
If you want to merge the files in the whole tree of the
directory, use `-r` or `--recursive` flag with the commmand.

### Cronjob
In real-world use cases, you may need to run this command
periodically. You can use
[crontab](https://www.geeksforgeeks.org/crontab-in-linux-with-examples/)
tool on Linux in order to run the command periodically,
e.g. on every minute.

## Uninstall
Simply remove the script file with `rm`:
```
rm /usr/bin/dotd
```