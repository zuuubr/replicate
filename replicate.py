import os


def programm_code():
	with open('replicate.py', 'r') as code_file:
		code = code_file.read()
	return code

def replicate(target_patch, code):
	with open(target_patch + 'replicate.py', 'w') as replicate_file:
		replicate_file.write(code)

def delete():
	pass

def main():
	# ОСТОРОЖНО УДАЛИТ ВСЕ ФАЙЛЫ!!!
	os.startfile('cmd.exe','runas')
	target_patch = "C:\Программирование\Python\Файл для тестов\Проверка репликатора"
	code = programm_code()

	#replicate(target_patch, code)
	#delete(target_patch)


main()
