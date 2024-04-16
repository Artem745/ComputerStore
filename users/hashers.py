from django.contrib.auth.hashers import BasePasswordHasher

class MyPasswordHasher(BasePasswordHasher):
    algorithm = 'empty'
    def verify(self, password, encoded):
        """Check if the given password is correct."""
        print(password, encoded)
        return password == encoded

    def encode(self, password, salt):
        return password

    def safe_summary(self, encoded):
        return {
            ('algorithm'): self.algorithm,
        }
