import hashlib
import math


def function_f(x, y, z):
    return (x & y) | (~x & z)


def function_g(x, y, z):
    return (x & z) | (~z & y)


def function_h(x, y, z):
    return x ^ y ^ z


def function_i(x, y, z):
    return y ^ (~z | x)


def rotate_left(x, n):
    x &= 0xFFFFFFFF
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF


def table_constants():
    return [int(2**32 * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]


def splitting_flow(flow):
    return [flow[i:i+4] for i in range(0, 64, 4)]


def step_1(flow):
    len_ = (8 * len(flow)) & 0xffffffffffffffff
    flow.append(0x80)
    while len(flow) % 64 != 56:
        flow.append(0x00)
    return flow, len_


def step_2(flow, len_):
    return flow + len_.to_bytes(8, byteorder='little')


def step_3():
    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476
    return A, B, C, D


def step_4(flow, init):
    A, B, C, D = init
    t = table_constants()
    n = int(len(flow) // 64)
    flow = splitting_flow(flow)
    for i in range(0, n):
        AA, BB, CC, DD = A, B, C, D

        # Round 1
        A = (B + rotate_left((A + function_f(B, C, D) + int.from_bytes(flow[0], 'little') + t[0]), 7)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_f(A, B, C) + int.from_bytes(flow[1], 'little') + t[1]), 12)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_f(D, A, B) + int.from_bytes(flow[2], 'little') + t[2]), 17)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_f(C, D, A) + int.from_bytes(flow[3], 'little') + t[3]), 22)) & 0xFFFFFFFF

        A = (B + rotate_left((A + function_f(B, C, D) + int.from_bytes(flow[4], 'little') + t[4]), 7)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_f(A, B, C) + int.from_bytes(flow[5], 'little') + t[5]), 12)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_f(D, A, B) + int.from_bytes(flow[6], 'little') + t[6]), 17)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_f(C, D, A) + int.from_bytes(flow[7], 'little') + t[7]), 22)) & 0xFFFFFFFF

        A = (B + rotate_left((A + function_f(B, C, D) + int.from_bytes(flow[8], 'little') + t[8]), 7)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_f(A, B, C) + int.from_bytes(flow[9], 'little') + t[9]), 12)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_f(D, A, B) + int.from_bytes(flow[10], 'little') + t[10]), 17)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_f(C, D, A) + int.from_bytes(flow[11], 'little') + t[11]), 22)) & 0xFFFFFFFF

        A = (B + rotate_left((A + function_f(B, C, D) + int.from_bytes(flow[12], 'little') + t[12]), 7)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_f(A, B, C) + int.from_bytes(flow[13], 'little') + t[13]), 12)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_f(D, A, B) + int.from_bytes(flow[14], 'little') + t[14]), 17)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_f(C, D, A) + int.from_bytes(flow[15], 'little') + t[15]), 22)) & 0xFFFFFFFF

        # Round 2
        A = (B + rotate_left((A + function_g(B, C, D) + int.from_bytes(flow[1], 'little') + t[16]), 5)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_g(A, B, C) + int.from_bytes(flow[6], 'little') + t[17]), 9)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_g(D, A, B) + int.from_bytes(flow[11], 'little') + t[18]), 14)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_g(C, D, A) + int.from_bytes(flow[0], 'little') + t[19]), 20)) & 0xFFFFFFFF

        A = (B + rotate_left((A + function_g(B, C, D) + int.from_bytes(flow[5], 'little') + t[20]), 5)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_g(A, B, C) + int.from_bytes(flow[10], 'little') + t[21]), 9)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_g(D, A, B) + int.from_bytes(flow[15], 'little') + t[22]), 14)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_g(C, D, A) + int.from_bytes(flow[4], 'little') + t[23]), 20)) & 0xFFFFFFFF

        A = (B + rotate_left((A + function_g(B, C, D) + int.from_bytes(flow[9], 'little') + t[24]), 5)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_g(A, B, C) + int.from_bytes(flow[14], 'little') + t[25]), 9)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_g(D, A, B) + int.from_bytes(flow[3], 'little') + t[26]), 14)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_g(C, D, A) + int.from_bytes(flow[8], 'little') + t[27]), 20)) & 0xFFFFFFFF

        A = (B + rotate_left((A + function_g(B, C, D) + int.from_bytes(flow[13], 'little') + t[28]), 5)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_g(A, B, C) + int.from_bytes(flow[2], 'little') + t[29]), 9)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_g(D, A, B) + int.from_bytes(flow[7], 'little') + t[30]), 14)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_g(C, D, A) + int.from_bytes(flow[12], 'little') + t[31]), 20)) & 0xFFFFFFFF

        # Round 3
        A = (B + rotate_left((A + function_h(B, C, D) + int.from_bytes(flow[5], 'little') + t[32]), 4)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_h(A, B, C) + int.from_bytes(flow[8], 'little') + t[33]), 11)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_h(D, A, B) + int.from_bytes(flow[11], 'little') + t[34]), 16)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_h(C, D, A) + int.from_bytes(flow[14], 'little') + t[35]), 23)) & 0xFFFFFFFF

        A = (B + rotate_left((A + function_h(B, C, D) + int.from_bytes(flow[1], 'little') + t[36]), 4)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_h(A, B, C) + int.from_bytes(flow[4], 'little') + t[37]), 11)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_h(D, A, B) + int.from_bytes(flow[7], 'little') + t[38]), 16)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_h(C, D, A) + int.from_bytes(flow[10], 'little') + t[39]), 23)) & 0xFFFFFFFF

        A = (B + rotate_left((A + function_h(B, C, D) + int.from_bytes(flow[13], 'little') + t[40]), 4)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_h(A, B, C) + int.from_bytes(flow[0], 'little') + t[41]), 11)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_h(D, A, B) + int.from_bytes(flow[3], 'little') + t[42]), 16)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_h(C, D, A) + int.from_bytes(flow[6], 'little') + t[43]), 23)) & 0xFFFFFFFF

        A = (B + rotate_left((A + function_h(B, C, D) + int.from_bytes(flow[9], 'little') + t[44]), 4)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_h(A, B, C) + int.from_bytes(flow[12], 'little') + t[45]), 11)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_h(D, A, B) + int.from_bytes(flow[15], 'little') + t[46]), 16)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_h(C, D, A) + int.from_bytes(flow[2], 'little') + t[47]), 23)) & 0xFFFFFFFF

        # Round 4
        A = (B + rotate_left((A + function_i(B, C, D) + int.from_bytes(flow[0], 'little') + t[48]), 6)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_i(A, B, C) + int.from_bytes(flow[7], 'little') + t[49]), 10)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_i(D, A, B) + int.from_bytes(flow[14], 'little') + t[50]), 15)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_i(C, D, A) + int.from_bytes(flow[5], 'little') + t[51]), 21)) & 0xFFFFFFFF

        A = (B + rotate_left((A + function_i(B, C, D) + int.from_bytes(flow[12], 'little') + t[52]), 6)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_i(A, B, C) + int.from_bytes(flow[3], 'little') + t[53]), 10)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_i(D, A, B) + int.from_bytes(flow[10], 'little') + t[54]), 15)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_i(C, D, A) + int.from_bytes(flow[1], 'little') + t[55]), 21)) & 0xFFFFFFFF

        A = (B + rotate_left((A + function_i(B, C, D) + int.from_bytes(flow[8], 'little') + t[56]), 6)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_i(A, B, C) + int.from_bytes(flow[15], 'little') + t[57]), 10)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_i(D, A, B) + int.from_bytes(flow[6], 'little') + t[58]), 15)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_i(C, D, A) + int.from_bytes(flow[13], 'little') + t[59]), 21)) & 0xFFFFFFFF

        A = (B + rotate_left((A + function_i(B, C, D) + int.from_bytes(flow[4], 'little') + t[60]), 6)) & 0xFFFFFFFF
        D = (A + rotate_left((D + function_i(A, B, C) + int.from_bytes(flow[11], 'little') + t[61]), 10)) & 0xFFFFFFFF
        C = (D + rotate_left((C + function_i(D, A, B) + int.from_bytes(flow[2], 'little') + t[62]), 15)) & 0xFFFFFFFF
        B = (C + rotate_left((B + function_i(C, D, A) + int.from_bytes(flow[9], 'little') + t[63]), 21)) & 0xFFFFFFFF

        A += AA
        B += BB
        C += CC
        D += DD

        A &= 0xFFFFFFFF
        B &= 0xFFFFFFFF
        C &= 0xFFFFFFFF
        D &= 0xFFFFFFFF

    buf_hash = [A, B, C, D]
    return sum(x << (32 * i) for i, x in enumerate(buf_hash))


