from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile.jpg', upload_to='profiles')

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    # def save(self, *args, **kwargs):
    #     try:
    #         this = Profile.objects.get(id=self.id)
    #         if this.image != self.image and this.image.name != 'default_profile.jpg':
    #             this.image.delete(save=False)
    #     except Profile.DoesNotExist:
    #         pass
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)