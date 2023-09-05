import random
import string
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

user_ids = list(range(1, 50000))


def generate_customer_data() -> dict:
    random_user_id = random.choice(user_ids)

    customer_name = fake.name()
    customer_gender = fake.random_element(
        ["Male", "Female"])  # Generate random gender
    customer_occupation = fake.job()  # Generate a random job/occupation

    # Generate a random order value between 10 and 1000
    order_value = round(random.uniform(10, 1000), 2)

    # Generate a random order date within the last 365 days
    today = datetime.now()
    order_date = today - timedelta(days=random.randint(1, 365))

    return {
        'user_id': random_user_id,
        'customer_name': customer_name,
        'customer_gender': customer_gender,
        'customer_occupation': customer_occupation,
        'order_value': order_value,
        'order_date': order_date.strftime('%Y-%m-%d')
    }
