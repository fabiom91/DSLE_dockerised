import json

class ApiAuth:
    def __init__(self, api_file):
        with open(api_file) as f:
            self.mapping = json.load(f)
            self.reverse_mapping = { v: k for k,v in self.mapping.items() }
    
    def is_valid(self, api_key):
        return api_key in self.reverse_mapping
    
    def get_user(self, api_key):
        return self.reverse_mapping.get(api_key, None)
    
    def get_api_key(self, user):
        return self.mapping.get(user, None)

    # def get_api_list(self):
    #     return self.reverse_mapping


