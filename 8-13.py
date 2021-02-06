def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('Yinyang', 'Guaiji',age='19',nationality='China',position='Student')
print(user_profile)
