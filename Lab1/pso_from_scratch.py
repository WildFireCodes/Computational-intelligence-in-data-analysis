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
        return np.array([np.random.uniform(self.spawn_x, self.spawn_y) for _ in range(n_dims) for _ in range(birds_num)]).reshape(-1, n_dims)

    def bare_bones(self, pop_i, best_pop):
        return np.random.normal((pop_i - best_pop)/2, np.abs(pop_i - best_pop)) #mean, sigma

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
        best_bird = bird_pop[int(np.random.uniform(0, birds_num))] # randomowy ptaszek - pierwszy najlepszy
        best_val = function(best_bird)

        for i in range(n_iters):
            score = np.apply_along_axis(function, 1, bird_pop)
            print(repr(score) + 'wynik')
            print('\n')
            best_idx = np.argsort(score)[0] # min
            print(repr(best_idx) + 'index')
            print('\n')
            best_bird = bird_pop[best_idx] # min
            best_val = function(best_bird)
            print(repr(best_val) + 'best val')
            print('\n')

            print(repr(i) +'. Best_bird:'+ repr(best_bird) +'best val:'+ repr(best_val))
            print('\n')
            next_bird_pop = self.update_functions_options[option](bird_pop, best_bird)
            print(repr(next_bird_pop) + 'nowa populacja')
            print('\n')
            next_score = np.apply_along_axis(function, 1, next_bird_pop)#.reshape(1, birds_num)
            print(repr(next_score) + 'nowy wynik')
            print('\n')
            print('\n')
            #mask = next_score < score #zamiana tych lepszych
            #bird_pop[mask] = next_bird_pop[mask]

            if np.std(next_score) < 0.001:
                print('STOP!')
                break
        
        return best_bird, best_val