import requests
import json

class Light:
	light_id = '0'
	on = False
	brightness = 0
	hue = 0
	saturation = 0

	def __init__(self, light_id, state = None):
		self.light_id = light_id
		self.update(state)

	def update(self, state = None):
		if(state == None): #Then we refresh
			state = get_state(self.light_id)
		else:
			if 'on' in state.keys():
				self.on = state['on']
			if 'bri' in state.keys():
				self.brightness = state['bri']
			if 'hue' in state.keys():
				self.hue = state['hue']
			if 'sat' in state.keys():
				self.saturation = state['sat']

	def to_dict(self):
		return {'Light #': self.light_id, 'is on': self.on, 'bri': self.brightness, 'hue': self.hue, 'sat': self.saturation }
