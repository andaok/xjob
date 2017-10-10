from multiprocessing import Process
import os

def f(mip):
    print('function f')
    print 'hello', mip
    import salt.client
    local = salt.client.LocalClient()
    local.cmd('*', 'cmd.run', ['ip a'])
if __name__ == '__main__':
    print('main line')
    p = Process(target=f, args=('10.58.11.231',))
    p.start()
    p.join(5)





