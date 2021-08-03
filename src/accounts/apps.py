from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'src.accounts'

    # actstream register model
    # def ready(self):
    #     from actstream import registry
    #     registry.register(self.get_model('Account'))
