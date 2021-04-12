class JsonParsing:
    def get_keys(self, d_or_l, keys_list):
        if isinstance(d_or_l, dict):
            for k, v in iter(sorted(d_or_l.items())):
                if isinstance(v, list):
                    self.get_keys(v, keys_list)
                elif isinstance(v, dict):
                    self.get_keys(v, keys_list)
                keys_list.append(k)
        elif isinstance(d_or_l, list):
            for i in d_or_l:
                if isinstance(i, list):
                    self.get_keys(i, keys_list)
                elif isinstance(i, dict):
                    self.get_keys(i, keys_list)
        else:
            print("** Skipping item of type: {}".format(type(d_or_l)))
        print(keys_list)
        return keys_list
