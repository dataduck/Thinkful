import logging
import csv

#Set the log output file, and the log level 
logging.basicConfig(filename="output.log", level= logging.DEBUG)

def put(name, snippet, filename):
	"""Store a snippet with an associated name in the CSV file"""
	pass
	logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
	logging.debug("Opening file")
	with open(filename, "a") as f: 
		writer = csv.writer(f)
		logging.debug("Writing snippet to file")
		writer.writerow([name, snippet])
	logging.debug("Write successful")
	return name, snippet 
