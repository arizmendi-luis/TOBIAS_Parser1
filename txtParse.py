from ast import Index
import pandas as pd 

class csvParser: 
    """ 
        #CSVParser parses through given data   
    """    
    #TODO decompose this function very long 
    # perhaps between parasing and actually creating 
    # a dictionary 
    def readCSV(csvInput) -> dict: 
        """
        Args: Takes in a csv in this case a txt file; and 
        parses through it documenting the different data points 
        and their values for temperatures, accelerations, 
        baramoter readings, time, ect.
            
        Returns: 
            dict: holding relevent data for each point in time  
        """     
        newDict = {}  
        num_points = 0 
        counter = 7 # number of rows per data collection point
        rawCSV = pd.read_csv(csvInput, header = None) 

        # values for the points in which data is collected for a 
        # certain amount of time 
        
        #temperatures
        temp_c = [] #temperature in degrees celcius 
        temp_f = [] #temperature in degrees farenheit 

        # barometer
        press = [] #pressure in Pa 
        alt = [] #altitude in meters 

        #acceleromter 
        acc_x = [] #aceleration in the x axis in m/s^2
        acc_y = [] #acceleration in the y axis in m/s^2
        acc_z = [] #acceleration in the z axis in m/s^2 

        #gyroscope
        gy_x = [] # gyroscope reading in x axis in radians per second 
        gy_y = [] # gyroscope reading in y axis in radians per second 
        gy_z = [] # gyroscope reading in z axis in radians per second  

        #time 
        time = [] #time in miliseconds after starting equipment 

        for row in rawCSV.iterrows():  
            #TODO add some sort of checker other than counter 
            # to make sure the right thing is being checked 
            # ie check that the row begins with words such as temperature 
            # Pressure and corresponds with a certain value of counter 
            # could be used to report errors instead of doing a whole 
            # bad output when counter and key words are used togeher to 
            # check one another   
            line = row[1][0] 
            sWord = line[0:line.find(" ")]  
            # Gather temperature 
            if (sWord == 'Temperature' or sWord == ""): 
                i = line.find('= ') 
                if (line.find('*C') != -1):  
                    j = line.find('*C')
                    temp_c += [float(line[i+2:j-1])]   
                else: 
                    j = line.find('*F') 
                    temp_f += [float(line[i+2:j-1])]  
            # Gather Pressure  
            if (sWord == 'Pressure'): 
                i = line.find('= ')  
                j = line.find('Pa')
                press += [float(line[i+2:j-1])] 
            # Gather Altitude 
            if (sWord == 'Approx'): 
                i = line.find('= ')  
                j = line.find('m')
                alt += [float(line[i+2:j-1])]  

            # Gather Acceleration 
            if (sWord == 'Accel'): 
                x = line.find('X: ') 
                y = line.find('Y: ') 
                z = line.find('Z: ') 
                j = line.find(' m/s^2') 
                acc_x += [float(line[x+3:y-2])] 
                acc_y += [float(line[y+3:z-2])]  
                acc_z += [float(line[z+3: j])] 
            # Gather Gyroscope   
            if (sWord == 'Gyro'): 
                x = line.find('X: ') 
                y = line.find('Y: ') 
                z = line.find('Z: ') 
                j = line.find(' radians/s') 
                gy_x += [float((line[x+3:y-2]))] 
                gy_y += [float((line[y+3:z-2]))]  
                gy_z += [float((line[z+3: j-1]))]  
            # gather time 
            try:
                int(sWord) 
                time += [float(line)]  
            except: 
                pass
            
        newDict = {'Temperature_F' : temp_f, 'Temperature_C': temp_c, 'Pressure_Pa': press, 'Altitude_m': alt, 
        'Acc_X' :acc_x, 'Acc_Y' : acc_y, 'Acc_z' : acc_z, 'Gyro_X' : gy_x , 'Gyro_Y' : gy_y , 'Gyro_Z': gy_z , 
        'time': time } 

        return newDict
