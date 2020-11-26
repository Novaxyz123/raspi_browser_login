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
The part (beginning with 'Edit this file...' and ending with '* m h  dom mon dow   command') should appear, add the lines I have shown on lines 22-26 and 51-52 below as shown. (I also used cron to reboot the Pi daily):

DISPLAY=:0
TERM=xterm
UID=0
USER=root
XAUTHORITY=/home/pi/.Xauthority

* Edit this file to introduce tasks to be run by cron.
 
* Each task to run has to be defined through a single line
* indicating with different fields when the task will be run
* and what command to run for the task
 
* To define the time you can provide concrete values for
* minute (m), hour (h), day of month (dom), month (mon),
* and day of week (dow) or use '*' in these fields (for 'any'). 
* Notice that tasks will be started based on the cron's system
* daemon's notion of time and timezones.
 
* Output of the crontab jobs (including errors) is sent through
* email to the user the crontab file belongs to (unless redirected).
 
* For example, you can run a backup of all your user accounts
* at 5 a.m every week with:
0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
 
* For more information see the manual pages of crontab(5) and cron(8)
 
* m h  dom mon dow   command

 * 9 * * * /usr/bin/python3.4 /home/pi/iris_login.py >> /home/pi/logfile 2>&1
55 11 * * * reboot
