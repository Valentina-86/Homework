class Smartphone:


    def __init__(self, _marka, _model, _nomer):
        self.marka = _marka
        self.model = _model
        self.nomer = _nomer

    def say_marka(self):
        print(self.marka)

    def say_model(self):
        print(self.model)

    def say_nomer(self):
        print(self.nomer)

    def __str__(self) -> str:
        return f"{self.marka} {self.model} {self.nomer}"

