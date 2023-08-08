common_url = 'https://maimaidx-eng.com/'


def targetURL(url: str):
    target_url = common_url + url

    return target_url


def chartType(url: str):
    if url == 'https://maimaidx-eng.com/maimai-mobile/img/music_standard.png':
        return 'Standard'
    elif url == 'https://maimaidx-eng.com/maimai-mobile/img/music_dx.png':
        return 'DX'
    else:
        return ' '


def diificulty(url: str):
    if url == 'https://maimaidx-eng.com/maimai-mobile/img/diff_master.png':
        return 'Master'
    elif url == 'https://maimaidx-eng.com/maimai-mobile/img/diff_expert.png':
        return 'Expert'
    elif url == 'https://maimaidx-eng.com/maimai-mobile/img/diff_advanced.png':
        return 'Advanced'
    elif url == 'https://maimaidx-eng.com/maimai-mobile/img/diff_basic.png':
        return 'Basic'
    else:
        return ' '
