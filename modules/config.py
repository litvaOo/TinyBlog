import json

class Config:
    host = ''
    user = ''
    password = ''
    db_name = ''
    port = ''

    @staticmethod
    def buildConnectionString():
        config_file = json.loads(open('config.json', 'r', encoding='utf8').read())

        Config.host = config_file['host']
        Config.user = config_file['user']
        Config.password = config_file['password']
        Config.db_name = config_file['db_name']
        Config.port = config_file['port']

        return 'postgresql://' + Config.user + ':' + Config.password + "@" + Config.host + ":" + Config.port + "/" + Config.db_name
