import os
import config

root = config.get("root")
os.rmdir(root)
os.mkdir(root)

import initDB
