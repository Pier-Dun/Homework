import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if (nickname == i.nickname) and (hash(password) == i.password):
                self.current_user = i
                return
        print(f'Пользователь {nickname} не существует')

    def register(self, nickname, password, age):
        for i in self.users:
            if nickname == i.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        self.users.append(User(nickname, password, age))
        self.current_user = self.users[-1]

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            exists = False
            for j in self.videos:
                if i.title == j.title:
                    print("Такое видео уже есть")
                    exists = True
                    break
            if not exists:
                self.videos.append(i)

    def get_videos(self, vid):
        all_vid = []
        for i in self.videos:
            if vid.upper() in i.title.upper():
                all_vid.append(i.title)
        return all_vid

    def watch_video(self, film_name):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for t in self.videos:
            if film_name == t.title:
                if not t.adult_mode or self.current_user.age >= 18:
                    for i in range(t.time_now, t.duration):
                        time.sleep(1)
                        t.time_now += 1
                        print(t.time_now, end=' ')
                    print('Конец видео')
                    t.time_now = 0
                else:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')

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