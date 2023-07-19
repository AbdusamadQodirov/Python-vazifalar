def get_full_name(ism, familiya, otasi = ''):
    if otasi:
        return f"{ism} {familiya} {otasi}".title()
    else:
        return f"{ism} {familiya}".title()
def get_perimetr(r, pi = 3.14):
    return 2* pi * r
def get_eng_kattasin_qaytar(a, b, c):
    return max(a, b, c)
def get_title_list(*args):
    return [i.title() for i in list(args)]
def get_juft_sonlarni(*args):
    return [i for i in list(args) if i % 2 == 0]
def get_fibonachchi(*args):
    args = list(args)
    args[0] = 1
    args[1] = 1
    j = 0
    for i in range(2, len(args)):
        if args[i] == args[i - 1] + args[i - 2]:
            j += 1
    if j == len(args) - 2:
        return True
    else:
        return False




