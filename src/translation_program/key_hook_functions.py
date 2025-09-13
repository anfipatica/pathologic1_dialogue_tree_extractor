from pynput import keyboard

NOT_ACTIVATED=0
CTRL_LEFT=-1
CTRL_RIGHT=1

hotkey_activated: int = NOT_ACTIVATED
ctrl_pressed: bool = False


def	ft_on_press(key: keyboard.Key):
	global ctrl_pressed
	global hotkey_activated
	if key == keyboard.Key.ctrl:
		ctrl_pressed = True
	elif (ctrl_pressed == True):
		if key == keyboard.Key.left:
			hotkey_activated = CTRL_LEFT
			keyboard_ = keyboard.Controller()
			keyboard_.type("\n")
		if key == keyboard.Key.right:
			hotkey_activated = CTRL_RIGHT
			keyboard_ = keyboard.Controller()
			keyboard_.type("\n")



def	ft_on_release(key: keyboard.Key):
	global ctrl_pressed
	global hotkey_activated
	if (key == keyboard.Key.ctrl):
		ctrl_pressed = False
		hotkey_activated = NOT_ACTIVATED
	elif ((key == keyboard.Key.left or key == keyboard.Key.right) and hotkey_activated != NOT_ACTIVATED):
		hotkey_activated = NOT_ACTIVATED
