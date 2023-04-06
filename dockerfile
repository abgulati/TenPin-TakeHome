FROM python:3.9-slim-buster
RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user
USER app_user
COPY . .
CMD ["bash"]
CMD [ "python", "./ten_pin.py" ]