# RSA-Crack
RSA密码算法是使用最为广泛的公钥密码体制。该体制简单且易于实现，只需要选择5个参数即可（两个素数𝑝和𝑞 、 模数𝑁 = 𝑝𝑞 、 加密指数𝑒和解密
指数𝑑）。设𝑚为待加密消息，RSA 体制破译相当于已知𝑚𝑒 mod 𝑁，能否还原𝑚的数论问题。目前模数规模为 1024 比特的RSA 算法一般情况下是安全
的，但是如果参数选取不当，同样存在被破译的可能。