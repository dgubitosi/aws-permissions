#!/usr/bin/python3

import json

with open("iam_definition.json") as f:
    definition = json.load(f)

    for serv in definition:
        service = serv['prefix']

        # arns
        arns = ''
        for res in serv['resources']:
            arn = res['arn']
            arns += f'{service} => {arn}\n'

        # permissions
        permissions = ''
        for priv in serv['privileges']:
            action = priv['privilege']
            desc = priv['description']
            level = priv['access_level'].replace(' ','-').lower()

            resources = []
            for res in priv['resource_types']:
                resource = res['resource_type']
                if resource == '':
                    resource = '*'
                resources.append(resource)
            resources.sort()
            permissions += f'{service}:{action} [{level}] => {",".join(resources)}\n'

    with open("arns.txt", "w") as out:
        out.write(arns)

    with open("permissions.txt", "w") as out:
        out.write(permissions)
