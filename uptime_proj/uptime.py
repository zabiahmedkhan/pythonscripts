#!/usr/bin/python
import subprocess
from flask import Flask

app=Flask(__name__)


@app.route('/uptime')
def uptime():
	open_pipe=subprocess.Popen("uptime", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output,err=open_pipe.communicate()
	rc=open_pipe.wait()
	return output.strip()

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True, port=11000) 
