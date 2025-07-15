class INS:

    def __init__(self,
                 T_lower, T_upper,
                 I_lower, I_upper,
                 F_lower, F_upper):

        assert 0 <= T_lower <= 1
        assert 0 <= T_upper <= 1
        assert 0 <= I_lower <= 1
        assert 0 <= I_upper <= 1
        assert 0 <= F_lower <= 1
        assert 0 <= F_upper <= 1
        assert T_lower <= T_upper
        assert I_lower <= I_upper
        assert F_lower <= F_upper
        assert 0 <= T_lower + I_lower + F_lower <= 3
        assert 0 <= T_upper + I_upper + F_upper <= 3

        self.T_lower = T_lower
        self.T_upper = T_upper
        self.I_lower = I_lower
        self.I_upper = I_upper
        self.F_lower = F_lower
        self.F_upper = F_upper


    def __str__(self):

        return (f"<[{self.T_lower}, {self.T_upper}],"
                f"[{self.I_lower},{self.I_upper}],"
                f"[{self.F_lower},{self.F_upper}]>")
    

class NS:

    def __init__(self,
                 truth,
                 indeterminacy,
                 falsehood):

        assert 0 <= truth <= 1
        assert 0 <= indeterminacy <= 1
        assert 0 <= falsehood <= 1
        assert 0 <= truth + indeterminacy + falsehood <= 3

        self.T = truth
        self.I = indeterminacy
        self.F = falsehood


    def __str__(self):

        return (f"<{self.T},"
                f"{self.I},"
                f"{self.F}>")
    

