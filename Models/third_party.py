from reliableVotinSystem.Security.Paillier_Cipher import *
class Third_party():
    def __init__(self):
        self.public_key, self.private_key = generate_keys()

    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.private_key