class User:
    def __init__(self, user_id, name):
        self._id = user_id
        self._name = name
        self._access_level = 'user'

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_access_level(self, new_level):
        if new_level in ['user', 'admin']:
            old_level = self._access_level
            self._access_level = new_level
            print(f"Уровень доступа пользователя '{self._name}' изменен с '{old_level}' на '{self._access_level}'.")
        else:
            print("Ошибка: Неверный уровень доступа. Допустимые значения: 'user', 'admin'.")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self.users = []

    def add_user(self, user):
        if isinstance(user, User):
            if user not in self.users:
                self.users.append(user)
                print(f"Пользователь '{user.get_name()}' добавлен.")
            else:
                print(f"Пользователь '{user.get_name()}' уже существует.")
        else:
            print("Ошибка: объект не является пользователем.")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"Пользователь '{user.get_name()}' удален.")
        else:
            print("Ошибка: пользователь не найден в списке.")

    def list_users(self):
        if not self.users:
            print("Список пользователей пуст.")
        else:
            print("Список пользователей:")
            for user in self.users:
                print(f"- {user.get_name()} (ID: {user.get_id()}, Уровень доступа: {user.get_access_level()})")

    def change_user_access_level(self, user, new_level):
        if user in self.users:
            user.set_access_level(new_level)
        else:
            print(f"Ошибка: пользователь '{user.get_name()}' не найден в списке.")


admin = Admin(user_id=1, name="Александр")
user1 = User(user_id=2, name="Иван")
user2 = User(user_id=3, name="Мария")

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user1)  # Попытка добавить уже существующего пользователя

admin.list_users()

# Использование сеттера для изменения уровня доступа пользователя
admin.change_user_access_level(user1, "admin")
admin.change_user_access_level(user2, "moderator")  # Неверный уровень доступа

admin.list_users()

admin.remove_user(user1)
admin.remove_user(user1)  # Попытка удалить несуществующего пользователя

admin.list_users()
