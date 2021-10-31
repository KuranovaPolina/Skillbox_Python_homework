import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def sites_func(phone_name_list):
    for i in phone_name_list:
        new_site = copy.deepcopy(site)
        new_site['html']['head']['title'] = 'Куплю/продам {0} недорого'.format(i)
        new_site['html']['body']['h2'] = 'У нас самая низкая цена на {0}'.format(i)
        print(i)
        print("site =", new_site)


N = int(input("N = "))
products_list = []
for _ in range(N):
    product_name = input("Product name: ")
    products_list.insert(0, product_name)
    sites_func(products_list)

'''
# version with recursion - problem
if i == "телефон":
    new_site = copy.deepcopy(site)
    return new_site
else:
    new_site = sites_func(phone_name_list[1:])
    new_site['html']['head']['title'] = 'Куплю/продам {0} недорого'.format(i)
    new_site['html']['body']['h2'] = 'У нас самая низкая цена на {0}'.format(i)
    print(i)
    print(new_site)
'''

# зачтено
