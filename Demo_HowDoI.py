import PySimpleGUI as sg
import subprocess
import howdoi

# Test this command in a dos window if you are having trouble.
HOW_DO_I_COMMAND =  'python -m howdoi.howdoi -n 2'

# if you want an icon on your taskbar for this gui, then change this line of code to point to the ICO file
DEFAULT_ICON = 'E:\\TheRealMyDocs\\Icons\\QuestionMark.ico'

def HowDoI():
    '''
    Make and show a window (PySimpleGUI form) that takes user input and sends to the HowDoI web oracle
    Excellent example of 2 GUI concepts
        1. Output Element that will show text in a scrolled window
        2. Non-Window-Closing Buttons - These buttons will cause the form to return with the form's values, but doesn't close the form
    :return: never returns
    '''
    # -------  Make a new FlexForm  ------- #
    # Set system-wide options that will affect all future forms.  Give our form a spiffy look and feel
    sg.SetOptions(background_color='#9FB8AD', text_element_background_color='#9FB8AD', element_background_color='#9FB8AD', scrollbar_color=None, input_elements_background_color='#F7F3EC', button_color=('white', '#475841'))
    form = sg.FlexForm('How Do I ??', auto_size_text=True, default_element_size=(30, 2), icon=DEFAULT_ICON)
    layout =  [
                [sg.Text('Ask and your answer will appear here....', size=(40, 1))],
                [sg.Output(size=(88, 20))],
                [ sg.Spin(values=(1, 2, 3, 4), initial_value=1, size=(2, 1), key='Num Answers'), sg.T('Num Answers'), sg.Checkbox('Display Full Text', key='full text')],
                [sg.Multiline(size=(85, 5), enter_submits=True, key='query'),
                sg.ReadFormButton('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
                sg.SimpleButton('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]
              ]
    form.Layout(layout)
    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    while True:
        (button, value) = form.Read()

        if button == 'SEND':
            QueryHowDoI(value['query'], value['Num Answers'], value['full text'])      # send string without carriage return on end
        else:
            break           # exit button clicked

    exit(69)

def QueryHowDoI(Query, num_answers, full_text):
    '''
    Kicks off a subprocess to send the 'Query' to HowDoI
    Prints the result, which in this program will route to a gooeyGUI window
    :param Query: text english question to ask the HowDoI web engine
    :return: nothing
    '''
    howdoi_command = HOW_DO_I_COMMAND
    full_text_option = ' -a' if full_text else ''
    t = subprocess.Popen(howdoi_command + ' '+ Query + ' -n ' + str(num_answers)+full_text_option, stdout=subprocess.PIPE)
    (output, err) = t.communicate()
    print('You asked: '+ Query)
    print('_______________________________________')
    print(output.decode("utf-8") )
    exit_code = t.wait()

if __name__ == '__main__':
    HowDoI()

