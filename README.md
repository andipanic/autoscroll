# autoscroll
Python script using xdotool for automated mouse wheel scrolling.

## Requirements

This was intended to be used on linux.
The only requirement is xdotool and python (and potentially a .autoscroll file).

## About

This script was written around 04/28/2016.
I wrote this to solve the problem of scrolling through wikipedia pages as well as pdfs.

In my usual setup, I have this hooked into a keyboard shortcut (most Window Managers have a way to do this).  The shortcut runs start_autoscroll.sh.  This script checks to see if there is a autoscroll.py process running.  If so, it kills the process.  If not, it starts a new one.

It's only 'eye candy' feature, is that it speeds up to the desired speed.  This is to help adjust your eyes to the jarring effect of moving text.

### Enjoy!
;P
