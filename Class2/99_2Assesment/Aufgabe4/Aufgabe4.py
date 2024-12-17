import threading

# Zwei Locks erstellen
lock1 = threading.Lock()
lock2 = threading.Lock()


def process1():
    lock1.acquire()
    print("Prozess 1 hat Lock 1 erhalten")
    # Hier kann Code ausgeführt werden
    lock2.acquire()
    print("Prozess 1 hat Lock 2 erhalten")
    # Hier kann weiterer Code ausgeführt werden
    lock1.release()
    lock2.release()


def process2():
    lock1.acquire()
    print("Prozess 2 hat Lock 2 erhalten")
    # Hier kann Code ausgeführt werden
    lock2.acquire()
    print("Prozess 2 hat Lock 1 erhalten")
    # Hier kann weiterer Code ausgeführt werden
    lock1.release()
    lock2.release()


# Zwei Threads erstellen und starten
thread1 = threading.Thread(target=process1)
thread2 = threading.Thread(target=process2)
thread1.start()
thread2.start()
# Auf die Threads warten
thread1.join()
thread2.join()
print("Programm beendet")
