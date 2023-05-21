## NeRF

[NeRF Medium](https://towardsdatascience.com/its-nerf-from-nothing-build-a-vanilla-nerf-with-pytorch-7846e4c45666)

NeRFs 依赖于一种古老而优雅的概念，称为光场或辐射场。

光场是描述光在三维空间中传输的函数。它描述了光线在空间中每个 x=(x, y, z) 坐标和每个方向 d 中移动的方向，可以用 θ 和 ϕ 角度或单位向量来描述。它们共同形成了一个 5D 特征空间，描述了 3D 场景中的光传输。

受到这种表示的启发，NeRF 尝试近似一个函数，将这个空间映射到由颜色 c=(R,G,B) 和密度 σ 组成的 4D 空间，您可以将其视为在这个 5D 坐标空间中光线被终止的可能性（例如被遮挡）的似然度。

因此，标准的 NeRF 是一个形式为 $F:(x,d) -> (c,σ)$ 的函数。

