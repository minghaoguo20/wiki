## NeRF

[NeRF Medium](https://towardsdatascience.com/its-nerf-from-nothing-build-a-vanilla-nerf-with-pytorch-7846e4c45666)

NeRFs 依赖于一种古老而优雅的概念，称为光场或辐射场。

光场是描述光在三维空间中传输的函数。它描述了光线在空间中每个 x=(x, y, z) 坐标和每个方向 d 中移动的方向，可以用 θ 和 ϕ 角度或单位向量来描述。它们共同形成了一个 5D 特征空间，描述了 3D 场景中的光传输。

受到这种表示的启发，NeRF 尝试近似一个函数，将这个空间映射到由颜色 c=(R,G,B) 和密度 σ 组成的 4D 空间，您可以将其视为在这个 5D 坐标空间中光线被终止的可能性（例如被遮挡）的似然度。

因此，标准的 NeRF 是一个形式为 $F:(x,d) -> (c,σ)$ 的函数。

![nerf](https://www.researchgate.net/publication/348213072/figure/fig4/AS:976456033267712@1609816668013/NeTF-network-architecture-we-adopt-an-MLP-structure-analogous-to-the-one-used-in-NeRF.png)

![nerf](https://miro.medium.com/max/9999/1*q3fLvJFfoUdtVhsXeeTNXw.png)

[白話Neural Radiance Fields (NeRF): 類神經網路在View Synthesis的熱門新方向](https://medium.com/ai-blog-tw/%E7%99%BD%E8%A9%B1neural-radiance-fields-nerf-%E9%A1%9E%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF%E5%9C%A8view-synthesis%E7%9A%84%E7%86%B1%E9%96%80%E6%96%B0%E6%96%B9%E5%90%91-23be9411d399)