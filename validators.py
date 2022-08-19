import re

from wtforms import ValidationError

from models import User


class ValueVSOwnedValidator:
    """Validates that user has enough money to sent given amount

    :param message: error message
    """

    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):

        if not re.match(r'^[0-9.]*$', field.data):
            raise ValidationError(
                self.message
                or field.gettext(
                    "Dopuszczone wyłącznie cyfry oraz znak kropki."
                )
            )

        if float(field.data) > float(form.owned_value.data):
            raise ValidationError(
                self.message
                or field.gettext(
                    "Stan Twojego konta jest niższy od wpisanej wartości."
                )
            )

        return


class UserExistsValidator:
    """Validates that given name exists in the User table

    :param message: error message
    """

    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        users = User.query.order_by(User.name).all()

        if field.data not in [user.name for user in users]:
            raise ValidationError(
                self.message
                or field.gettext(
                    "Osoba, do której chcesz wysłać przelew, nie posiada konta."

                )
            )

        return
