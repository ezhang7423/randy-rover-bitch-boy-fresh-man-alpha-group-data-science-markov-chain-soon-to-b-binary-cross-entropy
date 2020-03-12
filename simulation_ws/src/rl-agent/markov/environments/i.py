import os

cwd = "/home/ete/rover/simulation_ws/src/rl-agent/markov/environments"
version = "initial"
episode = 0
with open(os.path.join(cwd, "run.txt"), "r+") as fout:
    data = fout.read().splitlines()
run = int(data[1].split(" ")[1])


class test:
    def __init__(self):
        self.run = run

    def write(self):
        with open(os.path.join(cwd, "run.txt"), "r+") as fout:
            data = fout.read().splitlines()
            data[1] = "run " + str(self.run + 1)
            fout.seek(0)
            fout.write("\n".join(data))
            fout.truncate()
            print(data)
        os.mkdir(os.path.join(cwd, "outputs", version, str(episode), str(self.run)))
        run = self.run
        self.run += 1


tes = test()
tes.write()
