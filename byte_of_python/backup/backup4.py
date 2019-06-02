'''
Программа для резервного копирования. Версия 4.0

Программа позволяет делать резервные копии файлов. Создает
отдельные папки в зависимости от даты, из-за чего каталог с
резеврными копиями имеет иерархичность. К имени архива можно
добавить пользовательский комментарий.
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

# Комментарий пользователя для архива
comment = input('Введите комментарий для резервной копии --> ')

# Имя файла архива. Проверяется наличие комментария
if len(comment) == 0:
	file_name = today + os.sep + now + '.zip'
else:
	# Добавляем к имени файла комментарий и заменяем пробелы на нижнее подчеркивание
	file_name = today + os.sep + now + '_' + \
					comment.replace(' ', '_') + '.zip'

# Создаем каталог для резервных копий, если его еще нет
if not os.path.exists(today):
	os.mkdir(today)
print('Каталог успешно создан')

# Команда для создания архива
command = 'zip -qr {0} {1}'.format(file_name, ' '.join(sources))

# Выполнение команды для создания архива
if os.system(command) == 0:
	print('Резервная копия успешно создана в', file_name)
else:
	print('Создание резервной копии НЕ УДАЛОСЬ')
