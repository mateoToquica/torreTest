import datetime

def validator_quantity(json_value, years, titles):
    tmp = json_value.get('education')
    validator = 'No aplica'
    if (len(tmp) > int(titles)):
        validator =  'Aplica'
    if count_years(json_value) > int(years)*12:
        validator = 'Aplica'
    return validator

def count_years(json_value):
    months = {'January': 1, 'February': 2, 'March': 3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
    experiences = json_value.get('experiences')
    cont_months = 0
    for experience in experiences:
        if experience.get('category') == 'jobs':
            from_month = (months[experience.get('fromMonth')])
            from_year = experience.get('fromMonth')

            to_month = (months[experience.get('fromMonth')])
            to_year = experience.get('fromMonth')

            start_date = datetime.datetime(int(from_year), from_month, 1)
            end_date = datetime.datetime(int(to_year), to_month, 1)

            num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
            cont_months += num_months
    return cont_months
