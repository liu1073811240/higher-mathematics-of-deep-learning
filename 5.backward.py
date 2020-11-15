import torch


x = torch.tensor(torch.ones(2, 2, 2), requires_grad=True)
print(x)
print(torch.ones(2, 2, 2))

x = torch.nn.Parameter(torch.ones(2, 2, 2), requires_grad=True)
print(x)

"""
dg/dx = dg/dz * dz/dy * dy/dx
"""
y = x + 2
z = y ** 2
g = z.mean()
g.backward()
print(x.grad)



