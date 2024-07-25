FROM python:slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=webui/app.py
ENV PYTHONPATH=/usr/src/app

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]