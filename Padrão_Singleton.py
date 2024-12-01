import threading
import re


class UserRegistry:
    """
    Classe Singleton para gerenciar o registro de usuários.
    """
    _instance = None
    _lock = threading.Lock()  # Garante thread-safety

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:  # Verifica novamente dentro do lock
                if not cls._instance:
                    cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # O init será chamado apenas na primeira criação
        if not hasattr(self, "_users"):
            self._users = {}

    def register_user(self, username, email):
        """
        Registra um novo usuário.
        """
        if username in self._users:
            raise ValueError(f"Usuário '{username}' já registrado.")
        self._users[username] = email
        print(f"Usuário '{username}' registrado com sucesso.")

    def get_user_email(self, username):
        """
        Obtém o e-mail de um usuário.
        """
        return self._users.get(username, None)

    def list_users(self):
        """
        Lista todos os usuários registrados.
        """
        return self._users


def is_valid_username(username):
    """Valida o nome de usuário (não vazio, alfanumérico)."""
    return bool(username and username.isalnum())


def is_valid_email(email):
    """Valida o formato do email."""
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_regex, email) is not None


def get_user_input():
    """Obtém e valida os dados do usuário."""
    while True:
        username = input("Digite o nome de usuário: ").strip()
        if not is_valid_username(username):
            print("Nome de usuário inválido! Deve ser alfanumérico e não vazio.")
            continue

        email = input("Digite o e-mail: ").strip()
        if not is_valid_email(email):
            print("E-mail inválido! Certifique-se de usar um formato válido.")
            continue

        return username, email


# Testes
if __name__ == "__main__":
    registry = UserRegistry()

    print("Bem-vindo ao sistema de registro de usuários!")

    while True:
        print("\n1. Registrar usuário")
        print("2. Listar usuários")
        print("3. Obter e-mail de um usuário")
        print("4. Sair")
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            try:
                username, email = get_user_input()
                registry.register_user(username, email)
            except ValueError as e:
                print(e)
 
        elif choice == "2":
            users = registry.list_users()
            if users:
                print("Usuários registrados:")
                for user, email in users.items():
                    print(f"- {user}: {email}")
            else:
                print("Nenhum usuário registrado.")

        elif choice == "3":
            username = input("Digite o nome de usuário: ").strip()
            email = registry.get_user_email(username)
            if email:
                print(f"E-mail de {username}: {email}")
            else:
                print(f"Usuário '{username}' não encontrado.")

        elif choice == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
