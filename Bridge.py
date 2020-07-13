import requests
import json
from Light import Light

class Bridge:
	ip = ''
	user = ''
	url = ''
	# There is a default unique id to every light, we're not using that.
	lights = []

	def __init__(self, ip = '192.168.1.2', user = 'jIOM2WREtiBG6eWt2bL9kBAqtdbsOy-B81LTnzHw'):
		self.ip = ip
		self.user = user
		self.url = 'http://' + ip + '/api/' + user
		self.lights = self.get_lights()

	def get_lights(self):
		lights = []
		response = requests.get(self.url + '/lights')
		if(self.success(response)):
			for num, info in response.json().items():
				state = info['state']
				light = Light(num, state)
				lights.append(light)
		return lights

	# later implement error handling
	def success(self, response):
		return (response.status_code == 200)

	def get_state(self, light):
		response = requests.get(self.url + '/lights/' + str(light.light_id))
		if (self.success(response)):
			return response.json()['state']

	def set_state(self, light, new_state):
		response = requests.put(self.url + '/lights/' + str(light.light_id) + '/state', data=json.dumps(new_state))
		if (self.success(response)):
			light.update(new_state)
			# print(light.to_dict())

	def set(self, lights, new_state):
		if (lights == None): #if nothing passed in assume all.
			for light in self.lights:
				self.set_state(light, new_state)
		else:
			for light in lights:
				self.set_state(light, new_state)

	def update_lights(self):
		for light in self.lights:
			light.update()

	def print_lights(self):
		for light in self.lights:
			print(light.to_dict())

	def set_on(self, on, lights = None):
		new_state = {'on': on}
		self.set(lights, new_state)

	def set_brightness(self, bri, lights = None):
		new_state = {'bri': bri}
		self.set(lights, new_state)

	def set_hue(self, hue, lights = None):
		new_state = {'hue': hue}
		self.set(lights, new_state)

	def set_saturation(self, sat, lights = None):
		new_state = {'sat': sat}
		self.set(lights, new_state)
	# def purp_state(self):
	# 	return {'on': True, 'hue': 47433}
