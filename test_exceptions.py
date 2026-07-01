from bot.exceptions import ValidationError

try:
    raise ValidationError("Quantity must be greater than zero.")
except ValidationError as e:
    print("Caught Exception:")
    print(e)