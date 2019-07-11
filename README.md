# FREE PIZZA 🍕

Are you a #LdnOnt native? Did you miss your free name day at Stobies? Don't let that happen again! 
This python script that will check Stobies twitter and text you if it's your day for free pizza 🍕

## Getting Started 
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites 
* **Python 3.5+**
* **Twitter Developer Account + App created**
* **Twilio Account** 
* **config**.py 

### Installing 
Clone the repository 
```shell
$ git clone https://github.com/megfh/Pizza-Py.git
```

Install required libraries 
```shell
$ pip3 install -r requirements.txt 
```

Create your **config**.py  file with the following format:  
```python
# info can be found at https://developer.twitter.com/en/apps/{yourAppId} under "Keys and tokens"
TWITTER_CONFIG = {
    "consumer_key": "",
    "consumer_secret": "",
    "access_token": "",
    "access_token_secret": "",
}

# info can be found at https://www.twilio.com/console
TWILIO_CONFIG = {
    "account_sid": "", 
    "auth_token": "", 
    "sender": "" # your twilio phone number
}

# remember to include country code (1) before phone numbers && include alternate spellings of any names! 
CONTACTS = {
    "Meghan": "+11234567891", 
    "Megan": "+11234567891", 
    "Meg": "+11234567891", 
    "Thomas": "+17891234567", 
    "Tom": "+17891234567",
}
```

## Run 
```shell 
$ python3 pizza.py
```

## Built With 
[Tweepy](https://www.tweepy.org/) 

[Twilio](https://www.twilio.com/) 

## Author 
* **Meghan Hannon** - software developer - [github](https://github.com/megfh)

## N.B. 
* Inspiration: I missed my name day last time because I forgot to check twitter, and I don't like missing out on free pizza 🍕
* I have this script set to run on a cron schedule on my raspberry pi, but the AWS lambda free tier would be another viable option for running on a defined schedule 
* It may not be pretty, but it works 😊




