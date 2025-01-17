import random

# DIDs
# emily.space: did:plc:jcoy7v3a2t4rcfdh6i4kza25
# astronomy.blue: did:plc:xy2zorw2ys47poflotxthlzg


# Pinned posts dict, where:
# - keys are a link to the post in ATProto format
# - values are the post weight (higher = more likely to be shown)
PINNED_POSTS = {    
    "at://did:plc:xy2zorw2ys47poflotxthlzg/app.bsky.feed.post/3kyzye4lujs2w": 3.0,  # Signup instructions
    "at://did:plc:xy2zorw2ys47poflotxthlzg/app.bsky.feed.post/3l3xtpvv46k24": 1.5,  # List of new feeds from Sep 12th 2024
    "at://did:plc:xy2zorw2ys47poflotxthlzg/app.bsky.feed.post/3kyxnyimjna2a": 0.5,  # Like the feed pls
    # "at://did:plc:xy2zorw2ys47poflotxthlzg/app.bsky.feed.post/3lfhcdbpfzk2f": 3.0,  # AAS 245
}

def add_pinned_post_to_feed(body):
    post = random.choices(population=list(PINNED_POSTS.keys()), weights=list(PINNED_POSTS.values()))[0]
    body["feed"].insert(0, {"post": post})
