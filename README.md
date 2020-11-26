# raspi_browser_login

My goal was to have a RasberryPi that controls a TV monitor to lauch a browser, access a particular website and login with a username and password, this was done twice daily (as the browser session would expire after 12 hours and I wanted this website to be logged in 24/7 on this particular monitor).

I scheduled this script to lauch on the Raspberry Pi using crontab.
Here's my guide:

Starting from scratch on a Raspberry Pi 3 Model B with GUI access via VNC:

Open terminal and run the following commands:
sudo apt-get update
sudo apt-get install iceweasel -y
sudo python3 - m install selenium==2.53.5 - (latest version of selenium is not compatible)
sudo reboot

Now we need the Python script shown in the repository saved to the home/pi folder on the Pi.

Then we will use Cron to schedule the script to run:
In Terminal again, type in 'cron -e'.
The part (beginning with 'Edit this file...' and ending with '* m h  dom mon dow   command') should appear, add the additional lines as shown (DISPLAY... etc.) (I also used cron to reboot the Pi daily):

DISPLAY=:0 
TERM=xterm 
UID=0 
USER=root 
XAUTHORITY=/home/pi/.Xauthority

** Edit this file to introduce tasks to be run by cron..... (crontab populates with this notice)

0 9 * * * /usr/bin/python3.4 /home/pi/iris_login.py >> /home/pi/logfile 2>&1
55 11 * * * reboot



