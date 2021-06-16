import os

##########################################
# Contains variables used throughout the project
##########################################

PORT = int(os.environ.get('PORT', 5000))

DATABASE_URL = os.environ['DATABASE_URL'].replace('postgres', 'postgresql', 1)

TOKEN = os.environ['TOKEN']

OFFTOPIC_GROUP = -1001415779011

GROUP = -1001374176745  # -1001327617858 for test group

ADMINS = (703453307,  # Nyx
          806473770,  # BlueBettle
          984010225  # Phoenix
          )

VERIFIED_USERS = set(ADMINS + (
    924295169,  # Lucky
    1038099761,  # Abhiskek
    1128670209  # LalitSaini
))