#!/usr/bin/env python

from typing import Union, Optional, List, Dict
from random import randint

class Roster:
    def __init__(
        self,
        names: Union[str, List[str]],
        delim: Optional[str] = "\n"
    ) -> None:
        if isinstance(names, str):
            self.names = names.split(delim)
        elif isinstance(names, list):
            self.names = names

    def generate_ids(self) -> Dict[str, int]:
        return {n: randint(0,255) for n in self.names}


if __name__ == "__main__":
    r1 = Roster("nick\ncarla\nlivvy\njosie")
    print(r1.generate_ids())

    r2 = Roster("nick,emily,sam,vince", delim=",")
    print(r2.generate_ids())

    r3 = Roster(["nick", "giuli", "joe", "anna"])
    print(r3.generate_ids())
