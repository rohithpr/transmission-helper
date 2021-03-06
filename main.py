'''
Checks if there are any active downloads pending and initiates a shutdown
procedure in case all downloads have finished.
'''

import os
import threading
import time
import Tkinter
import tkMessageBox
import transmissionrpc

# Set to False if user clicks on Cancel
# Set to True if user clicks on Ok or doesn't respond
SHUTDOWN = None

def get_download_status():
    ''' (None) -> bool
    Returns False if any file is still being downloaded or if
    Transmission is not reachable at localhost:9091.
    '''
    try:
        tc = transmissionrpc.Client('localhost', port=9091)
        torrents = tc.get_torrents()
        for torrent in torrents:
            if torrent.status == 'downloading':
                return False
        return True
    except: # Couldn't connect, don't try to shutdown
        return False

def show_message_box():
    ''' (None) -> None
    Show a dialog box so that the user can cancel the shutdown process.
    The global variable SHUTDOWN is set if the user responds to the dialog box.
    '''
    global SHUTDOWN

    # Create a temp window so that there aren't two windows on opening the message box
    temp = Tkinter.Tk()
    temp.withdraw()

    # Set global variable to the response received from the user
    SHUTDOWN = tkMessageBox.askokcancel(
            title="All torrents downloaded", 
            message="Computer is about to be shutdown.\
             Press cancel to abort!")
    return

def main():
    ''' (None) -> bool
    Checks the status of active downloads and initiates shutdown procedure.
    '''
    global SHUTDOWN
    all_done = get_download_status()

    # Open dialog box if all the downloads have finished
    if all_done:
        gui_thread = threading.Thread(target=show_message_box)
        gui_thread.start()

        # User gets 120 seconds to abort the operation
        for i in range(60):
            time.sleep(2)
            # Check if the user has responded to the dialogbox
            if SHUTDOWN is not None:
                gui_thread.join()
                break
        else: # Shutdown if user hasn't taken any action 
            SHUTDOWN = True
        return SHUTDOWN
    else: # Don't shutdown, active downloads or transmission offline
        return SHUTDOWN

def shutdown():
    ''' (None)
    Reads and executes the contents of the file 'command' to shut down the computer.
    '''
    with open('command') as fp:
        command = fp.readline()
    os.system(command)

if __name__ == '__main__':
    action = main()
    if action:
        shutdown()
