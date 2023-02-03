import torch
import time

cpu_sum_t,gpu_sum_t,cpu_mul_t,gpu_mul_t, x= [],[],[],[],[]
TEST = 100

for i in range (TEST):
    x.append(i)
for i in range (TEST):
    t1 = torch.rand(4096,4096)
    t2 = torch.rand(4096,4096)
    start_time = time.time()
    t1.add(t2)
    cpu_sum_t.append((time.time() - start_time))
    if torch.cuda.is_available():
        t1 = t1.cuda()
        t2 = t2.cuda()
        start_time = time.time()
        t1.add(t2)
        gpu_sum_t.append((time.time() - start_time))
print(cpu_sum_t)
print(gpu_sum_t)

for i in range (TEST):
    t1 = torch.rand(4096,4096)
    t2 = torch.rand(4096,4096)
    start_time = time.time()
    cpu_t3 = t1.mm(t2.t())
    cpu_mul_t.append((time.time() - start_time))
    if torch.cuda.is_available():
        t1 = t1.cuda()
        t2 = t2.cuda()
        start_time = time.time()
        gpu_t3 = t1.mm(t2.t())
        gpu_mul_t.append((time.time() - start_time))
print(cpu_mul_t)
print(gpu_mul_t)

import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
axs[0].scatter(x,cpu_sum_t)
axs[0].scatter(x,gpu_sum_t)
axs[1].scatter(x,cpu_mul_t)
axs[1].scatter(x,gpu_mul_t)