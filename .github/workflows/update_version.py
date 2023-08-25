"""Automatically updates the Lichess-Bot version."""
import os
import datetime
import yaml

with open('versioning.yml') as version_file:
    versioning_info = yaml.safe_load(version_file)

current_version = versioning_info['Lichess_Bot_version']

utc_datetime = datetime.datetime.utcnow()
new_version = f"{utc_datetime.month}.{utc_datetime.day}.{utc_datetime.year}."
if current_version.startswith(new_version):
    current_version_list = current_version.split(".")
    current_version_list[-1] = str(int(current_version_list[-1]) + 1)
    new_version = ".".join(current_version_list)
else:
    new_version += "1"

versioning_info['Lichess_Bot_version'] = new_version

with open('versioning.yml', 'w') as version_file:
    yaml.dump(versioning_info, version_file, sort_keys=False)

with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print(f'new_version={new_version}', file=fh)
