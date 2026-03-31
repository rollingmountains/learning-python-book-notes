# config_value = 100


class Config:
    def __init__(self, value=500):
        self.value = value

    def __repr__(self):
        return f"{self.value}"
