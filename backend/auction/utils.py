def duration_to_seconds(duration):
    """
    Method takes timedelta argument and returns seconds
    """
    return duration.seconds


def get_or_none(classmodel, **kwargs):
    """
    Method takes model name and can get instance, but if there is no instances returns None
    """

    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.MultipleObjectsReturned as e:
        print('Error:', e)

    except classmodel.DoesNotExist:
        return None
