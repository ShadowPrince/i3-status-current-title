## Overview
Puts current window's title into status bar at position 0, if there is no active window puts there current workspace name.

## Installation
First of all you need [py3status](http://github.com/ultrabug/py3status) installed and configured, than you copy i3-status-current-title.py inside your's plugins directory.

## Configuration
There is some constants located at beginning of the file:

* `MAX_WIDTH`: if length of title greater than that value it will be cutted to last 60 chars (not first, but last).
* `CACHED_TIME`: cached time in seconds, delay in which information about current window updates. Default set to 0, so information updates as fast as py3status updates 
