# .devcontainer/Dockerfile
FROM ${PWD}/Dockerfile

# Add development-specific layers
RUN pip install --no-cache-dir pylint autopep8 black yapf bandit flake8 mypy pycodestyle pydocstyle

# Set up non-root user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
USER $USERNAME

CMD ["/bin/bash"]