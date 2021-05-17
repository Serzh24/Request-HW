import requests

class Superhero:
    def __init__(self, name):
        self.name = name
        self.intelegence = {}
        self.response_dict = {}

    def get_data(self, url):
        # url = "https://superheroapi.com/api/2619421814940190/search/hulk"
        response = requests.get(url)
        self.response_dict = response.json()
        # import pprint
        # pprint.pprint(self.response_dict)
        return self.response_dict

    def get_intelegence(self):
        self.intelegence = {self.name: int(self.response_dict['results'][0]['powerstats']['intelligence'])}
        return self.intelegence

    def __str__(self):
        res = (f'Интеллект {self.name} равен {self.intelegence}')
        return res

hulk = Superhero('Hulk')
hulk.get_data("https://superheroapi.com/api/2619421814940190/search/hulk")
hulk.get_intelegence()
print(hulk)
batman = Superhero('Batman')
batman.get_data("https://superheroapi.com/api/2619421814940190/search/batman")
batman.get_intelegence()
print(batman)
thanos = Superhero('Thanos')
thanos.get_data("https://superheroapi.com/api/2619421814940190/search/thanos")
thanos.get_intelegence()
print(thanos)
superheroes = {**hulk.intelegence, **batman.intelegence, **thanos.intelegence}
print('Отсортируем супергероев по увеличению интеллекта:')
for i in sorted(superheroes.items(), key=lambda para: para[1]):
    print(i)