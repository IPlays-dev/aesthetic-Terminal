def terminal(times=100,speed=0.3):
	import time
	import random
	files = "[0x7ffd3a2b1c08] SEGFAULT @ 0xdeadbeef | core dumped → /var/crash/proc_4471.core | err "
	files_2 = "kvmd-nginx: [warn] 1024 worker_connections exceed open file limit: 768 | epoll_wait() "
	files_3 = "EXT4-fs error (device sda3): ext4_find_entry:1455: inode #2: comm kworker/u8:2: reading directory lblock 0 | JBD2: recovery failed | remounting filesystem read-only | I/O error, dev sda, sector 488396799"
	files_4 = "[drm:amdgpu_dm_atomic_commit_tail [amdgpu]] *ERROR* Waiting for fences timed out! | dmesg: GPU hang detected | ring gfx timeout | GPU reset begin | VRAM lost | resubmitting IB failed (-108) "
	files_5 = "python3.11: /lib/x86_64-linux-gnu/libc.so.6: version GLIBC_2.38 not found | Aborted (core dumped) | Fatal Python error: _Py_HashRandomization_Init: failed to get random numbers to initialize Python | SystemError: <built-in function exit> returned a result with an error set "
	files_6 = "pacakge succesfully compiled code:49 "
	files_7 = "https://youtube.com/@iplays_bs"
	box = [files,files_2,files_3,files_4,files_5,files_6,files_7]
	for i in range(times):
		output = random.choice(box)
		time.sleep(speed)
		print(f"Packet installed.iso no: {i}")
		print(output)
		
# if you want to Run this program just type this --> terminal()
# you can set how many times you wanna run this like this --> terminal(24)
# you can set how fast the terminal moves like this --> terminal(24,0.6)
    # to set your own speed the you must also input "times" -->(24,0.6)
#                  <<<<< developed by IPLays>>>>>>
