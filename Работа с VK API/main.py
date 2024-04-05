import vk_api

api_token = "ваш токен"

vk_ses = vk_api.VkApi(token=api_token)

user = vk_ses.method("users.get", {"user_ids": 1}) # вызываем метод users.get для получения информации о человеке с id 1
id_1 = user[0]['first_name'] + ' ' + user[0]['last_name']

print(f'\nЧеловек с id 1: {id_1}')

friends = vk_ses.method("friends.get", {"user_ids": 250786765, "fields": 'nickname'}) # вызываем метод friends.get для получения cписка друзей

print(f"\nСписок друзей:") # из полученной выше информации оставляем только имя и фамилию
for name in friends['items']:
    print(name['first_name'] + ' ' + name['last_name'])
