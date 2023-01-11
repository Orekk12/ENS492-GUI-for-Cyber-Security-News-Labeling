import PySimpleGUI as sg 
from lstm_model import label_lstm

labels =  ["fraud","hacker groups","government", "corporation", "unrelated", "darknet", "cyber defense", "hacking", 
          "security concepts", "security products", "network security", "cyberwar", "geopolitical", "data breach",
          "vulnerability", "platform", "cyber attack"]

tags = []

def get_tags_news(news_text, which_model):
    if which_model == 2:
        label_list = label_lstm(news_text, labels)
        print(label_list)
        return label_list
            
    #print("news text:", news_text)
    #tags = ["fraud", "zort"]
    #return tags

def get_which_model(is_all, is_bert, is_lstm, is_cnn):
    if is_all:
        return 0
    if is_bert:
        return 1
    if is_lstm:
        return 2
    if is_cnn:
        return 3

def tags_to_string():
    str = ""
    for tag in tags:
        str += tag + ", "
    return str

def update_tag_results_gui():
    tag_results_obj.update(disabled = False)
    tag_results_obj.update(value=tags_to_string())
    tag_results_obj.update(disabled = True)
    
sg.theme('System Default 1')  # Let's set our own color theme

# STEP 1 define the layout
layout = [ 
            [sg.Text('Please select the machine learning model(s) you want to generate the tags with:')],
            [sg.Radio('BERT', "MLModelRadio", default=True, size=(10,1), k='is_bert'), sg.Radio('LSTM', "MLModelRadio", default=True, size=(10,1), k='is_lstm'),
             sg.Radio('CNN', "MLModelRadio", default=True, size=(10,1), k='is_cnn'), sg.Radio('All Models', "MLModelRadio", default=True, size=(10,1), k='is_all')],
            [sg.Text("Please enter the new's text:")],
            [sg.Multiline(size=(60,20), expand_x=True, expand_y=True, k='news_text')],
            [sg.Text("Tags:")],
            [sg.Multiline(size=(20,5), expand_x=True, expand_y=True, k='tag_results_gui', disabled = True)],
            [sg.Button('Run'), sg.Button('Exit')]
         ]

#STEP 2 - create the window
window = sg.Window('Cyber Security News Tagger', layout)

tag_results_obj = window['tag_results_gui']

# STEP3 - the event loop
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    
    if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):#print all values
        print('============ Event = ', event, ' ==============')
        print('-------- Values Dictionary (key=value) --------')
        for key in values:
            print(key, ' = ',values[key])
    if event == 'Run':
        tags = get_tags_news([values['news_text']], get_which_model(values['is_all'], values['is_bert'], values['is_lstm'], values['is_cnn']))
        #tags = ["zart", "zort"]
        
        update_tag_results_gui()
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
      break
    
window.close()
