import configparser


class GetSettings:
    def __init__(self, settings_ini):
        settings = configparser.ConfigParser()
        settings.read(settings_ini)

        print(settings['DEFAULT']['Ip'])
        # 132.32.44.12

        print(settings['DEFAULT']['Port'])
        # 7777
