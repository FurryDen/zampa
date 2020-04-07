<p align="center">
<img src="https://i2.wp.com/furryden.it/wp-content/uploads/2018/07/CHI-SIAMO1_sito.png?ssl=1" alt="Smiley face" height="297" width="800">
</p>

[![Python3.7+](https://img.shields.io/badge/Python-3.7%2B-green.svg)](https://www.python.org/downloads) [![Group](https://img.shields.io/badge/Group-FurryDen-blue)](https://t.me/officialfurryden)

## How to start

<b>Clone this repo:</b> ```git clone https://github.com/FurryDen/zampa.git```
<br>

## Requirements ⚙️

Besides [Python 3.7+](https://www.python.org/downloads/) we will be using the following packages:

<b>Install requirements</b> (https://github.com/FurryDen/zampa/blob/master/requirements.txt)
<br>
<b>Command:</b> ```pip install -r requirements.txt``` <b>Or</b> ```pip3 install -r requirements.txt```

<br>

## Global Commands List
<br>
<h3>Commands to be executed in response to a username</h3>
<br>


| Command | Description |
| --- | --- |
| /ban | ban user |
| /muta | mute user |
| /smuta | unmute user |
| /info | user information and chat id |
| /delete | delete message |
| /kick | kick user |
<br>
<h3>Commands to be executed in chat</h3>
{text} = text to insert

| Command | Description |
| --- | --- |
| /a {text}| announcement |
| /setfissa {text} | set pin message by bot |
| /fissa | pin message by bot |
| /info | user information and chat id |
| /delete | delete message |
| /kick | kick user |
| /meteo yourcityname | weather |
<br>
<h3>Welcome Settings</h3>

| Command | Description |
| --- | --- |
| /setwelcome | set the welcome for your group |
| /listwelcome | watch your welcome by group |
| /updatewelcome | update your welcome by group |
| /add BUTTON,example.com | add button into welcome |
| /listbutton | remove and see the welcome buttons |


<b>Import the database from the /SQL folder</b>
<br>
<b>In your shell start this bot use this command=></b> ```python3 bot.py```

### Do you have problems installing mysqlclient requirements?
Use this command:
<ul>
<li><b>Centos:</b> sudo yum install mysql-devel</li>
<li><b>Ubuntu/Debian:</b> sudo apt-get install python-dev default-libmysqlclient-dev</li>
<li><b>Fedora:</b> sudo dnf install python python-devel mysql-devel redhat-rpm-config gcc</li>
</ul>

<b>Important Note: This bot only works with python telegram bot 12.1.1+</b>
<br>

## How can I create a plugin?
🔷 Go to the /plugins folder (https://github.com/FurryDen/zampa/tree/master/plugins)
<br>
🔷 inside the plugins folder you will find the ```__init__.py``` file
    Every time you add a plugin inside the folder you have to add the name of the file in the ```__all__``` array
    For example:
    if we create the banana.py file we have to insert banana inside ```__all__```
    <br>
    <a href="https://imgur.com/pMiwxIR"><img src="https://i.imgur.com/pMiwxIR.png" title="source: imgur.com" /></a>
    <a href="https://imgur.com/dR0nN1P"><img src="https://i.imgur.com/dR0nN1P.png" title="source: imgur.com" /></a>
    <br>
🔷Now let's go to bot.py and enter our plugin command with the following command line:
    ```dispatcher.add_handler (CommandHandler ("banana", plugins.banana.init))```
    where we will insert plugins.filename.functionname
    and in "banana" enter the command that will work on telegram (/banana)
    <a href="https://imgur.com/sOoPruP"><img src="https://i.imgur.com/sOoPruP.png" title="source: imgur.com" /></a>
    <br>
🔷 Video Tutorial: https://youtu.be/Bmm37wG1EZQ

# Credits
<br>
Thanks to https://github.com/SteelManITA
<br>
Thanks to https://github.com/stefano-mecocci
<br>
Thanks to https://github.com/JervNorsk
<br>
Thanks to https://github.com/Kavuti/python-italy-telegram-bot

## License 📄

Please read the [LICENSE](LICENSE) provided in this rep