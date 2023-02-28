import os
import datetime

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from botocore.signers import CloudFrontSigner


CDN_IMAGE_URL = os.getenv('CDN_IMAGE_URL')
CF_KEY_ID = os.getenv('CF_KEY_ID')


def rsa_signer(message):
    # .pem is the private keyfile downloaded from CloudFront keypair
    with open('private_keyfile.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())


def generate_signed_url_tiktok_img(imageid):
    key_id = CF_KEY_ID
    url = f"{CDN_IMAGE_URL}/tiktok/img/{imageid}.jpeg"
    current_time = datetime.datetime.utcnow()
    expire_date = current_time + datetime.timedelta(days=1)
    cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)
    # Create a signed url that will be valid until the specfic expiry date
    # provided using a canned policy.
    signed_url = cloudfront_signer.generate_presigned_url(url, date_less_than=expire_date)
    return signed_url


def generate_signed_url_ig_story_img(userid, imageid):
    key_id = CF_KEY_ID
    url = f"{CDN_IMAGE_URL}/instagram/{userid}/stories/{imageid}.jpeg"
    current_time = datetime.datetime.utcnow()
    expire_date = current_time + datetime.timedelta(days=2)
    cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)
    # Create a signed url that will be valid until the specfic expiry date
    # provided using a canned policy.
    signed_url = cloudfront_signer.generate_presigned_url(url, date_less_than=expire_date)
    return signed_url


def generate_signed_url_ig_story_video(userid, imageid):
    key_id = CF_KEY_ID
    url = f"{CDN_IMAGE_URL}/instagram/{userid}/stories/{imageid}.mp4"
    current_time = datetime.datetime.utcnow()
    expire_date = current_time + datetime.timedelta(days=2)
    cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)
    # Create a signed url that will be valid until the specfic expiry date
    # provided using a canned policy.
    signed_url = cloudfront_signer.generate_presigned_url(url, date_less_than=expire_date)
    return signed_url
