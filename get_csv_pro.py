base_test_url = '';
base_prod_url = '';

bool_prod = false;
csv_endpoint = '';

if bool_prod:
  endpoint = 'http://' + base_prod_url + csv_endpoint;
else:
  endpoint = 'http://' + base_test_url + csv_endpoint;
  
