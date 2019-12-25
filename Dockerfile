FROM python:3.8

# Copy certificate into container
COPY /certs /certs
COPY pip.conf /etc/pip.conf

# ENV REQUESTS_CA_BUNDLE=/certs/CPAROOT-CA.pem

# Point pip at container certificate
# RUN pip config set global.cert /certs/CPAROOT-CA.pem
# RUN pip config set global.timeout 180
# RUN pip config set global.trusted-host pypi.org pypi.python.org files.pythonhosted.org

# Create a non-root user
RUN groupadd docker --gid 1000 \
    && useradd docker --create-home --shell /bin/bash --uid 1000 --gid 1000

ENV PATH=/home/docker/.local/bin:$PATH

USER docker

# Install poetry
RUN pip install poetry --user

# Set poetry configuration
RUN poetry config virtualenvs.create true \
    && poetry config virtualenvs.in-project true

ENTRYPOINT [ "/bin/bash" ]