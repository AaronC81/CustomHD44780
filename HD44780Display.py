import time

class HD44780Display:
	def __init__(self, write_pin_fn, pin_mode_fn, rs, en, d4, d5, d6, d7, light):
		self.write_pin = write_pin_fn
		self.pin_mode = pin_mode_fn
		self.rs = rs
		self.en = en
		self.d4 = d4
		self.d5 = d5
		self.d6 = d6
		self.d7 = d7
		self.light = light
		
		self.pin_mode(rs, 1)
		self.pin_mode(en, 1)
		self.pin_mode(d4, 1)
		self.pin_mode(d5, 1)
		self.pin_mode(d6, 1)
		self.pin_mode(d7, 1)
		self.pin_mode(light, 1)
		
		self.delay = 0.0005
		
	def begin(self):
		# Perform initialization sequence
		self._write_bits(0x3)
		self._write_bits(0x3)
		self._write_bits(0x3)
		self._write_bits(0x2)
		self._write_bits(0x0)
		self._write_bits(0x6)
		self._write_bits(0x0)
		self._write_bits(0xC)
		self._write_bits(0x2)
		self._write_bits(0x8)
		self._write_bits(0x0)
		self._write_bits(0x1)
		
	def backlight(self, mode):
		self.write_pin(self.light, mode)
		
	def write(self, msg):
		for char in msg:
			char_code = ord(char)
			top_half = (char_code & 0xF0) >> 4
			bottom_half = char_code & 0x0F
			self._write_bits(top_half, 1)
			self._write_bits(bottom_half, 1)
			
	def clear(self):
		self._write_bits(0x0)
		self._write_bits(0x1)
		
	def set_line(self, line):
		if line == 1:
			self._write_bits(0x8)
			self._write_bits(0x0)
		elif line == 2:
			self._write_bits(0xC)
			self._write_bits(0x0)
		else:
			raise Exception("Invalid line")
		
	def _toggle_enable(self):
		time.sleep(self.delay)
		self.write_pin(self.en, 1)
		time.sleep(self.delay)
		self.write_pin(self.en, 0)
		time.sleep(self.delay)
		
	def _write_bits(self, bits, mode=0):
		# Split integer into bits
		print(bits)
		d7, d6, d5, d4 = map(int, "{0:04b}".format(bits))
		
		self.write_pin(self.rs, mode)
		
		time.sleep(self.delay)
		
		self.write_pin(self.d4, d4)
		self.write_pin(self.d5, d5)
		self.write_pin(self.d6, d6)
		self.write_pin(self.d7, d7)
		
		print [d4, d5, d6, d7]
		
		self._toggle_enable()