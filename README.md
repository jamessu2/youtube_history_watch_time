# youtube_history_watch_time
See how much time you've wasted on Youtube


Goals:
- Figure out how to ping the Youtube API with an API key
	- Need OAuth instead?
- Get a list of Youtube video links from my watch history
- Find the videos in that list that have been watched since 6am of that day
- Retreive the watch time / video length of those videos
- Calculate a total sum of time wasted on Youtube
- Also print out the name of each video, and the watch time / video length associated with that video





If on a Mac, for the first time you need to:

```
cd /Applications/Python3.7	# or whatever your Python version is
./Install\ Certificates.command
```

to resolve a *"certificate verify failed"* error.

From https://github.com/nficano/pytube/issues/241: "It installs a set of default Root Certificates for the python ssl module by installing the certifi https://pypi.python.org/pypi/certifi."