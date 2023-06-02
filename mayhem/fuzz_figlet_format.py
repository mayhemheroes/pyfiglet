#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from pyfiglet import figlet_format

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    text = fdp.ConsumeUnicodeNoSurrogates(1000)

    figlet_format(text)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()