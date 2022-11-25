import matplotlib.pyplot as plt
import numpy as np


class ShowData:
    def __init__(self, file_path):
        file = open(file_path, 'r')

        MasN=list(map(int,file.readline().split())) 
        Hz=list(map(int,file.readline().split())) 
        Hy=list(map(int,file.readline().split())) 
        rho = np.empty((len(Hy),len(Hz)), dtype=float) 
        print(MasN)
        for i in range(len(Hz)): 
            rho[i]=list(map(int,file.readline().split())) 
        
        Listx=[] 
        Listy=[] 
        for i in range (len(Hy)): 
            Listx.append(np.sum(Hy[:i])/1000) 
        for i in range (len(Hz)): 
            Listy.append(np.sum(Hz[:i])/1000) 
        
        fig, axs= plt.subplots(1, figsize=(5,5), constrained_layout=True) 
        
        
        positiony=np.arange(len(Listx)) 
        positionz=np.arange(len(Listy)) 
        axs.set_xticks(positiony) 
        axs.set_yticks(positionz) 
        axs.set_xticklabels(Listx) 
        axs.set_yticklabels(Listy) 
        axs.set_xlim([0, positiony[-1]]) 
        axs.set_ylim([positionz[-1], 0]) 
        p2 = axs.imshow(rho, cmap='jet' , aspect='auto', interpolation='bilinear', origin="upper") #cmap='jet'   cmap='RdBu'
        fig.colorbar(p2, ax=axs) 
        
        plt.show()

if __name__ == "__main__":
    ShowData("test_data/x.txt")
