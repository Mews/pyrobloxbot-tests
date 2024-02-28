import keyboard as kb
import multiprocessing as mp
import os, time, signal

conn = mp.Queue()

def listen(queue:mp.Queue):
    while True:
        if kb.is_pressed("ctrl+m"):
            main_process_pid = queue.get()
            os.kill(main_process_pid, signal.SIGTERM)

if __name__ == "__main__":
    main_process = mp.current_process()

    mp.Process(target=listen, args=(conn,), daemon=True).start()
    conn.put(os.getpid())

    while True:
        print("Main process running", time.perf_counter())
        time.sleep(1)