#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ws4py.client.threadedclient import WebSocketClient

class DummyClient(WebSocketClient):
    def opened(self):
        def data_provider():
            for i in range(1, 200, 25):
                yield "#" * i

        #余計なものを送ると怒られるっぽいので送らない
        #self.send(data_provider())

        #同上
        #for i in range(0, 200, 25):
          #print i
          #self.send("*" * i)

      #いらなそうなので削除
      #def closed(self, code, reason=None):
        #print "Closed down", code, reason

    def received_message(self, m):
        print m
        mess = str(m).split(" ")
        if mess[0] == "Hello,":
          name = " ".join(mess[2:])
          send_mess = "Hello, " + name
          #print send_mess
          self.send(send_mess)
        else:
          print name + "said:" + str(m)
        if len(m) == 175:
          self.close(reason='Bye bye')

if __name__ == '__main__':
    try:
        ws = DummyClient('ws://challenge-server.code-check.io/api/websocket/hello', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
