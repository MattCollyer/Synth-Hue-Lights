class Moog:
	pitchwheel_position = 0
	cutoff_position = 0
	notes = []
	last_note = 0

	def __init__(self, cutoff = 0, pitchwheel = 0):
		self.cutoff_position = cutoff
		self.pitchwheel_position = pitchwheel
		self.notes = []
		self.last_note = 0
	def set_pitchwheel(self, pitchwheel):
		self.pitchwheel_position = pitchwheel

	def set_cutoff(self, cutoff):
		self.cutoff_position = cutoff

	def add_note(self, note_message):
		self.notes.append(note_message)

	def remove_note(self, off_note):
		#Save the last note played so we can mess with it later
		if(len(self.notes) == 1):
			self.last_note = self.notes[0].note
			self.notes.pop()
		else:
			to_delete = None
			for note_msg in self.notes:
				if (note_msg.note == off_note.note):
					to_delete = note_msg
			self.notes.remove(to_delete)

	def empty_notes(self):
		return not self.notes

	def cutoff(self, message):
		is_cutoff_knob = (message.type == 'control_change' and message.control == 19)
		return  is_cutoff_knob and self.threshold(message.value, self.cutoff_position, 20)

	def pitchwheel(self, message):
		is_pitchwheel = (message.type == 'pitchwheel')
		return is_pitchwheel and self.threshold(message.pitch, self.pitchwheel_position, 1500)

	def threshold(self, value, prev, threshold):
		return (abs(value - prev) > threshold)

	def get_note_difference(self):
		newest_index = len(self.notes) - 1
		if(newest_index > 1):
			return self.notes[newest_index].note - self.notes[newest_index - 1].note
		elif(self.last_note != 0):
			return self.notes[newest_index].note - self.last_note
		else:
			return 0
