from chimerax.core.commands import run
import numpy as np
work_directory = np.loadtxt("path.txt")
work_directory = str(work_directory)
print(work_directory)

command1 = "measure sasa /*"
run(session, command1)