#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from pyfiglet import print_figlet

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    text = fdp.ConsumeUnicodeNoSurrogates(1000)

    print_figlet(text)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()