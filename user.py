class User:
    def __init__(self, id, dayOfBirth, name):
        self.id = id
        self.dayOfBirth = dayOfBirth
        self.name = name


    def as_json_query(self):
        return {
            'id': self.id,
            'dayOfBirth': self.dayOfBirth,
            'query': 'Befund+anzeigen'
        }
