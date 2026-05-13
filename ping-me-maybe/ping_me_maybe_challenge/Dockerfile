FROM python:3.11-slim

RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf

WORKDIR /opt/webapp

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/

RUN mkdir -p /var/backups/network
RUN mkdir -p /opt/.internal

RUN echo "The old network diagnostic backup was moved to /var/backups/network/" > /home/ctf/note.txt
RUN echo "Emergency admin token location: /opt/.internal/.admin_recovery_token" > /var/backups/network/diagnostic.log
RUN echo "AK26{p1ng_m3_b4by_0n3_m0r3_t1m3}" > /opt/.internal/.admin_recovery_token

RUN chown -R root:root /opt/webapp
RUN chown -R ctf:ctf /home/ctf
RUN chmod 644 /home/ctf/note.txt
RUN chmod 644 /var/backups/network/diagnostic.log
RUN chmod 644 /opt/.internal/.admin_recovery_token

USER ctf

WORKDIR /home/ctf

CMD ["python", "/opt/webapp/app.py"]