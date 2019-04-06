# EmailTrackExtension
An extension to track emails being sent.

There are 2 components to this, a frontend chrome-extension and the backend python program running flask.

The chrome extension runs in the background waiting until a browser navigates to a gmail "compose" url, at this point it kicks into action and adds a "Add tracker" button in the same row as the Send button. This button should be clicked just before sending the email, it grabs the email's subject and who it's too and sends it to the server set in the savepixel.js, when the email is opened it'll trigger an image that is in the email(1 pixel and not visible) to ping the server and sending a notification that the email has been opened. Opening the email yourself may trigger this.

Installation:

Setup a dropbox account and get a dropbox API token, put it in the backend.py as equal to the variable dropboxkey.

Then go to notify.run

Click create a channel,

Copy the URL there and open it on all devices you wish to get notifications on, on those devices press subscribe this device.

Put the URL as equal to the variable "notifyendpoint" in the backend.py

Run the backend.py on a server, make sure it is portforwarded, grab the URL to that server including the port, put it in savepixel.js as equal to the serverurl.

Put the files manifest.json, savepixel.js and background.js into a folder, next go to chrome://extensions on your chrome browser, make sure Developer is turned on in the top right hand corner.

Press load unpacked and find the folder you made.

Now when you open a new email in gmail it will offer a button labelled Add tracker.

Press this button just before hitting send(wait 2-3 seconds after pressing the button to be safe).
