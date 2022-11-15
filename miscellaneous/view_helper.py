def get_template_name(item_name, page_number):
    template_name = f'{item_name}/{page_number}.html'
    return template_name


def get_next_page(limit_page, page_number):
    next_page = page_number + 1
    if next_page > (limit_page - 1):
        next_page = 0
    return next_page


def get_previous_page(page_number):
    previous_page = page_number - 1
    if previous_page < 0:
        previous_page = 0
    return previous_page
