import mido
from Bridge import Bridge
from Synth import Moog
from itertools import permutations
import random

bridge = Bridge()
lights = bridge.lights
moog = Moog()
#Temp. Disgusting I KNOW.
lights = bridge.lights

# lightz = list(set().union(permutations(lights, 1),permutations(lights, 2),permutations(lights, 3), permutations(lights, 4)))

bridge.set_saturation(254)
bridge.set_brightness(0)
with mido.open_input() as inport:
	for message in inport:
		if (message.type == 'note_on'):
			moog.add_note(message)
			# current_hue = bridge.get_state(lights[1])['hue']
			# print(current_hue + (moog.get_note_difference() * 200))
			# bridge.set_hue(current_hue + (moog.get_note_difference() * 20))
			bridge.set_on(True)
		elif (message.type == 'note_off'):
			moog.remove_note(message)
			if(moog.empty_notes()):
				bridge.set_on(False)
		elif (moog.cutoff(message)):
				bridge.set_hue(message.value * 500)
				moog.set_cutoff(message.value)
		elif (moog.pitchwheel(message)):
				bridge.set_brightness(int((message.pitch + 8191) * 0.016))
				moog.set_pitchwheel(message.pitch)

#jIOM2WREtiBG6eWt2bL9kBAqtdbsOy-B81LTnzHw


# What controls what??


# Velocity -- brightness?
#

# Knobs with power:
# Cutoff. Higher more red, lower more blue.
