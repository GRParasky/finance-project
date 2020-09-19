from domains.entry.model import *

from database import save, commit


def create(obj: Entry):
    return save(obj)
