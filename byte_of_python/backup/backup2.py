'''
Программа позволяет делать резервные копии файлов. Создает
отдельные папки в зависимости от даты, из-за чего каталог с
резеврными копиями имеет иерархичность.
'''

import os
import time

# Файлы и каталоги для резервного копирования
sources = ['/Users/neuropassenger/backup']

# Каталог для хранения резервных копий
backup_dir = '/Users/neuropassenger/Desktop/Learning/python.edu/workshop/backups'

# Текущая дата
today = backup_dir + os.sep + time.strftime('%Y%m%d')

# Текущее время
now = time.strftime('%H%M%S')

# Создаем каталог для резервных копий, если его еще нет
if not os.path.exists(today):
	os.mkdir(today)
print('Каталог успешно создан')

# Имя файла архива
file_name = today + os.sep + now + '.zip'

# Команда для создания архива
command = 'zip -qr {0} {1}'.format(file_name, ' '.join(sources))

# Выполнение команды для создания архива
if os.system(command) == 0:
	print('Резервная копия успешно создана в', file_name)
else:
	print('Создание резервной копии НЕ УДАЛОСЬ')
	print(command)
