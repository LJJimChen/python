import time, threading, multiprocessing


def loop():
    print "thread %s is running" % threading.current_thread().name
    for n in range(0, 5):
        print "thread %s >>>>%s" % (threading.current_thread().name, n)
        time.sleep(1)

    print "thread %s is ended" % threading.current_thread().name


print "thread %s is running" % threading.current_thread().name
t = threading.Thread(target=loop, name="loopThread")
t.start()
t.join()
print "thread %s is ended" % threading.current_thread().name

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice', ), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob', ), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
