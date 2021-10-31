import datetime

from requests.api import get

def validator_quantity(json_value, years, titles):
    tmp = json_value.get('education')
    validator = 'No aplica'
    if (len(tmp) > int(titles)):
        validator =  'Aplica'
    if count_years(json_value) > int(years)*12:
        validator = 'Aplica'
    print(validator)
    return validator
def get_now():
    return datetime.datetime.now()
def count_years(json_value):
    months = {'January': 1, 'February': 2, 'March': 3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
    experiences = json_value.get('experiences')
    cont_months = 0
    for experience in experiences:
        if experience.get('category') == 'jobs':
            
        
            from_month = (months[experience.get('fromMonth')])
            from_year = experience.get('fromYear')
            if experience.get('fromMonth') != None and experience.get('toYear') != None:
                to_month = (months[experience.get('toMonth')])
                to_year = experience.get('toYear')
            else:
                to_month = None
                to_year = None

            start_date = datetime.datetime(int(from_year), from_month, 1)
            if to_month != None and to_year != None:

                end_date = datetime.datetime(int(to_year), to_month, 1)
            else:
                end_date = get_now()
            num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
            cont_months += num_months
    return cont_months
