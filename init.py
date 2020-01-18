import os
import config

root = config.get("root")

os.mkdir(root)

import initDB
