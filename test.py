from requests import post

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовокdfdsd',
                 'content': 'sdcdscsdc Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())
