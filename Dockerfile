FROM python:3.8

# Copy certificate into container
COPY /certs/CPAROOT-CA.pem /certs/CPAROOT-CA.pem
COPY pip.conf /etc/pip.conf

ENV REQUESTS_CA_BUNDLE=/certs/CPAROOT-CA.pem

# Point pip at container certificate
# RUN pip config set global.cert /certs/CPAROOT-CA.pem
# RUN pip config set global.timeout 180
# RUN pip config set global.trusted-host pypi.org pypi.python.org files.pythonhosted.org

# Install poetry
RUN pip install 'Poetry==1.0.0b4'

# Set poetry configuration
RUN poetry config virtualenvs.create false
RUN poetry config virtualenvs.in-project false

# Copy poetry lock file into container
# COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

# Install poetry dependencies
RUN poetry install

ENTRYPOINT [ "/bin/bash" ]