import random, string

def generate_tandom_email_and_password(domain=None, email_prefix=None, password=None):
    """
    This function generates a random email and password.
    :param domain: The domain to be used in the email. If not provided, the domain will be 'example.com'
    :param email_prefix: The prefix to be used in the email. If not provided, the prefix will be 'testuser'
    :param password: The password to be used. If not provided, the password will be 'password123!'
    :return: A tuple containing the email and password
    """

    
    domain = domain if domain else 'example.com' # check if domain is provided, if not, use example.com
    email_prefix = email_prefix if email_prefix else 'testuser' # check if email_prefix is provided, if not, use testuser
    password = password if password else 'password123!' # check if password is provided, if not, use password123!

    random_email_length = 10
    rnadom_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_length))
    email = f"{email_prefix}_{rnadom_string}@{domain}"

    password_length = 10
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))

    random_info = {'email': email, 'password': password}
    return random_info

print(generate_tandom_email_and_password())