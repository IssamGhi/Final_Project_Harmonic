postgresql = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'zayn',
    'db': 'metelyk'
}

postgresql_test = {
    'host': 'localhost:5431',
    'user': 'postgres',
    'password': 'zayn',
    'db': 'metelyk'
}

postgresql_string = "postgresql://{}:{}@{}/{}".format(postgresql['user'], postgresql['password'], postgresql['host'], postgresql['db'])
postgresql_string_test = "postgresql://{}:{}@{}/{}".format(postgresql_test['user'], postgresql_test['password'], postgresql_test['host'], postgresql_test['db'])
