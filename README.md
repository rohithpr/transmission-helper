# Transmission Helper

A script that helps to shutdown your computer once your downloads have finished.

### Setup

* Create a virtualenv called `venv` in the same directory as `loader.sh`.
* Install transmissionrpc, Tkinter and tkMessageBox in the `venv`.
* Write the command that can be used to shutdown the system without getting a prompt for a password in the file `command`.
* The default command file requires `consolekit` to be installed.
* You may have to enable remote access (port 9091) on Transmission for this program to work correctly.

## Testing it's working

Executing `sh loader.sh` should do the following in the said scenarios. Please try it out in the given order.

* Transmission is not running: return propmt.
* Transmission is running and has active downloads: return propmt.
* Transmission is running and does not have active downloads: open dialog box.
    1. Clicking on `Cancel` returns the prompt
    2. Clicking on `Ok` shuts down your computer
