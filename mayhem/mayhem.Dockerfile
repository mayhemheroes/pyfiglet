# Image with atheris installed
FROM fuzzers/atheris:2.0.7-python3.9

# Add the project source code
ADD . /src
WORKDIR /src

# Move fonts
RUN cp -R pyfiglet/fonts-standard pyfiglet/fonts

# Install dependencies
RUN pip install .

# Change permissions on fuzzers
RUN chmod +x /src/mayhem/fuzz_*.py
