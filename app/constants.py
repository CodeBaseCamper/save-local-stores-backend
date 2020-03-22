import os


class DefaultPaths(enumerate):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    LOG_PATH = os.path.join(ROOT_DIR, 'log')
    PDF_PATH = os.path.join(ROOT_DIR, 'vouchers')
