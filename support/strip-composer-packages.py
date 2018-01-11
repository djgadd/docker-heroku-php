import sys
import json

# Strips packages from the composer.lock and composer.json file, so we don't
# install packages into the docker image (saves a little time during image
# builds)

def parse_json(file_path):
    return json.load(open(file_path))

def write_json(file_path, data):
    with open(file_path, 'w') as output_file:
        json.dump(data, output_file, indent = 4)

# Parse the JSON
lck = parse_json(sys.argv[1])
cmp = parse_json(sys.argv[2])

# Remove packages from the lock data
if 'packages' in lck:
    lck['packages'] = []

# Remove packages-dev from the lock data
if 'packages-dev' in lck:
    lck['packages-dev'] = []

# Strip all but the platform requirements from the json data
if 'require' in cmp:
    if 'platform' in lck and lck['platform']:
        cmp['require'] = lck['platform']
    else:
        cmp['require'] = {}

# Strip all but the dev platform requirements from the json data
if 'require-dev' in cmp:
    if 'platform-dev' in lck and lck['platform-dev']:
        cmp['require-dev'] = lck['platform-dev']
    else:
        cmp['require-dev'] = {}

# Write the data
write_json(sys.argv[1], lck)
write_json(sys.argv[2], cmp)
