import torch
import random

checkpoint = torch.load('test.pth')  # pth 파일에서 가중치 불러오기

for x in range(len(checkpoint['weight']['enc_p.emb_phone.weight'][0])):
    checkpoint['weight']['enc_p.emb_phone.weight'][0][x] *= random.uniform(1.2, 0.8) * random.choice([-1, 1]))

    for x in range(len(checkpoint['weight']['enc_p.emb_phone.bias'])):
        checkpoint['weight']['enc_p.emb_phone.bias'][x] *= random.uniform(1.2, 0.8)

    for y in range(len(checkpoint['weight']['enc_p.proj.weight'])):  # weight 계열 특성값 변환 예시
        for
    x in range(len(checkpoint['weight']['enc_p.proj.weight'][y])):
    checkpoint['weight']['enc_p.proj.weight'][y][x] *= (random.uniform(1.2, 0.8) * random.choice([-1, 1]))

    for x in range(len(checkpoint['weight']['enc_p.proj.bias'])):  # bias 계열 특성값 변환 예시
        checkpoint['weight']['enc_p.proj.bias'][x] *= random.uniform(1.2, 0.8)

    for z in range(len(checkpoint['weight']['dec.conv_pre.weight'])):
        for
    y in range(len(checkpoint['weight']['dec.conv_pre.weight'][z])):
    for x in range(len(checkpoint['weight']['dec.conv_pre.weight'][z][y])):
        checkpoint['weight']['dec.conv_pre.weight'][z][y][x] *= (random.uniform(1.2, 0.8) * random.choice([-1, 1]))

    for x in range(len(checkpoint['weight']['dec.conv_pre.bias'])):
        checkpoint['weight']['dec.conv_pre.bias'][x] *= (random.uniform(1.2, 0.8) * random.choice([-1, 1]))

    for x in range(len(checkpoint['weight']['emb_g.weight'][0])):
        checkpoint['weight']['emb_g.weight'][0][x] = random.uniform(0, 1.2) ** 2 * random.choice([-1, 1])

    for y in range(len(checkpoint['weight']['dec.conv_post.weight'])):
        for
    x in range(len(checkpoint['weight']['dec.conv_post.weight'][y])):
    checkpoint['weight']['dec.conv_post.weight'][y][x] *= random.uniform(1.2, 0.8)

    for y in range(len(checkpoint['weight']['dec.cond.weight'])):
        for
    x in range(len(checkpoint['weight']['dec.cond.weight'][y])):
    checkpoint['weight']['dec.cond.weight'][y][x][0] *= random.uniform(1.2, 0.8)

    for x in range(len(checkpoint['weight']['dec.cond.bias'])):
        checkpoint['weight']['dec.cond.bias'][x] *= (random.uniform(1.2, 0.8) * random.choice([-1, 1]))

    for z in range(12):
        for
    x in range(len(checkpoint['weight'][f'dec.resblocks.{z}.convs1.0.bias'])):
    checkpoint['weight'][f'dec.resblocks.{z}.convs1.0.bias'][x] *= random.uniform(1.2, 0.8)

    x = 2
    PATH = f'test{x}.pth'
    torch.save(checkpoint, PATH)