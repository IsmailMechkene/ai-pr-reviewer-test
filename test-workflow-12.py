API_KEY = "sk-1234567890abcdefghijklmnop"

def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def process_items(items):
    result = []
    for item in items:
        if item:
            if item['active']:
                if item['type'] == 'premium':
                    if item['balance'] > 0:
                        result.append(item['balance'] * 1.5)
                    else:
                        result.append(0)
                else:
                    result.append(item['balance'])
    return result

password = "admin1234"
EOF
