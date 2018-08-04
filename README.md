# mail-rbl-check
Simple Python script to monitor presence of IP(s) on defined RBL. Designed to
be easily used with other monitoring/alerting tools such as Zabbix. Should work
on any system with Python 2.x/3.x


Description
---------
Script will check if IP or set of IPs is present on predefined RBL set. Can
work in following modes:
1. Global (-g) display occurence count on all RBLs
2. Detailed (-d) diplay status of IP on each RBL

Moreover, if any IP was listed on any RBL, exit code will be different than 0.
Zero means clean pass, no IP(s) listed on RBLs


Requirements
---------
There are none. :-)
It's written with portability in mind, so tried to use as
much already availabe modules as possible. For a price of configuration files
readability/formatting.


Configuration
---------
TODO


Examples
---------
- python rblcheck.py -i 1.2.3.4 - checks if IP 1.2.3.4 is listed on any RBL, status
can be read by exit code.
- python rblcheck.py -i 1.2.3.4 -g - displays on how many RBLs IP 1.2.3.4 was present
- python rblcheck.py -i 1.2.3.4 -d - displays status of IP 1.2.3.4 on each RBL


Usage
---------
- clone this repository
- adjust config files
- run the script (with proper arguments, check examples)


Contribution
---------
Help is always welcome, so clone this repository, send pull requests or create
issues if you find any bugs.


License
---------
See LICENSE file.
