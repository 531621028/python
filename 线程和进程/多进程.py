import os
print('Process (%s) start...' % os.getppid())
from multiprocessing import Process
def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
	 print('Parent process %s.' % os.getpid())
	 p = Process(target=run_proc,args=('test',))
	 print('Child process will start.')
	 p.start()
	 p.join()
	 print('Child process end.')

#对Pool对象调用join()方法会等待所有子进程执行完毕，
#调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
from multiprocessing import Pool
import time,random
def long_time_task(name):
	 print('Run task %s (%s)...' % (name, os.getpid()))
	 start = time.time()
	 time.sleep(random.random() * 3)
	 end = time.time()
	 print('Task %s runs %0.2f seconds.' % (name,(end - start)))

if __name__ == '__main__':
	print('Parent process %s.' % os.getppid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')
#很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
#subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
#import subprocess
#print('$ nslookup www.python.org')
#r = subprocess.call(['nslookup', 'www.python.org'])
#print(r)
#print('Exit code:', r)
from multiprocessing import Process,Queue
import os,time,random
# 写数据进程执行的代码:
def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue' % value)
		q.put(value)
		time.sleep(random.random())
# 读数据进程执行的代码:
def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue' % value)

if __name__ == '__main__':
	# 父进程创建Queue，并传给各个子进程：
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	# 启动子进程pw，写入:
	pw.start()
	# 启动子进程pr，读取:
	pr.start()
	# 等待pw结束:
	pw.join()
	# pr进程里是死循环，无法等待其结束，只能强行终止:
	pr.terminate()