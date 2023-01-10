from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User,UserProfile

@receiver(post_save,sender=User)
def post_save_profile_create(sender,instance,created,**kwargs):
    if created:
        print(created)
        UserProfile.objects.create(user=instance)
        print ("User profile created")
    else:
        try:
            profile = UserProfile.objects.create(user=instance)
            profile.save()
        except:
            UserProfile.objects.create(user=instance)
            print("Dosent Existed Created profile")
        print ("User Updated profile")


@receiver(pre_save,sender=User)
def pre_save_profile(sender,instance,**kwargs):
    print(instance.username,"is created")
