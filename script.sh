#!/bin/bash

function runTest(){
    cd /home/seluser/test 
    pytest Test_Menu.py >> /var/log/cron.log 2>&1
}

runTest