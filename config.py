import os

MONGODB_URL = 'mongodb+srv://cluster0.pzkiu.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority'
MONGODB_CERT = os.environ.get('MONGODB_ATLAS_CERT')
if MONGODB_CERT[:10] != '-----BEGIN':
    if '..' in MONGODB_CERT:
        raise ValueError('No backing up the directory tree!')
    else:
        cert = os.path.join(os.path.dirname(__file__), '..', MONGODB_CERT)
        # may throw an error if the file doesn't exist; that's fine
        with open(cert, 'rb') as contents:
            MONGODB_CERT = contents.read().decode('utf8')
