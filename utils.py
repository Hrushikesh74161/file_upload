from django.core.signing import Signer
from django.conf import settings


signer = Signer(key=settings.HASH_SALT)