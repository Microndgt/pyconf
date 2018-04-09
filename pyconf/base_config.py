class BaseConfig:
    def __init__(self, config_file):
        self.sections = {}
        self._add_section('root')

        self.load(config_file)

    def load(self, config_file):
        raise NotImplementedError

    def _add_section(self, name, last_section=None):
        """Adds an empty section with the given name.

        :param name: new section name.
        """
        if last_section is None:
            last_section = self.sections
        last_section[name] = Section()
        return last_section[name]

    def get_config(self):
        """Gets all section items.

        :returns: dictionary with section name as key and section values and value.
        """

        return {section: self.sections[section].get_values() for section in self.sections}

    def get(self, key):
        """Tries to get a value from the ``root`` section dict_props by the given key.

        :param key: lookup key.
        :returns: value (str, bool, int, or float) if key exists, None otherwise.
        """

        if key in self.sections:
            return self.sections[key]

        return self['root'].get(key)

    def _add_dict_prop_to_section(self, key, value, section=None, pure=False):
        """Adds a key-value item to the given section.

        :param key: new item key.
        :param value: new item value.
        :param section: (optional) section name (``root`` by default).
        """
        if section is None:
            section = self.sections['root']
        section._add_dict_prop(key, value, pure=pure)

    def _add_list_prop_to_section(self, value, section=None):
        """Adds a flag value to the given section.

        :param value: new item value.
        :param section: (optional) section name (``root`` by default).
        """
        if section is None:
            section = self.sections['root']
        section._add_list_prop(value)

    def __repr__(self):
        return str(self.get_config())

    def __str__(self):
        return str(self.get_config())

    def __getitem__(self, key):
        if key in self.sections:
            return self.sections[key]
        else:
            try:
                return self.sections['root'][key]
            except KeyError:
                pass

        raise KeyError(key)

    def __setitem__(self, key, value):
        try:
            self.sections['root'][key] = value
            return None
        except KeyError as e:
            raise e

    def __eq__(self, other):
        return self.sections == other.sections


class Section:
    """INI configuration section.

    A Section instance stores both key-value and flag items, in ``dict_props`` and ``list_props`` attributes respectively.

    It is possible to iterate over a section; flag values are listed first, then key-value items.
    """

    def __init__(self):
        self.dict_props = {}
        self.list_props = []

    def get_values(self):
        """Gets section values.

        If section contains only flag values, a list is returned.

        If section contains only key-value items, a dictionary is returned.

        If section contains both flag and key-value items, a tuple of both is returned.
        """

        if self.list_props and self.dict_props:
            return self.list_props, self.dict_props

        return self.list_props or self.dict_props or None

    def get(self, key):
        """Tries to get a value from the dict_props by the given key.

        :param key: lookup key.
        :returns: value if key exists (str, bool, int, or float), None otherwise.
        """

        return self.dict_props.get(key)

    def _get_value_type(self, value):
        """Checks if the given value is boolean, float, int, of str.

        Returns converted value if conversion is possible (str, bool, int, or float).

        :param value: value to check.
        """

        value = value.strip()

        if value == 'True':
            return True
        elif value == 'False':
            return False
        else:
            try:
                return_value = int(value)
            except ValueError:
                try:
                    return_value = float(value)
                except ValueError:
                    return value

            return return_value

    def _add_dict_prop(self, key, value, pure=False):
        """Adds a key-value item to section."""
        if pure:
            self.dict_props[key] = value
            return
        typed_value_map = map(self._get_value_type, value.split(','))

        typed_value_tuple = tuple(typed_value_map)

        if len(typed_value_tuple) == 1:
            self.dict_props[key] = typed_value_tuple[0]
        else:
            self.dict_props[key] = typed_value_tuple

    def _add_list_prop(self, value):
        """Adds a flag value to  section."""
        typed_value_map = map(self._get_value_type, value.split(','))

        typed_value_tuple = tuple(typed_value_map)

        if len(typed_value_tuple) == 1:
            self.list_props.append(typed_value_tuple[0])
        else:
            self.list_props.append(typed_value_tuple)

    def __repr__(self):
        return str(self.get_values())

    def __str__(self):
        return str(self.get_values())

    def __iter__(self):
        for list_prop in self.list_props:
            yield list_prop

        for dict_prop in self.dict_props:
            yield dict_prop

    def __getitem__(self, key):
        try:
            return self.dict_props[key]
        except KeyError:
            pass

        try:
            return self.list_props[key]
        except (KeyError, TypeError):
            pass

        raise KeyError(key)

    def __setitem__(self, key, value):
        try:
            self.dict_props[key] = value
            return None
        except KeyError:
            pass

        try:
            self.list_props[key] = value
            return None
        except (KeyError, TypeError) as e:
            raise e

    def __eq__(self, other):
        return self.dict_props == other.dict_props and self.list_props == other.list_props
