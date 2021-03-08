from database import DataBase


db = DataBase()
# db.init_base_roles()
# db.init_base_roles()  # создали несколько базовых ролей
# db.create_user("alex", "123", "alex@gmail.com", "Russia")
# db.create_user("tom", "qwe", "tom_qwe@gmail.com", "USA")
# db.create_user("admin", "123", "admin@gmail.com", "Russia", role_id=1)
# db.create_user("sergey", "qwe", "ssssss@gmail.com", "Canada", role_id=2)
print("Пользователи:\n")
db.show_all_users()
print("\nСписок доступных ролей:\n")
db.show_all_roles()
