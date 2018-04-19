"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, email, first_name, last_name, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password


def get_by_email(email, customers):
    """Get customer name and password based on email."""
    if customers.get(email):
        print customers[email]
        return customers[email]
    # else:
    #     print "Not a customer"

def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customer info.

    Dictionary will be {id: Customer object}
    """

    customers = {}

    for line in open(filepath):
        (first_name,
         last_name,
         email,
         password) = line.strip().split("|")

        customers[email] = Customer(email, first_name, last_name, password)

    return customers

all_customers = read_customers_from_file('customers.txt')
#get_by_email('janet@hotmail.com', customer_list)


