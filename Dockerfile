FROM selenium/standalone-chrome
LABEL maintainer="jose.castrejon@softtek.com"
#Exposing port to be used by Selenium
EXPOSE 4444

#Installing dependences
RUN sudo apt-get update && \
    sudo apt-get install -y python3.6 && \
    sudo apt-get -y install cron && \
    sudo apt install -y python3-pip 
#Installing pip for Python
RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python
#Installing pip modules
RUN sudo pip3 install keyboard && sudo pip3 install selenium && sudo pip3 install pytest
#Enable cron on system
#RUN sudo systemctl enable cron
#Set workdir and copying TEST script, execution permissions will be given
WORKDIR /home/seluser
ADD pages ./pages
ADD test ./test
#Setting up simple cron task by adding crontab file to cron.d directory
ADD crontab /etc/cron.d/simple-cron 
#Adding script to execute as cronjob and giving execution permissions to him and simple cron on cron.d dir
ADD script.sh .
RUN sudo chmod 0777 script.sh
RUN sudo chmod 0644 /etc/cron.d/simple-cron
#Creating a log file
RUN sudo touch /var/log/cron.log && sudo chmod 0777 /var/log/cron.log 
#Adding modified entrypoint to /opt/bin DIR, this is important, otherwise Selenium will not start
ADD entry_point.sh /opt/bin/entry_point.sh
RUN sudo chown root /opt/bin/entry_point.sh && sudo chmod 0777 /opt/bin/entry_point.sh










