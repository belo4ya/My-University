from __future__ import annotations

from functools import partial

import bs4


def get_text(name: str, tag: bs4.element.Tag) -> str | None:
    _tag = tag.find(name)
    return _tag and _tag.get_text()


def parse_reviewers_xml(path: str) -> list[dict]:
    with open(path) as f:
        soup = bs4.BeautifulSoup(f, 'lxml-xml')

    user_list = []
    for user in soup.find_all('user'):
        user_get_text = partial(get_text, tag=user)

        id_ = user_get_text('id')
        username = user_get_text('username')
        name = user_get_text('name')
        sex = user_get_text('sex')
        mail = user_get_text('mail')
        registered = user_get_text('registered')
        birthdate = user_get_text('birthdate')
        name_prefix = user.get('prefix', None)
        country_tag = user.find('country')
        if country_tag:
            country = country_tag.get_text()
            country_code = country_tag.get('code', None)
        else:
            country = country_code = None

        user_list.append({
            'id': id_,
            'username': username,
            'name': name,
            'sex': sex,
            'mail': mail,
            'registered': registered,
            'birthdate': birthdate,
            'name_prefix': name_prefix,
            'country': country,
            'country_code': country_code,
        })

    return user_list
