# Google+ Activity Saver

A Django application that saves Google+ activities in to a local database.

## Usage
### Installation:
1. Copy gplusacts to your project directory.
2. Include “gplusacts” in your project's settings.py.
3. Include a URL to your project's urls.py like:  
url(r"^gplus/", include("gplusacts.urls"))
4. Run “./manage.py syncdb” to create the database.

### Downloading an activities feed:
(Might be good idea to put this in a Crontab.)  
./manage.py gplusactsdl [profile id] [api key]

## Why am I doing this?
I'm learning Django and this seems like a nice project to get me going. I know that you can use the Google+ API directly on a web page and just process the JSON on the fly. However, I figured that if I did that on several sites hosted under one IP address, I might have to spend extra money on increasing the usage quota. Besides, a wise man once told me that caching never harmed anyone.

## TODO
Dunno. Maybe try to change the way the admin interfaces look? We'll see.