class NCN:

    def __init__(self, 
            T_lower, T_upper, 
            I_lower, I_upper, 
            F_lower, F_upper, 
            truth, 
            indeterminacy, 
            falsehood):

        self.ins = INS(T_lower, T_upper, I_lower, I_upper, F_lower, F_upper)
        self.ns = NS(truth, indeterminacy, falsehood)


    def __str__(self):

        return (f"({str(self.ins)}, "
               f"{str(self.ns)})")


    def p_union(self, other):

        return NCN(
            max(self.ins.T_lower, other.ins.T_lower),
            max(self.ins.T_upper, other.ins.T_upper),
            max(self.ins.I_lower, other.ins.I_lower),
            max(self.ins.I_upper, other.ins.I_upper),
            max(self.ins.F_lower, other.ins.F_lower),
            max(self.ins.F_upper, other.ins.F_upper),
            max(self.ns.T, other.ns.T),
            max(self.ns.I, other.ns.I),
            max(self.ns.F, other.ns.F)
        )


    def p_intersection(self, other):

        return NCN(
            min(self.ins.T_lower, other.ins.T_lower),
            min(self.ins.T_upper, other.ins.T_upper),
            min(self.ins.I_lower, other.ins.I_lower),
            min(self.ins.I_upper, other.ins.I_upper),
            min(self.ins.F_lower, other.ins.F_lower),
            min(self.ins.F_upper, other.ins.F_upper),
            min(self.ns.T, other.ns.T),
            min(self.ns.I, other.ns.I),
            min(self.ns.F, other.ns.F)
        )


    def r_union(self, other):

        return NCN(
            max(self.ins.T_lower, other.ins.T_lower),
            max(self.ins.T_upper, other.ins.T_upper),
            max(self.ins.I_lower, other.ins.I_lower),
            max(self.ins.I_upper, other.ins.I_upper),
            max(self.ins.F_lower, other.ins.F_lower),
            max(self.ins.F_upper, other.ins.F_upper),
            min(self.ns.T, other.ns.T),
            min(self.ns.I, other.ns.I),
            min(self.ns.F, other.ns.F)
        )


    def r_intersection(self, other):

        return NCN(
            min(self.ins.T_lower, other.ins.T_lower),
            min(self.ins.T_upper, other.ins.T_upper),
            min(self.ins.I_lower, other.ins.I_lower),
            min(self.ins.I_upper, other.ins.I_upper),
            min(self.ins.F_lower, other.ins.F_lower),
            min(self.ins.F_upper, other.ins.F_upper),
            max(self.ns.T, other.ns.T),
            max(self.ns.I, other.ns.I),
            max(self.ns.F, other.ns.F)
        )


    def complement(self):

        return NCN(
            round(1 - self.ins.T_upper, 2),
            round(1 - self.ins.T_lower, 2),
            round(1 - self.ins.I_upper, 2),
            round(1 - self.ins.I_lower, 2),
            round(1 - self.ins.F_upper, 2),
            round(1 - self.ins.F_lower, 2),
            round(1 - self.ns.T, 2),
            round(1 - self.ns.I, 2),
            round(1 - self.ns.F, 2)
        )


    def __eq__(self, other):

        return (
            self.ins.T_lower == other.ins.T_lower and
            self.ins.T_upper == other.ins.T_upper and
            self.ins.I_lower == other.ins.I_lower and
            self.ins.I_upper == other.ins.I_upper and
            self.ins.F_lower == other.ins.F_lower and
            self.ins.F_upper == other.ins.F_upper and
            self.ns.T == other.ns.T and
            self.ns.I == other.ns.I and
            self.ns.F == other.ns.F
        )


    def __add__(self, other):

        return NCN(
              round(self.ins.T_lower + other.ins.T_lower - self.ins.T_lower * other.ins.T_lower, 2),
              round(self.ins.T_upper + other.ins.T_upper - self.ins.T_upper * other.ins.T_upper, 2),
              round(self.ins.I_lower * other.ins.I_lower, 2),
              round(self.ins.I_upper * other.ins.I_upper, 2),
              round(self.ins.F_lower * other.ins.F_lower, 2),
              round(self.ins.F_upper * other.ins.F_upper, 2),
              round(self.ns.T + other.ns.T - self.ns.T * other.ns.T, 2),
              round(self.ns.I * other.ns.I, 2),
              round(self.ns.F * other.ns.F, 2)
        )


    def __mul__(self, other):

        return NCN(
              round(self.ins.T_lower * other.ins.T_lower, 2),
              round(self.ins.T_upper * other.ins.T_upper, 2),
              round(self.ins.I_lower + other.ins.I_lower - self.ins.I_lower * other.ins.I_lower, 2),
              round(self.ins.I_upper + other.ins.I_upper - self.ins.I_upper * other.ins.I_upper, 2),
              round(self.ins.F_lower + other.ins.F_lower - self.ins.F_lower * other.ins.F_lower, 2),
              round(self.ins.F_upper + other.ins.F_upper - self.ins.F_upper * other.ins.F_upper, 2),
              round(self.ns.T * other.ns.T, 2),
              round(self.ns.I + other.ns.I - self.ns.I * other.ns.I, 2),
              round(self.ns.F + other.ns.F - self.ns.F * other.ns.F, 2)
        )


    def scalar_multiplication(self, scalar):

        assert scalar > 0

        return NCN(
              round(1 - ((1 - self.ins.T_lower) ** scalar), 2),
              round(1 - ((1 - self.ins.T_upper) ** scalar), 2),
              round(self.ins.I_lower ** scalar, 2),
              round(self.ins.I_upper ** scalar, 2),
              round(self.ins.F_lower ** scalar, 2),
              round(self.ins.F_upper ** scalar, 2),
              round(1 - ((1 - self.ns.T) ** scalar), 2),
              round(self.ns.I ** scalar, 2),
              round(self.ns.F ** scalar, 2)
        )


    def containment(self, other):

        return (
            self.ins.T_lower <= other.ins.T_lower and
            self.ins.T_upper <= other.ins.T_upper and
            self.ins.I_lower >= other.ins.I_lower and
            self.ins.I_upper >= other.ins.I_upper and
            self.ins.F_lower >= other.ins.F_lower and
            self.ins.F_upper >= other.ins.F_upper and
            self.ns.T <= other.ns.T and
            self.ns.I >= other.ns.I and
            self.ns.F >= other.ns.F
        )


    def score(self):

        return (
            round(((6 + self.ins.T_lower + self.ins.T_upper
          - self.ins.I_lower - self.ins.I_upper
          - self.ins.F_lower - self.ins.F_upper
          + self.ns.T - self.ns.I - self.ns.F) / 9), 2)
        )


    def accuracy(self):

        return (
            round((self.ins.T_lower + self.ins.T_upper
          - self.ins.F_lower - self.ins.F_upper
          + self.ns.T - self.ns.F), 2)
        )


    def certainty(self):

        return (
            round((self.ins.T_lower + self.ins.T_upper + self.ns.T), 2)
        )


    def distance_measure(self, other):

        return (1 / 9) * (
            abs(self.ins.T_lower - other.ins.T_lower) +
            abs(self.ins.I_lower - other.ins.I_lower) +
            abs(self.ins.F_lower - other.ins.F_lower) +
            abs(self.ins.T_upper - other.ins.T_upper) +
            abs(self.ins.I_upper - other.ins.I_upper) +
            abs(self.ins.F_upper - other.ins.F_upper) +
            abs(self.ns.T - other.ns.T) +
            abs(self.ns.I - other.ns.I) +
            abs(self.ns.F - other.ns.F)
        )
    

    def correlation_measure(self, other):

        return (
            ((1 / 3) * (self.ns.T * other.ns.T + 
                        self.ns.I * other.ns.I + 
                        self.ns.F * other.ns.F)) +
            ((1 / 6) * (self.ins.T_upper * other.ins.T_upper + 
                        self.ins.T_lower * other.ins.T_lower + 
                        self.ins.I_upper * other.ins.I_upper + 
                        self.ins.I_lower * other.ins.I_lower + 
                        self.ins.F_upper * other.ins.F_upper + 
                        self.ins.F_lower * other.ins.F_lower))
            )
    

