#! /usr/local/bin/stackless2.6

import cherrypy

class HelloWorld(object):
  def index(self, name='World'):
    return f'Hello, <b>{name}</b>!'
  index.exposed = True

if __name__ == "__main__":
  cherrypy.quickstart(HelloWorld())
