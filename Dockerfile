FROM python:3

# Copy certificate into container
COPY CPAROOT-CA.pem /certs/CPAROOT-CA.pem

# Point pip at container certificate
RUN pip config set global.cert /certs/CPAROOT-CA.pem
RUN pip config set global.timeout 180
RUN pip config set global.trusted-host pypi.org
RUN pip config set global.trusted-host pypi.python.org
RUN pip config set global.trusted-host files.pythonhosted.org

# Install poetry
RUN pip install 'Poetry==0.12.17'

# Set poetry configuration
RUN poetry config settings.virtualenvs.create false

# Copy poetry lock file into container
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

# Install poetry dependencies
RUN poetry install

ENTRYPOINT [ "/bin/bash" ]