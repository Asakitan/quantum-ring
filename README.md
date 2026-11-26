# 量子环上的容错探测布点

**证明署名：** Chain.Ren · 独立研究 · [完整证明](quantum-ring-proof.md) · 版本日期：2026-11-26

[固定版本证明](https://github.com/Asakitan/quantum-ring/blob/proof-v1.0.0/quantum-ring-proof.md) · [GitHub Release 与公开时间](https://github.com/Asakitan/quantum-ring/releases/tag/proof-v1.0.0) · [引用信息](CITATION.cff)

在均匀最近邻量子环上，磁通是未知但静态的，探测采用固定间隔的二元投影测量。设环有 $N$ 个格点，$p$ 是 $N$ 的最小素因子，最多允许任意 $r$ 个已装探测点在运行前永久失效。

在无采样混叠的条件下，若要求对所有初态和磁通都以概率 1 最终探测到粒子，最少需要：

$$
m_*=\left\lceil\frac{p(r+1)}{p-1}\right\rceil.
$$

当 $m_*\le N$ 时，连续安装 $m_*$ 个探测点即可达到下界；否则无解。例如，同样允许一个探测点失效，12 点环至少需要 4 个探测点，11 点环只需 3 个。结论针对**最终**探测概率，不比较有限等待时间内哪种布点最快。

## 复核

在项目根目录运行（Python 3.9+，仅需标准库）：

~~~bash
python -B verify_quantum_ring.py
~~~

脚本用整数矩阵独立核验 3 至 10 点环的 2,032 个非空探测点集和 60 个环长与故障预算组合。任意环长的结论由正文中的解析证明给出。

[完整证明](quantum-ring-proof.md) · [项目状态](STATUS.md) · [MIT 许可证](LICENSE)
