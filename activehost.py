# -*- coding: utf-8 -*-
import os
import subprocess

DONT_OUTPUT = open(os.devnull, "w")

def ping(ip):
	response = subprocess.call(["ping", "-c", "2", ip], stdout=DONT_OUTPUT, stderr=subprocess.STDOUT)
	if response == 0:
		print "La maquina esta respondiendo"
	else:
		print "La maquina no esta respondiendo"

while True:
	print "Ingrese un IP or exit para salir"
	ip = raw_input("> ")

	if ip == 'exit':
		break

	ping(ip)
	continue

