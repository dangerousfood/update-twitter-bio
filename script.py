import twitter
import datetime
SCOLDING_DATE = datetime.datetime(2019, 8, 11)
api = twitter.Api(consumer_key='x',
                      consumer_secret='x',
                      access_token_key='x',
                      access_token_secret='x')
time = datetime.datetime.now() - SCOLDING_DATE
api.UpdateProfile(description=str(time.days) + ' days since my employer has scolded me about my tweeting')