from configparser import ConfigParser


class GetSettings:
    def __init__(self, settings_ini):
        settings = ConfigParser()
        settings.read(settings_ini)

        print(settings['DEFAULT']['Ip'])
        # 132.32.44.12

        print(settings['DEFAULT']['Port'])
        # 7777


if __name__ == "__main__":
    test = GetSettings("settings.ini")
    print(test)
