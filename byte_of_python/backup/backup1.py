import os
import time

# Файлы и каталоги для резервного копирования
sources = ['~/backup', '~/ssl/server.key']

# Каталог для хранения резервных копий
backup_dir = '~/Desktop/Learning/python.edu/workshop/backups'

# Имя файла для архива
archive = backup_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# Команда командой строки для помещения файлов и архив
backup_zip = "zip -qr {0} {1}".format(archive, ' '.join(sources))

# Запускаем создание резервной копии
if os.system(backup_zip) == 0:
	print('Резервная копия успешно создана в', archive)
else:
	print('Создание резервной копии не удалось', backup_zip)