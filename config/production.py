from logging.config import dictConfig
from config.default import *

SQLAlCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLAlCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'+\xa8J\n\x01\xa5(\x1c\xaf\xfe\x1e\xf1dm\xf9\x1c'

dictConfig({
	'version' : 1,
	'formatters' : {
		'default' : {
			'format' : '[%(asctime)s] %(levelname)s in %(module)s : %(message)',
		}
	},
	'handlers' : {
		'file' : {
			'level' : 'INFO',
			'class' : 'logging.handlers.RotatingFileHandler',
			'filename' : os.path.join(BASE_DIR, 'logs/myproject.log'),
			'maxBytes' : 1024 * 1024 * 5 , # 5MB
			'backupCount' : 5,
			'formatter' : 'default',
		},
	},
	'root' : {
		'level' : 'INFO',
		'handlers' : ['file']
	}
})