#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
import threading 
import time

class WebSocket_Server:
    def __init__(self):
        self.updates_info = 'None'
        self.threading_controller()

    async def sokcet_worker(self,websocket, path):
        print ('time..')
        while True:
            print (self.updates_info,' is sand!')
            await websocket.send(self.updates_info)
            await asyncio.sleep(random.random() * 3)
    
    def update(self):
        # add your updated output here
        print ('info is updated')
        while True:
            self.updates_info = datetime.datetime.utcnow().isoformat() + 'Z'
            print ('current_info:',self.updates_info)
            time.sleep(1)

    def websocket_excute(self):
        print ('server is started')
        # ------ use async and threading ------- #
        host = '127.0.0.1'
        port = 5678
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        start_server = websockets.serve(self.sokcet_worker, host, port) # python 3.6: no reuse_port
        loop.run_until_complete(start_server)
        loop.run_forever()


    def threading_controller(self):
        socket_thread = threading.Thread(target=self.websocket_excute,args=())
        socket_thread.start()
        update_thread = threading.Thread(target=self.update,args=())
        update_thread.start()
        
        update_thread.join()
        socket_thread.join()

if __name__=='__main__':
    socket_test = WebSocket_Server()

