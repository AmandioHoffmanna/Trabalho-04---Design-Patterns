from typing import List, Protocol


class Observer(Protocol):
    """Interface para os observadores."""
    def update(self, event: str, data: dict):
        pass


class NotificationSystem:
    """
    Classe que gerencia notificações usando o padrão Observer.
    """
    def __init__(self):
        self._observers: List[Observer] = []

    def subscribe(self, observer: Observer):
        """Inscreve um observador para receber notificações."""
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer):
        """Remove um observador da lista de inscritos."""
        self._observers.remove(observer)

    def notify(self, event: str, data: dict):
        """Notifica todos os observadores sobre um evento."""
        for observer in self._observers:
            observer.update(event, data)


class UserRegistry:
    """
    Classe para gerenciar o registro de usuários.
    Integra-se com o sistema de notificações.
    """
    def __init__(self, notification_system: NotificationSystem):
        self._users = {}
        self._notification_system = notification_system

    def register_user(self, username: str, email: str):
        """Registra um novo usuário e notifica os observadores."""
        if username in self._users:
            raise ValueError(f"Usuário '{username}' já registrado.")
        self._users[username] = email
        print(f"Usuário '{username}' registrado com sucesso.")
        # Notifica os observadores
        self._notification_system.notify("USER_REGISTERED", {"username": username, "email": email})

    def list_users(self):
        """Lista todos os usuários registrados."""
        return self._users


class EmailNotificationService:
    """
    Observador que envia notificações por e-mail.
    """
    def update(self, event: str, data: dict):
        if event == "USER_REGISTERED":
            print(f"[Email] Bem-vindo(a), {data['username']}! Um e-mail foi enviado para {data['email']}.")


class AuditLogService:
    """
    Observador que registra eventos em logs.
    """
    def update(self, event: str, data: dict):
        if event == "USER_REGISTERED":
            print(f"[Log] Usuário registrado: {data['username']} ({data['email']}).")


# Testes
if __name__ == "__main__":
    # Sistema de notificações
    notification_system = NotificationSystem()

    # Observadores
    email_service = EmailNotificationService()
    audit_log_service = AuditLogService()

    # Inscrição de observadores
    notification_system.subscribe(email_service)
    notification_system.subscribe(audit_log_service)

    # Sistema de registro de usuários
    user_registry = UserRegistry(notification_system)

    print("Bem-vindo ao sistema de registro de usuários com notificações!")
    while True:
        print("\n1. Registrar usuário")
        print("2. Listar usuários")
        print("3. Sair")
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            username = input("Digite o nome de usuário: ").strip()
            email = input("Digite o e-mail: ").strip()
            try:
                user_registry.register_user(username, email)
            except ValueError as e:
                print(e)

        elif choice == "2":
            users = user_registry.list_users()
            if users:
                print("Usuários registrados:")
                for user, email in users.items():
                    print(f"- {user}: {email}")
            else:
                print("Nenhum usuário registrado.")

        elif choice == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
