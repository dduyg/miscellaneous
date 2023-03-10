# Question 2


def get_followers(n_followers, t_followers):
    giveaways = 0
    while n_followers < t_followers:
        n_followers += n_followers * 0.1
        giveaways += 1
    return giveaways

get_followers(100000,200000)
