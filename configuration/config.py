from configparser import ConfigParser


class Configuration:
    """Singleton class for getting configuration parameters
                    from defined file."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, file_name):
        self.parser = ConfigParser()
        self.parser.read(file_name)

    # representation of all config file sections
    def __repr__(self):
        return str(self.parser.sections())

    # get data from config file and validate it
    def _get_valid_data(self, section, param_name):
        value = self.parser.get(section, param_name)
        if value.isdigit():
            return int(value)
        elif value in ('true', 'false'):
            return bool(value)
        return value

    # get dictionary: section_dict = {param_name, validated_value}
    def _get_section_dict(self, section):
        return {name: self._get_valid_data(section, name) for name in self.parser.options(section)}

    @property
    def player(self):
        return self._get_section_dict('player')

    @property
    def barrier(self):
        return self._get_section_dict('barrier')

    @property
    def window(self):
        return self._get_section_dict('window')

    @property
    def game(self):
        return self._get_section_dict('game')

    @property
    def menu(self):
        return self._get_section_dict('menu')

    @property
    def loading(self):
        return self._get_section_dict('loading')

    def ending(self):
        return self._get_section_dict('ending')


config = Configuration('configuration/config.ini')
