from opencodelists import actions

from .factories import OrganisationFactory, UserFactory


def test_activate_user():
    user = UserFactory(is_active=False)

    user = actions.activate_user(user=user, password="test")

    # user has been activated and has a password set
    assert user.is_active
    assert user.has_usable_password()


def test_create_organisation():
    o = actions.create_organisation(name="Test University", url="https://test.ac.uk")
    assert o.name == "Test University"
    assert o.slug == "test-university"
    assert o.url == "https://test.ac.uk"


def test_create_user():
    org = OrganisationFactory()

    user = actions.create_user(
        username="testym",
        name="Testy McTesterson",
        email="test@example.com",
        organisation=org,
    )

    assert user.username == "testym"
    assert user.name == "Testy McTesterson"
    assert user.email == "test@example.com"
    assert user.organisation == org
