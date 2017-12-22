#prime.py for Cisco Prime API V2
##howto use this program
- On your Cisco prime server you need to setup a user:
Administration -> users, roles, AAA -> users and create a user, asign to NBI Read group.
- Open the code and change the following lines
	- LOGINUSER = 'xxxx'
	- LOGINPASSWORD = 'xxxx'
	- PRIMEIP = 'a.b.c.d'
- now you can run the program
	- python prime.py -user "username" or at leat part of it
	- python prime.py -mac "mac" or at leat part of the mac in dot notation "xx:xx:xx:xx:xx:xx"
