import addModule as a
import subModule as s
import mulModule as m
import divModule as d

if __name__ == '__main__':
    print(f'a.add(10, 20): {a.add(10, 20)}')
    print(f's.add(10, 20): {s.sub(10, 20)}')
    print(f'm.add(10, 20): {m.mul(10, 20)}')
    print(f'd.add(10, 20): {d.div(10, 20)}')

    print(f'__name__: {__name__}')