__author__ = 'Myroslav'

def append_date(d1,d2):
    day = [c + 1 for c in range(31)]
    mon = [c + 1 for c in range(12)]
    yer = [c + 1 for c in range(99)]
    exc = 'Помилка вводу'
    mass = []
    mass.append(d1)

    zero = '0'
    i = int(mass[-1][-2:]) - 1
    j = int(mass[-1][-4:-2]) - 1
    z = int(mass[-1][2:4])
    while(mass[-1] != d2):
        if mass[-1][2:4] == d2[2:4]:
            while mass[-1][-4:-2] != d2[-4:-2]:
                if mass[-1][-4:-2] < d2[-4:-2]:
                    while mass[-1][-2:] != '31':
                        if mass[-1][-2:-1] == '0':
                            zero = '0'
                        else:
                            zero = ''
                        mass.append('{0}{1}{2}{3}'.format(mass[-1][:4], mass[-1][-4:-2], zero, str(day[i] + 1)))
                        i += 1
                        if len(mass[-1]) == 9:
                            new = mass[-1][:6] + mass[-1][7:]
                            mass[-1] = new
                    i = 0
                elif mass[-1][-2:] < d2[-2:]:
                    return exc
                    break

                else:
                    while mass[-1][-2:] != '31':
                        if mass[-1][-2:-1] == '0':
                            zero = '0'
                        else:
                            zero = ''
                        mass.append('{0}{1}{2}{3}'.format(mass[-1][:4], mass[-1][-4:-2], zero, str(day[i] + 1)))
                        i += 1
                        if len(mass[-1]) == 9:
                            new = mass[-1][:6] + mass[-1][7:]
                            mass[-1] = new
                if mass[-1][-4:-3] == '0':
                    zero = '0'
                else:
                    zero = ''
                mass.append('{0}{1}{2}'.format(mass[-1][:4], '{0}{1}'.format(zero, str(mon[j] + 1)), '01'))
                if len(mass[-1]) == 9:
                    new = mass[-1][:4] + mass[-1][-4:]
                    mass[-1] = new
                j += 1
                i = 0
            if mass[-1][-4:-2] == d2[-4:-2]:
                while mass[-1][-2:] != d2[-2:]:
                    if mass[-1][-2:-1] == '0':
                        zero = '0'
                    else:
                        zero = ''
                    mass.append('{0}{1}{2}{3}'.format(mass[-1][:4], mass[-1][-4:-2], zero, str(day[i] + 1)))
                    i += 1
                    if len(mass[-1]) == 9:
                        new = mass[-1][:6] + mass[-1][7:]
                        mass[-1] = new
        else:
            if mass[-1][:4] > d2[:4]:
                return exc
                break

            else:
                while mass[-1][-4:-2] != '12':
                    if mass[-1][-4:-2] < d2[-4:-2]:
                        while mass[-1][-2:] != '31':
                            if mass[-1][-2:-1] == '0':
                                zero = '0'
                            else:
                                zero = ''
                            mass.append('{0}{1}{2}{3}'.format(mass[-1][:4], mass[-1][-4:-2], zero, str(day[i] + 1)))
                            i += 1
                            if len(mass[-1]) == 9:
                                new = mass[-1][:6] + mass[-1][7:]
                                mass[-1] = new
                        i = 0
                    else:
                        while mass[-1][-2:] != '31':
                            if mass[-1][-2:-1] == '0':
                                zero = '0'
                            else:
                                zero = ''
                            mass.append('{0}{1}{2}{3}'.format(mass[-1][:4], mass[-1][-4:-2], zero, str(day[i] + 1)))
                            i += 1
                            if len(mass[-1]) == 9:
                                new = mass[-1][:6] + mass[-1][7:]
                                mass[-1] = new
                    if mass[-1][-4:-3] == '0':
                        zero = '0'
                    else:
                        zero = ''
                    mass.append('{0}{1}{2}'.format(mass[-1][:4], '{0}{1}'.format(zero, str(mon[j] + 1)), '01'))
                    if len(mass[-1]) == 9:
                        new = mass[-1][:4] + mass[-1][-4:]
                        mass[-1] = new
                    j += 1
                    i = 0
                if mass[-1][-4:-2] == '12':
                    while mass[-1][-2:] != '31':
                        if mass[-1][-2:-1] == '0':
                            zero = '0'
                        else:
                            zero = ''
                        mass.append('{0}{1}{2}{3}'.format(mass[-1][:4], mass[-1][-4:-2], zero, str(day[i] + 1)))
                        i += 1
                        if len(mass[-1]) == 9:
                            new = mass[-1][:6] + mass[-1][7:]
                            mass[-1] = new
            j = 0
            i = 0
            z +=1
            mass.append('20{0}{1}'.format(str(z),'0101'))
            print(mass[-1])
    return mass
    # print(len(mass))
    # print(mass)
if __name__ == '__main__':
    n =append_date('20101010','20101020')
    print(n)
    print(len(n))
    # day = [c + 1 for c in range(31)]
    # mon = ["01","02","03","04","05","06","07","08","09","10","11","12",]
    # day= ["01","02","03","04","05","06","07","08","09","10","11","12",'13','14','15']
    # m = []
    # for i in range(len(mon)):
    #     for j in range(len(day)):
    #         m.append('2017{0}{1}'.format(mon[i],day[j]))
    # print(len(m))
    # print(m)
    # l= [append_date(m[i],m[-1]) for i in range(len(m)-1)]
    # print(len(l))
    # print(l)
    #append_date(d1 = '20191101',d2 = '20191231')



