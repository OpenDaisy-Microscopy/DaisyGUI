import time

from picamera import PiCamera
from picamera.array import PiRGBArray

class Camera(PiCamera):
	
	def __init__(self):
		super(Camera, self).__init__()
		
		# set default resolution
		self.resolution = (1640, 1232)
		
		# set default save directory
		self.savedir = '/home/pi/ScopeControl/'
		
	def capture(self):
		# get time/date signature
		#~ current_time = time.strftime("%Y%m%d_time%H%Ms%S")
		#~ file_name = self.savedir + "Im_"+current_time+".jpg"
		file_name = self.savedir + "Im.jpg"
		
		# use parent method to capture
		super(Camera, self).capture(file_name, format="jpeg", use_video_port=False)
