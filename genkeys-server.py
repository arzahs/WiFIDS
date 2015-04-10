#!/usr/bin/python
###########################################################
#WiFIDS - genkeys-server.py							      #
#Key Generation for WiFiDS                                #
#Roger Baker, Houston Hunt, Prashant Kumar, Garrett Miller#
#Some Crypto Functions inspired by:                       #
#https://launchkey.com/docs/api/encryption                #
###########################################################

from Crypto.PublicKey import RSA 

#Generates RSA Keys
def generate_RSA(bits=2048):

	new_key = RSA.generate(bits, e=65537) 
	f = open('server-public.key','w')
	f.write(new_key.publickey().exportKey("PEM"))
	f.close()
	
	f = open('server-private.key','w')
	f.write(new_key.exportKey("PEM"))
	f.close()
	
generate_RSA()