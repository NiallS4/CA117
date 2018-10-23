def swap_keys_values(my_dict):
	new_dict = {v:k for k, v in my_dict.items()}
	return new_dict