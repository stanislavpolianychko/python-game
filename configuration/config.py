from configparser import ConfigParser


class Configuration:
    """Singleton class for getting configuration parameters
                    form defined file"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, file_name):
        self.parser = ConfigParser()
        self.parser.read(file_name)

    # representation of all config file sections
    def __repr__(self):
        return str(self.parser.sections())

    # get data from config file and validate it
    def __get_valid_data(self, section, param_name):
        value = self.parser.get(section, param_name)
        if value.isdigit():
            return int(value)
        elif value in ('true', 'false'):
            return bool(value)
        return value

    # get dictionary: section_dict = {param_name, validated_value}
    def __get_section_dict(self, section):
        return {name: self.__get_valid_data(section, name) for name in self.parser.options(section)}

    @property
    def player(self):
        return self.__get_section_dict('player')

    @property
    def barrier(self):
        return self.__get_section_dict('barrier')

    @property
    def window(self):
        return self.__get_section_dict('window')


config = Configuration('configuration/config.ini')
