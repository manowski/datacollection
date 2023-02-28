import os


from src.users.models import InstagramUser


def add_new_instgram_user_direct(**kwargs):
    username = kwargs.get("username")
    node_url = os.getenv("NODE_URL")
    url = f"{node_url}/instagram/user/{username}"
    get_request = requests.get(url)
    get_response = get_request.json()

    if "graphql" in get_response:
        data_json = get_response.get("graphql").get("user")
        user_id = data_json.get("id")
        username = data_json.get("username")
        full_name = data_json.get("full_name")
        biography = data_json.get("biography")
        external_url = data_json.get("external_url")
        fbid = data_json.get("fbid")
        is_business_account = data_json.get("is_business_account")
        business_address_json = data_json.get("business_address_json")
        business_email = data_json.get("business_email")
        business_phone_number = data_json.get("business_phone_number")
        business_category_name = data_json.get("business_category_name")
        category_name = data_json.get("category_name")

        profile_pic_url = data_json.get("profile_pic_url")
        profile_pic_url_hd = data_json.get("profile_pic_url_hd")

        is_verified = data_json.get("is_verified")

        edge_follow = int(data_json.get("edge_follow").get("count"))
        edge_followed_by = int(data_json.get("edge_followed_by").get("count"))
        edge_media_count = int(data_json.get("edge_owner_to_timeline_media").get("count"))

        user = InstagramUser.objects.create(
            username=username,
            user_id=user_id,
            full_name=full_name,
            description=biography,
            external_url=external_url,
            fbid=fbid,
            profile_pic=profile_pic_url,
            profile_pic_hd=profile_pic_url_hd,
            is_verified=is_verified,
            is_business_account=is_business_account,
            business_address_json=business_address_json,
            business_email=business_email,
            business_phone_number=business_phone_number,
            business_category_name=business_category_name,
            category_name=category_name,
            followers_count=edge_followed_by,
            following_count=edge_follow,
            media_count=edge_media_count
        )

        photos_location = data_json.get("edge_owner_to_timeline_media").get("edges")
        crawl_instagram_posts_direct(
            photos_location=photos_location,
            user_id=user
        )
