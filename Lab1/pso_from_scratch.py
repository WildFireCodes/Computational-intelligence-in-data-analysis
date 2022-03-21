import numpy as np

class pso:
    def __init__(self, spawn_x = -5, spawn_y = 5, damping = 0.7298, social_tendency = None, individualistic_tendency = None):
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y
        self.damping = damping
        self.social_tendency = social_tendency
        self.individualistic_tendency = individualistic_tendency

        self.update_functions_options = {'bare bones': self.bare_bones, 
                                        'canonical pso': self.canonical_pso,
                                        'gauss pso': self.gauss_pso}

    def create_population(self, n_dims, birds_num = 16):
        return np.random.uniform(self.spawn_x, self.spawn_y, size = (birds_num, n_dims)) #for _ in range(n_dims) for _ in range(birds_num)]).reshape(-1, n_dims)

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

    def pso_engine(self, function, n_dims = 2, birds_num = 16, n_iters = 300, option = 'bare bones'):
        bird_pop = self.create_population(n_dims, birds_num)

        # tworze populacje -> wyniki dla populacji -> wartosc minimalna -> nowa populacja z nowymi wynikami -> czy sie przesuwa 
        for i in range(n_iters):
            bird_pop_score = np.apply_along_axis(function, 1, bird_pop)
            best_bird = bird_pop[np.argmin(bird_pop_score)]
            best_val_bird = function(best_bird)

            next_bird_pop = self.update_functions_options[option](bird_pop, best_bird)
            # next_bird_pop = self.canonical_pso(bird_pop, best_bird, new_bird_pop, velocity)
            next_bird_pop_score = np.apply_along_axis(function, 1, next_bird_pop)

            #canonical pso
            velocity = next_bird_pop - bird_pop
                
            mask = next_bird_pop_score < bird_pop_score #zamiana tych lepszych
            bird_pop[mask] = next_bird_pop[mask]

            if np.std(next_bird_pop_score) < 0.001:
                break
        
        return best_bird, best_val_bird