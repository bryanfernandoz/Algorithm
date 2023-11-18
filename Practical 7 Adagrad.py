from math import sqrt
from numpy import asarray
from numpy.random import rand
from numpy.random import seed
from numpy import arange
from numpy import meshgrid
from matplotlib import pyplot
from numpy import asarray

def objective(x,y):
    return x**2.0 + y**2.0

r_min, r_max = -1.0, 1.0
xaxis =arange(r_min, r_max, 0.1)
yaxis =arange(r_min, r_max, 0.1)
x,y = meshgrid(xaxis, yaxis)
results = objective(x,y)
figure = pyplot.figure()
axis = figure.gca(projection='3d')
axis.plot_surface(x,y, results, cmap='jet')
pyplot.show()

bounds = asarray([[-1.0, 1.0], [-1.0,1.0]])
xaxis = arange(bounds[0,0], bounds[0,1], 0.1)
yaxis = arange(bounds[1,0], bounds[1,1], 0.1)

x,y = meshgrid(xaxis, yaxis)
results = objective(x,y)
pyplot.contourf(x,y, results, levels=50, cmap ='jet')
pyplot.show()

def derivative(x,y):
    return asarray([x * 2.0, y * 2.0])

solution = bounds[:,0] + rand(len(bounds)) * (bounds[:,1] - bounds[:,0])
sq_grad_sums = [0.0 for _ in range(bounds.shape[0])]

for it in range(n_iter):
    gradient = derivative(solution[0], solution[1])

for it in range(gradient.shape[0]):
    sq_grad_sums[i] +=gradient[i]**2.0

new_solution = list()

for i in range(solution.shape[0]):
    alpha = step_size / (1e-8 + sqrt(sq_grad_sums[i]))
    value = solution[i] - aplha * gradient[i]
    new_solution.append(value)

solution  = asarray(new_solution)
solution_eval = objective(solution[0], solution[1])
print('>%d f(%s) = %.5f' % (it, solution, solution_eval))

def adagrad(objective, derivativative, bounds, n_iter, step_size):
    solution = bounds[:,0] + rand(len(bounds)) * (bounds[:,1] - bounds[:,0])
    sq_grad_sum = [0.0 for _ in range(bounds.shape[0])]
    for it in range(n_iter):
        gradient = derivative(solution[0], solution[1])
        for i in range(gradient.shape[0]):
            sq_grad_sums[i] += gradient[i]**2.0
        new_solution = list()
        for i in range(solution.shape[0]):
            alpha = step_size / (1e-8 +sqrt(sq_grad_sums[i]))
            value = solution[i] - aplha * gradient[i]
            new_solution.append(value)
        solution = asarray(new_solution)
        solution_eval = objective(solution[0], solution[1])
        print('>%d f(%s) = %.5f' % (it, solution, solution_eval))
    return[solution, solution_eval]

seed(1)
bounds = asarray([[-1.0, 1.0], [-1.0, 1.0]])
n_iter = 50
step_size = 0.1
best, score = adagrad(objective, derivative, bounds, n_iter, step_size)
print('Done!')
print('f(%s) = %f' % (best, score))
            

    
    


    
