# youtube_history_watch_time
**INCOMPLETE PROJECT**

See how much time you've wasted on Youtube

# QUICK UPDATE: (Dec 6th, 2019)
It appears that authentification for data retrieval that's specific to a user account requires OAuth, and not just an API key.

For the purposes of getting familiar with the Youtube API, I will play around with projects that play around with public data (in which an API key would be sufficient), and then come back to this project later.


# Goals
- Figure out how to ping the Youtube API with an API key
	- Need OAuth instead?
- Get a list of Youtube video links from my watch history
- Find the videos in that list that have been watched since 6am of that day
- Retreive the watch time / video length of those videos
- Calculate a total sum of time wasted on Youtube
- Also print out the name of each video, and the watch time / video length associated with that video



# Sidenotes

If on a Mac, for the first time you need to:

```
cd /Applications/Python3.7	# or whatever your Python version is
./Install\ Certificates.command
```

to resolve a *"certificate verify failed"* error.

From https://github.com/nficano/pytube/issues/241: "It installs a set of default Root Certificates for the python ssl module by installing the certifi https://pypi.python.org/pypi/certifi."