from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod

class Musician(ABC):
    members = []
    def __init__(self, name="unknown"):
        self.name=name
        Musician.members.append(self.name)
    
class Band(Musician):
    instances=[]
    def __init__(self, name, members):
        self.name=name
        self.members=members
        Band.instances.append(self)
    @classmethod 
    def __repr__(self):
        pass
    @classmethod 
    def get_instrument(self):
        pass
    classmethod
    def play_solo(self):
        pass
    def play_solos(self):
        pass

    def __str__(self):        
        return f"We are {self.name} and we are music band"

    def __repr__(self):
        return f"Band instance. Name = {self.name}"

    @classmethod
    def to_list(cls):        
        return cls.instances

    
class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar" 
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    def get_instrument(self):
        return 'guitar'
    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    def get_instrument(self):
        return 'bass'
    def play_solo(self):
        return "bom bom buh bom"
    
class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"   
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
    def get_instrument(self):
        return 'drums'
    def play_solo(self):
        return "rattle boom crash"