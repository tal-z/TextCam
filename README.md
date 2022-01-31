# TextCam!

Textcam displays a super low-res stream of ASCII-art, pulled directly from a client's webcam and displayed over a server to another client. 

![Hello World!](https://raw.githubusercontent.com/tal-z/TextCam/master/hello_world.gif)


## How It Works
TextCam uses Flask to serve up templates.
The templates contain javascript that interfaces with the Flask server.

The first template to note is `recorder.html`. 
This template contains the JavaScript necessary to access the client's webcam and send frame data to the server.

The second template to note is `webcam_feed.html`.
This template contains the JavaScript necessary to pull frame data from the server.

These templates are each routes through the server, which processes received data with the `image2text` Python module.

Finally, the`webcam_feed.html` template is embedded in the `viewer.html` template. 
The `viewer.html` template is responsible for controlling the display/formatting of the text with CSS.