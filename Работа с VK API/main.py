import vk_api

# мой api
api_token = 'vk1.a.qRyCPuTQlyx0QaKd8MBUMQP0LjwCFCCbhQamMrp0vBqN3PipYN7nLFMA-aENIsDqxqR7Q0rFrrAshafp-CVZSyqviFF96Zm9e8PHYU9xWkkBkv7ZEGlJ9GVSNct9EOlF4jlEy7HX6SsWaTQmatqHNnFGQO55Hsz83qZRJpWHjq5NbMfoyy84DOGuYExA6UXL'

vk_ses = vk_api.VkApi(token=api_token)

# вызываем метод users.get для получения информации о человеке с id 1
user = vk_ses.method("users.get", {"user_ids": 1})
id_1 = user[0]['first_name'] + ' ' + user[0]['last_name']

print(f'\nЧеловек с id 1: {id_1}')

# вызываем метод friends.get для получения cписка друзей
friends = vk_ses.method("friends.get", {"user_ids": 250786765, "fields": 'nickname'})

# из полученной выше информации оставляем только имя и фамилию
print(f"\nСписок друзей:")
for name in friends['items']:
    print(name['first_name'] + ' ' + name['last_name'])