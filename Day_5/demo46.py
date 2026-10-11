

import logging

logging.basicConfig(filename='demo.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logging.info('application process started')
logging.warning('5 records has missing email addresses')
logging.error('Failed to connect to the database')


