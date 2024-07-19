class UrTube:
    def __init__(self):
        self.users = list()
        self.videos = list()
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        for user in self.users:
           if user.nickname == nickname:
                if user.password == hash(password):
                    self.current_user = nickname

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname != nickname:
                pass
            else:
                print(f'Пользователь {nickname} уже существует')
                return
        self.current_user = User(nickname, hash(password), age)
        self.users.append(self.current_user)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for new_video in videos:
            for video in self.videos:
                if video == new_video:
                    break
            else:
                self.videos.append(new_video)

    def get_videos(self, words: str):
        words = words.lower()
        result = list()
        for video in self.videos:
            if words in video.title.lower():
                result.append(video.title)
        return result


    def watch_video(self, name_film: str):
        for name_of_film in self.videos:
            if name_film == name_of_film.title:
                if self.current_user == None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                    return
                if self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for i in range(1, name_of_film.duration + 1):
                    print(i, end=' ')
                print("Конец видео")



class Video:
    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')