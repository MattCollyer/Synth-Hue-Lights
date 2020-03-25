import mido
from Bridge import Bridge

bridge = Bridge()
lights = bridge.lights

cutoff_position = 0
pitchwheel_position = 0
bridge.set_saturation(254)
bridge.set_brightness(0)
note_stack = []
with mido.open_input() as inport:
	for message in inport:
		print(message)
		if (message.type == 'note_on'):
			bridge.set_on(True)
			note_stack.append(message)
		elif (message.type == 'note_off'):
			note_stack.pop()
			if(not note_stack):
				bridge.set_on(False)
		elif (message.type == 'control_change' and message.control == 19): #if cuttoff knob
			difference = message.value - cutoff_position
			if (abs(difference) > 20):
				bridge.set_hue(message.value * 500)  #for NOW!TEMPorary
				cutoff_position = message.value
		elif (message.type == 'pitchwheel'):
			difference = message.pitch - pitchwheel_position
			if (abs(difference) > 1000):
				bridge.set_brightness(int((message.pitch + 8191) * 0.016))
				pitchwheel_position = message.pitch
#jIOM2WREtiBG6eWt2bL9kBAqtdbsOy-B81LTnzHw


# What controls what??


# Velocity -- brightness?
#

# Knobs with power:
# Cutoff. Higher more red, lower more blue.
