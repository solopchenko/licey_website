# from django.core.exceptions import ValidationError
#
# def validate_url(value):
#
#     value_1_invalid = False
#     value_2_invalid = False
#
#     try:
#         url_validator(value)
#     except:
#         value_1_invalid = True
#
#     value_2_url = 'http://' + value
#     try:
#         url_validator(value_2_url)
#     except:
#         value_2_invalid = True
#
#     if value_1_invalid == False and value_2_invalid == False:
#         raise ValidationError("Invalid URL for this field")
#     return value