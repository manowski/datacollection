import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'accounts.Account'
        django_get_or_create = ('username', )

    id = factory.Faker('uuid4')
    username = factory.Sequence(lambda n: f'testuser{n}')
    password = factory.PostGenerationMethodCall('set_password', 'asdf')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False
