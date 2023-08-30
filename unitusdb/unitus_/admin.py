from django.contrib import admin
from .models import Profile
models=(Profile)

admin.site.register(models)

from .models import User
models=(User)

admin.site.register(models)

from .models import Department
models=(Department)

admin.site.register(models)

from .models import Test
models=(Test)

admin.site.register(models)

from .models import Macroaree
models=(Macroaree)

admin.site.register(models)

from .models import Macroaree_test
models=(Macroaree_test)

admin.site.register(models)

from .models import Availability
models=(Availability)

admin.site.register(models)
# Register your models here.
