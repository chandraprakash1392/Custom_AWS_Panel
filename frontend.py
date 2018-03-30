#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import os
#from http.server import BaseHTTPRequestHandler, HTTPServer
#import socketserver


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html;charset=utf-8')
        self.send_header('access-control-allow-origin', '*')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        env=''
        if self.path == '/eu-central-1':
           env = 'eu-central-1'
        if self.path == '/eu-west-1':
           env = 'eu-west-1'
        if self.path == '/ap-south-1':
           env = 'ap-south-1'
        json = os.popen("/opt/aws_panel/backend.py %s" %env).read()
        html ='<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Excel To HTML using codebeautify.org</title></head><body><!DOCTYPE html><html><head><meta charset="UTF-8"><title>Excel To HTML using codebeautify.org</title></head><body><!DOCTYPE html><html><head><title>AWS Instance Status</title><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous"><script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular.min.js"></script><style type="text/css"> .border-bottom{border-bottom: 1px solid #e5e5e5;}.box-shadow{box-shadow: 0 .25rem .75rem rgba(0, 0, 0, .05);}.text-dark.active, .text-dark.active:hover{cursor: pointer; color: #007bff !important;}</style></head><body><main ng-app="myapp" ng-controller="InstanceCtrl"><div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom box-shadow"><h5 class="my-0 mr-md-auto font-weight-normal">AWS Instance Status</h5><nav class="my-2 my-md-0 mr-md-3"><a class="p-2 text-dark" ng-class="{\'active\':selected==\'/eu-central-1\'}" href="/eu-central-1">Production</a><a class="p-2 text-dark" ng-class="{\'active\':selected==\'/eu-west-1\'}" href="/eu-west-1">Acceptance</a><a class="p-2 text-dark" ng-class="{\'active\':selected==\'/ap-south-1\'}" href="/ap-south-1">Development</a></nav></div><div class="container"><div class="row"><div class="col-md-6"><input type="search" class="form-control ds-input" placeholder="Search..." ng-model="searchString"></div></div><br/><table class="table table-striped" id="result"><thead><tr><th>Id</th><th>Name</th><th>State</th><th>Public IP</th><th>Private IP</th></tr></thead><tbody><tr ng-repeat="instance in instances | filter:searchString"><td>{{instance.instance_id}}</td><td>{{instance.instance_name}}</td><td>{{instance.instance_state}}</td><td>{{instance.instance_public_ip}}</td><td>{{instance.instance_private_ip}}</td><td>{{instance.instance_vpc_id}}</td><td>{{instance.instance_volumes}}</td><td>{{instance.instance_key_name}}</td><td>{{instance.instance_type}}</td></tr></tbody></table></div></main><script type="text/javascript">var myapp=angular.module(\'myapp\', []);myapp.controller(\'InstanceCtrl\', function($scope, $http){$scope.instances='+json+'; $scope.selected=window.location.pathname;});</script></body></html>'

#        self.wfile.write(os.sys(aws_panel/backend.py %s) %env)
        self.wfile.write(html)

#    def do_HEAD(self):
#        self._set_headers()
#
#    def do_POST(self):
#        # Doesn't do anything with posted data
#        self._set_headers()
#        self.wfile.write("<html><body><h1>POST!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=S, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

