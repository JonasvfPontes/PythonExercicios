import numpy as np
import matplotlib.pyplot as plt

#eu estava vendo um vídeo qualquer no Youtube
#https://www.youtube.com/watch?v=kjpNLbv4wJw

x = np.arange(1, 6)
plt.style.use('ggplot')
plt.ion()
for i in range(5):
    dados = np.random.randint(20, 30, 5)
    plt.cla()
    plt.clf()
    plt.bar(x, dados)
    plt.pause(3)
plt.ioff()





