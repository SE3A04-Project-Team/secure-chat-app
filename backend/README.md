# Secure Chat Application Backend

This repo contains all the backend services surrounding message delivery and storage.

# run instructions
perform test with

    python3 start_server.py localhost {port}

Each client joins with

    python3 client.py localhost {port} USER{#}



# File structure
Interfaces are contained in the 'headers' folder.
implementations are contained in the 'src' folder. 


# Strict typing in Python 

To improve our efficiency and quality of code, we will be using type hinting.

For a complete guide see these [docs](https://docs.python.org/3/library/typing.html) or [cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).


# Samples
    def greeting(name: str) -> str:
        return "hello" + name


Sample List
   
    def get_list() -> list[str]:
        return list_1

Sample Class

    class ClassName:

        x_pos: int
        name: str

        def get_name(self, do_print: bool ) -> str:
            # do stuff
            return self.name

User Defined Class

    from headers.A import A

    def f(foo:A) -> int:
        # dio stuff


User Defined Class, if class is defined after usage

    from __future__ import annotations

    def f(foo: A) -> int:
        # do stuff
    

    class A:

        def create(self) -> A:
            # do stuff
