DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s' % ( 'admin', 'Password', '10.60.202.70', '3306', 'Nelp' )
SQLALCHEMY_TRACK_MODIFICATIONS = False