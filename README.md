# twitter-covid-bot

Python version:
```
$ python3 --version
Python 3.9.12
```

Activate `venv`:
```
$ python3 -m venv twitter-covid-bot-venv                                                                              <main ✗>
$ source twitter-covid-bot-venv/bin/activate  
```
Your shell prompt will change to show the name of the activated environment. Once activated, install packages and add to `requirements.txt`, i.e:
```
(twitter-covid-bot-venv) $ pip install Flask
Successfully installed Flask-2.0.3 Jinja2-3.1.1 MarkupSafe-2.1.1 Werkzeug-2.0.3 click-8.0.4 itsdangerous-2.1.2
(twitter-covid-bot-venv) $ pip freeze > requirements.txt                                                              
(twitter-covid-bot-venv) $ cat requirements.txt                                                                       
click==8.0.4
Flask==2.0.3
itsdangerous==2.1.2
Jinja2==3.1.1
MarkupSafe==2.1.1
Werkzeug==2.0.3
```

The `requirements.txt` can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with `install -r:
```
(twitter-covid-bot-venv) $ python3 -m pip install -r requirements.txt
```

To stop using the virtual environment:
```
(twitter-covid-bot-venv) $ deactivate
$ 
```

# Sources: 
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/).
- [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)