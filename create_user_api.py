# Replace <XXX> in the below script with your site url and user credentials.
# The auth_token lines can be commented (#) out for Flow sites with 2FA turned off.
# - If removing the auth_token line, also remove the preceeding comma.
# Modify the sg.create string to fit the intended workflow.

import shotgun_api3

two_factor = input('Enter 2FA Code: ')
username = "<XXX>"
legacy_password = "<XXX>"
site_url = "<XXX>"
sg = shotgun_api3.Shotgun("site_url",
                          login="username",
                          password="legacy_password",
                          auth_token=two_factor)

sg.create('HumanUser', {
                       'firstname': 'Mr. Tester',
                       'lastname': 'Testerino',
                       'email': 'testertesterino@emaildomain.com'})
