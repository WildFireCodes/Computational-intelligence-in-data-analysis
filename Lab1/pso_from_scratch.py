import numpy as np

class ParticleSwarmOptimization:
    def __init__(self, spawn = [-5, 5], damping = 0.7298, social_tendency = 2.05, individualistic_tendency = 2.05):
        self.spawn = spawn
        self.damping = damping
        self.social_tendency = social_tendency
        self.individualistic_tendency = individualistic_tendency

        self.update_functions_options = {'bare_bones': self.bare_bones, 
                                        'canonical_pso': self.canonical_pso,
                                        'gauss_pso': self.gauss_pso}

    def create_population(self, n_dims, birds_num = 16):
        return np.random.uniform(self.spawn[0], self.spawn[1], size = (birds_num, n_dims)) #for _ in range(n_dims) for _ in range(birds_num)]).reshape(-1, n_dims)

    def bare_bones(self, pop_i, best_pop):
        return np.random.normal((pop_i + best_pop)/2, np.abs(pop_i - best_pop)) #mean, sigma

    def canonical_pso(self, pop_i, best_pop, prev_pop, velocity):
        '''vi - velocity, pi - prev_pop, xi - pop_i, pg - best_pop'''

        velocity = self.damping * (velocity + 
                                np.random.uniform(0, self.individualistic_tendency) * (prev_pop - pop_i) + 
                                np.random.uniform(0, self.social_tendency) * (best_pop - pop_i))

        return velocity + pop_i

    def gauss_pso():
        pass

    def pso_engine(self, function, n_dims = 2, birds_num = 16, n_iters = 300, option = 'bare_bones'):
        bird_pop = self.create_population(n_dims, birds_num)
        update_function = self.update_functions_options[option]

        if(option == 'bare_bones'):
            return self.bare_bones_loop(bird_pop, function, n_iters, update_function)
        
        return self.canonical_loop_pso(bird_pop, function, n_dims, birds_num, n_iters, update_function)

    def canonical_loop_pso(self, bird_pop, function, n_dims, birds_num, n_iters, update_function):
        velocity = np.zeros((birds_num, n_dims))
        prev_pop = bird_pop/3

        for i in range(n_iters):
            bird_pop_score = np.apply_along_axis(function, 1, bird_pop)

            best_bird = bird_pop[np.argmin(bird_pop_score)]
            best_val_bird = function(best_bird)

            next_bird_pop = update_function(bird_pop, best_bird, prev_pop, velocity)
            next_bird_pop_score = np.apply_along_axis(function, 1, next_bird_pop)

            velocity = next_bird_pop - bird_pop
            prev_pop = bird_pop
                
            filtered_array =  bird_pop_score > next_bird_pop_score
            bird_pop[filtered_array] = next_bird_pop[filtered_array]

            if np.std(next_bird_pop) < 0.01:
                break
        
        return best_bird, best_val_bird, i

    def bare_bones_loop(self, bird_pop, function, n_iters, update_function):
        for i in range(n_iters):
            bird_pop_score = np.apply_along_axis(function, 1, bird_pop)

            best_bird = bird_pop[np.argmin(bird_pop_score)]
            best_val_bird = function(best_bird)

            next_bird_pop = update_function(bird_pop, best_bird)  
            next_bird_pop_score = np.apply_along_axis(function, 1, next_bird_pop)
                
            filtered_array =  bird_pop_score > next_bird_pop_score #filtering array to get [True False] vector and swap for better bird
            bird_pop[filtered_array] = next_bird_pop[filtered_array]

            if np.std(next_bird_pop) < 0.01: #checking if std betweend new bird population is less than 0.01 - if true than stop algorithm
                break
        
        return best_bird, best_val_bird, i