class NCS:

    def __init__(self):

        self.ncs = []


    def add_element(self, ncn):

        assert isinstance(ncn, NCN)
        self.ncs.append(ncn)


    def __str__(self):

        string = "{\n"
        for i in range(len(self.ncs)):
            if i < len(self.ncs) - 1:
                string += f"{self.ncs[i]}, \n"
            else:
                string += f"{self.ncs[i]}"
        string += "\n}"

        return string


    def __len__(self):

        return len(self.ncs)


    def __getitem__(self, index):

        return self.ncs[index]


    def p_union(self, other):

        p_union_set = NCS()
        for i in range(len(self.ncs)):
            p_union_set.add_element(self.ncs[i].p_union(other.ncs[i]))

        return p_union_set


    def p_intersection(self, other):

        p_intersection_set = NCS()
        for i in range(len(self.ncs)):
            p_intersection_set.add_element(self.ncs[i].p_intersection(other.ncs[i]))

        return p_intersection_set


    def r_union(self, other):

        r_union_set = NCS()
        for i in range(len(self.ncs)):
            r_union_set.add_element(self.ncs[i].r_union(other.ncs[i]))

        return r_union_set


    def r_intersection(self, other):

        r_intersection_set = NCS()
        for i in range(len(self.ncs)):
            r_intersection_set.add_element(self.ncs[i].r_intersection(other.ncs[i]))

        return r_intersection_set


    def complement(self):

        complement_set = NCS()
        for i in range(len(self.ncs)):
            complement_set.add_element(self.ncs[i].complement())

        return complement_set

    def __eq__(self, other):

        for i in range(len(self.ncs)):
            if not (self.ncs[i] == other.ncs[i]):
                return False
        return True


    def __add__(self, other):

        add_set = NCS()
        for i in range(len(self.ncs)):
            add_set.add_element(self.ncs[i] + other.ncs[i])

        return add_set


    def __mul__(self, other):

        mul_set = NCS()
        for i in range(len(self.ncs)):
            mul_set.add_element(self.ncs[i] * other.ncs[i])

        return mul_set


    def scalar_multiplication(self, scalar):

        scalar_mul_set = NCS()
        for i in range(len(self.ncs)):
            scalar_mul_set.add_element(self.ncs[i].scalar_multiplication(scalar))

        return scalar_mul_set


    def containment(self, other):

        for i in range(len(self.ncs)):
            if not(self.ncs[i].containment(other.ncs[i])):
                return False
        return True


    def score(self):

        score_set = []
        for i in range(len(self.ncs)):
            score_set.append(self.ncs[i].score())

        return score_set


    def accuracy(self):

        accuracy_set = []
        for i in range(len(self.ncs)):
            accuracy_set.append(self.ncs[i].accuracy())

        return accuracy_set


    def certainty(self):

        certainty_set = []
        for i in range(len(self.ncs)):
            certainty_set.append(self.ncs[i].certainty())

        return certainty_set


    def distance_measure(self, other):

        distance_set = []
        for i in range(len(self.ncs)):
            distance_set.append(self.ncs[i].distance_measure(other.ncs[i]))

        return (1 / len(self.ncs)) * sum(distance_set)
    

    def correlation_measure(self, other):

        correlation_self_other = 0
        correlation_self_self = 0
        correlation_other_other = 0

        for i in range(len(self.ncs)):
            correlation_self_other += self.ncs[i].correlation_measure(other.ncs[i])

        for i in range(len(self.ncs)):
            correlation_self_self += self.ncs[i].correlation_measure(self.ncs[i])

        for i in range(len(self.ncs)):
            correlation_other_other += other.ncs[i].correlation_measure(other.ncs[i])

        return round((correlation_self_other / ((correlation_self_self * correlation_other_other) ** 0.5)), 2)