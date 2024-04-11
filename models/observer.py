from pydantic import BaseModel


class Subscriber(BaseModel):
    ip_address: str
    port: int

    def __eq__(self, other):
        return self.ip_address == other.ip_address and self.port == other.port
