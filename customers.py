"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""
    def __init__(self, first_name, last_name, email, password):
    	self.first = first_name
    	self.last = last_name
    	self.email = email
    	self.password = password

    def __repr__(self):
    	return f"<Customer {self.first} {self.last}>"

    # TODO: need to implement this


def read_customers_from_file(filepath):
    """
    """

    customers_dict = {}

    with open(filepath) as file:
        for line in file:
            (first, 
            last, 
            email, 
            password) = line.strip().split("|")

            customers_dict[email] = Customer(first, last, email, password)

    return customers_dict


def get_by_email(email):
	""""""
	return customers[email]

customers = read_customers_from_file("customers.txt")