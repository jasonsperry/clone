REQUESTS_PER_USER_PER_SEC = 180
WAIT_SEC = 1

RAW_DATA = 'raw_data'
STRUCTURED_DATA = 'structured_data'
RAW_MESSAGE = 'raw_message'

CREDENTIALS_FILENAME = 'credentials.json'

STATUS_READY = 0
STATUS_CONVERTED = 1
STATUS_NEED_CONVERTION = 2
STATUS_RAW_SAVED = 3
STATUS_QUARANTINE = -1

#API RELATED
MESSAGES_MAX_RESULTS = 10000

REQUESTS_PER_BATCH = 10
BATCHES_PER_TIME = 10


#GMAIL API
GMAIL_BASE_URL = 'https://gmail.googleapis.com'
GMAIL_BATCH_PATH = '/batch/gmail/v1'
DEFAULT_SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']