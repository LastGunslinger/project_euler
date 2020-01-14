ARG USER

FROM python:3.8

ARG USER

# Create a non-root user
RUN groupadd ${USER} --gid 1000 \
    && useradd ${USER} --create-home --shell /bin/bash --uid 1000 --gid 1000

ENV PATH=/home/${USER}/.local/bin:$PATH

# Copy certificate into container
COPY --chown=${USER}:${USER} certs /etc/certs
COPY --chown=${USER}:${USER} pip.conf /etc/pip.conf

RUN chown -R docker:docker /usr/local

USER ${USER}

# Install poetry
RUN pip install poetry --user

# Set poetry configuration
RUN poetry config virtualenvs.create false \
    && poetry config virtualenvs.in-project false

ENTRYPOINT [ "/bin/bash" ]
