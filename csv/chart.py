import matplotlib.pyplot as plt  # as .. sinonimo


def chart(label, value):
    fig, ax = plt.subplots()
    ax.bar(label, value)
    plt.savefig('bar.png')


def chart2(label, value):
    fig, ax = plt.subplots()
    ax.pie(value, labels=label)
    ax.axis('equal')
    plt.savefig('pie.png')


if __name__ == '__main__':
    label = ['a', 'b', 'c', 'd', 'e', 'f']
    value = [10, 40, 34, 44, 54, 60]
    chart(label, value)
    chart2(label, value)