def step_5(buf_hash):
    hash_ = buf_hash.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(hash_, byteorder='big'))


def md5(word: str):
    word = bytearray(word, encoding='ASCII')
    flow, len_ = step_1(word)
    flow = step_2(flow, len_)
    init = step_3()
    buf = step_4(flow, init)
    hash_md5 = step_5(buf)
    return hash_md5


def true_md5(word: str):
    word = bytearray(word, encoding='ASCII')
    return hashlib.md5(word).hexdigest()


if __name__ == '__main__':
    dataset = [
        'Cat', 'd0g', 'message digest', 'pick', 'terrain', 'heavy bag', 'linen',
        'junk', 'root', 'albatross', 'geology', 'seaweed', 'detachment', 'dawn',
        'fraction', 'faith', 'suffer', 'classic', 'hundred', 'league', 'compound',
        'association', 'pier', 'sheriff', 'crazy', 'nearby', 'thrombosis', 'hell',
        'This is a very, very, very, very long message!'
    ]
    for i in dataset:
        my = md5(i)
        res = true_md5(i)
        if len(i) > 16:
            print('{:>16}'.format(i[:13] + '...'), f' =>  {my}  ==  {res}  =>  {my == res}')
        else:
            print('{:>16}'.format(i), f' =>  {my}  ==  {res}  =>  {my == res}')
