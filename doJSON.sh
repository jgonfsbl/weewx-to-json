#! /bin/bash

#
# Frist, we do activate the virtualenv(ironment)
#
source venv/bin/activate

#
# Now that the virtualenv is running, then
# we can do execute the script
#
python3 weewx2json.py

#
# Finally, we do deactivate the virtualenv
#
deactivate
