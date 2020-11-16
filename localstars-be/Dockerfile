FROM python:3.7.3

COPY start.sh /
COPY requirements.txt /

RUN chmod +x ./start.sh

# Following https://stackoverflow.com/questions/23391839/clone-private-git-repo-with-dockerfile
#for a secure git clone method

RUN pip install -r requirements.txt 

ADD repo-key /
RUN \
  chmod 600 /repo-key && \  
  echo "IdentityFile /repo-key" >> /etc/ssh/ssh_config && \  
  echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \  
    git clone git@github.com:jasonwer/starfleet.git && \
    chmod 777 ./starfleet/localstars-be/start.sh

ENTRYPOINT ./starfleet/localstars-be/start.sh

