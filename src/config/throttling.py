from rest_framework.throttling import UserRateThrottle


class SubscriptionRateThrottle(UserRateThrottle):
    # Define a custom scope name to be referenced by DRF in config/common.py
    scope = "subscription"

    def __init__(self):
        super().__init__()

    def allow_request(self, request, view):
        """
        Override rest_framework.throttling.SimpleRateThrottle.allow_request
        Check to see if the request should be throttled.
        On success calls `throttle_success`.
        On failure calls `throttle_failure`.
        """

        if request.user.is_staff:
            # No throttling
            return True

        if request.user.is_active:
            user_daily_limit = request.user.tier
            if user_daily_limit or user_daily_limit == 0:
                # Override the default from config/common.py
                self.duration = 3600
                self.num_requests = user_daily_limit
            else:
                # No throttling
                return True

        return super().allow_request(request=request, view=view)
