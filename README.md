# Transmission Helper

A script that helps to shutdown your computer once your downloads have finished.

### What it does

* The script checks if all the downloads have finished.
* If they're done then it opens a dialog box informing the user that the computer is about to be shutdown.
* The user get 120 seconds to respond to the dialog box. You may hit `Cancel` to abort shutdown.
* If there has been no input from the user within 120 seconds or if the user clicks `Ok` the computer is shutdown.

#### Note: The dialog box should open even if you are using using another app in fullscreen mode (video player etc) but it hasn't been tested thoroughly.

### Setup

* Clone this directory from Github into your `home` (mandatory) directory.
* Give execution permission to `loader.sh`.
* Create a virtualenv called `venv` in the same directory as `loader.sh`.
* Install transmissionrpc, Tkinter and tkMessageBox in the `venv`.
* Write the command that can be used to shutdown the system without getting a prompt for a password in the file `command`. **It is important that the command does not ask for password**.
* The default command in the file requires `consolekit` to be installed.
* You may have to enable remote access (port 9091) on Transmission for this program to work correctly.
* Get Transmission to execute `loader.sh` on the completion of each download.

## Check the working of the script

Executing `sh loader.sh` should do the following in the said scenarios. Please try it out in the given order.

* Transmission is not running: return propmt.
* Transmission is running and has active downloads: return propmt.
* Transmission is running and does not have active downloads: open dialog box.
  1. Clicking on `Cancel` returns the prompt.
  2. Clicking on `Ok` shuts down your computer.

## Possible sources of errors

* This directory isnt present in your `Home` directory (~).
* The virtual environment isn't called `venv`.
* The command `source` isn't executable from a shell script. This can be fixed.
* The scripts don't have execution permission.
* The command in the file `command` does not shutdown your computer on executing it from a terminal or ask for a password.
* Remote access hasn't been enabled or it's on a port other than 9091.
* The sript isn't being called at the end of a download. Go to `Edit > Preferences > Downloading`, check `Call script when torrent is completed` and point it to `loader.sh`.
