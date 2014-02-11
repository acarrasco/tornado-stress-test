import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.httpclient

import math
import random
import json
import time

class MainHandler(tornado.web.RequestHandler):
    
    count
    def somecomp(self, data):
        return [x**3 for x in data]
    
    @tornado.gen.engine
    @tornado.web.asynchronous
    def get(self):
        start = time.time() 
        client = tornado.httpclient.AsyncHTTPClient()
        res = yield tornado.gen.Task(client.fetch, 'http://localhost:8888')
        MainHandler.count += 1
        print time.time()-start, MainHandler.count
        self.finish(json.dumps(self.somecomp(json.loads(res.body))))

application = tornado.web.Application([
    (r"/", MainHandler),
], {'debug':True})

if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
