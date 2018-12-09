#This is a video generator for low amplitude flash signals.

import numpy as np
import os 

os.chdir('./sample')

for i in range(0,999):    
    np.random.seed()
    
    #black image
    blank = np.zeros((1000, 1000))
    
    #20 targets per image
    targets = np.zeros((20,2))
    
    
    for x in range(0,19):
        
        #create truths
        targets[x][0]=np.random.randint(3,997)
        targets[x][1]=np.random.randint(3,997)
        
        #apply truthes and a ring around them to the blank image
        blank[int(targets[x][0]),int(targets[x][1])]     = 2 
    
        blank[int(targets[x][0])-1,int(targets[x][1])]   = 1
        blank[int(targets[x][0])-1,int(targets[x][1]+1)] = 1 
        blank[int(targets[x][0])-1,int(targets[x][1]-1)] = 1 
        blank[int(targets[x][0]),int(targets[x][1]-1)]   = 1 
        blank[int(targets[x][0]),int(targets[x][1]+1)]   = 1 
        blank[int(targets[x][0])+1,int(targets[x][1])]   = 1
        blank[int(targets[x][0])+1,int(targets[x][1]+1)] = 1 
        blank[int(targets[x][0])+1,int(targets[x][1]-1)] = 1 
    
    #apply gaussian noise, not limited to a normal grayscale range
    noise = np.random.normal(128,30,(1000,1000))
    
    complete = blank+noise
    
    #save the sample images and truths
    np.save('s_'+str(i),complete)
    np.save('t_'+str(i),targets)
