def post_analyzer(likes_list):
    total_likes = 0

    # Loop to calculate total likes
    for like in likes_list:
        total_likes += like

    # Condition check
    if total_likes >= 1000:
        status = "Viral Post"
    else:
        status = "Normal Engagement"

    print("Total Likes:", total_likes)
    print("Post Status:", status)


# Input
likes = [200, 300, 150, 400]
post_analyzer(likes)