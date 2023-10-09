# 二维码生成器
# 二维码的本质就是一段字符串
# 我们可以把任意的字符串，制作成一个二维码图片
# 生活中使用的二维码更多的是一个URL（网址）
# 这里我们使用第三方库（qrcode）

import qrcode

img = qrcode.make('haha!')
img.save('qrcode.png')
