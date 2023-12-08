from index import params_string, params, params_three, venue, extract_details_from_venue

def test_params_string():
    query = params_string(params)
    assert query == '&ll=40.7,-74&query=tacos'

def test_params_string_three():
    query = params_string(params_three)
    assert query == '&ll=40.7,-74&query=tacos&radius=10'

def test_extract_details_from_venue():
    details = extract_details_from_venue(venue)
    assert details == {'id':'5b2932a0f5e9d70039787cf2', 'name': 'Los Tacos Al Pastor','location': [40.70243624175102, -73.98753900608666]}
