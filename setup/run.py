#!/usr/bin/python3

import sys
import setup


img_build_id = setup.get_img_buildid()

shared_drive_path = 'dock'
if len(sys.argv) == 2:
   shared_drive_path = sys.argv[1]

print('running app:', shared_drive_path)
setup.run(shared_drive_path)


