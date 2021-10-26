# -*- coding: utf-8 -*-
# @Time    : 2020-10-26 21:31:02
# @Author  : lilin
# @File    : signal_analyse.py
# @Software: Pycharm

import numpy as np
from scipy.stats import norm
import scipy.signal as signal
from scipy.fftpack import fft, ifft, fftfreq, hilbert
import pywt


class SignalFeatures(object):

    def __init__(self, x, fs):
        self.x = x.astype(np.float)
        self.fs = fs
        self.length = x.shape[0]
        self.algo_sets = {
            "时域波形": self.shiyuboxing,
            "时间轴": self.timeaxis,
            # ------------时域指标------------
            "均值": self.junzhi,
            "均方值": self.junfangzhi,
            "均方根值": self.junfanggenzhi,
            "峰值": self.fengzhi,
            "峰峰值": self.fengfengzhi,
            "最小值": self.zuixiaozhi,
            "最大值": self.zuidazhi,
            "标准差": self.biaozhuncha,
            "方差": self.fangcha,
            "平均幅值": self.pingjunfuzhi,
            "方根幅值": self.fanggenfuzhi,
            "偏斜度": self.pianxiedu,
            "峭度": self.qiaodu,
            "波形指标": self.boxingzhibiao,
            "脉冲指标": self.maichongzhibiao,
            "峰值指标": self.fengzhizhibiao,
            "裕度指标": self.yuduzhibiao,
            "峭度指标": self.qiaoduzhibiao,
            "偏斜度指标": self.pianxieduzhibiao,
            "K因子": self.kyinzi,
            # ------------ 频域指标 ------------
            "谱能量": self.punengliang,
            "重心频率": self.zhongxinpinlv,
            "均方频率": self.junfangpinlv,
            "均方根频率": self.junfanggenpinlv,
            "谱方差": self.pufangcha,
            "谱二阶矩": self.puerjieju,
            "谱峭度": self.puqiaodu,
            "谱偏斜度": self.pupianxiedu,
            # ------------ 数据质量保障方法 --------------
            "张量分解": self.zhangliangfenjie,
            "KNN": self.knn,
            # ------------ 信号处理方法 --------------
            "概率密度函数": self.gailvmiduhanshu,
            "概率分布函数": self.gailvfenbuhanshu,
            "自相关函数": self.zixiangguanhanshu,
            "频谱": self.pinpu,
            "功率谱": self.gonglvpu,
            "倒频谱": self.daopinpu,
            "包络谱": self.baoluopu,
        }

    def timeaxis(self):
        return np.linspace(0, self.length/self.fs, self.length, endpoint=False)

    def shiyuboxing(self):
        return self.timeaxis(), self.x

    # -------------------------------------时域指标--------------------------------
    # 均值
    def junzhi(self):
        return np.mean(self.x, axis=0)

    # 均方值
    def junfangzhi(self):
        return np.mean(self.x ** 2, axis=0)

    # 有效值(均方根值)
    def junfanggenzhi(self):
        return np.sqrt(np.mean(self.x ** 2, axis=0))

    # 峰值
    def fengzhi(self):
        return np.max(np.abs(self.x), axis=0)

    # 峰峰值
    def fengfengzhi(self):
        return np.max(self.x, axis=0) - np.min(self.x, axis=0)

    # 最小值
    def zuixiaozhi(self):
        return np.min(self.x, axis=0)

    # 最大值
    def zuidazhi(self):
        return np.max(self.x, axis=0)

    # 标准差
    def biaozhuncha(self):
        return np.std(self.x, axis=0)

    # 方差
    def fangcha(self):
        return np.var(self.x, axis=0)

    # 平均幅值
    def pingjunfuzhi(self):
        return np.mean(np.abs(self.x), axis=0)

    # 方根幅值
    def fanggenfuzhi(self):
        return np.square(np.mean(np.sqrt(np.abs(self.x)), axis=0))

    # 偏斜度
    def pianxiedu(self):
        return np.mean((self.x - np.mean(self.x, axis=0)) ** 3)

    # 峭度
    def qiaodu(self):
        return np.mean((self.x - np.mean(self.x, axis=0)) ** 4)

    # 波形指标
    def boxingzhibiao(self):
        return self.junfanggenzhi() / self.pingjunfuzhi()

    # 脉冲指标
    def maichongzhibiao(self):
        return self.fengzhi() / self.pingjunfuzhi()

    # 峰值指标
    def fengzhizhibiao(self):
        return self.fengzhi() / self.junfanggenzhi()

    # 裕度指标
    def yuduzhibiao(self):
        return self.fengzhi() / self.fanggenfuzhi()

    # 峭度指标
    def qiaoduzhibiao(self):
        return np.mean((self.x - np.mean(self.x, axis=0)) ** 4) / np.std(self.x, axis=0) ** 4

    # 偏斜度指标
    def pianxieduzhibiao(self):
        return np.mean((self.x - np.mean(self.x, axis=0)) ** 3) / np.std(self.x, axis=0) ** 3

    # K因子
    def kyinzi(self):
        return self.junfanggenzhi() * self.fengzhi()

    # -------------------------------------频域指标--------------------------------
    def sk(self, x):
        # 写法1
        # datalen = self.x.shape[0]
        # y = self.x - np.mean(self.x, axis=0)
        # y = fft(y, axis=0)
        # y = np.abs(y)
        # y = 2.0 / datalen * y[:int(datalen / 2)]
        # return y
        # 写法2
        y = x - np.mean(x, axis=0)
        y = fft(y, axis=0)[:x.shape[0]//2]
        y = np.abs(y) / x.shape[0] * 2.
        return y

    def fk(self, x):
        # 写法1
        # datalen = self.x.shape[0]
        # f = np.arange(0, datalen) * self.fs / datalen
        # f = f[:int(datalen / 2)]
        # f = f.reshape((int(datalen / 2), 1))
        # return f[:, 0]
        # 写法2
        return fftfreq(x.shape[0], 1/self.fs)[:x.shape[0]//2]
#         return np.linspace(0, x.shape[0]//2, x.shape[0])

    # 频谱
    def pinpu(self):
        return self.fk(self.x), self.sk(self.x)

    # 谱能量
    def punengliang(self):
        return np.mean(self.sk(self.x), axis=0)

    # 重心频率
    def zhongxinpinlv(self):
        return np.mean(np.multiply(self.sk(self.x), self.fk(self.x)), axis=0)

    # 均方频率
    def junfangpinlv(self):
        return np.mean(np.square(self.sk(self.x)), axis=0)

    # 均方根频率
    def junfanggenpinlv(self):
        return np.sqrt(self.junfangpinlv())

    # 谱方差
    def pufangcha(self):
        return np.var(self.sk(self.x), axis=0)

    # 谱二阶矩
    def puerjieju(self):
        return np.sum(np.multiply(np.square(self.fk(self.x)), self.sk(self.x))) / np.sum(self.sk(self.x))

    # 谱峭度
    def puqiaodu(self):
        return np.mean(np.power((self.sk(self.x) - self.punengliang()), 4), axis=0) / np.square(self.pufangcha())

    # 谱偏斜度
    def pupianxiedu(self):
        return np.mean(np.power((self.sk(self.x) - self.punengliang()), 3), axis=0) / np.power(np.sqrt(self.pufangcha()), 3)

    # ------------------------ 数据质量保障方法 --------------------------

    # 张量分解
    def zhangliangfenjie(self):
        return 0
    # KNN
    def knn(self):
        return 0

    # -------------------------- 信号处理方法 ----------------------------
    # 概率密度函数
    def gailvmiduhanshu(self):
        x_data = self.x[np.argsort(self.x)]
        y_data = norm.pdf(x_data, loc=self.junzhi(), scale=self.biaozhuncha())
        return x_data, y_data

    # 概率分布函数
    def gailvfenbuhanshu(self):
        x_data = self.x[np.argsort(self.x)]
        y_data = norm.cdf(x_data, loc=self.junzhi(), scale=self.biaozhuncha())
        return x_data, y_data

    # 自相关函数
    def zixiangguanhanshu(self):
        x_data = np.linspace(-(self.length-1), (self.length-1), 2*self.length-1) / self.fs
        y_data = signal.fftconvolve(self.x, self.x[::-1], mode='full')
        return x_data, y_data

    # 功率谱
    def gonglvpu(self, method="welch", **kwds):
        if method=="welch":
            return signal.welch(self.x, self.fs, **kwds)
        elif method=="bt":
            y_data = self.sk(self.zixiangguanhanshu()[1])
            x_data = self.fk(y_data)
            return x_data, y_data
        else:
            return signal.periodogram(self.x, self.fs, **kwds)

    # 倒频谱
    def daopinpu(self):
        x_data = np.linspace(0, self.length, self.length, endpoint=False)
        y_data = np.real(ifft(np.log(np.abs(fft(self.x)))))
        return x_data, np.abs(y_data)

    # 包络谱
    def baoluopu(self):
        x_data = self.fk(self.x)
        y_data = self.sk(np.abs(self.x + hilbert(self.x)*1j))
        return x_data, y_data

    # ---------------------- 其余信号处理方法，由于通用性较差，仅在此给出使用示例 ---------------------
    # 短时傅里叶变换时频图
    def shipintu_stft(self, **kwds):
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.stft.html#scipy.signal.stft
        f, t, Zxx = signal.stft(self.x, fs=self.fs, **kwds)
        return t, f, np.abs(Zxx.T)

    # 功率谱时频图
    def shipintu_spectrogram(self, **kwds):
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.spectrogram.html#scipy.signal.spectrogram
        f, t, Zxx = signal.spectrogram(self.x, fs=self.fs, **kwds)
        return t, f, np.abs(Zxx.T)

    # 连续小波分解时频图
    def shipintu_cwt(self, wavelet="cgau8", totalscale=256):
        # https://blog.csdn.net/zhoudapeng01/article/details/107025901/
        # https://blog.csdn.net/weixin_42943114/article/details/89603208
        fc = pywt.central_frequency(wavelet)  # 中心频率
        cparam = 2 * fc * totalscale
        scales = cparam/np.arange(totalscale, 1, -1)
        Zxx, f = pywt.cwt(self.x, scales=scales, wavelet=wavelet, sampling_period=1./self.fs)  # 连续小波变换
        t = self.timeaxis()
        return t, f, np.abs(Zxx.T)

    # 小波包分解
    def wavepackage(self, wavelet='db1', mode='symmetric', maxlevel=3, need_energy=False, **kwds):
        # https://blog.csdn.net/zds13257177985/article/details/102896041?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-1-102896041.nonecase&utm_term=python%20%E5%B0%8F%E6%B3%A2%E5%8C%85%E8%83%BD%E9%87%8F%E7%86%B5&spm=1000.2123.3001.4430
        wp = pywt.WaveletPacket(data=self.x, wavelet=wavelet, mode=mode, maxlevel=maxlevel, **kwds)
        tree = {}
        for row in range(1, maxlevel+1):
            for i in [node.path for node in wp.get_level(row, 'freq')]:
                tree[i] = wp[i].data
        f = np.linspace(0, self.length//2, 2**maxlevel, endpoint=False)  # 表示每个区间开始的频率
        if need_energy:
            last_level = list(tree.values())[-2**maxlevel:]
            energy = [np.power(np.linalg.norm(item, ord=None), 2) for item in last_level]
            return f, energy
        return f, tree

    # 多阶离散小波分解
    def wavedec(self, **kwds):
        coef = pywt.wavedec(self.x, **kwds)
        return coef