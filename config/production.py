from config.default import *

SQLAlCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLAlCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'+\xa8J\n\x01\xa5(\x1c\xaf\xfe\x1e\xf1dm\xf9\x1c'