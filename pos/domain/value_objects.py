from dataclasses import dataclass


@dataclass(frozen=True)
class Rfc:
    value: str

    def __str__(self):
        return self.value
