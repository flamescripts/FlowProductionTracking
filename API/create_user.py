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
