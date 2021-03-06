import PySimpleGUI as sg

# Robotics design pattern
# Uses Realtime Buttons to simulate the controls for a robot
# Rather than sending a single click when a button is clicked, Realtime Buttons
#       send button presses continuously while the button is pressed down.
# Two examples, one using fancy graphics, one plain.

def RemoteControlExample():
    # Make a form, but don't use context manager
    back ='#eeeeee'
    image_forward = 'ButtonGraphics/RobotForward.png'
    image_backward = 'ButtonGraphics/RobotBack.png'
    image_left = 'ButtonGraphics/RobotLeft.png'
    image_right = 'ButtonGraphics/RobotRight.png'
    sg.SetOptions(border_width=0, button_color=('black', back), background_color=back, element_background_color=back, text_element_background_color=back)
    form = sg.FlexForm('Robotics Remote Control', auto_size_text=True)
    status_display_elem = sg.T('', justification='center', size=(19,1))
    form_rows = [[sg.Text('Robotics Remote Control')],
                 [status_display_elem],
                 [sg.T(' '*10), sg.RealtimeButton('Forward', image_filename=image_forward)],
                 [ sg.RealtimeButton('Left', image_filename=image_left), sg.T('     '), sg.RealtimeButton('Right', image_filename=image_right)],
                 [sg.T(' '*10), sg.RealtimeButton('Reverse', image_filename=image_backward)],
                 [sg.T('')],
                 [sg.Quit(button_color=('black', 'orange'))]
                 ]

    form.LayoutAndRead(form_rows, non_blocking=True)

    #
    # Some place later in your code...
    # You need to perform a ReadNonBlocking on your form every now and then or
    # else it won't refresh.
    #
    # your program's main loop
    while (True):
        # This is the code that reads and updates your window
        button, values = form.ReadNonBlocking()
        if button is not None:
            status_display_elem.Update(button)
        else:
            status_display_elem.Update('')
        # if user clicked quit button OR closed the form using the X, then break out of loop
        if button == 'Quit' or values is None:
            break

    form.CloseNonBlockingForm()


def RemoteControlExample_NoGraphics():
    # Make a form, but don't use context manager
    form = sg.FlexForm('Robotics Remote Control', auto_size_text=True)
    status_display_elem = sg.T('', justification='center', size=(19,1))
    form_rows = [[sg.Text('Robotics Remote Control')],
                 [status_display_elem],
                 [sg.T(' '*10), sg.RealtimeButton('Forward')],
                 [ sg.RealtimeButton('Left'), sg.T('                '), sg.RealtimeButton('Right')],
                 [sg.T(' '*10), sg.RealtimeButton('Reverse')],
                 [sg.T('')],
                 [sg.Quit(button_color=('black', 'orange'))]
                 ]
    # Display form to user
    form.LayoutAndRead(form_rows, non_blocking=True)

    #
    # Some place later in your code...
    # You need to perform a ReadNonBlocking on your form every now and then or
    # else it won't refresh.
    #
    # your program's main loop
    while (True):
        # This is the code that reads and updates your window
        button, values = form.ReadNonBlocking()
        if button is not None:
            status_display_elem.Update(button)
        else:
            status_display_elem.Update('')
        # if user clicked quit button OR closed the form using the X, then break out of loop
        if button == 'Quit' or values is None:
            break

    form.CloseNonBlockingForm()




# ------------------------------------- main -------------------------------------
def main():
    RemoteControlExample_NoGraphics()
    # Uncomment to get the fancy graphics version.  Be sure and download the button images!
    RemoteControlExample()
    sg.MsgBox('End of non-blocking demonstration')

if __name__ == '__main__':

    main()
