import requests
import json

class RunMain:

	def send_get(self,url,data):
		res = requests.get(url=url,data=data).json()
		return res
		
	def send_post(self,url,data):
		res = requests.post(url=url,data=data).json()
		return res

	def run_main(self,url,method,data=None):
		res = None
		if method == 'GET':
			res = self.send_get(url,data)
		else:
			res = self.send_post(url,data)
		return res

if __name__ == '__main__':
	url = 'http://127.0.0.1:8000/api/get_event_list/'
	data = {
		'eid':'1'
	}
	r1 = RunMain().run_main(url,'GET',data)
	r2 = RunMain().send_get(url,data)
	r3 = requests.get(url,data).json()
	print(r2)

