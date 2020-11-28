from read_binary_relations import *
from binary_relation import *
from neiman_morgenshtern_optimization import *
from k_optimization import *


if __name__ == '__main__':
    binary_relations = read_from_file("variant_15.txt")
    for binary_relation in binary_relations:
        acyclic = binary_relation.is_acyclic()
        if not acyclic:
            print(binary_relation.name, "is not acyclic")
            find_all_k_opt_solutions(binary_relation.matrix)
        else:
            print(binary_relation.name, "is acyclic")
            find_neiman_morgenshtern_solution(binary_relation.matrix)

