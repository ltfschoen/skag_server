import sys

def get_squared(query_params):
	print("get_squared with query_params: ", query_params)
	if query_params['my_param'] is not None:
		return float(query_params['my_param'])**2
	else:
		return None

def main(query_params={}, **args):
	print("Received Flask API endpoint Query Parameters: ", query_params, file=sys.stderr)
	return get_squared(query_params)

if __name__ == "__main__":
    main()