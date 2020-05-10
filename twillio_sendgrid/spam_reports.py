import sendgrid
from datetime import datetime, timedelta
import json

API_KEY = 'Registrate your own API_KEY'
sg = sendgrid.SendGridAPIClient(API_KEY)


def how_spammed(str_date):
    dt = datetime.strptime(str_date, '%Y-%m-%d')
    response = sg.client.suppression.spam_reports.get(query_params={
        'start_time': int(dt.timestamp()),
        'end_time': int((dt + timedelta(days=1)).timestamp())
    })
    return len(json.loads(response.body))