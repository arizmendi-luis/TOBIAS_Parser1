import matplotlib.pyplot as plt

class analyze: 
    """ 
        #plotter uses matplotlib to plot   
    """    
    #TODO document
    def plotter(dataDic): 
        f1 = plt.figure(1)  
        x = dataDic['time']   
        y = dataDic['Acc_X']  
        y2 = dataDic['Acc_Y'] 
        y3 = dataDic['Acc_z']

        plt.plot(x, y, color='green', label = 'x-axis', linewidth=1, markersize=10)  
        plt.plot(x, y2, color='red', label = 'y-axis', linewidth=1, markersize=10) 
        plt.plot(x, y3, color='blue', label = 'z-axis', linewidth=1, markersize=10) 
        plt.title("Acceleration over time") 
        plt.xlabel('Time (MS)') 
        plt.ylabel('Acceleration (m/s^2)') 
        plt.legend(loc="upper left") 
   
        y = dataDic['Gyro_X']  
        y2 = dataDic['Gyro_Y'] 
        y3 = dataDic['Gyro_Z'] 

        f2 = plt.figure(2)
        plt.plot(x, y, color='green', label = 'x-axis', linewidth=1, markersize=5)  
        plt.plot(x, y2, color='red', label = 'y-axis', linewidth=1, markersize=5) 
        plt.plot(x, y3, color='blue', label = 'z-axis', linewidth=1, markersize=5) 
        plt.title("Gyroscope Data") 
        plt.xlabel('Time (MS)') 
        plt.ylabel('gyro (radians/s') 
        plt.legend(loc="upper left")
        plt.show()        

        result = 'finished' 
        return result 