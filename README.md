# perfect_circle
A script that draws a perfect circle in the middle of the display.
Written for https://neal.fun/perfect-circle/

# How to use
## Dependencies
- Python
- pip
- PyAutoGUI

To be honest, I haven't tested this script on other systems, so if you have any problems running the code, solve problems according to Python output.

## Step-by-step Guide on usage
After you installed all the dependencies and ran "python draw_circle.py" in your console/terminal, you should see a little hint, how to use the script. Square brackets ([]) mean that the argument is optional.
radius - radius of the square, limited with the size of your display;
waiting time - it's time you have to focus on your browser (or another application where you need a perfect circle);
step - determines difference between two dots in degrees.

After you run the script with appopriate arguments, you should move to your browser or another application.

# Known Bugs
- There is no standard way of canceling the process, so when the script starts drawing circles, the only way is aborting the process (close the terminal or Ctrl + C)
- The script is very slow due to limitations of used library (PyAutoGUI)
- I haven't tested this program on Windows, only Linux (Fedora 38 w/ KDE Plasma + X11 & Wayland), so maybe it doesn't work on Windows at all :)
- If you have dual (or more) monitors, you should either stretch the browser over the entire area or temporarly disconnect a monitor
