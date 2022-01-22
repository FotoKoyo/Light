import speech_recognition as sr
import webbrowser as wb

def internet():
	r = sr.Recognizer()

	def listen():
		text =''
		with sr.Microphone() as sourse:
			print("Говорите что вы хотите найти")
			r.adjust_for_ambient_noise(sourse)
			audio = r.listen(sourse)
			try:
				text = (r.recognize_google(audio, language="ru-RU")).lower()
			except:
				pass

		print(f"Вы сказали: {text}")
		return(text)

	def exe(task):
		mas = ['лайт', 'light', 'пожалуйста', 'давай']
		keys = ('найди', 'найти', 'ищи', 'открой')
		for i in mas:
			task = task.replace(i, '')
			task = task.replace('  ', '  ')
		task = task.strip()

		for i in keys:
			if i in task:
				zapros = task.replace(i, '')
				zapros = zapros.strip()
				task = 'найди'

		if task == 'найди':
			wb.open(f'https://www.google.com/search?q={zapros}&oq=%{zapros}&aqs=chrome..69i57j0i67j0i67i433j0i67l3j0i433i512j0i512j0i433i512j0i67i433.4137j0j7&sourceid=chrome&ie=UTF-8')
			

	while True:
		exe(listen())