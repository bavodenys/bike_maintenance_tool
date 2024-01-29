import json
import os
import requests


def check_for_update(tool_major_version, tool_minor_version):
    request_update = False
    response = requests.get(url='https://bade-website.vercel.app/tool_versions')
    if response.status_code == 200:
        versions = response.json()['bike_maintenance_tool']
        if versions['major'] > tool_major_version:
            request_update = True
        elif versions['major'] == tool_major_version:
            if versions['minor'] > tool_minor_version:
                request_update = True
            elif versions['minor'] == tool_minor_version:
                pass  # User has the latest tool version
            else:
                pass  # User has a tool with a minor version bigger than the official tool??
        else:
            pass  # User has a tool with a major version bigger than the official tool???
    else:
        pass # Could not retrieve versions from the database
    return request_update




def distance_conversion(distance, gain):
    return round(distance*gain, 2)
