import numpy as np

NUM_REQUEST = 100000
CACHE_SIZE = 50
GROUPS = 10
GROUP_SIZE = 500
NUM_PHASES = 5
PHASE_SIZE = 5000

class PhaseChangePlugin:
 def input(self, inputfile):
    pass
 def run(self):
    pass
 def output(self, outputfile):
    outfile = open(outputfile, 'w')
    phase_size = NUM_REQUEST / NUM_PHASES
    current_group = None
    
    workingSet = []
    eps = 0.0
    for i in range(0, NUM_PHASES) :
            
        current_group = np.random.randint(0, GROUPS)
        
        ## Create working set
        workingSet = []
        for j in range(0, GROUP_SIZE) :
            p = 2.0 * CACHE_SIZE / GROUP_SIZE
            if np.random.rand() < p :
                workingSet.append(j*current_group)
        ## Create a vertical line
        outfile.write(str(-1))
        outfile.write("\n")
        
        for _ in range(0, PHASE_SIZE) :
        
            if np.random.rand() < 1-eps :
                n = len(workingSet)
                q = workingSet[np.random.randint(0,n)]
            else:
                q = np.random.randint(0, GROUP_SIZE)*current_group
            outfile.write(str(q))
            outfile.write("\n")
    
#         print current_group
        
        
