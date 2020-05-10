import sendgrid

API_KEY = 'Registrate your own API_KEY'
sg = sendgrid.SendGridAPIClient(API_KEY)

def best_country(str_date):
    response = sg.client.geo.stats.get(query_params={
        'start_date':str_date,
        'end_date':str_date
    })
    import json

    data = json.loads(response.body)
    max_data = max(data[0]['stats'], key=lambda a: a['metrics']['unique_clicks'])
    return max_data['name']