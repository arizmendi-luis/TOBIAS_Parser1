import PySimpleGUI as sg 
import webbrowser 

#components/ functions/ global variables  
from globally import version  
from txtParse import csvParser 
from plot import analyze

"""
   The Window class serves to be the ui for the application
   It will take in a .txt file which will be parsed 
   It also give sthe option for a readmefile/documentaion
   file to be opned in case of user confusion 
   and a cancelation feature via a cancel button
"""
class Window:
    """This starts the GUI and uses selenium to import orders
    """
    def setUpGui() -> sg.Window:
        """setUpGui creates window for 
            user to begin  aka is ui
        Returns:
            sg.Window: ui for the beginning  
        """ 

        sg.theme('DarkRed2') #Theme can be changed (Favorite Themes: 'DarkBlue13', 'DefaultNoMoreNagging' )
        #TODO make astetically pleasing and adding finsih window 
        """ 
        Summary: The Layout of the primary window for the GUI
        Returns:
            layout for window
        """
        layout = [ 
            [sg.Push(), sg.Text('Welcome to TOBIAS Parser'), sg.Push()], 
            [sg.Push(), sg.Text('Please Import your .txt File'), sg.Push()], 
            [sg.Push(), sg.Text('', key="-InvalidCSV-", text_color="red"), sg.Push()], 
            [sg.Push(), sg.Input(enable_events=True, size=(18, 1)), 
            sg.FileBrowse(key="-File-"), sg.Push()], 
            [sg.Push(), sg.Button('Ok'), sg.Button('Cancel')],   
            [sg.Button('Need Help?'), sg.Push(), sg.Push()], 
            [sg.Text('version ' + version), sg.Push()], 
        ] 

        window = sg.Window('TOBIAS Data Analyzer', layout, size=(500,230), resizable=True) 
        return window  

    window = setUpGui() 

    while True:  
        event, values = window.read() 

        csvInput = values["-File-"] 

        if event == 'Ok': #if user clicks Ok button 
            
            #TODO add conditions when ok, aka rerouting to macro path, checking 
            # if login is ok and csv has been chosen, if not then red text should appear 
            # to signify to user that an error has occured  
            dataDict = csvParser.readCSV(csvInput) 
            charts = analyze.plotter(dataDict)   
            
        if event == 'Need Help?': 
            path = "TOBIAS README.pdf" 
            webbrowser.open_new(path)
        
        if event in (sg.WIN_CLOSED, 'Cancel'):  # if user closes window or clicks cancel
                break  
            
    window.close()



